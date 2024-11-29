import pathlib
from tensorflow.keras.models import load_model

# TODO: set the file based on current file instead current Working Directory
MODEL_PATH = 'model.keras'
model = load_model(pathlib.Path(pathlib.Path('.').parent / MODEL_PATH).resolve())
CLASSES = ['Normal', 'bacteria', 'virus']