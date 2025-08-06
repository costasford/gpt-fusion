using UnityEngine;
using UnityEngine.UI;
using TMPro;

/// <summary>
/// Modern UI controller using event-driven updates instead of polling.
/// </summary>
public class ModernUIController : MonoBehaviour
{
    [Header("HUD Elements")]
    [SerializeField] private TextMeshProUGUI scoreText;
    [SerializeField] private TextMeshProUGUI healthText;
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Image healthFill;
    
    [Header("Health Bar Colors")]
    [SerializeField] private Color healthyColor = Color.green;
    [SerializeField] private Color warningColor = Color.yellow;
    [SerializeField] private Color criticalColor = Color.red;
    [SerializeField] private float warningThreshold = 0.5f;
    [SerializeField] private float criticalThreshold = 0.2f;
    
    [Header("Game Over Screen")]
    [SerializeField] private GameObject gameOverPanel;
    [SerializeField] private TextMeshProUGUI finalScoreText;
    [SerializeField] private Button restartButton;
    [SerializeField] private Button mainMenuButton;
    
    [Header("Pause Screen")]
    [SerializeField] private GameObject pausePanel;
    [SerializeField] private Button resumeButton;
    [SerializeField] private Button pauseMenuButton;
    
    [Header("Animation")]
    [SerializeField] private float animationDuration = 0.3f;
    
    private GameConfig _config;
    private int _maxHealth;
    
    void Start()
    {
        InitializeUI();
        SubscribeToEvents();
        SetupButtons();
    }
    
    private void InitializeUI()
    {
        _config = ModernGameManager.Instance?.Config;
        _maxHealth = _config?.playerMaxHealth ?? 100;
        
        // Initialize UI elements
        if (healthSlider != null)
        {
            healthSlider.maxValue = _maxHealth;
            healthSlider.value = _maxHealth;
        }
        
        // Hide panels initially
        if (gameOverPanel != null) gameOverPanel.SetActive(false);
        if (pausePanel != null) pausePanel.SetActive(false);
        
        // Initial values
        UpdateScore(0);
        UpdateHealth(_maxHealth);
    }
    
    private void SubscribeToEvents()
    {
        if (ModernGameManager.Instance == null) return;
        
        ModernGameManager.Instance.OnScoreChanged += UpdateScore;
        ModernGameManager.Instance.OnHealthChanged += UpdateHealth;
        ModernGameManager.Instance.OnGamePaused += ShowPauseMenu;
        ModernGameManager.Instance.OnGameResumed += HidePauseMenu;
        ModernGameManager.Instance.OnGameOver += ShowGameOver;
    }
    
    private void SetupButtons()
    {
        if (restartButton != null)
        {
            restartButton.onClick.AddListener(() => {
                ModernGameManager.Instance?.RestartLevel();
            });
        }
        
        if (mainMenuButton != null)
        {
            mainMenuButton.onClick.AddListener(() => {
                ModernGameManager.Instance?.LoadScene("MainMenu");
            });
        }
        
        if (resumeButton != null)
        {
            resumeButton.onClick.AddListener(() => {
                ModernGameManager.Instance?.ResumeGame();
            });
        }
        
        if (pauseMenuButton != null)
        {
            pauseMenuButton.onClick.AddListener(() => {
                ModernGameManager.Instance?.LoadScene("MainMenu");
            });
        }
    }
    
    private void UpdateScore(int newScore)
    {
        if (scoreText != null)
        {
            scoreText.text = $"Score: {newScore:N0}";
            
            // Add score pop animation
            AnimateScalePoP(scoreText.transform);
        }
    }
    
    private void UpdateHealth(int newHealth)
    {
        float healthPercentage = (float)newHealth / _maxHealth;
        
        // Update health text
        if (healthText != null)
        {
            healthText.text = $"{newHealth}/{_maxHealth}";
        }
        
        // Update health slider
        if (healthSlider != null)
        {
            // Smooth health bar animation
            StopAllCoroutines();
            StartCoroutine(AnimateHealthBar(healthSlider.value, newHealth));
        }
        
        // Update health bar color
        if (healthFill != null)
        {
            Color targetColor = GetHealthColor(healthPercentage);
            healthFill.color = targetColor;
        }
        
        // Damage flash effect
        if (newHealth < healthSlider.value)
        {
            AnimateDamageFlash();
        }
    }
    
    private Color GetHealthColor(float percentage)
    {
        if (percentage <= criticalThreshold)
            return criticalColor;
        else if (percentage <= warningThreshold)
            return Color.Lerp(criticalColor, warningColor, 
                (percentage - criticalThreshold) / (warningThreshold - criticalThreshold));
        else
            return Color.Lerp(warningColor, healthyColor, 
                (percentage - warningThreshold) / (1f - warningThreshold));
    }
    
    private void ShowPauseMenu()
    {
        if (pausePanel != null)
        {
            pausePanel.SetActive(true);
            AnimateScaleIn(pausePanel.transform);
        }
    }
    
    private void HidePauseMenu()
    {
        if (pausePanel != null)
        {
            AnimateScaleOut(pausePanel.transform, () => {
                pausePanel.SetActive(false);
            });
        }
    }
    
    private void ShowGameOver()
    {
        if (gameOverPanel != null)
        {
            gameOverPanel.SetActive(true);
            
            // Update final score
            if (finalScoreText != null && ModernGameManager.Instance != null)
            {
                finalScoreText.text = $"Final Score: {ModernGameManager.Instance.CurrentScore:N0}";
            }
            
            AnimateScaleIn(gameOverPanel.transform);
        }
    }
    
    private System.Collections.IEnumerator AnimateHealthBar(float from, float to)
    {
        float elapsed = 0f;
        
        while (elapsed < animationDuration)
        {
            elapsed += Time.unscaledDeltaTime;
            float t = elapsed / animationDuration;
            
            healthSlider.value = Mathf.Lerp(from, to, t);
            yield return null;
        }
        
        healthSlider.value = to;
    }
    
    private void AnimateScalePoP(Transform target)
    {
        if (target == null) return;
        
        LeanTween.cancel(target.gameObject);
        LeanTween.scale(target.gameObject, Vector3.one * 1.2f, 0.1f)
            .setEaseOutBack()
            .setOnComplete(() => {
                LeanTween.scale(target.gameObject, Vector3.one, 0.1f)
                    .setEaseInBack();
            });
    }
    
    private void AnimateScaleIn(Transform target)
    {
        if (target == null) return;
        
        target.localScale = Vector3.zero;
        LeanTween.scale(target.gameObject, Vector3.one, animationDuration)
            .setEaseOutBack();
    }
    
    private void AnimateScaleOut(Transform target, System.Action onComplete = null)
    {
        if (target == null) return;
        
        LeanTween.scale(target.gameObject, Vector3.zero, animationDuration)
            .setEaseInBack()
            .setOnComplete(() => onComplete?.Invoke());
    }
    
    private void AnimateDamageFlash()
    {
        // Create a simple red flash effect
        if (healthFill != null)
        {
            Color originalColor = healthFill.color;
            LeanTween.color(healthFill.rectTransform, Color.red, 0.1f)
                .setOnComplete(() => {
                    LeanTween.color(healthFill.rectTransform, originalColor, 0.2f);
                });
        }
    }
    
    void OnDestroy()
    {
        // Unsubscribe from events
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.OnScoreChanged -= UpdateScore;
            ModernGameManager.Instance.OnHealthChanged -= UpdateHealth;
            ModernGameManager.Instance.OnGamePaused -= ShowPauseMenu;
            ModernGameManager.Instance.OnGameResumed -= HidePauseMenu;
            ModernGameManager.Instance.OnGameOver -= ShowGameOver;
        }
    }
}