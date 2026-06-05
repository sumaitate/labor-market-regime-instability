#################################################################################
# GLOBALS
#################################################################################

PROJECT_NAME = ML_LaborTightnessRegimeShift
PYTHON_VERSION = 3.11
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS
#################################################################################

.PHONY: requirements
requirements:
$(PYTHON_INTERPRETER) -m pip install --upgrade pip
$(PYTHON_INTERPRETER) -m pip install -e .

.PHONY: reproduce
reproduce: requirements
$(PYTHON_INTERPRETER) scripts/run_pipeline.py

.PHONY: data
data: reproduce

.PHONY: clean
clean:
$(PYTHON_INTERPRETER) -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if p.is_dir()]"

.PHONY: lint
lint:
ruff format --check
ruff check

.PHONY: format
format:
ruff check --fix
ruff format

.PHONY: help
help:
@echo Available rules:
@echo   requirements
@echo   reproduce
@echo   data
@echo   clean
@echo   lint
@echo   format

.DEFAULT_GOAL := help
