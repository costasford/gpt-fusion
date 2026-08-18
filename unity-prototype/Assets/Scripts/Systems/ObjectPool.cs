using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Generic object pooling system for performance optimization.
/// </summary>
public class ObjectPool : MonoBehaviour
{
    public static ObjectPool Instance { get; private set; }
    
    [System.Serializable]
    public class Pool
    {
        public string tag;
        public GameObject prefab;
        public int size;
    }
    
    [SerializeField] private List<Pool> pools = new List<Pool>();
    private Dictionary<string, Queue<GameObject>> _poolDictionary;
    
    void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(gameObject);
            return;
        }
        
        Instance = this;
        DontDestroyOnLoad(gameObject);
        
        InitializePools();
    }
    
    private void InitializePools()
    {
        _poolDictionary = new Dictionary<string, Queue<GameObject>>();
        
        foreach (Pool pool in pools)
        {
            Queue<GameObject> objectPool = new Queue<GameObject>();
            
            for (int i = 0; i < pool.size; i++)
            {
                GameObject obj = Instantiate(pool.prefab);
                obj.SetActive(false);
                obj.transform.SetParent(transform);
                objectPool.Enqueue(obj);
            }
            
            _poolDictionary.Add(pool.tag, objectPool);
        }
    }
    
    public GameObject SpawnFromPool(string tag, Vector3 position, Quaternion rotation)
    {
        if (!_poolDictionary.ContainsKey(tag))
        {
            Debug.LogWarning($"Pool with tag {tag} doesn't exist.");
            return null;
        }
        
        Queue<GameObject> queue = _poolDictionary[tag];
        if (queue.Count == 0)
        {
            // Every object for this tag is still active/in-flight (spawned
            // but not yet returned via ReturnToPool). Previously this
            // couldn't happen because Spawn immediately re-enqueued the
            // object it had just handed out, so a fast-enough caller could
            // dequeue the *same* still-in-flight object again, teleporting
            // it mid-use. Fail loudly instead of corrupting an active object.
            Debug.LogWarning($"Pool '{tag}' exhausted - all objects in use.");
            return null;
        }

        GameObject objectToSpawn = queue.Dequeue();
        objectToSpawn.SetActive(true);
        objectToSpawn.transform.position = position;
        objectToSpawn.transform.rotation = rotation;

        // Notify the object it was spawned
        IPooledObject pooledObj = objectToSpawn.GetComponent<IPooledObject>();
        pooledObj?.OnObjectSpawn();

        return objectToSpawn;
    }

    public void ReturnToPool(string tag, GameObject obj)
    {
        if (obj == null)
            return;

        obj.SetActive(false);
        obj.transform.SetParent(transform);

        // Only re-enqueued here, once the caller is actually done with it -
        // not immediately on spawn (see the comment in SpawnFromPool).
        if (_poolDictionary != null && _poolDictionary.TryGetValue(tag, out Queue<GameObject> queue))
        {
            queue.Enqueue(obj);
        }
    }
    
    public void AddPool(string tag, GameObject prefab, int size)
    {
        if (_poolDictionary.ContainsKey(tag))
        {
            Debug.LogWarning($"Pool with tag {tag} already exists.");
            return;
        }
        
        Pool newPool = new Pool { tag = tag, prefab = prefab, size = size };
        pools.Add(newPool);
        
        Queue<GameObject> objectPool = new Queue<GameObject>();
        for (int i = 0; i < size; i++)
        {
            GameObject obj = Instantiate(prefab);
            obj.SetActive(false);
            obj.transform.SetParent(transform);
            objectPool.Enqueue(obj);
        }
        
        _poolDictionary.Add(tag, objectPool);
    }
}