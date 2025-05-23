from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    base_source_url: str
    data_path: Path
    url_params: list
    target_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    transformed_filename: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    target_column: str
    model_params: dict = field(default_factory=dict)