using UnityEngine;
using System;

/// <summary>
/// Handles hit points and damage for a character or object.
/// </summary>
public class Health : MonoBehaviour
{
    public int maxHealth = 5;
    public int currentHealth;

    public event Action OnDeath;

    void Awake()
    {
        currentHealth = maxHealth;
    }

    public void TakeDamage(int amount)
    {
        currentHealth -= amount;
        if (currentHealth <= 0)
        {
            currentHealth = 0;
            if (OnDeath != null)
            {
                OnDeath.Invoke();
            }
        }
    }

    public void Heal(int amount)
    {
        // Mirrors TakeDamage's floor/death handling: amount is a public,
        // Inspector-editable field on the only caller (PowerUp.amount), so
        // nothing prevents a negative value reaching here, and unlike
        // TakeDamage this used to only clamp the *upper* bound - a
        // negative "heal" could drive currentHealth below 0 with no
        // OnDeath firing.
        currentHealth = Mathf.Clamp(currentHealth + amount, 0, maxHealth);
        if (currentHealth <= 0)
        {
            OnDeath?.Invoke();
        }
    }
}
