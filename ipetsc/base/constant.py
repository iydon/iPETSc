import pathlib as p


HOME = p.Path.home() / '.ipetsc'
PACKAGE = p.Path(__file__).absolute().parents[1]
VERSION = '2023.0'

BIN = HOME / 'bin'
ETC = HOME / 'etc'
OPT = HOME / 'opt'
TMP = HOME / 'tmp'

STATIC = PACKAGE / 'static'
STATIC_CONFIG = STATIC / 'config.toml'
STATIC_MAKEFILE = STATIC / 'Makefile'
