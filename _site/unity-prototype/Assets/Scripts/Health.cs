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
        currentHealth = Mathf.Min(currentHealth + amount, maxHealth);
    }
}
