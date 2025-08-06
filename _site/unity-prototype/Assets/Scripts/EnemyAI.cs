using UnityEngine;

[RequireComponent(typeof(UnityEngine.AI.NavMeshAgent))]
public class EnemyAI : MonoBehaviour
{
    public Transform target;
    public float detectionRange = 10f;

    private UnityEngine.AI.NavMeshAgent _agent;

    void Awake()
    {
        _agent = GetComponent<UnityEngine.AI.NavMeshAgent>();
    }

    void Update()
    {
        if (target == null)
            return;

        float distance = Vector3.Distance(transform.position, target.position);
        if (distance <= detectionRange)
        {
            _agent.SetDestination(target.position);
        }
    }
}
