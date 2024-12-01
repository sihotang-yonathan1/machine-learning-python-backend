import gdown
import pathlib

def check_model() -> None:
    model_path = (pathlib.Path('.').parent / pathlib.Path('model.keras')).resolve()

    if not model_path.exists():
        # ID dari link file
        file_id = "1T1SqRnigmF2IhrHt-4ANWVEXY5HKvmbO"
        # Unduh file
        gdown.download(f"https://drive.google.com/uc?id={file_id}", "model.keras", quiet=True)
    else:
        print("Model file already exists")
        
check_model()