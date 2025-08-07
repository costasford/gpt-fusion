using System;
using System.IO;
using UnityEngine;

/// <summary>
/// Comprehensive save/load system with JSON serialization and multiple save slots.
/// </summary>
public class SaveSystem : MonoBehaviour
{
    public static SaveSystem Instance { get; private set; }
    
    [SerializeField] private int maxSaveSlots = 3;
    [SerializeField] private bool autoSaveEnabled = true;
    [SerializeField] private float autoSaveInterval = 60f; // seconds
    
    private SaveData _currentSave;
    private int _currentSlot = 0;
    private float _autoSaveTimer;
    private string _saveFolderPath;
    
    // Events
    public event Action<SaveData> OnGameLoaded;
    public event Action<SaveData, int> OnGameSaved;
    public event Action<string> OnSaveError;
    
    // Properties
    public SaveData CurrentSave => _currentSave;
    public int CurrentSlot => _currentSlot;
    public int MaxSaveSlots => maxSaveSlots;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        InitializeSaveSystem();
    }
    
    void Update()
    {
        if (autoSaveEnabled && SettingsManager.Instance?.Settings.autoSaveEnabled == true)
        {
            _autoSaveTimer += Time.deltaTime;
            if (_autoSaveTimer >= autoSaveInterval)
            {
                AutoSave();
                _autoSaveTimer = 0f;
            }
        }
    }
    
    private void InitializeSaveSystem()
    {
        _saveFolderPath = Path.Combine(Application.persistentDataPath, "Saves");
        
        // Create saves directory if it doesn't exist
        if (!Directory.Exists(_saveFolderPath))
        {
            Directory.CreateDirectory(_saveFolderPath);
        }
        
        _currentSave = new SaveData();
        Debug.Log($"Save system initialized. Save folder: {_saveFolderPath}");
    }
    
    public void CreateNewGame()
    {
        _currentSave = new SaveData
        {
            playerName = "Player",
            currentLevel = 0,
            playerHealth = 100,
            playerScore = 0,
            playTime = 0f,
            creationDate = DateTime.Now.ToBinary(),
            lastSaveDate = DateTime.Now.ToBinary()
        };
        
        Debug.Log("New game created");
    }
    
    public bool SaveGame(int slotIndex = -1)
    {
        if (slotIndex == -1) slotIndex = _currentSlot;
        
        if (slotIndex < 0 || slotIndex >= maxSaveSlots)
        {
            OnSaveError?.Invoke($"Invalid save slot: {slotIndex}");
            return false;
        }
        
        try
        {
            // Update save data from game state
            UpdateSaveDataFromGame();
            
            string fileName = GetSaveFileName(slotIndex);
            string filePath = Path.Combine(_saveFolderPath, fileName);
            string json = JsonUtility.ToJson(_currentSave, true);
            
            File.WriteAllText(filePath, json);
            
            _currentSlot = slotIndex;
            OnGameSaved?.Invoke(_currentSave, slotIndex);
            
            Debug.Log($"Game saved to slot {slotIndex}: {filePath}");
            return true;
        }
        catch (Exception e)
        {
            string error = $"Failed to save game: {e.Message}";
            OnSaveError?.Invoke(error);
            Debug.LogError(error);
            return false;
        }
    }
    
    public bool LoadGame(int slotIndex)
    {
        if (slotIndex < 0 || slotIndex >= maxSaveSlots)
        {
            OnSaveError?.Invoke($"Invalid save slot: {slotIndex}");
            return false;
        }
        
        string fileName = GetSaveFileName(slotIndex);
        string filePath = Path.Combine(_saveFolderPath, fileName);
        
        if (!File.Exists(filePath))
        {
            OnSaveError?.Invoke($"Save file not found: {fileName}");
            return false;
        }
        
        try
        {
            string json = File.ReadAllText(filePath);
            _currentSave = JsonUtility.FromJson<SaveData>(json);
            _currentSlot = slotIndex;
            
            // Apply save data to game state
            ApplySaveDataToGame();
            
            OnGameLoaded?.Invoke(_currentSave);
            Debug.Log($"Game loaded from slot {slotIndex}: {filePath}");
            return true;
        }
        catch (Exception e)
        {
            string error = $"Failed to load game: {e.Message}";
            OnSaveError?.Invoke(error);
            Debug.LogError(error);
            return false;
        }
    }
    
    public bool DeleteSave(int slotIndex)
    {
        if (slotIndex < 0 || slotIndex >= maxSaveSlots)
        {
            OnSaveError?.Invoke($"Invalid save slot: {slotIndex}");
            return false;
        }
        
        string fileName = GetSaveFileName(slotIndex);
        string filePath = Path.Combine(_saveFolderPath, fileName);
        
        if (!File.Exists(filePath))
        {
            return true; // Already deleted
        }
        
        try
        {
            File.Delete(filePath);
            Debug.Log($"Save file deleted: {fileName}");
            return true;
        }
        catch (Exception e)
        {
            string error = $"Failed to delete save: {e.Message}";
            OnSaveError?.Invoke(error);
            Debug.LogError(error);
            return false;
        }
    }
    
    public SaveSlotInfo GetSaveSlotInfo(int slotIndex)
    {
        if (slotIndex < 0 || slotIndex >= maxSaveSlots)
        {
            return null;
        }
        
        string fileName = GetSaveFileName(slotIndex);
        string filePath = Path.Combine(_saveFolderPath, fileName);
        
        if (!File.Exists(filePath))
        {
            return new SaveSlotInfo { slotIndex = slotIndex, isEmpty = true };
        }
        
        try
        {
            string json = File.ReadAllText(filePath);
            SaveData saveData = JsonUtility.FromJson<SaveData>(json);
            
            return new SaveSlotInfo
            {
                slotIndex = slotIndex,
                isEmpty = false,
                playerName = saveData.playerName,
                currentLevel = saveData.currentLevel,
                playTime = saveData.playTime,
                creationDate = DateTime.FromBinary(saveData.creationDate),
                lastSaveDate = DateTime.FromBinary(saveData.lastSaveDate)
            };
        }
        catch (Exception e)
        {
            Debug.LogError($"Failed to read save slot info: {e.Message}");
            return new SaveSlotInfo { slotIndex = slotIndex, isEmpty = true };
        }
    }
    
    public SaveSlotInfo[] GetAllSaveSlots()
    {
        SaveSlotInfo[] slots = new SaveSlotInfo[maxSaveSlots];
        
        for (int i = 0; i < maxSaveSlots; i++)
        {
            slots[i] = GetSaveSlotInfo(i);
        }
        
        return slots;
    }
    
    public void AutoSave()
    {
        if (_currentSave != null && ModernGameManager.Instance?.CurrentState == GameState.Playing)
        {
            SaveGame(_currentSlot);
            Debug.Log("Auto-save completed");
        }
    }
    
    private void UpdateSaveDataFromGame()
    {
        if (ModernGameManager.Instance != null)
        {
            _currentSave.playerHealth = ModernGameManager.Instance.PlayerHealth;
            _currentSave.playerScore = ModernGameManager.Instance.CurrentScore;
            _currentSave.lastSaveDate = DateTime.Now.ToBinary();
        }
        
        // Update play time
        _currentSave.playTime += Time.unscaledTime;
        
        // Add more game state data as needed
        _currentSave.hasCompletedTutorial = true; // Example
    }
    
    private void ApplySaveDataToGame()
    {
        if (ModernGameManager.Instance != null)
        {
            // Apply health and score
            ModernGameManager.Instance.Heal(_currentSave.playerHealth - ModernGameManager.Instance.PlayerHealth);
            ModernGameManager.Instance.AddScore(_currentSave.playerScore - ModernGameManager.Instance.CurrentScore);
        }
        
        // Apply other game state data as needed
    }
    
    private string GetSaveFileName(int slotIndex)
    {
        return $"save_slot_{slotIndex:00}.json";
    }
    
    void OnDestroy()
    {
        // Clean up events
        OnGameLoaded = null;
        OnGameSaved = null;
        OnSaveError = null;
    }
}

[System.Serializable]
public class SaveData
{
    [Header("Player Info")]
    public string playerName = "Player";
    public int currentLevel = 0;
    public int playerHealth = 100;
    public int playerScore = 0;
    public float playTime = 0f;
    
    [Header("Game Progress")]
    public bool hasCompletedTutorial = false;
    public int highestLevelReached = 0;
    public int totalEnemiesDefeated = 0;
    public int totalItemsCollected = 0;
    
    [Header("Inventory")]
    public int coins = 0;
    public int[] items = new int[0]; // Item IDs
    public int[] itemQuantities = new int[0];
    
    [Header("Achievements")]
    public string[] unlockedAchievements = new string[0];
    
    [Header("Statistics")]
    public float totalTimeInGame = 0f;
    public int totalDeaths = 0;
    public int totalJumps = 0;
    public float distanceTraveled = 0f;
    
    [Header("Metadata")]
    public long creationDate;
    public long lastSaveDate;
    public string gameVersion = Application.version;
}

[System.Serializable]
public class SaveSlotInfo
{
    public int slotIndex;
    public bool isEmpty;
    public string playerName;
    public int currentLevel;
    public float playTime;
    public DateTime creationDate;
    public DateTime lastSaveDate;
}