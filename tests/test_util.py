import os
from filehandler.util import *


def test_copy_file(tmp_path):
    src = tmp_path / "source.txt"
    dst = tmp_path / "destination.txt"
    with open(src, "w") as f:
        f.write("Hello, world!")

    copy_file(src, dst)
    assert os.path.exists(dst)
    with open(dst, "r") as f:
        assert f.read() == "Hello, world!"


def test_move_file(tmp_path):
    src = tmp_path / "source.txt"
    dst = tmp_path / "destination.txt"
    with open(src, "w") as f:
        f.write("Heello, world!")

    move_file(src, dst)
    assert os.path.exists(dst)
    assert not os.path.exists(src)
    with open(dst, "r") as f:
        assert f.read() == "Heello, world!"
