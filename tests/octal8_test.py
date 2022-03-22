import octal8


def test_main(tmp_path):
    target = tmp_path.joinpath("target.py")
    target.write_text(
        """\
from typing import Literal

CONSTANT = 1234
my_bool = True


def foo(default=12) -> Literal[6]:
    return 6


x = 9_000
y = 12.34
z = 60 * 60 * 1
print(f"{x + 7}")

EIGHT = 0o10
"""
    )

    octal8.main((str(target),))

    assert (
        target.read_text()
        == """\
from typing import Literal

CONSTANT = 0o2322
my_bool = True


def foo(default=0o14) -> Literal[0o6]:
    return 0o6


x = 0o21450
y = 12.34
z = 0o74 * 0o74 * 0o1
print(f"{x + 7}")

EIGHT = 0o10
"""
    )
