import platform
import subprocess
import sys

entrypath = "main.py"
options = [
    # https://nuitka.net/doc/api-doc.html
    #
    #
    # "--verbose",
    #
    # run immediately once compilation finished
    # "--run",
    #
    #
    "--debug",
    #
    #
    "--follow-imports",
    #
    #
    "--mingw64",
    # "--clang",
    #
    #
    "--standalone",
    #
    #
    "--output-dir=nuitka-dist",
    #
    #
    # "--include-data-dir=config=config",
    "--include-data-dir=assets=assets",
    "--include-data-dir=conf=conf",
    "--include-data-dir=data=",
    "--include-data-dir=logs=",
    #
    # plugins
    # "--enable-plugin=pyqt6",
]
options_platform_specified = [
    # windows
    # "--windows-uac-admin",
    "--windows-console-mode=force",
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
    print(command)
    subprocess.check_call(command)
