@echo off

@REM pip upgrade
python -m pip install --upgrade pip

@REM install poetry
python -m pip install poetry=="1.4.2"

@REM install gsc_materials
python -m poetry config virtualenvs.create false
del poetry.lock
python -m pip uninstall counterfeit_trademark --yes
python -m poetry install --only-root
@REM This command reads the pyproject.toml file in the current directory, resolves the dependencies, and installs them.

@REM ------------------------------------
@REM install other libraries dependencies
@REM ------------------------------------
@REM `poetry export` does not include libraries 
@REM .. that were installed directly using pip 
@REM .. and are not listed in the pyproject.toml file.
python -m poetry export --format requirements.txt --output requirements.txt --without-hashes 
python -m pip install -r requirements.txt
del requirements.txt

@REM install pre-commit hooks
python -m pip install pre-commit
python -m pre-commit install --hook-type pre-commit


@REM -------------------------
@REM set environment variables
@REM -------------------------
set PROJECT_PATH=%cd%
set SOURCE_PATH="%PROJECT_PATH%\counterfeit_trademark"
set PYTHONPATH=%SOURCE_PATH%