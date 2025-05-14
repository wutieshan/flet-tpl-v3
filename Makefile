target=main.py


.PHONY:
run:
	python -u $(target)


.PHONY:
flet-build:
#	python -u devtools/nuitka_build.py
#	python -m nuitka --debug --follow-imports --standalone --mingw64 --output-dir=nuitka-dist test.py
	flet build windows -v --exclude .venv/