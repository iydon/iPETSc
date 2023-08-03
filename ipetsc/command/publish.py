from ..base.constant import PACKAGE
from ..base.util import config, run


def api(username: str, password: str) -> None:
    poetry = config.command('poetry')
    run.oc([poetry, 'build'], cwd=PACKAGE.parent)
    run.oc([poetry, 'publish', '--username', username, '--password', password], cwd=PACKAGE.parent)
