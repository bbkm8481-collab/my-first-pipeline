# CI/CD ML Pipeline

## Overview
End-to-end CI/CD pipeline for deploying a machine learning model using Jenkins, Docker and Flask.

## Tech Stack
- Python
- Flask
- Docker
- Jenkins

## Project Structure
- train.py
- app.py
- Dockerfile
- Jenkinsfile

## Workflow
1. Train model
2. Build Docker image
3. Run Jenkins pipeline
4. Deploy API
5. Test prediction endpoint

## Sample API Request
POST /predict

{
  "square_footage": 1200,
  "bedrooms": 3
}
