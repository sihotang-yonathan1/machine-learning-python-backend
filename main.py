from typing import Annotated
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

import numpy as np

from lib.handler import CLASSES
from utils.image_handling import load_image_from_bytes
from config.configuration import app, BASE_PATH
from config.model import model

from scripts.model_download import check_model

# Cara barbar
import subprocess

@app.post(f'{BASE_PATH}/image')
async def post_image(image: Annotated[UploadFile, File()]):
    try:
        image_data = await image.read()

        # Load and preprocess the image from bytes
        _image = load_image_from_bytes(image_data, target_size=(224, 224))
    
        predictions: np.ndarray = model.predict(_image)

        predicted_label_index = np.argmax(predictions)
        predicted_label = CLASSES[predicted_label_index]
        
        # May raise error
        _result: np.ndarray = predictions[0]

        return {
            'data': {
                'result': predicted_label,
                '_prediction_value': {
                    CLASSES[counter].lower(): value
                    for counter, value in enumerate(_result.tolist())
                }
            }
        }

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

# if __name__ == '__main__':
#     check_model()
#     subprocess.run(['fastapi', 'run', 'main.py'])

