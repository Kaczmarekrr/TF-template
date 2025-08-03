"""
Common config files for various option in repo that is not directly connected to training, data handling or demos.
"""
from dataclasses import dataclass


@dataclass
class CommonConfig:
    # model config
    export_path: str = "./exports"
    
    # clearml

    clearml_project_name: str = "my_project"