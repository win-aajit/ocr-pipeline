from fastapi import FastAPI, UploadFile, File
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

import os
import shutil

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_KEY = "key"
ENDPOINT = "endpoint"

client = ImageAnalysisClient(ENDPOINT, AzureKeyCredential(API_KEY))

#OCR AZURE VISION
def run_azure_ocr(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "rb") as image_file:
        image_data = image_file.read()

    result = client.analyze(
        image_data = image_data,
        visual_features=[VisualFeatures.READ]
    )

    extracted_text = []
    for block in result.read.blocks:
        for line in block.lines:
            extracted_text.append(line.text)

    text_output = " ".join(extracted_text)
    print(text_output)


# check if up
@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as imageFile:
        shutil.copyfileobj(file.file, imageFile)
    return {"filename": file.filename}

@app.post("/process")
def process(filename: str):
    try:
        text = run_azure_ocr(filename)
        return {"extracted_text": text}
    except FileNotFoundError:
        return {"error": "File not found. Please upload first."}
    except Exception as e:
        return {"error": str(e)}