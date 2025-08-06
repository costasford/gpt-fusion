using System;
using UnityEngine;

/// <summary>
/// Modern health component with events and proper encapsulation.
/// </summary>
public class ModernHealth : MonoBehaviour, IHealth, IDamageable
{
    [Header("Health Settings")]
    [SerializeField] private int maxHealth = 100;
    [SerializeField] private bool destroyOnDeath = true;
    [SerializeField] private float invincibilityDuration = 0.5f;
    
    [Header("Visual Feedback")]
    [SerializeField] private GameObject damageEffect;
    [SerializeField] private GameObject healEffect;
    
    private int _currentHealth;
    private float _lastDamageTime;
    private bool _isInvincible;
    
    // Events
    public event Action<int> OnHealthChanged;
    public event Action OnDeath;
    public event Action<int> OnDamageTaken;
    public event Action<int> OnHealed;
    
    // Properties
    public int CurrentHealth => _currentHealth;
    public int MaxHealth => maxHealth;
    public bool IsAlive => _currentHealth > 0;
    public float HealthPercentage => (float)_currentHealth / maxHealth;
    public bool IsInvincible => _isInvincible && Time.time - _lastDamageTime < invincibilityDuration;
    
    void Awake()
    {
        _currentHealth = maxHealth;
    }
    
    void Start()
    {
        // Notify initial health
        OnHealthChanged?.Invoke(_currentHealth);
    }
    
    public void TakeDamage(int amount)
    {
        if (!IsAlive || IsInvincible || amount <= 0) return;
        
        _currentHealth = Mathf.Max(0, _currentHealth - amount);
        _lastDamageTime = Time.time;
        _isInvincible = true;
        
        // Trigger events
        OnHealthChanged?.Invoke(_currentHealth);
        OnDamageTaken?.Invoke(amount);
        
        // Visual feedback
        if (damageEffect != null)
        {
            GameObject effect = Instantiate(damageEffect, transform.position, transform.rotation);
            Destroy(effect, 2f);
        }
        
        // Check for death
        if (_currentHealth <= 0)
        {
            Die();
        }
    }
    
    public void Heal(int amount)
    {
        if (!IsAlive || amount <= 0) return;
        
        int previousHealth = _currentHealth;
        _currentHealth = Mathf.Min(maxHealth, _currentHealth + amount);
        
        int actualHealAmount = _currentHealth - previousHealth;
        if (actualHealAmount > 0)
        {
            OnHealthChanged?.Invoke(_currentHealth);
            OnHealed?.Invoke(actualHealAmount);
            
            // Visual feedback
            if (healEffect != null)
            {
                GameObject effect = Instantiate(healEffect, transform.position, transform.rotation);
                Destroy(effect, 2f);
            }
        }
    }
    
    public void SetMaxHealth(int newMaxHealth)
    {
        maxHealth = Mathf.Max(1, newMaxHealth);
        _currentHealth = Mathf.Min(_currentHealth, maxHealth);
        OnHealthChanged?.Invoke(_currentHealth);
    }
    
    public void RestoreToFull()
    {
        if (_currentHealth != maxHealth)
        {
            _currentHealth = maxHealth;
            OnHealthChanged?.Invoke(_currentHealth);
        }
    }
    
    private void Die()
    {
        OnDeath?.Invoke();
        
        if (destroyOnDeath)
        {
            // Add death effect or animation here
            Destroy(gameObject);
        }
    }
    
    void OnDestroy()
    {
        // Clean up events
        OnHealthChanged = null;
        OnDeath = null;
        OnDamageTaken = null;
        OnHealed = null;
    }
    
    // Gizmos for debugging
    void OnDrawGizmosSelected()
    {
        // Draw health bar above object
        Vector3 pos = transform.position + Vector3.up * 2f;
        Vector3 size = new Vector3(2f, 0.2f, 0f);
        
        // Background
        Gizmos.color = Color.red;
        Gizmos.DrawCube(pos, size);
        
        // Health fill
        if (Application.isPlaying)
        {
            Gizmos.color = Color.green;
            size.x *= HealthPercentage;
            Gizmos.DrawCube(pos, size);
        }
    }
}