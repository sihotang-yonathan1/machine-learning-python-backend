from PIL import Image
from io import BytesIO

import numpy as np


def load_image_from_bytes(image_bytes, target_size=(224, 224)):
    # Create a BytesIO stream from the image bytes
    img = Image.open(BytesIO(image_bytes))

    # Ubah ke RGB jika belum RGB (misal dari grayscale)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize image to target size (e.g., 224x224)
    img = img.resize(target_size)
    
    # Convert image to a numpy array
    img_array = np.array(img)
    
    # If the image has an alpha channel (RGBA), convert to RGB
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]
    
    # Normalize the image to [0, 1]
    # img_array = img_array.astype(np.float32) / 255.0
    img_array = img_array / 255.0
    
    # Expand dimensions to match the expected input shape (batch size, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array