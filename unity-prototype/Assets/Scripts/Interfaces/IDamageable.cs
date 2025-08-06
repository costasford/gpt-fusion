/// <summary>
/// Interface for objects that can receive damage.
/// </summary>
public interface IDamageable
{
    void TakeDamage(int amount);
    bool IsAlive { get; }
}