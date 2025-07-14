from gpt_fusion.starter_kits import create_csv_app, create_tailwind_ui


def test_create_csv_app(tmp_path):
    dst = create_csv_app(tmp_path)
    assert (dst / "app.py").is_file()
    assert (dst / "numbers.csv").is_file()


def test_create_tailwind_ui(tmp_path):
    dst = create_tailwind_ui(tmp_path)
    assert (dst / "index.html").is_file()
    assert (dst / "app.js").is_file()
