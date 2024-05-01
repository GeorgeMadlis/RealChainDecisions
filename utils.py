import os
import yaml
from path import Path


def load_config(file_path: str):
    """
    loads yaml file
    Args:
    file_path
    Returns:
    dictinionary
    """
    if os.path.isfile(file_path):
        return yaml.safe_load(Path(file_path).read_text())
    else:
        print(f'Error: missing file {file_path}')
        return None
