using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

/// <summary>
/// Fun achievement system with quirky achievements for the demo.
/// </summary>
public class AchievementSystem : MonoBehaviour
{
    public static AchievementSystem Instance { get; private set; }
    
    [SerializeField] private List<Achievement> achievements = new List<Achievement>();
    [SerializeField] private GameObject achievementPopupPrefab;
    [SerializeField] private Transform uiParent;
    
    private HashSet<string> _unlockedAchievements = new HashSet<string>();
    private Dictionary<string, int> _progressCounters = new Dictionary<string, int>();
    private float _sessionStartTime;
    
    // Events
    public event Action<Achievement> OnAchievementUnlocked;
    public event Action<Achievement, int, int> OnAchievementProgress;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        InitializeAchievements();
        LoadProgress();
        _sessionStartTime = Time.time;
    }
    
    void Start()
    {
        SubscribeToEvents();
    }
    
    private void InitializeAchievements()
    {
        // Quirky and funny achievements for the demo
        achievements = new List<Achievement>
        {
            // Tutorial achievements
            new Achievement("first_steps", "Baby Steps", "Take your first steps in the game!", AchievementType.Tutorial, 1),
            new Achievement("first_shot", "Trigger Happy", "Fire your first shot!", AchievementType.Tutorial, 1),
            new Achievement("first_death", "Learning Experience", "Die for the first time. Don't worry, it happens to everyone!", AchievementType.Tutorial, 1),
            
            // Combat achievements
            new Achievement("sharpshooter", "Sharpshooter", "Hit 10 enemies without missing", AchievementType.Combat, 10),
            new Achievement("pacifist_run", "Peace Was Never An Option... Wait", "Survive 60 seconds without shooting", AchievementType.Special, 60),
            new Achievement("spray_and_pray", "Spray and Pray", "Fire 100 shots in a single session", AchievementType.Combat, 100),
            new Achievement("enemy_slayer", "Bug Exterminator", "Defeat 50 enemies", AchievementType.Combat, 50),
            
            // Movement achievements
            new Achievement("speed_demon", "Gotta Go Fast", "Move at max speed for 10 seconds straight", AchievementType.Movement, 10),
            new Achievement("couch_potato", "Statue Mode", "Stand perfectly still for 30 seconds", AchievementType.Funny, 30),
            new Achievement("marathon_runner", "Marathon Runner", "Travel a total distance of 1000 units", AchievementType.Movement, 1000),
            new Achievement("dizzy", "Spin Cycle", "Rotate 10 full circles in 5 seconds", AchievementType.Funny, 10),
            
            // Survival achievements
            new Achievement("survivor", "Still Breathing", "Survive for 5 minutes", AchievementType.Survival, 300),
            new Achievement("iron_man", "Iron Constitution", "Survive 10 minutes without taking damage", AchievementType.Survival, 600),
            new Achievement("close_call", "That Was Close!", "Survive with exactly 1 HP", AchievementType.Special, 1),
            
            // Collection achievements
            new Achievement("collector", "Hoarder", "Collect 25 items", AchievementType.Collection, 25),
            new Achievement("coin_collector", "Penny Pincher", "Collect 100 coins", AchievementType.Collection, 100),
            new Achievement("treasure_hunter", "Treasure Hunter", "Find a rare item", AchievementType.Special, 1),
            
            // Time-based achievements
            new Achievement("night_owl", "Dedicated Player", "Play for 1 hour total", AchievementType.Time, 3600),
            new Achievement("speedrunner", "Speed Runner", "Complete the demo in under 2 minutes", AchievementType.Special, 120),
            
            // Quirky achievements
            new Achievement("pause_master", "Pause Master", "Pause the game 50 times", AchievementType.Funny, 50),
            new Achievement("settings_explorer", "Perfectionist", "Open the settings menu 10 times", AchievementType.Funny, 10),
            new Achievement("clicker", "Persistent", "Click 500 times", AchievementType.Funny, 500),
            new Achievement("afk", "AFK Champion", "Leave the game running for 10 minutes", AchievementType.Funny, 600),
            
            // Meta achievements
            new Achievement("achievement_hunter", "Achievement Hunter", "Unlock 10 achievements", AchievementType.Meta, 10),
            new Achievement("completionist", "Completionist", "Unlock all achievements", AchievementType.Meta, 25),
            new Achievement("first_save", "Progress Saver", "Save your game for the first time", AchievementType.Tutorial, 1),
        };
        
        Debug.Log($"Initialized {achievements.Count} achievements");
    }
    
    private void SubscribeToEvents()
    {
        // Subscribe to game events to track progress
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.OnHealthChanged += OnHealthChanged;
            ModernGameManager.Instance.OnScoreChanged += OnScoreChanged;
            ModernGameManager.Instance.OnGamePaused += OnGamePaused;
        }
        
        if (SaveSystem.Instance != null)
        {
            SaveSystem.Instance.OnGameSaved += OnGameSaved;
        }
    }
    
    public void TrackProgress(string achievementId, int amount = 1)
    {
        if (_unlockedAchievements.Contains(achievementId))
            return; // Already unlocked
        
        Achievement achievement = achievements.FirstOrDefault(a => a.id == achievementId);
        if (achievement == null)
        {
            Debug.LogWarning($"Achievement not found: {achievementId}");
            return;
        }
        
        if (!_progressCounters.ContainsKey(achievementId))
        {
            _progressCounters[achievementId] = 0;
        }
        
        _progressCounters[achievementId] += amount;
        int currentProgress = _progressCounters[achievementId];
        
        OnAchievementProgress?.Invoke(achievement, currentProgress, achievement.targetValue);
        
        if (currentProgress >= achievement.targetValue)
        {
            UnlockAchievement(achievement);
        }
    }
    
    public void UnlockAchievement(Achievement achievement)
    {
        if (_unlockedAchievements.Contains(achievement.id))
            return; // Already unlocked
        
        _unlockedAchievements.Add(achievement.id);
        OnAchievementUnlocked?.Invoke(achievement);
        
        ShowAchievementPopup(achievement);
        SaveProgress();
        
        Debug.Log($"🏆 Achievement Unlocked: {achievement.title} - {achievement.description}");
        
        // Check meta achievements
        if (achievement.id != "achievement_hunter" && achievement.id != "completionist")
        {
            TrackProgress("achievement_hunter");
            if (_unlockedAchievements.Count >= achievements.Count - 1) // -1 for completionist itself
            {
                TrackProgress("completionist");
            }
        }
    }
    
    public void UnlockAchievement(string achievementId)
    {
        Achievement achievement = achievements.FirstOrDefault(a => a.id == achievementId);
        if (achievement != null)
        {
            UnlockAchievement(achievement);
        }
    }
    
    private void ShowAchievementPopup(Achievement achievement)
    {
        if (achievementPopupPrefab != null && uiParent != null)
        {
            GameObject popup = Instantiate(achievementPopupPrefab, uiParent);
            AchievementPopup popupComponent = popup.GetComponent<AchievementPopup>();
            popupComponent?.ShowAchievement(achievement);
        }
    }
    
    // Event handlers
    private void OnHealthChanged(int health)
    {
        if (health == 1)
        {
            UnlockAchievement("close_call");
        }
    }
    
    private void OnScoreChanged(int score)
    {
        TrackProgress("enemy_slayer");
    }
    
    private void OnGamePaused()
    {
        TrackProgress("pause_master");
    }
    
    private void OnGameSaved(SaveData saveData, int slot)
    {
        UnlockAchievement("first_save");
    }
    
    // Public methods for tracking specific actions
    public void OnPlayerMoved(Vector3 movement)
    {
        if (movement.magnitude > 0.1f)
        {
            UnlockAchievement("first_steps");
            TrackProgress("marathon_runner", Mathf.RoundToInt(movement.magnitude));
        }
    }
    
    public void OnProjectileFired()
    {
        UnlockAchievement("first_shot");
        TrackProgress("spray_and_pray");
    }
    
    public void OnPlayerDied()
    {
        UnlockAchievement("first_death");
    }
    
    public void OnItemCollected()
    {
        TrackProgress("collector");
    }
    
    public void OnCoinCollected()
    {
        TrackProgress("coin_collector");
    }
    
    public void OnSettingsOpened()
    {
        TrackProgress("settings_explorer");
    }
    
    public void OnClick()
    {
        TrackProgress("clicker");
    }
    
    // Save/Load system
    private void SaveProgress()
    {
        string achievementsJson = JsonUtility.ToJson(new SerializableStringArray(_unlockedAchievements.ToArray()));
        PlayerPrefs.SetString("UnlockedAchievements", achievementsJson);
        
        foreach (var counter in _progressCounters)
        {
            PlayerPrefs.SetInt($"AchievementProgress_{counter.Key}", counter.Value);
        }
        
        PlayerPrefs.Save();
    }
    
    private void LoadProgress()
    {
        string achievementsJson = PlayerPrefs.GetString("UnlockedAchievements", "");
        if (!string.IsNullOrEmpty(achievementsJson))
        {
            try
            {
                SerializableStringArray data = JsonUtility.FromJson<SerializableStringArray>(achievementsJson);
                _unlockedAchievements = new HashSet<string>(data.array);
            }
            catch (Exception e)
            {
                Debug.LogError($"Failed to load achievements: {e.Message}");
                _unlockedAchievements = new HashSet<string>();
            }
        }
        
        foreach (var achievement in achievements)
        {
            int progress = PlayerPrefs.GetInt($"AchievementProgress_{achievement.id}", 0);
            if (progress > 0)
            {
                _progressCounters[achievement.id] = progress;
            }
        }
    }
    
    public List<Achievement> GetAllAchievements() => achievements;
    public HashSet<string> GetUnlockedAchievements() => new HashSet<string>(_unlockedAchievements);
    public int GetProgress(string achievementId) => _progressCounters.GetValueOrDefault(achievementId, 0);
    
    void OnDestroy()
    {
        SaveProgress();
        OnAchievementUnlocked = null;
        OnAchievementProgress = null;
    }
}

[System.Serializable]
public class Achievement
{
    public string id;
    public string title;
    public string description;
    public AchievementType type;
    public int targetValue;
    public bool isHidden;
    
    public Achievement(string id, string title, string description, AchievementType type, int targetValue, bool isHidden = false)
    {
        this.id = id;
        this.title = title;
        this.description = description;
        this.type = type;
        this.targetValue = targetValue;
        this.isHidden = isHidden;
    }
}

public enum AchievementType
{
    Tutorial,
    Combat,
    Movement,
    Survival,
    Collection,
    Time,
    Special,
    Funny,
    Meta
}

[System.Serializable]
public class SerializableStringArray
{
    public string[] array;
    
    public SerializableStringArray(string[] array)
    {
        this.array = array;
    }
}