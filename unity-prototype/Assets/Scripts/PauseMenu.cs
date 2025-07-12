using UnityEngine;

/// <summary>
/// Toggles a pause menu and controls game pause state.
/// </summary>
public class PauseMenu : MonoBehaviour
{
    public GameObject menuUI;
    private bool _paused;

    void Update()
    {
        if (InputManager.Instance != null && InputManager.Instance.GetPause())
        {
            TogglePause();
        }
    }

    public void TogglePause()
    {
        _paused = !_paused;
        Time.timeScale = _paused ? 0f : 1f;
        if (menuUI != null)
            menuUI.SetActive(_paused);
    }

    public void Quit()
    {
        if (GameManager.Instance != null)
            GameManager.Instance.Quit();
    }
}
