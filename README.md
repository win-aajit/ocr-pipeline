# ocr-pipeline

🚀 Overview

This project is a scalable document intelligence pipeline that extracts text from images using Azure Computer Vision OCR. It is built with FastAPI, containerized with Docker, and deployed using Kubernetes for scalability.

The system allows users to:

Upload image files
Process them using OCR
Retrieve extracted text via API endpoints
🏗️ Architecture
Client → FastAPI API → Upload Image
                     → Store Locally (/uploads)
                     → Azure OCR Processing
                     → Return Extracted Text
Tech Stack
Backend: FastAPI
OCR: Azure Computer Vision (Image Analysis API)
Containerization: Docker
Orchestration: Kubernetes
Language: Python 3.10
