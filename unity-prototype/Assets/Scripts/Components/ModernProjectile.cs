using UnityEngine;

/// <summary>
/// Modern pooled projectile with configurable behavior.
/// </summary>
[RequireComponent(typeof(Rigidbody))]
public class ModernProjectile : MonoBehaviour, IPooledObject
{
    [Header("Projectile Settings")]
    [SerializeField] private LayerMask targetLayers = -1;
    [SerializeField] private bool usePhysics = true;
    [SerializeField] private GameObject hitEffect;
    [SerializeField] private TrailRenderer trail;
    
    private GameConfig _config;
    private Vector3 _direction;
    private float _spawnTime;
    private Rigidbody _rigidbody;
    private bool _hasHit;
    
    void Awake()
    {
        _rigidbody = GetComponent<Rigidbody>();
    }
    
    void Start()
    {
        _config = ModernGameManager.Instance?.Config;
    }
    
    void Update()
    {
        if (_config == null) return;
        
        // Check lifetime
        if (Time.time - _spawnTime > _config.projectileLifetime)
        {
            ReturnToPool();
            return;
        }
        
        // Move projectile if not using physics
        if (!usePhysics && !_hasHit)
        {
            transform.Translate(_direction * _config.projectileSpeed * Time.deltaTime, Space.World);
        }
    }
    
    public void OnObjectSpawn()
    {
        _config = ModernGameManager.Instance?.Config;
        _spawnTime = Time.time;
        _hasHit = false;
        
        // Reset trail if present
        if (trail != null)
        {
            trail.Clear();
        }
        
        // Set direction based on forward
        _direction = transform.forward;
        
        // Apply physics if enabled
        if (usePhysics && _rigidbody != null && _config != null)
        {
            _rigidbody.velocity = _direction * _config.projectileSpeed;
        }
    }
    
    public void Initialize(Vector3 direction, float? customSpeed = null)
    {
        _direction = direction.normalized;
        
        if (usePhysics && _rigidbody != null && _config != null)
        {
            float speed = customSpeed ?? _config.projectileSpeed;
            _rigidbody.velocity = _direction * speed;
        }
        
        transform.forward = _direction;
    }
    
    void OnTriggerEnter(Collider other)
    {
        if (_hasHit) return;
        
        // Check if target is in correct layer
        if ((targetLayers.value & (1 << other.gameObject.layer)) == 0)
            return;
        
        // Don't hit the object that fired this projectile
        if (other.transform == transform.parent)
            return;
        
        _hasHit = true;
        
        // Try to damage target
        IDamageable damageable = other.GetComponent<IDamageable>();
        if (damageable != null && _config != null)
        {
            damageable.TakeDamage(_config.projectileDamage);
        }
        
        // Spawn hit effect
        if (hitEffect != null)
        {
            GameObject effect = Instantiate(hitEffect, transform.position, Quaternion.identity);
            Destroy(effect, 2f);
        }
        
        // Return to pool
        ReturnToPool();
    }
    
    private void ReturnToPool()
    {
        if (ObjectPool.Instance != null)
        {
            ObjectPool.Instance.ReturnToPool("Projectile", gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    void OnDisable()
    {
        // Stop physics when returning to pool
        if (_rigidbody != null)
        {
            _rigidbody.velocity = Vector3.zero;
            _rigidbody.angularVelocity = Vector3.zero;
        }
    }
}