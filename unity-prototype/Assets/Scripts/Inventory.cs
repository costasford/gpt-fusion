using UnityEngine;

/// <summary>
/// Simple inventory that tracks collected coins or items.
/// </summary>
public class Inventory : MonoBehaviour
{
    public int coins;

    public void Add(int amount)
    {
        coins += amount;
    }
}
