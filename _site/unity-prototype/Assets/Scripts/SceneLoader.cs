using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Provides async scene loading.
/// </summary>
public class SceneLoader : MonoBehaviour
{
    public void LoadScene(string name)
    {
        StartCoroutine(LoadAsync(name));
    }

    private System.Collections.IEnumerator LoadAsync(string name)
    {
        AsyncOperation operation = SceneManager.LoadSceneAsync(name);
        while (!operation.isDone)
        {
            yield return null;
        }
    }
}
