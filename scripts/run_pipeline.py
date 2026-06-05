from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTEBOOKS = [
    "00_data_build.ipynb",
    "01_exploratory_data_analysis.ipynb",
    "02_feature_engineering.ipynb",
    "03_baseline_models.ipynb",
    "04_structural_benchmark.ipynb",
    "05_forecast_benchmark.ipynb",
    "06_result_and_analysis.ipynb",
]


def main() -> None:
    notebook_dir = ROOT / "notebooks"
    executed_dir = ROOT / "reports" / "executed_notebooks"
    executed_dir.mkdir(parents=True, exist_ok=True)

    missing = [name for name in NOTEBOOKS if not (notebook_dir / name).exists()]
    if missing:
        missing_text = "\n".join(f"  - notebooks/{name}" for name in missing)
        raise FileNotFoundError(
            "The reproducibility pipeline is missing required notebooks:\n"
            f"{missing_text}\n\n"
            "Either add the missing notebooks or update NOTEBOOKS in scripts/run_pipeline.py."
        )

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")

    for name in NOTEBOOKS:
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
                "--ExecutePreprocessor.cwd=" + str(ROOT),
            ],
            cwd=ROOT,
            env=env,
            check=True,
        )

    print("\nReproducibility pipeline completed successfully.")
    print(f"Executed notebooks written to: {executed_dir}")


if __name__ == "__main__":
    main()
