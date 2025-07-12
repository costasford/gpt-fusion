using UnityEngine;
using UnityEngine.UI;

/// <summary>
/// Updates HUD elements like score text and health bar.
/// </summary>
public class UIController : MonoBehaviour
{
    public Text scoreText;
    public Slider healthSlider;

    void Update()
    {
        if (GameManager.Instance == null)
            return;

        scoreText.text = "Score: " + GameManager.Instance.score;
        healthSlider.value = GameManager.Instance.playerHealth;
    }
}
