using System;
using UnityEngine;
using UnityEngine.Audio;

/// <summary>
/// Settings system with persistent data and event notifications.
/// </summary>
public class SettingsManager : MonoBehaviour
{
    public static SettingsManager Instance { get; private set; }
    
    [Header("Audio")]
    [SerializeField] private AudioMixer audioMixer;
    
    // Settings data
    private GameSettings _settings;
    
    // Events
    public event Action<GameSettings> OnSettingsChanged;
    public event Action<float> OnMasterVolumeChanged;
    public event Action<float> OnMusicVolumeChanged;
    public event Action<float> OnSFXVolumeChanged;
    public event Action<int> OnQualityChanged;
    public event Action<bool> OnFullscreenChanged;
    
    // Properties
    public GameSettings Settings => _settings;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        LoadSettings();
        ApplySettings();
    }
    
    private void LoadSettings()
    {
        // Load settings from PlayerPrefs or use defaults
        _settings = new GameSettings
        {
            // Audio settings
            masterVolume = PlayerPrefs.GetFloat("MasterVolume", 1f),
            musicVolume = PlayerPrefs.GetFloat("MusicVolume", 0.8f),
            sfxVolume = PlayerPrefs.GetFloat("SFXVolume", 1f),
            
            // Graphics settings
            qualityLevel = PlayerPrefs.GetInt("QualityLevel", QualitySettings.GetQualityLevel()),
            isFullscreen = PlayerPrefs.GetInt("Fullscreen", Screen.fullScreen ? 1 : 0) == 1,
            targetFrameRate = PlayerPrefs.GetInt("TargetFrameRate", 60),
            vsyncEnabled = PlayerPrefs.GetInt("VSync", QualitySettings.vSyncCount > 0 ? 1 : 0) == 1,
            
            // Gameplay settings
            mouseSensitivity = PlayerPrefs.GetFloat("MouseSensitivity", 1f),
            invertYAxis = PlayerPrefs.GetInt("InvertY", 0) == 1,
            autoSaveEnabled = PlayerPrefs.GetInt("AutoSave", 1) == 1,
            subtitlesEnabled = PlayerPrefs.GetInt("Subtitles", 0) == 1,
            
            // Accessibility
            colorBlindMode = (ColorBlindMode)PlayerPrefs.GetInt("ColorBlindMode", 0),
            textSize = (TextSize)PlayerPrefs.GetInt("TextSize", 1), // Medium
            motionSicknessReduction = PlayerPrefs.GetInt("MotionSickness", 0) == 1
        };
    }
    
    private void ApplySettings()
    {
        // Apply audio settings
        SetMasterVolume(_settings.masterVolume);
        SetMusicVolume(_settings.musicVolume);
        SetSFXVolume(_settings.sfxVolume);
        
        // Apply graphics settings
        QualitySettings.SetQualityLevel(_settings.qualityLevel);
        Screen.SetResolution(Screen.currentResolution.width, Screen.currentResolution.height, _settings.isFullscreen);
        Application.targetFrameRate = _settings.targetFrameRate;
        QualitySettings.vSyncCount = _settings.vsyncEnabled ? 1 : 0;
        
        Debug.Log("Settings applied successfully");
    }
    
    public void SetMasterVolume(float volume)
    {
        volume = Mathf.Clamp01(volume);
        _settings.masterVolume = volume;
        
        if (audioMixer != null)
        {
            // Convert 0-1 to -80-0 dB (logarithmic)
            float dbValue = volume > 0 ? Mathf.Log10(volume) * 20 : -80f;
            audioMixer.SetFloat("MasterVolume", dbValue);
        }
        
        PlayerPrefs.SetFloat("MasterVolume", volume);
        OnMasterVolumeChanged?.Invoke(volume);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetMusicVolume(float volume)
    {
        volume = Mathf.Clamp01(volume);
        _settings.musicVolume = volume;
        
        if (audioMixer != null)
        {
            float dbValue = volume > 0 ? Mathf.Log10(volume) * 20 : -80f;
            audioMixer.SetFloat("MusicVolume", dbValue);
        }
        
        PlayerPrefs.SetFloat("MusicVolume", volume);
        OnMusicVolumeChanged?.Invoke(volume);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetSFXVolume(float volume)
    {
        volume = Mathf.Clamp01(volume);
        _settings.sfxVolume = volume;
        
        if (audioMixer != null)
        {
            float dbValue = volume > 0 ? Mathf.Log10(volume) * 20 : -80f;
            audioMixer.SetFloat("SFXVolume", dbValue);
        }
        
        PlayerPrefs.SetFloat("SFXVolume", volume);
        OnSFXVolumeChanged?.Invoke(volume);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetQualityLevel(int level)
    {
        level = Mathf.Clamp(level, 0, QualitySettings.names.Length - 1);
        _settings.qualityLevel = level;
        
        QualitySettings.SetQualityLevel(level);
        PlayerPrefs.SetInt("QualityLevel", level);
        OnQualityChanged?.Invoke(level);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetFullscreen(bool fullscreen)
    {
        _settings.isFullscreen = fullscreen;
        
        Screen.fullScreen = fullscreen;
        PlayerPrefs.SetInt("Fullscreen", fullscreen ? 1 : 0);
        OnFullscreenChanged?.Invoke(fullscreen);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetTargetFrameRate(int frameRate)
    {
        _settings.targetFrameRate = frameRate;
        
        Application.targetFrameRate = frameRate;
        PlayerPrefs.SetInt("TargetFrameRate", frameRate);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetVSync(bool enabled)
    {
        _settings.vsyncEnabled = enabled;
        
        QualitySettings.vSyncCount = enabled ? 1 : 0;
        PlayerPrefs.SetInt("VSync", enabled ? 1 : 0);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetMouseSensitivity(float sensitivity)
    {
        _settings.mouseSensitivity = Mathf.Clamp(sensitivity, 0.1f, 5f);
        PlayerPrefs.SetFloat("MouseSensitivity", _settings.mouseSensitivity);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetInvertYAxis(bool invert)
    {
        _settings.invertYAxis = invert;
        PlayerPrefs.SetInt("InvertY", invert ? 1 : 0);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetAutoSave(bool enabled)
    {
        _settings.autoSaveEnabled = enabled;
        PlayerPrefs.SetInt("AutoSave", enabled ? 1 : 0);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetSubtitles(bool enabled)
    {
        _settings.subtitlesEnabled = enabled;
        PlayerPrefs.SetInt("Subtitles", enabled ? 1 : 0);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetColorBlindMode(ColorBlindMode mode)
    {
        _settings.colorBlindMode = mode;
        PlayerPrefs.SetInt("ColorBlindMode", (int)mode);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetTextSize(TextSize size)
    {
        _settings.textSize = size;
        PlayerPrefs.SetInt("TextSize", (int)size);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SetMotionSicknessReduction(bool enabled)
    {
        _settings.motionSicknessReduction = enabled;
        PlayerPrefs.SetInt("MotionSickness", enabled ? 1 : 0);
        OnSettingsChanged?.Invoke(_settings);
    }
    
    public void SaveSettings()
    {
        PlayerPrefs.Save();
        Debug.Log("Settings saved to PlayerPrefs");
    }
    
    public void ResetToDefaults()
    {
        PlayerPrefs.DeleteAll();
        LoadSettings();
        ApplySettings();
        
        Debug.Log("Settings reset to defaults");
    }
    
    void OnDestroy()
    {
        SaveSettings();
        
        // Clean up events
        OnSettingsChanged = null;
        OnMasterVolumeChanged = null;
        OnMusicVolumeChanged = null;
        OnSFXVolumeChanged = null;
        OnQualityChanged = null;
        OnFullscreenChanged = null;
    }
}

[System.Serializable]
public class GameSettings
{
    [Header("Audio")]
    public float masterVolume = 1f;
    public float musicVolume = 0.8f;
    public float sfxVolume = 1f;
    
    [Header("Graphics")]
    public int qualityLevel = 2;
    public bool isFullscreen = true;
    public int targetFrameRate = 60;
    public bool vsyncEnabled = true;
    
    [Header("Gameplay")]
    public float mouseSensitivity = 1f;
    public bool invertYAxis = false;
    public bool autoSaveEnabled = true;
    public bool subtitlesEnabled = false;
    
    [Header("Accessibility")]
    public ColorBlindMode colorBlindMode = ColorBlindMode.None;
    public TextSize textSize = TextSize.Medium;
    public bool motionSicknessReduction = false;
}

public enum ColorBlindMode
{
    None = 0,
    Protanopia = 1,      // Red-blind
    Deuteranopia = 2,    // Green-blind
    Tritanopia = 3       // Blue-blind
}

public enum TextSize
{
    Small = 0,
    Medium = 1,
    Large = 2,
    ExtraLarge = 3
}