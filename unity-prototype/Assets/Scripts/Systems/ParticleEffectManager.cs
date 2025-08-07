using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Manages particle effects and visual feedback for the demo.
/// </summary>
public class ParticleEffectManager : MonoBehaviour
{
    public static ParticleEffectManager Instance { get; private set; }
    
    [Header("Effect Prefabs")]
    [SerializeField] private GameObject collectEffectPrefab;
    [SerializeField] private GameObject achievementEffectPrefab;
    [SerializeField] private GameObject damageEffectPrefab;
    [SerializeField] private GameObject healEffectPrefab;
    [SerializeField] private GameObject powerUpEffectPrefab;
    [SerializeField] private GameObject deathEffectPrefab;
    [SerializeField] private GameObject coffeeEffectPrefab;
    [SerializeField] private GameObject goldenEffectPrefab;
    
    [Header("Screen Effects")]
    [SerializeField] private Material screenFlashMaterial;
    [SerializeField] private float flashDuration = 0.1f;
    
    private Dictionary<string, GameObject> _effectPool = new Dictionary<string, GameObject>();
    private Dictionary<string, Queue<ParticleSystem>> _particlePools = new Dictionary<string, Queue<ParticleSystem>>();
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        InitializeEffectPools();
    }
    
    private void InitializeEffectPools()
    {
        // Pre-populate particle pools for performance
        CreatePool("collect", collectEffectPrefab, 10);
        CreatePool("achievement", achievementEffectPrefab, 5);
        CreatePool("damage", damageEffectPrefab, 5);
        CreatePool("heal", healEffectPrefab, 3);
        CreatePool("powerup", powerUpEffectPrefab, 3);
        CreatePool("death", deathEffectPrefab, 2);
        CreatePool("coffee", coffeeEffectPrefab, 8);
        CreatePool("golden", goldenEffectPrefab, 2);
    }
    
    private void CreatePool(string poolName, GameObject prefab, int poolSize)
    {
        if (prefab == null) return;
        
        _particlePools[poolName] = new Queue<ParticleSystem>();
        
        for (int i = 0; i < poolSize; i++)
        {
            GameObject instance = Instantiate(prefab, transform);
            ParticleSystem particles = instance.GetComponent<ParticleSystem>();
            
            if (particles != null)
            {
                instance.SetActive(false);
                _particlePools[poolName].Enqueue(particles);
            }
            else
            {
                Destroy(instance);
            }
        }
    }
    
    public void PlayEffect(EffectType effectType, Vector3 position, Quaternion rotation = default)
    {
        string poolName = GetPoolNameForEffect(effectType);
        
        if (_particlePools.ContainsKey(poolName) && _particlePools[poolName].Count > 0)
        {
            ParticleSystem effect = _particlePools[poolName].Dequeue();
            
            if (effect != null)
            {
                effect.transform.position = position;
                effect.transform.rotation = rotation == default ? Quaternion.identity : rotation;
                effect.gameObject.SetActive(true);
                
                // Customize effect based on type
                CustomizeEffect(effect, effectType);
                
                effect.Play();
                
                // Return to pool after the effect finishes
                StartCoroutine(ReturnToPoolAfterPlay(effect, poolName));
            }
        }
        else
        {
            // Fallback: Create a temporary effect if pool is empty
            CreateTemporaryEffect(effectType, position, rotation);
        }
    }
    
    private void CustomizeEffect(ParticleSystem effect, EffectType effectType)
    {
        var main = effect.main;
        
        switch (effectType)
        {
            case EffectType.Collect:
                main.startColor = Color.yellow;
                main.startSpeed = 3f;
                break;
                
            case EffectType.Achievement:
                main.startColor = Color.gold;
                main.startSpeed = 5f;
                break;
                
            case EffectType.Damage:
                main.startColor = Color.red;
                main.startSpeed = 8f;
                break;
                
            case EffectType.Heal:
                main.startColor = Color.green;
                main.startSpeed = 2f;
                break;
                
            case EffectType.PowerUp:
                main.startColor = Color.magenta;
                main.startSpeed = 4f;
                break;
                
            case EffectType.Death:
                main.startColor = Color.black;
                main.startSpeed = 10f;
                break;
                
            case EffectType.Coffee:
                main.startColor = new Color(0.6f, 0.3f, 0.1f); // Brown
                main.startSpeed = 3f;
                break;
                
            case EffectType.Golden:
                main.startColor = Color.yellow;
                main.startSpeed = 6f;
                // Add sparkle effect
                var emission = effect.emission;
                emission.rateOverTime = 50f;
                break;
        }
    }
    
    private System.Collections.IEnumerator ReturnToPoolAfterPlay(ParticleSystem effect, string poolName)
    {
        yield return new WaitForSeconds(effect.main.duration + effect.main.startLifetime.constantMax);
        
        if (effect != null)
        {
            effect.gameObject.SetActive(false);
            _particlePools[poolName].Enqueue(effect);
        }
    }
    
    private void CreateTemporaryEffect(EffectType effectType, Vector3 position, Quaternion rotation)
    {
        GameObject prefab = GetPrefabForEffect(effectType);
        
        if (prefab != null)
        {
            GameObject temp = Instantiate(prefab, position, rotation);
            ParticleSystem particles = temp.GetComponent<ParticleSystem>();
            
            if (particles != null)
            {
                CustomizeEffect(particles, effectType);
                particles.Play();
                
                // Auto-destroy after playing
                Destroy(temp, particles.main.duration + particles.main.startLifetime.constantMax + 1f);
            }
            else
            {
                Destroy(temp, 2f);
            }
        }
    }
    
    private string GetPoolNameForEffect(EffectType effectType)
    {
        switch (effectType)
        {
            case EffectType.Collect: return "collect";
            case EffectType.Achievement: return "achievement";
            case EffectType.Damage: return "damage";
            case EffectType.Heal: return "heal";
            case EffectType.PowerUp: return "powerup";
            case EffectType.Death: return "death";
            case EffectType.Coffee: return "coffee";
            case EffectType.Golden: return "golden";
            default: return "collect";
        }
    }
    
    private GameObject GetPrefabForEffect(EffectType effectType)
    {
        switch (effectType)
        {
            case EffectType.Collect: return collectEffectPrefab;
            case EffectType.Achievement: return achievementEffectPrefab;
            case EffectType.Damage: return damageEffectPrefab;
            case EffectType.Heal: return healEffectPrefab;
            case EffectType.PowerUp: return powerUpEffectPrefab;
            case EffectType.Death: return deathEffectPrefab;
            case EffectType.Coffee: return coffeeEffectPrefab;
            case EffectType.Golden: return goldenEffectPrefab;
            default: return collectEffectPrefab;
        }
    }
    
    // Screen effects
    public void FlashScreen(Color color, float duration = -1f)
    {
        if (duration < 0) duration = flashDuration;
        
        StartCoroutine(ScreenFlashCoroutine(color, duration));
    }
    
    private System.Collections.IEnumerator ScreenFlashCoroutine(Color color, float duration)
    {
        // This would need a UI overlay or post-processing effect
        // For now, just log the effect
        Debug.Log($"Screen flash: {color} for {duration} seconds");
        yield return new WaitForSeconds(duration);
    }
    
    // Convenience methods
    public void PlayCollectEffect(Vector3 position) => PlayEffect(EffectType.Collect, position);
    public void PlayAchievementEffect(Vector3 position) => PlayEffect(EffectType.Achievement, position);
    public void PlayDamageEffect(Vector3 position) => PlayEffect(EffectType.Damage, position);
    public void PlayHealEffect(Vector3 position) => PlayEffect(EffectType.Heal, position);
    public void PlayDeathEffect(Vector3 position) => PlayEffect(EffectType.Death, position);
    public void PlayCoffeeEffect(Vector3 position) => PlayEffect(EffectType.Coffee, position);
    public void PlayGoldenEffect(Vector3 position) => PlayEffect(EffectType.Golden, position);
    
    // Trail effects for moving objects
    public void AttachTrailEffect(GameObject target, EffectType effectType, float duration = 5f)
    {
        StartCoroutine(TrailEffectCoroutine(target, effectType, duration));
    }
    
    private System.Collections.IEnumerator TrailEffectCoroutine(GameObject target, EffectType effectType, float duration)
    {
        float elapsed = 0f;
        
        while (elapsed < duration && target != null)
        {
            PlayEffect(effectType, target.transform.position);
            yield return new WaitForSeconds(0.1f);
            elapsed += 0.1f;
        }
    }
    
    // Camera shake effect
    public void ShakeCamera(float intensity = 1f, float duration = 0.5f)
    {
        Camera mainCamera = Camera.main;
        if (mainCamera != null)
        {
            StartCoroutine(CameraShakeCoroutine(mainCamera, intensity, duration));
        }
    }
    
    private System.Collections.IEnumerator CameraShakeCoroutine(Camera camera, float intensity, float duration)
    {
        Vector3 originalPosition = camera.transform.position;
        float elapsed = 0f;
        
        while (elapsed < duration)
        {
            float x = Random.Range(-intensity, intensity);
            float y = Random.Range(-intensity, intensity);
            
            camera.transform.position = originalPosition + new Vector3(x, y, 0f);
            
            elapsed += Time.deltaTime;
            yield return null;
        }
        
        camera.transform.position = originalPosition;
    }
}

public enum EffectType
{
    Collect,
    Achievement,
    Damage,
    Heal,
    PowerUp,
    Death,
    Coffee,
    Golden
}