using UnityEngine;

/// <summary>
/// Quirky collectible items for the office escape demo.
/// </summary>
public class QuirkyCollectible : MonoBehaviour
{
    [Header("Collectible Settings")]
    [SerializeField] private CollectibleType collectibleType;
    [SerializeField] private int pointValue = 10;
    [SerializeField] private AudioClip collectSound;
    [SerializeField] private GameObject collectEffect;
    [SerializeField] private bool isRare = false;
    
    [Header("Animation")]
    [SerializeField] private float bobSpeed = 2f;
    [SerializeField] private float bobHeight = 0.5f;
    [SerializeField] private float rotationSpeed = 90f;
    
    private Vector3 _startPosition;
    private DemoController _demoController;
    private bool _collected = false;
    
    void Start()
    {
        _startPosition = transform.position;
        _demoController = FindObjectOfType<DemoController>();
        
        // Add some randomness to animation
        bobSpeed += Random.Range(-0.5f, 0.5f);
        rotationSpeed += Random.Range(-30f, 30f);
    }
    
    void Update()
    {
        if (_collected) return;
        
        // Bob up and down
        float newY = _startPosition.y + Mathf.Sin(Time.time * bobSpeed) * bobHeight;
        transform.position = new Vector3(transform.position.x, newY, transform.position.z);
        
        // Rotate
        transform.Rotate(0, rotationSpeed * Time.deltaTime, 0);
    }
    
    void OnTriggerEnter(Collider other)
    {
        if (_collected) return;
        
        if (other.CompareTag("Player"))
        {
            CollectItem(other.gameObject);
        }
    }
    
    private void CollectItem(GameObject player)
    {
        _collected = true;
        
        // Play sound effect
        if (collectSound != null)
        {
            AudioSource.PlayClipAtPoint(collectSound, transform.position);
        }
        
        // Spawn particle effect
        if (collectEffect != null)
        {
            Instantiate(collectEffect, transform.position, Quaternion.identity);
        }
        
        // Add score
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.AddScore(pointValue);
        }
        
        // Handle specific collectible types
        HandleCollectibleSpecifics();
        
        // Disable the visual
        GetComponent<Renderer>().enabled = false;
        GetComponent<Collider>().enabled = false;
        
        // Destroy after a short delay (to allow sound/effects to play)
        Destroy(gameObject, 1f);
    }
    
    private void HandleCollectibleSpecifics()
    {
        switch (collectibleType)
        {
            case CollectibleType.CoffeeCup:
                _demoController?.OnCoffeeCollected();
                break;
                
            case CollectibleType.GoldenDonut:
                _demoController?.OnGoldenDonutFound();
                break;
                
            case CollectibleType.PaperClip:
                ShowQuirkyMessage("A paperclip! The universal office tool!");
                break;
                
            case CollectibleType.RubberBand:
                ShowQuirkyMessage("Rubber band acquired! Now you can... make a rubber band ball?");
                break;
                
            case CollectibleType.StickyNote:
                ShowQuirkyMessage("A sticky note with someone's lunch order. Useful!");
                break;
                
            case CollectibleType.PenCap:
                ShowQuirkyMessage("Just a pen cap. Where's the pen though?");
                break;
                
            case CollectibleType.KeyCard:
                ShowQuirkyMessage("Employee keycard found! 'John Smith - Bathroom Monitor'");
                break;
                
            case CollectibleType.TPS_Report:
                ShowQuirkyMessage("TPS Report collected. Did you remember the cover sheet?");
                if (AchievementSystem.Instance != null)
                {
                    AchievementSystem.Instance.UnlockAchievement("tps_report");
                }
                break;
                
            case CollectibleType.Stapler:
                ShowQuirkyMessage("A friendly stapler! Unlike those red ones...");
                break;
                
            case CollectibleType.Calculator:
                ShowQuirkyMessage("Calculator! Time to crunch some numbers... or play games.");
                break;
        }
        
        // Track rare items
        if (isRare && AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.OnItemCollected();
        }
        
        // General collection tracking
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.OnItemCollected();
            
            if (collectibleType == CollectibleType.CoffeeCup)
            {
                AchievementSystem.Instance.OnCoinCollected(); // Coffee cups count as "coins"
            }
        }
    }
    
    private void ShowQuirkyMessage(string message)
    {
        Debug.Log($"💼 {message}");
        // In a real implementation, this would show in the UI
    }
    
    // Static method to create collectibles at runtime
    public static GameObject CreateCollectible(CollectibleType type, Vector3 position, GameObject prefab)
    {
        GameObject collectible = Instantiate(prefab, position, Quaternion.identity);
        QuirkyCollectible component = collectible.GetComponent<QuirkyCollectible>();
        
        if (component != null)
        {
            component.collectibleType = type;
            
            // Set properties based on type
            switch (type)
            {
                case CollectibleType.GoldenDonut:
                    component.pointValue = 500;
                    component.isRare = true;
                    break;
                case CollectibleType.CoffeeCup:
                    component.pointValue = 50;
                    break;
                case CollectibleType.TPS_Report:
                    component.pointValue = 100;
                    component.isRare = true;
                    break;
                default:
                    component.pointValue = 10;
                    break;
            }
        }
        
        return collectible;
    }
}

public enum CollectibleType
{
    CoffeeCup,      // Main currency
    GoldenDonut,    // Rare treasure
    PaperClip,      // Common office item
    RubberBand,     // Common office item
    StickyNote,     // Common office item
    PenCap,         // Common office item
    KeyCard,        // Special item
    TPS_Report,     // Reference to Office Space
    Stapler,        // Friendly version
    Calculator      // Office tool
}