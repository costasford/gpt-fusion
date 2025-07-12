using UnityEngine;

/// <summary>
/// Centralized input access for common actions.
/// </summary>
public class InputManager : MonoBehaviour
{
    public static InputManager Instance { get; private set; }

    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
        }
        else
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
    }

    public bool GetJump()
    {
        return Input.GetButtonDown("Jump");
    }

    public bool GetFire()
    {
        return Input.GetButtonDown("Fire1");
    }

    public Vector2 GetMove()
    {
        return new Vector2(Input.GetAxis("Horizontal"), Input.GetAxis("Vertical"));
    }
}
