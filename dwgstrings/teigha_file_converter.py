import os
import sys

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

    # TODO: This won't correctly compare version number components with
    # different numbers of digits
    return max(candidates)

def find_teigha():
    if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        return find_teigha_windows()
    elif sys.platform.startswith('linux'):
        raise NotImplementedError("Help is needed finding Teigha's install "
                                  "location on Linux. Please get in touch via "
                                  "the GitHub issue tracker.")
    elif sys.platform.startswith('darwin'):
        raise NotImplementedError("Help is needed finding Teigha's install "
                                  "location on OS X. Please get in touch via "
                                  " the GitHub issue tracker.")
    else:
        raise NotImplementedError("Teigha File Converter is only distributed "
                                  "for Windows, Mac OS X, and Linux")
