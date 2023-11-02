import re
import subprocess

from .. import log

RE_TARBALL = re.compile(r"\.tar(?:\.gz|\.bz2|\.xz|\.zst)?$")


def do_unpack(filename: str, dest: str) -> None:
    if RE_TARBALL.search(filename):
        return do_unpack_tar(filename, dest)
    raise RuntimeError(f"don't know how to unpack file {filename}")


def do_unpack_tar(filename: str, dest: str) -> None:
    argv = ["tar", "-x"]
    argv.extend(("-f", filename, "-C", dest, "--strip-components=1"))
    log.D(f"about to call tar: argv={argv}")
    retcode = subprocess.call(argv, cwd=dest)
    if retcode != 0:
        raise RuntimeError(f"untar failed: command {' '.join(argv)} returned {retcode}")