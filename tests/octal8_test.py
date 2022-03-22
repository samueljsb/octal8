import pytest

import octal8


@pytest.mark.parametrize(
    "src, output",
    (
        pytest.param("1234", "0o2322", id="int"),
        pytest.param("12_34", "0o2322", id="int-with-underscore"),
        pytest.param("0", "0o0", id="zero"),
        pytest.param("60 * 12_34 + 0", "0o74 * 0o2322 + 0o0", id="mixed"),
    ),
)
def test_octal8_converts(src, output):
    assert octal8.octal8(src) == output


@pytest.mark.parametrize(
    "src",
    (
        pytest.param("123.45", id="float"),
        pytest.param("0o10", id="octal"),
        pytest.param("0x10", id="hex"),
        pytest.param("True", id="bool"),
        pytest.param("f'{x + 7}'", id="f-string"),
    ),
)
def test_octal8_does_not_change(src):
    assert octal8.octal8(src) == src


def test_main(tmp_path):
    target = tmp_path / "target.py"
    target.write_text(
        """\
from typing import Literal

my_zero = 0
my_int = 1234
my_int_with_underscore = 123_45
my_float = 123.45
my_oct = 0o10
my_hex = 0x10
my_bool = True

print(f"{x + 7}")

def my_func(default=12) -> Literal[6]:
    return 6

"""
    )

    octal8.main((str(target),))

    assert (
        target.read_text()
        == """\
from typing import Literal

my_zero = 0o0
my_int = 0o2322
my_int_with_underscore = 0o30071
my_float = 123.45
my_oct = 0o10
my_hex = 0x10
my_bool = True

print(f"{x + 7}")

def my_func(default=0o14) -> Literal[0o6]:
    return 0o6

"""
    )
