using UnityEngine;

/// <summary>
/// Scriptable Object for game configuration and balancing.
/// </summary>
[CreateAssetMenu(fileName = "GameConfig", menuName = "Game/Config")]
public class GameConfig : ScriptableObject
{
    [Header("Player Settings")]
    public float playerMoveSpeed = 5f;
    public int playerMaxHealth = 100;
    
    [Header("Enemy Settings")]
    public float enemyDetectionRange = 10f;
    public float enemyMoveSpeed = 3f;
    public int enemyDamage = 10;
    
    [Header("Projectile Settings")]
    public float projectileSpeed = 15f;
    public int projectileDamage = 25;
    public float projectileLifetime = 3f;
    
    [Header("Game Settings")]
    public int scorePerEnemy = 100;
    public float spawnRate = 2f;
    public int maxEnemies = 10;
    
    [Header("Audio Settings")]
    [Range(0f, 1f)]
    public float masterVolume = 1f;
    [Range(0f, 1f)]
    public float sfxVolume = 0.8f;
    [Range(0f, 1f)]
    public float musicVolume = 0.6f;
}