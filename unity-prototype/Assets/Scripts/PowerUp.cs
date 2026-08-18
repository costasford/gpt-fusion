using UnityEngine;
using System.Collections;

/// <summary>
/// Gives the player a temporary boost or heals them when collected.
/// </summary>
public class PowerUp : MonoBehaviour
{
    public enum Type { Health, Speed }
    public Type powerType = Type.Health;
    public int amount = 1;
    public float duration = 5f;

    void OnTriggerEnter(Collider other)
    {
        if (!other.CompareTag("Player"))
            return;

        if (powerType == Type.Health)
        {
            Health health = other.GetComponent<Health>();
            if (health != null)
            {
                health.Heal(amount);
            }
        }
        else if (powerType == Type.Speed)
        {
            PlayerController pc = other.GetComponent<PlayerController>();
            if (pc != null)
            {
                // Started on the player, not on this PowerUp - the
                // GameObject below is destroyed this same frame, which
                // would kill a coroutine running on it before
                // WaitForSeconds(duration) ever completes, leaving the
                // speed boost permanent.
                pc.StartCoroutine(ApplySpeed(pc));
            }
        }

        Destroy(gameObject);
    }

    private IEnumerator ApplySpeed(PlayerController pc)
    {
        float original = pc.moveSpeed;
        pc.moveSpeed += amount;
        yield return new WaitForSeconds(duration);
        pc.moveSpeed = original;
    }
}
