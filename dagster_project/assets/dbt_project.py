import os
import sys
from pathlib import Path
from dagster_dbt import DbtProject

# Put the venv's Scripts folder first so dbt-core wins
os.environ["PATH"] = str(Path(sys.executable).parent) + os.pathsep + os.environ["PATH"]

dbt_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "ecommerce").resolve(),
    profiles_dir=Path.home() / ".dbt",
)
# dbt_project.prepare_if_dev()


