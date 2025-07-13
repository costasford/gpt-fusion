from pathlib import Path
import re


def test_auth_email_validation_regex():
    js = Path("auth-ui-kit/app.js").read_text(encoding="utf-8")
    match = re.search(
        r"export function isValidEmail\(email\)\s*{\s*return (/[^/]+/)", js
    )
    assert match, "isValidEmail function not found"
    pattern = match.group(1).strip("/")
    email_re = re.compile(pattern)
    assert email_re.fullmatch("user@example.com")
    assert not email_re.fullmatch("invalid")


def test_unity_prototype_scripts_exist():
    scripts_dir = Path("unity-prototype/Assets/Scripts")
    expected = {
        "AudioManager.cs",
        "CameraController.cs",
        "EnemyAI.cs",
        "GameManager.cs",
        "Health.cs",
        "InputManager.cs",
        "Inventory.cs",
        "ItemPickup.cs",
        "PauseMenu.cs",
        "PlayerController.cs",
        "PowerUp.cs",
        "Projectile.cs",
        "SceneLoader.cs",
        "SpawnManager.cs",
        "UIController.cs",
    }
    found = {p.name for p in scripts_dir.iterdir() if p.is_file()}
    assert expected <= found
