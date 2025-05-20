from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    base_source_url: str
    data_path: Path
    url_params: list
    target_dir: Path