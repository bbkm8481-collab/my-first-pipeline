# 1. Start with a lightweight Linux computer that already has Python 3.9 installed
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our model and our web app code into the container
COPY house_model.pkl /app/
COPY app.py /app/

# 4. Install the exact libraries our receptionist and model need
RUN pip install flask scikit-learn pandas joblib

# 5. Open port 5000 so the outside world can talk to the container
EXPOSE 5000

# 6. When the container turns on, run our web app
CMD ["python", "app.py"]