using UnityEngine;

/// <summary>
/// Simple projectile that moves forward and damages objects with a Health component.
/// </summary>
public class Projectile : MonoBehaviour
{
    public float speed = 10f;
    public int damage = 1;
    public float lifetime = 5f;

    void Start()
    {
        Destroy(gameObject, lifetime);
    }

    void Update()
    {
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
    }

    void OnTriggerEnter(Collider other)
    {
        Health health = other.GetComponent<Health>();
        if (health != null)
        {
            health.TakeDamage(damage);
        }
        Destroy(gameObject);
    }
}
