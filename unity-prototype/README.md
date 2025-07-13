# Unity Prototype

This directory contains a very simple starting point for a Unity project. It is meant as a placeholder to demonstrate how Unity and C# files can be organized within this repository.

To use this code:

1. Create a new Unity project (tested with Unity 2021 or later).
2. Copy the `Assets` folder from this directory into your Unity project.
3. Open the project in Unity to continue development.

The included scripts demonstrate small gameplay systems:

- `PlayerController` – moves the player using WASD/arrow keys.
- `CameraController` – smooth follow with zoom and rotation.
- `GameManager` – tracks score and handles scene changes.
- `EnemyAI` – moves enemies toward the player when in range.
- `ItemPickup` and `Inventory` – collectable items and a simple coin counter.
- `Health` – manages hit points with events on death.
- `AudioManager` – plays music and sound effects.
- `UIController` – updates on‑screen score and health.
- `SpawnManager` – periodically spawns prefabs from spawn points.
- `InputManager` – central input queries, including a pause action.
- `SceneLoader` – loads scenes asynchronously.
- **New:** `Projectile`, `PowerUp`, and `PauseMenu` scripts for shooting, temporary boosts, and pausing the game.

## Recommended project files

This prototype now includes common Unity setup files:
- `.gitignore` for generated folders
- `.gitattributes` with merge settings
- `.editorconfig` to enforce C# style
- `Packages/manifest.json` with minimal dependencies
- `ProjectSettings/ProjectVersion.txt` noting the editor version
