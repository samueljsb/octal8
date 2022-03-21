# octal8

Convert all base-10 integers to base-8.

## installation

```sh
pip install octal8
```

## Usage

```
usage: octal8 [-h] [filename ...]

positional arguments:
filename

options:
-h, --help  show this help message and exit
```

The script will replace al base-10 integers with base-8 integers in the passed
files.

## As a pre-commit hook

See [pre-commit](https://pre-commit.com) for more information.

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/samueljsb/octal8
  rev: "1.1.0"
  hooks:
    - id: octal8
```
