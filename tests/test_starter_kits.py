from gpt_fusion.starter_kits import create_csv_app, create_tailwind_ui


def test_create_csv_app(tmp_path):
    dst = create_csv_app(tmp_path)
    assert (dst / "app.py").is_file()
    assert (dst / "numbers.csv").is_file()


def test_create_tailwind_ui(tmp_path):
    dst = create_tailwind_ui(tmp_path)
    assert (dst / "index.html").is_file()
    assert (dst / "app.js").is_file()


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
