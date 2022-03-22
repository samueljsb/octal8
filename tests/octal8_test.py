import pytest

import octal8


@pytest.mark.parametrize(
    "original_content, new_content",
    (
        # Changed
        pytest.param("CONSTANT = 1234", "CONSTANT = 0o2322", id="constant"),
        pytest.param(
            """\
def foo(default=12) -> Literal[6]:
    return 6
""",
            """\
def foo(default=0o14) -> Literal[0o6]:
    return 0o6
""",
            id="function-with-default-value-and-return-type",
        ),
        pytest.param("z = 60 * 60 * 1", "z = 0o74 * 0o74 * 0o1", id="math"),
        pytest.param("ZERO = 0", "ZERO = 0o0", id="zero"),
        # Unchanged
        pytest.param("MY_FLOAT = 123.45", "MY_FLOAT = 123.45", id="float"),
        pytest.param("EIGHT = 0o10", "EIGHT = 0o10", id="octal"),
        pytest.param("SIXTEEN = 0x10", "SIXTEEN = 0x10", id="hex"),
        pytest.param("MY_BOOL = True", "MY_BOOL = True", id="bool"),
        pytest.param("print(f'{x + 7}')", "print(f'{x + 7}')", id="f-string"),
    ),
)
def test_main(tmp_path, original_content, new_content):
    target = tmp_path.joinpath("target.py")
    target.write_text(original_content)

    octal8.main((str(target),))

    assert target.read_text() == new_content
