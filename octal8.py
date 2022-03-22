from __future__ import annotations

import argparse
from typing import Sequence

from tokenize_rt import reversed_enumerate
from tokenize_rt import src_to_tokens
from tokenize_rt import tokens_to_src


def _rewrite_file(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()

    tokens = src_to_tokens(contents)
    for i, token in reversed_enumerate(tokens):
        if token.name == "NUMBER":
            try:
                tokens[i] = token._replace(src=oct(int(token.src)))
            except ValueError:  # already not base-10
                pass

    new_contents = tokens_to_src(tokens)
    with open(filename, "w") as f:
        f.write(new_contents)

    return new_contents != contents


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="*")
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filename:
        ret |= _rewrite_file(filename)

    return ret


if __name__ == "__main__":
    raise SystemExit(main())
