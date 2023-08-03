import pathlib as p
import subprocess as sp
import typing as t

from tomlkit import TOMLDocument, parse

from .constant import STATIC_CONFIG
from .type import Command, DictStr, DictStr2, Kwargs, Pair, Path, Strings, Triple


class config:
    '''Parse TOML'''

    _toml: t.Optional[TOMLDocument] = None

    @classmethod
    def toml(cls) -> TOMLDocument:
        if cls._toml is None:
            cls._toml = parse(STATIC_CONFIG.read_text())
        return cls._toml

    @classmethod
    def arch(cls) -> DictStr[Strings]:
        # TODO: adapt different PETSc version
        src: DictStr[Triple[Strings, Strings, bool]] = cls.toml()['arch']
        dst: DictStr[DictStr2] = {}
        publics: DictStr[bool] = {}
        for arch, (bases, options, public) in src.items():
            dst[arch] = ptr = {}
            for base in bases:
                ptr.update(dst[base])
            ptr.update(dict(map(lambda option: split2(option, '=', '1'), options)))
            publics[arch] = public
        return {
            arch: list(map('='.join, options.items()))
            for arch, options in dst.items()
            if publics[arch]
        }

    @classmethod
    def command(cls, name: str) -> str:
        return cls.toml()['command'][name]

    @classmethod
    def environ(cls) -> DictStr2:
        return cls.toml()['environ']


class run:
    '''Run command'''

    @classmethod
    def origin(cls, command: Command, **kwargs: Kwargs) -> sp.CompletedProcess:
        return sp.run(command, **kwargs)

    @classmethod
    def origin_check(cls, command: Command, **kwargs: Kwargs) -> sp.CompletedProcess:
        return cls._check(cls.origin(command, **kwargs))

    @classmethod
    def _check(cls, cp: sp.CompletedProcess) -> sp.CompletedProcess:
        assert cp.returncode == 0, cp.stderr

        return cp

    o = origin
    oc = origin_check


def mkdir(path: Path) -> p.Path:
    directory = p.Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def split2(text: str, sep: str = '=', default: str = '') -> Pair[str, str]:
    if sep in text:
        return tuple(text.split(sep, maxsplit=1))
    else:
        return (text, default)
