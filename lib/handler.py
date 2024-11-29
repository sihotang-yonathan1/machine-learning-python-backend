import pathlib
from tensorflow.keras.models import load_model

# TODO: set the file based on current file instead current Working Directory
model = load_model(pathlib.Path('model.keras').resolve())
CLASSES = ['Normal', 'bacteria', 'virus']