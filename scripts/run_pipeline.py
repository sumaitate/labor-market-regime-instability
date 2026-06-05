from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DATA_REFRESH_NOTEBOOKS = [
    "00_data_build.ipynb",
]

ANALYSIS_NOTEBOOKS = [
    "01_exploratory_data_analysis.ipynb",
    "02_feature_engineering.ipynb",
    "03_baseline_models.ipynb",
    "04_structural_benchmark.ipynb",
    "05_forecast_benchmark.ipynb",
    "06_result_and_analysis.ipynb",
]


def run_notebooks(notebooks: list[str]) -> None:
    notebook_dir = ROOT / "notebooks"
    executed_dir = ROOT / "reports" / "executed_notebooks"
    executed_dir.mkdir(parents=True, exist_ok=True)

    missing = [name for name in notebooks if not (notebook_dir / name).exists()]
    if missing:
        missing_text = "\n".join(f"  - notebooks/{name}" for name in missing)
        raise FileNotFoundError(
            "The reproducibility pipeline is missing required notebooks:\n"
            f"{missing_text}\n\n"
            "Update NOTEBOOKS in scripts/run_pipeline.py to match the repository."
        )

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")

    for name in notebooks:
        notebook_path = notebook_dir / name
        print(f"\n=== Executing {notebook_path.relative_to(ROOT)} ===", flush=True)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                str(notebook_path),
                "--output",
                name,
                "--output-dir",
                str(executed_dir),
                "--ExecutePreprocessor.timeout=1800",
                "--ExecutePreprocessor.kernel_name=python3",
            ],
            cwd=ROOT,
            env=env,
            check=True,
        )

    print("\nPipeline completed successfully.")
    print(f"Executed notebooks written to: {executed_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh-data",
        action="store_true",
        help="Also rerun the live data acquisition notebook. Requires internet and FRED_API_KEY.",
    )
    args = parser.parse_args()

    required_committed_input = ROOT / "data" / "processed" / "07_merged_data.csv"
    if not required_committed_input.exists():
        raise FileNotFoundError(
            "Missing committed input data: data/processed/07_merged_data.csv\n"
            "Run with --refresh-data only if you have internet access and FRED_API_KEY set."
        )

    notebooks = ANALYSIS_NOTEBOOKS
    if args.refresh_data:
        notebooks = DATA_REFRESH_NOTEBOOKS + ANALYSIS_NOTEBOOKS

    run_notebooks(notebooks)


if __name__ == "__main__":
    main()
