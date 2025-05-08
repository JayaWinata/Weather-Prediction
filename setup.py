import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s:] %(message)s:')

PROJECT_NAME = "weather_pred"

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/utils/helper.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/entity/config_entity.py',
    'src/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'Dockerfile',
    'notebooks/test.ipynb',
    'app/__init__.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'{filename} is already exist')