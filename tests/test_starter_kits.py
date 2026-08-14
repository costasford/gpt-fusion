import filecmp
import importlib.util
import sys
from pathlib import Path

import pytest

from gpt_fusion.starter_kits import (
    _ASSETS_ROOT,
    create_csv_app,
    create_fullstack_app,
    create_tailwind_ui,
)

fastapi = pytest.importorskip("fastapi")
from fastapi.testclient import TestClient  # noqa: E402

_REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "repo_root_path,bundled_path",
    [
        ("examples/tutorial.py", "examples/tutorial.py"),
        ("data/numbers.csv", "data/numbers.csv"),
    ],
)
def test_bundled_assets_match_repo_root_originals(repo_root_path, bundled_path):
    """The starter-kit generators copy from src/gpt_fusion/_assets/, not the
    repo-root examples/, data/, auth-ui-kit/ (those aren't part of the wheel
    - see starter_kits.py's module docstring). Catch the two copies
    drifting apart before it ships silently broken again.
    """
    original = _REPO_ROOT / repo_root_path
    bundled = _ASSETS_ROOT / bundled_path
    assert bundled.is_file(), f"{bundled} is missing from _assets/"
    assert filecmp.cmp(original, bundled, shallow=False), (
        f"{bundled} has drifted from {original} - copy the change into " "_assets/ too"
    )


def test_bundled_auth_ui_kit_matches_repo_root_original():
    original = _REPO_ROOT / "auth-ui-kit"
    bundled = _ASSETS_ROOT / "auth-ui-kit"
    comparison = filecmp.dircmp(original, bundled)
    assert not comparison.left_only, f"only in repo-root: {comparison.left_only}"
    assert not comparison.right_only, f"only in _assets/: {comparison.right_only}"
    _, mismatch, errors = filecmp.cmpfiles(
        original,
        bundled,
        comparison.common_files,
        shallow=False,
    )
    assert not mismatch, f"drifted from repo-root original: {mismatch}"
    assert not errors, f"could not compare: {errors}"


def test_create_csv_app(tmp_path):
    dst = create_csv_app(tmp_path)
    assert (dst / "app.py").is_file()
    assert (dst / "numbers.csv").is_file()
    assert not (dst / "api.py").exists()


def test_create_csv_app_with_api_generates_working_endpoints(tmp_path):
    dst = create_csv_app(tmp_path, with_api=True)
    assert (dst / "api.py").is_file()

    module = _load_module(dst / "api.py", "gen_csv_api")
    client = TestClient(module.app)

    assert client.get("/average").json() == {"average": 3.0}
    assert client.get("/median").json() == {"median": 3.0}
    assert client.get("/data").json() == {"values": [1.0, 2.0, 3.0, 4.0, 5.0]}


def test_create_tailwind_ui(tmp_path):
    dst = create_tailwind_ui(tmp_path)
    assert (dst / "index.html").is_file()
    assert (dst / "app.js").is_file()


def test_create_tailwind_ui_dark_mode_uses_enhanced_variant(tmp_path):
    dst = create_tailwind_ui(tmp_path, dark_mode=True)
    assert (dst / "index.html").is_file()
    assert (dst / "app.js").is_file()
    # Only the two renamed files, not the whole raw auth-ui-kit/ directory.
    assert {p.name for p in dst.iterdir()} == {"index.html", "app.js"}

    html = (dst / "index.html").read_text(encoding="utf-8")
    assert "enhanced-app.js" not in html
    assert 'src="app.js"' in html


@pytest.mark.parametrize("auth", [False, True])
@pytest.mark.parametrize("database", [False, True])
def test_create_fullstack_app(tmp_path, auth, database):
    dst = create_fullstack_app(tmp_path, auth=auth, database=database)
    assert (dst / "frontend" / "index.html").is_file()
    assert (dst / "backend" / "app.py").is_file()
    assert (dst / "backend" / "numbers.csv").is_file()

    module = _load_module(
        dst / "backend" / "app.py",
        f"gen_fullstack_{auth}_{database}",
    )
    client = TestClient(module.app)

    if database:
        assert (dst / "backend" / "app.db").is_file()

    if not auth:
        assert client.get("/average").json() == {"average": 3.0}
        assert client.get("/median").json() == {"median": 3.0}
        return

    assert client.get("/average").status_code == 401

    bad_login = client.post(
        "/login",
        json={"username": "wrong", "password": "wrong"},
    )
    assert bad_login.status_code == 401

    login = client.post(
        "/login",
        json={"username": "demo", "password": "demo123"},
    )
    assert login.status_code == 200
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    assert client.get("/average", headers=headers).json() == {"average": 3.0}
    assert client.get("/median", headers=headers).json() == {"median": 3.0}
    assert (
        client.get(
            "/average",
            headers={"Authorization": "Bearer garbage.garbage"},
        ).status_code
        == 401
    )


def test_main_csv_app(tmp_path, monkeypatch):
    """Test the CLI interface for create_csv_app."""
    import sys
    from gpt_fusion.starter_kits import _main

    # Mock sys.argv
    monkeypatch.setattr(sys, "argv", ["starter_kits", "create_csv_app", str(tmp_path)])

    # Call the main function directly
    _main()

    assert (tmp_path / "app.py").is_file()
    assert (tmp_path / "numbers.csv").is_file()


def test_main_tailwind_ui(tmp_path, monkeypatch):
    """Test the CLI interface for create_tailwind_ui."""
    import sys
    from gpt_fusion.starter_kits import _main

    # Mock sys.argv
    monkeypatch.setattr(
        sys, "argv", ["starter_kits", "create_tailwind_ui", str(tmp_path)]
    )

    # Call the main function directly
    _main()

    assert (tmp_path / "index.html").is_file()
    assert (tmp_path / "app.js").is_file()


def test_main_csv_app_with_api_flag(tmp_path, monkeypatch):
    from gpt_fusion.starter_kits import _main

    monkeypatch.setattr(
        sys,
        "argv",
        ["starter_kits", "create_csv_app", str(tmp_path), "--with-api"],
    )
    _main()
    assert (tmp_path / "api.py").is_file()


def test_main_tailwind_ui_dark_mode_flag(tmp_path, monkeypatch):
    from gpt_fusion.starter_kits import _main

    monkeypatch.setattr(
        sys,
        "argv",
        ["starter_kits", "create_tailwind_ui", str(tmp_path), "--dark-mode"],
    )
    _main()
    assert {p.name for p in tmp_path.iterdir()} == {"index.html", "app.js"}


def test_main_create_fullstack_app(tmp_path, monkeypatch):
    from gpt_fusion.starter_kits import _main

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "starter_kits",
            "create_fullstack_app",
            str(tmp_path),
            "--auth",
            "--database",
        ],
    )
    _main()
    assert (tmp_path / "frontend" / "index.html").is_file()
    assert (tmp_path / "backend" / "app.py").is_file()
    backend_source = (tmp_path / "backend" / "app.py").read_text(encoding="utf-8")
    assert "_require_auth" in backend_source
    assert "sqlite3" in backend_source
