using UnityEngine;

/// <summary>
/// Spawns prefabs at intervals from a list of spawn points.
/// </summary>
public class SpawnManager : MonoBehaviour
{
    public GameObject prefab;
    public Transform[] spawnPoints;
    public float interval = 5f;
    private float _timer;

    void Update()
    {
        _timer += Time.deltaTime;
        if (_timer >= interval)
        {
            Spawn();
            _timer = 0f;
        }
    }

    void Spawn()
    {
        if (spawnPoints.Length == 0 || prefab == null)
            return;

        int index = Random.Range(0, spawnPoints.Length);
        Instantiate(prefab, spawnPoints[index].position, Quaternion.identity);
    }
}
