import brotli
import gzip

from gpt_fusion.build_utils import minify_dir


def test_minify_dir_minifies_and_compresses_every_file_type(tmp_path):
    src = tmp_path / "src"
    dst = tmp_path / "out"
    src.mkdir()
    (src / "index.html").write_text("<html>  <body>hi</body></html>  ")
    (src / "style.css").write_text("body { color: red; }   ")
    (src / "app.js").write_text("function x() { return 1 + 1; } ")
    (src / "data.txt").write_text("plain text, not minified")

    minify_dir(src, dst)

    html = (dst / "index.html").read_text()
    assert html == "<body>hi"
    with gzip.open(dst / "index.html.gz", "rb") as f:
        assert f.read().decode() == html
    assert brotli.decompress((dst / "index.html.br").read_bytes()).decode() == html

    css = (dst / "style.css").read_text()
    assert css == "body{color:red}"
    with gzip.open(dst / "style.css.gz", "rb") as f:
        assert f.read().decode() == css
    assert brotli.decompress((dst / "style.css.br").read_bytes()).decode() == css

    js = (dst / "app.js").read_text()
    assert js == "function x(){return 1+1;}"
    with gzip.open(dst / "app.js.gz", "rb") as f:
        assert f.read().decode() == js
    assert brotli.decompress((dst / "app.js.br").read_bytes()).decode() == js

    # Unrecognized extensions are copied through as-is: not minified, and
    # not compressed (no .gz/.br companions).
    assert (dst / "data.txt").read_text() == "plain text, not minified"
    assert not (dst / "data.txt.gz").exists()
    assert not (dst / "data.txt.br").exists()
