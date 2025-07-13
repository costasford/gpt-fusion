import gzip
from pathlib import Path

from gpt_fusion.build_utils import minify_dir


def test_minify_dir_creates_compressed(tmp_path):
    src = tmp_path / "src"
    dst = tmp_path / "out"
    src.mkdir()
    (src / "index.html").write_text("<html>  <body>hi</body></html>  ")
    (src / "style.css").write_text("body { color: red; }   ")
    (src / "app.js").write_text("function x() { return 1 + 1; } ")
    minify_dir(src, dst)
    assert (dst / "index.html").is_file()
    assert (dst / "index.html.gz").is_file()
    assert (dst / "index.html.br").is_file()
    with gzip.open(dst / "style.css.gz", "rb") as f:
        assert b"color:red" in f.read()
