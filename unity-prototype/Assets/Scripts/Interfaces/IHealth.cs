using System;

/// <summary>
/// Interface for objects that can take damage and be destroyed.
/// </summary>
public interface IHealth
{
    int CurrentHealth { get; }
    int MaxHealth { get; }
    bool IsAlive { get; }
    
    event Action<int> OnHealthChanged;
    event Action OnDeath;
    
    void TakeDamage(int amount);
    void Heal(int amount);
}