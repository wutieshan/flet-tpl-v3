import platform
import subprocess
import sys

entrypath = "launch.py"
options = [
    # https://nuitka.net/doc/api-doc.html
    #
    #
    # "--verbose",
    #
    # run immediately once compilation finished
    "--run",
    #
    #
    "--debug",
    #
    #
    "--follow-imports",
    #
    #
    "--mingw64",
    "--clang",
    #
    #
    "--standalone",
    #
    #
    "--output-dir=build",
    #
    #
    "--include-data-dir=config=config",
    #
    # plugins
    "--enable-plugin=pyqt6",
]
options_platform_specified = [
    # windows
    # "--windows-uac-admin",
    "--windows-console-mode=disable",
]


if __name__ == "__main__":
    pprefix = None
    match platform.system().lower():
        case "windows":
            pprefix = "--windows"
        case "linux":
            ...
        case "darwin":
            ...

    optstr = " ".join(options)
    if pprefix:
        optstr += f" {' '.join(x for x in options_platform_specified if x.startswith(pprefix))}"

    command = f"{sys.executable} -m nuitka {optstr} {entrypath}"
    subprocess.check_call(command)
