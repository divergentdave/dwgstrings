import os
import sys

from . import exceptions


def find_teigha_windows():
    candidates = []
    program_files = os.environ['PROGRAMFILES']
    oda = os.path.join(program_files, "ODA")
    for subdir_name in os.listdir(oda):
        subdir = os.path.join(oda, subdir_name)
        if os.path.isdir(subdir):
            exe = os.path.join(subdir, "TeighaFileConverter.exe")
            if os.path.isfile(exe):
                candidates.append(exe)

    if len(candidates) == 0:
        raise exceptions.TeighaNotInstalledError()

    # TODO: This won't correctly compare version number components with
    # different numbers of digits
    return max(candidates)


def find_teigha():
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        return find_teigha_windows()
    elif sys.platform.startswith('linux'):
        return "/usr/bin/TeighaFileConverter"
    elif sys.platform.startswith('darwin'):
        return "/Applications/TeighaFileConverter.app"
    else:
        raise NotImplementedError("Teigha File Converter is only distributed "
                                  "for Windows, Mac OS X, and Linux")
