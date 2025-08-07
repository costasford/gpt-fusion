using System.Collections;
using UnityEngine;

/// <summary>
/// Main controller for the quirky demo experience.
/// "Office Escape: The Caffeinated Chronicles"
/// </summary>
public class DemoController : MonoBehaviour
{
    [Header("Demo Settings")]
    [SerializeField] private float demoTimeLimit = 120f; // 2 minutes
    [SerializeField] private GameObject[] quirkySoundEffects;
    [SerializeField] private string[] funnyMessages;
    
    [Header("Special Events")]
    [SerializeField] private float crazyModeChance = 0.1f;
    [SerializeField] private float crazyModeDuration = 10f;
    
    private bool _isCrazyModeActive;
    private float _demoStartTime;
    private int _coffeeCount;
    private bool _hasMetTheBoss;
    
    // Demo story messages
    private readonly string[] _storyMessages = {
        "Welcome to Cubicle Corp! You're the new intern.",
        "Your mission: Collect coffee cups to stay awake!",
        "Avoid the red staplers - they're possessed!",
        "Find the golden donut for extra points!",
        "Don't let the boss catch you slacking off!",
        "Coffee level critical - find more cups!",
        "CRAZY MODE ACTIVATED! Everything is faster now!",
        "The printer is jamming again... typical Monday.",
        "Someone microwaved fish in the break room. Evacuate!",
        "Congratulations! You survived corporate life for 2 minutes!"
    };
    
    void Start()
    {
        _demoStartTime = Time.time;
        StartCoroutine(DemoSequence());
        ShowMessage(_storyMessages[0]);
        
        // Track demo start
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("first_steps");
        }
    }
    
    void Update()
    {
        // Check for demo time limit
        float elapsedTime = Time.time - _demoStartTime;
        if (elapsedTime >= demoTimeLimit)
        {
            CompleteDemoSpeedrun();
        }
        
        // Random crazy mode activation
        if (!_isCrazyModeActive && Random.Range(0f, 1f) < crazyModeChance * Time.deltaTime)
        {
            StartCrazyMode();
        }
        
        // Track some funny achievements
        TrackQuirkyBehaviors();
    }
    
    private IEnumerator DemoSequence()
    {
        yield return new WaitForSeconds(5f);
        ShowMessage(_storyMessages[1]);
        
        yield return new WaitForSeconds(10f);
        ShowMessage(_storyMessages[2]);
        
        yield return new WaitForSeconds(15f);
        if (_coffeeCount < 3)
        {
            ShowMessage(_storyMessages[5]);
        }
        
        yield return new WaitForSeconds(30f);
        ShowMessage(_storyMessages[7]);
        
        yield return new WaitForSeconds(45f);
        if (Random.Range(0f, 1f) < 0.5f)
        {
            ShowMessage(_storyMessages[8]);
            TriggerFishEvacuation();
        }
        
        yield return new WaitForSeconds(60f);
        ShowMessage("Halfway through your shift! Keep going!");
        
        yield return new WaitForSeconds(90f);
        ShowMessage("Almost time to clock out!");
        
        yield return new WaitForSeconds(demoTimeLimit);
        ShowMessage(_storyMessages[9]);
    }
    
    public void OnCoffeeCollected()
    {
        _coffeeCount++;
        
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.OnItemCollected();
            
            // Special coffee achievements
            if (_coffeeCount == 1)
            {
                AchievementSystem.Instance.UnlockAchievement("first_caffeine_fix");
            }
            else if (_coffeeCount >= 10)
            {
                AchievementSystem.Instance.UnlockAchievement("caffeine_addict");
            }
        }
        
        // Show funny message
        string[] coffeeMessages = {
            "Ahh, sweet caffeine!",
            "*jittery typing intensifies*",
            "Energy level: MAXIMUM!",
            "One more cup and I'll see through time!",
            "I can taste colors now!",
        };
        
        ShowMessage(coffeeMessages[Random.Range(0, coffeeMessages.Length)]);
    }
    
    public void OnBossEncounter()
    {
        if (!_hasMetTheBoss)
        {
            _hasMetTheBoss = true;
            ShowMessage("Oh no! It's the boss! Act busy!");
            
            if (AchievementSystem.Instance != null)
            {
                AchievementSystem.Instance.UnlockAchievement("boss_encounter");
            }
        }
    }
    
    public void OnStaplerHit()
    {
        string[] staplerMessages = {
            "Ouch! That stapler has anger issues!",
            "Why are the office supplies so hostile?",
            "Note to self: Avoid red staplers.",
            "I think it's possessed by a disgruntled employee.",
            "That's what I get for not organizing the supply closet!",
        };
        
        ShowMessage(staplerMessages[Random.Range(0, staplerMessages.Length)]);
        
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("stapler_victim");
        }
    }
    
    public void OnGoldenDonutFound()
    {
        ShowMessage("🍩 GOLDEN DONUT ACQUIRED! The legends are true!");
        
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("golden_donut");
            AchievementSystem.Instance.UnlockAchievement("treasure_hunter");
        }
        
        // Add massive score bonus
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.AddScore(1000);
        }
    }
    
    private void StartCrazyMode()
    {
        if (_isCrazyModeActive) return;
        
        _isCrazyModeActive = true;
        ShowMessage(_storyMessages[6]);
        
        // Speed up the game
        Time.timeScale = 1.5f;
        
        // Start crazy visual effects
        StartCoroutine(CrazyModeSequence());
        
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("crazy_mode");
        }
    }
    
    private IEnumerator CrazyModeSequence()
    {
        float elapsed = 0f;
        
        while (elapsed < crazyModeDuration)
        {
            // Flash random colors or do other crazy effects
            yield return new WaitForSeconds(0.5f);
            elapsed += 0.5f;
        }
        
        // End crazy mode
        _isCrazyModeActive = false;
        Time.timeScale = 1f;
        ShowMessage("Phew! Back to normal... or as normal as this place gets.");
    }
    
    private void TriggerFishEvacuation()
    {
        // Create temporary speed boost
        if (ModernGameManager.Instance?.Config != null)
        {
            StartCoroutine(TemporarySpeedBoost(2f, 5f));
        }
        
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("fish_survivor");
        }
    }
    
    private IEnumerator TemporarySpeedBoost(float multiplier, float duration)
    {
        // This would need to be implemented in the player controller
        yield return new WaitForSeconds(duration);
        ShowMessage("The fish smell is gone. You can slow down now.");
    }
    
    private void CompleteDemoSpeedrun()
    {
        if (AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.UnlockAchievement("speedrunner");
            AchievementSystem.Instance.UnlockAchievement("office_survivor");
        }
        
        ShowMessage("Demo completed! Thanks for playing 'Office Escape: The Caffeinated Chronicles'!");
    }
    
    private void TrackQuirkyBehaviors()
    {
        // Track if player is standing still (for statue achievement)
        if (Input.GetAxis("Horizontal") == 0 && Input.GetAxis("Vertical") == 0)
        {
            // This would need proper implementation with a timer
        }
        
        // Track spinning
        // This would need to track rotation changes
        
        // Track button mashing
        if (Input.anyKeyDown && AchievementSystem.Instance != null)
        {
            AchievementSystem.Instance.OnClick();
        }
    }
    
    private void ShowMessage(string message)
    {
        Debug.Log($"📢 {message}");
        // In a real implementation, this would show in the UI
        // For now, it appears in the console
    }
    
    // Public methods for other scripts to call
    public void OnPlayerJumped()
    {
        if (AchievementSystem.Instance != null)
        {
            // Track for jumping achievement
        }
    }
    
    public void OnPlayerSpun(float rotationSpeed)
    {
        if (rotationSpeed > 720f) // 2 full rotations per second
        {
            if (AchievementSystem.Instance != null)
            {
                AchievementSystem.Instance.TrackProgress("dizzy");
            }
        }
    }
}