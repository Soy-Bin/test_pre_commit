# -----------------------------
# install counterfeit_trademark library
# -----------------------------

# upgrade pip
pip install --upgrade pip

# install poetry
pip install poetry=="1.4.2"

# install gsc_materials
poetry config virtualenvs.create false
rm poetry.lock
pip uninstall counterfeit_trademark --yes
poetry install --only-root  # This command reads the pyproject.toml file in the current directory, resolves the dependencies, and installs them.

# ------------------------------------
# install other libraries dependencies
# ------------------------------------
# `poetry export` does not include libraries 
# .. that were installed directly using pip 
# .. and are not listed in the pyproject.toml file.
poetry export --format requirements.txt --output requirements.txt --without-hashes 
pip install -r requirements.txt
rm requirements.txt

# install pre-commit hooks
pip install pre-commit
pre-commit install --hook-type pre-commit


# -------------------------
# set environment variables
# -------------------------
export PROJECT_PATH=$PWD
export SOURCE_PATH=$PROJECT_PATH/counterfeit_trademark
export PYTHONPATH=$SOURCE_PATH