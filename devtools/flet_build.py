# flet build


# requires
# reference: https://flet.dev/docs/publish
# 1. flutter sdk:
#   recommend to install automatically
#   run "flutter doctor -v" to check installation
# 2. windows
#   visual studio toolchain: https://visualstudio.microsoft.com/downloads/
#   `start ms-settings:developers` to enable developer mode


import subprocess


class FletBuild:
    @classmethod
    def build(cls):
        params = [
            "windows",
            "--output build",
            "--exlude .venv/",
        ]
        command = "flet build " + " ".join(params)
        print(command)
        subprocess.check_call(command)


if __name__ == "__main__":
    FletBuild.build()
