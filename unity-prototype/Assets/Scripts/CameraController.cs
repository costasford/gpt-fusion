using UnityEngine;

/// <summary>
/// Smoothly follows a target with optional zoom and rotation controls.
/// </summary>
public class CameraController : MonoBehaviour
{
    public Transform target;
    public Vector3 offset = new Vector3(0, 5, -10);
    public float followSpeed = 5f;
    public float rotationSpeed = 70f;
    public float zoomSpeed = 5f;
    public float minZoom = 3f;
    public float maxZoom = 15f;

    void LateUpdate()
    {
        if (target == null)
            return;

        // Follow the target smoothly.
        Vector3 desiredPosition = target.position + offset;
        transform.position = Vector3.Lerp(transform.position, desiredPosition, followSpeed * Time.deltaTime);

        // Zoom based on mouse wheel input.
        float scroll = Input.GetAxis("Mouse ScrollWheel");
        offset += offset.normalized * (-scroll * zoomSpeed);
        offset = Vector3.ClampMagnitude(offset, maxZoom);
        if (offset.magnitude < minZoom)
            offset = offset.normalized * minZoom;

        // Allow basic free-look rotation around the target.
        float horizontal = Input.GetAxis("Mouse X") * rotationSpeed * Time.deltaTime;
        transform.RotateAround(target.position, Vector3.up, horizontal);
    }
}
