using System;
using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Modern event-driven game manager with proper state management.
/// </summary>
public class ModernGameManager : MonoBehaviour
{
    public static ModernGameManager Instance { get; private set; }
    
    [SerializeField] private GameConfig gameConfig;
    
    // Game state
    private int _currentScore;
    private int _playerHealth;
    private bool _isPaused;
    private GameState _currentState = GameState.Playing;
    
    // Events
    public event Action<int> OnScoreChanged;
    public event Action<int> OnHealthChanged;
    public event Action OnGamePaused;
    public event Action OnGameResumed;
    public event Action OnGameOver;
    public event Action OnLevelComplete;
    
    // Properties
    public int CurrentScore => _currentScore;
    public int PlayerHealth => _playerHealth;
    public bool IsPaused => _isPaused;
    public GameState CurrentState => _currentState;
    public GameConfig Config => gameConfig;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        InitializeGame();
    }
    
    void Start()
    {
        SetGameState(GameState.Playing);
    }
    
    void Update()
    {
        // Handle pause input (keeping minimal Update usage)
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            TogglePause();
        }
    }
    
    private void InitializeGame()
    {
        if (gameConfig == null)
        {
            Debug.LogError("GameConfig is not assigned to ModernGameManager!");
            return;
        }
        
        _currentScore = 0;
        _playerHealth = gameConfig.playerMaxHealth;
        _isPaused = false;
    }
    
    public void AddScore(int value)
    {
        if (_currentState != GameState.Playing) return;
        
        _currentScore += value;
        OnScoreChanged?.Invoke(_currentScore);
    }
    
    public void TakeDamage(int amount)
    {
        if (_currentState != GameState.Playing) return;
        
        _playerHealth = Mathf.Max(0, _playerHealth - amount);
        OnHealthChanged?.Invoke(_playerHealth);
        
        if (_playerHealth <= 0)
        {
            GameOver();
        }
    }
    
    public void Heal(int amount)
    {
        if (_currentState != GameState.Playing) return;
        
        _playerHealth = Mathf.Min(gameConfig.playerMaxHealth, _playerHealth + amount);
        OnHealthChanged?.Invoke(_playerHealth);
    }
    
    public void TogglePause()
    {
        if (_currentState == GameState.GameOver) return;
        
        if (_isPaused)
        {
            ResumeGame();
        }
        else
        {
            PauseGame();
        }
    }
    
    public void PauseGame()
    {
        if (_isPaused) return;
        
        _isPaused = true;
        Time.timeScale = 0f;
        OnGamePaused?.Invoke();
    }
    
    public void ResumeGame()
    {
        if (!_isPaused) return;
        
        _isPaused = false;
        Time.timeScale = 1f;
        OnGameResumed?.Invoke();
    }
    
    public void GameOver()
    {
        SetGameState(GameState.GameOver);
        OnGameOver?.Invoke();
    }
    
    public void CompleteLevel()
    {
        SetGameState(GameState.LevelComplete);
        OnLevelComplete?.Invoke();
    }
    
    public void RestartLevel()
    {
        Time.timeScale = 1f; // Ensure time scale is reset
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
    
    public void LoadScene(string sceneName)
    {
        Time.timeScale = 1f; // Ensure time scale is reset
        SceneManager.LoadScene(sceneName);
    }
    
    public void LoadScene(int sceneIndex)
    {
        Time.timeScale = 1f; // Ensure time scale is reset
        SceneManager.LoadScene(sceneIndex);
    }
    
    public void QuitGame()
    {
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }
    
    private void SetGameState(GameState newState)
    {
        _currentState = newState;
    }
    
    void OnDestroy()
    {
        // Clean up events
        OnScoreChanged = null;
        OnHealthChanged = null;
        OnGamePaused = null;
        OnGameResumed = null;
        OnGameOver = null;
        OnLevelComplete = null;
    }
}

public enum GameState
{
    Playing,
    Paused,
    GameOver,
    LevelComplete
}