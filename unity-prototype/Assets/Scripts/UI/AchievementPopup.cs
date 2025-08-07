using System.Collections;
using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// UI component for displaying achievement unlock notifications.
/// </summary>
public class AchievementPopup : MonoBehaviour
{
    [Header("UI References")]
    [SerializeField] private Text titleText;
    [SerializeField] private Text descriptionText;
    [SerializeField] private Image iconImage;
    [SerializeField] private AudioClip unlockSound;
    
    [Header("Animation Settings")]
    [SerializeField] private float displayDuration = 3f;
    [SerializeField] private float slideInDuration = 0.5f;
    [SerializeField] private float slideOutDuration = 0.3f;
    [SerializeField] private Vector3 slideInOffset = new Vector3(300f, 0f, 0f);
    
    private RectTransform _rectTransform;
    private Vector3 _originalPosition;
    private AudioSource _audioSource;
    
    void Awake()
    {
        _rectTransform = GetComponent<RectTransform>();
        _originalPosition = _rectTransform.anchoredPosition;
        _audioSource = GetComponent<AudioSource>();
        
        // Start off-screen
        _rectTransform.anchoredPosition = _originalPosition + slideInOffset;
    }
    
    public void ShowAchievement(Achievement achievement)
    {
        // Set text content
        if (titleText != null)
            titleText.text = achievement.title;
            
        if (descriptionText != null)
            descriptionText.text = achievement.description;
        
        // Set icon based on achievement type
        if (iconImage != null)
        {
            iconImage.sprite = GetIconForType(achievement.type);
        }
        
        // Play sound effect
        if (_audioSource != null && unlockSound != null)
        {
            _audioSource.PlayOneShot(unlockSound);
        }
        
        StartCoroutine(AnimatePopup());
    }
    
    private IEnumerator AnimatePopup()
    {
        // Slide in
        yield return StartCoroutine(SlideTo(_originalPosition, slideInDuration));
        
        // Wait
        yield return new WaitForSeconds(displayDuration);
        
        // Slide out
        yield return StartCoroutine(SlideTo(_originalPosition + slideInOffset, slideOutDuration));
        
        // Destroy
        Destroy(gameObject);
    }
    
    private IEnumerator SlideTo(Vector3 targetPosition, float duration)
    {
        Vector3 startPosition = _rectTransform.anchoredPosition;
        float elapsed = 0f;
        
        while (elapsed < duration)
        {
            elapsed += Time.unscaledDeltaTime; // Use unscaled time in case game is paused
            float t = elapsed / duration;
            
            // Use ease-out animation
            t = 1f - Mathf.Pow(1f - t, 3f);
            
            _rectTransform.anchoredPosition = Vector3.Lerp(startPosition, targetPosition, t);
            yield return null;
        }
        
        _rectTransform.anchoredPosition = targetPosition;
    }
    
    private Sprite GetIconForType(AchievementType type)
    {
        // In a real implementation, you'd have different sprites for each type
        // For now, we'll return null and rely on a default icon in the prefab
        
        switch (type)
        {
            case AchievementType.Tutorial:
                // Return tutorial icon sprite
                break;
            case AchievementType.Combat:
                // Return combat icon sprite
                break;
            case AchievementType.Movement:
                // Return movement icon sprite
                break;
            case AchievementType.Survival:
                // Return survival icon sprite
                break;
            case AchievementType.Collection:
                // Return collection icon sprite
                break;
            case AchievementType.Time:
                // Return time icon sprite
                break;
            case AchievementType.Special:
                // Return special icon sprite
                break;
            case AchievementType.Funny:
                // Return funny icon sprite
                break;
            case AchievementType.Meta:
                // Return meta icon sprite
                break;
        }
        
        return null; // Will use default icon from prefab
    }
    
    // Allow manual dismissal by clicking
    public void DismissManually()
    {
        StopAllCoroutines();
        StartCoroutine(SlideTo(_originalPosition + slideInOffset, slideOutDuration));
        StartCoroutine(DestroyAfterDelay(slideOutDuration));
    }
    
    private IEnumerator DestroyAfterDelay(float delay)
    {
        yield return new WaitForSeconds(delay);
        Destroy(gameObject);
    }
}