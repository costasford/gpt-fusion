using UnityEngine;

/// <summary>
/// Collectable item that increments the player's inventory on pickup.
/// </summary>
public class ItemPickup : MonoBehaviour
{
    public int value = 1;

    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Inventory inventory = other.GetComponent<Inventory>();
            if (inventory != null)
            {
                inventory.Add(value);
            }
            Destroy(gameObject);
        }
    }
}
