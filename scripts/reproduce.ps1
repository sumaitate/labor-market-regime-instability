$ErrorActionPreference = "Stop"

python -m pip install --upgrade pip
python -m pip install -e .
python scripts/run_pipeline.py
