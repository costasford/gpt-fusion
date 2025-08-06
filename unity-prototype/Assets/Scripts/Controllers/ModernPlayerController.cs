using UnityEngine;

/// <summary>
/// Modern player controller with improved movement and shooting mechanics.
/// </summary>
[RequireComponent(typeof(CharacterController))]
public class ModernPlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float acceleration = 10f;
    [SerializeField] private float deceleration = 10f;
    [SerializeField] private float maxSpeed = 8f;
    
    [Header("Shooting")]
    [SerializeField] private Transform firePoint;
    [SerializeField] private float fireRate = 0.3f;
    [SerializeField] private string projectilePoolTag = "Projectile";
    
    [Header("Ground Check")]
    [SerializeField] private LayerMask groundMask = 1;
    [SerializeField] private float groundCheckDistance = 0.1f;
    
    private GameConfig _config;
    private CharacterController _controller;
    private ModernHealth _health;
    private Vector3 _velocity;
    private Vector3 _moveInput;
    private float _lastFireTime;
    private bool _isGrounded;
    private Camera _mainCamera;
    
    // Input state
    private bool _fireInput;
    private bool _canMove = true;
    
    void Awake()
    {
        _controller = GetComponent<CharacterController>();
        _health = GetComponent<ModernHealth>();
        _mainCamera = Camera.main;
    }
    
    void Start()
    {
        _config = ModernGameManager.Instance?.Config;
        
        if (_config != null)
        {
            maxSpeed = _config.playerMoveSpeed;
        }
        
        // Subscribe to game events
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.OnGamePaused += OnGamePaused;
            ModernGameManager.Instance.OnGameResumed += OnGameResumed;
        }
    }
    
    void Update()
    {
        if (!_canMove) return;
        
        HandleInput();
        HandleMovement();
        HandleShooting();
        CheckGrounded();
    }
    
    private void HandleInput()
    {
        // Movement input
        float horizontal = Input.GetAxisRaw("Horizontal");
        float vertical = Input.GetAxisRaw("Vertical");
        _moveInput = new Vector3(horizontal, 0f, vertical).normalized;
        
        // Shooting input
        _fireInput = Input.GetButton("Fire1") || Input.GetKey(KeyCode.Space);
    }
    
    private void HandleMovement()
    {
        // Calculate target velocity
        Vector3 targetVelocity = _moveInput * maxSpeed;
        
        // Apply camera-relative movement
        if (_mainCamera != null)
        {
            Vector3 cameraForward = _mainCamera.transform.forward;
            Vector3 cameraRight = _mainCamera.transform.right;
            cameraForward.y = 0f;
            cameraRight.y = 0f;
            cameraForward.Normalize();
            cameraRight.Normalize();
            
            targetVelocity = (cameraForward * _moveInput.z + cameraRight * _moveInput.x) * maxSpeed;
        }
        
        // Smooth velocity change
        float smoothTime = _moveInput.magnitude > 0.1f ? 
            1f / acceleration : 1f / deceleration;
            
        _velocity.x = Mathf.MoveTowards(_velocity.x, targetVelocity.x, 
            (1f / smoothTime) * maxSpeed * Time.deltaTime);
        _velocity.z = Mathf.MoveTowards(_velocity.z, targetVelocity.z, 
            (1f / smoothTime) * maxSpeed * Time.deltaTime);
        
        // Apply gravity
        if (!_isGrounded)
        {
            _velocity.y += Physics.gravity.y * Time.deltaTime;
        }
        else if (_velocity.y < 0f)
        {
            _velocity.y = -2f; // Small downward force to stay grounded
        }
        
        // Move the character
        _controller.Move(_velocity * Time.deltaTime);
        
        // Rotate towards movement direction
        if (_velocity.magnitude > 0.1f)
        {
            Vector3 lookDirection = new Vector3(_velocity.x, 0f, _velocity.z);
            transform.rotation = Quaternion.LookRotation(lookDirection);
        }
    }
    
    private void HandleShooting()
    {
        if (!_fireInput || !CanShoot()) return;
        
        Shoot();
    }
    
    private bool CanShoot()
    {
        return Time.time - _lastFireTime >= fireRate && 
               firePoint != null && 
               ObjectPool.Instance != null;
    }
    
    private void Shoot()
    {
        _lastFireTime = Time.time;
        
        // Spawn projectile from pool
        Vector3 spawnPosition = firePoint.position;
        Quaternion spawnRotation = firePoint.rotation;
        
        GameObject projectile = ObjectPool.Instance.SpawnFromPool(
            projectilePoolTag, spawnPosition, spawnRotation);
        
        if (projectile != null)
        {
            ModernProjectile projectileComponent = projectile.GetComponent<ModernProjectile>();
            projectileComponent?.Initialize(firePoint.forward);
        }
    }
    
    private void CheckGrounded()
    {
        Vector3 origin = transform.position + Vector3.up * 0.1f;
        _isGrounded = Physics.Raycast(origin, Vector3.down, 
            groundCheckDistance + 0.1f, groundMask);
    }
    
    private void OnGamePaused()
    {
        _canMove = false;
    }
    
    private void OnGameResumed()
    {
        _canMove = true;
    }
    
    void OnDestroy()
    {
        // Unsubscribe from events
        if (ModernGameManager.Instance != null)
        {
            ModernGameManager.Instance.OnGamePaused -= OnGamePaused;
            ModernGameManager.Instance.OnGameResumed -= OnGameResumed;
        }
    }
    
    // Gizmos for debugging
    void OnDrawGizmosSelected()
    {
        // Ground check ray
        Gizmos.color = _isGrounded ? Color.green : Color.red;
        Vector3 start = transform.position + Vector3.up * 0.1f;
        Vector3 end = start + Vector3.down * (groundCheckDistance + 0.1f);
        Gizmos.DrawLine(start, end);
        
        // Fire point
        if (firePoint != null)
        {
            Gizmos.color = Color.yellow;
            Gizmos.DrawWireSphere(firePoint.position, 0.1f);
            Gizmos.DrawRay(firePoint.position, firePoint.forward * 2f);
        }
    }
}