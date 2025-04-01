# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements into the container
COPY requirements.txt /app/

# Copy app code and data
COPY mock_worker.py mock_data.json /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "mock_worker:app", "--host", "0.0.0.0", "--port", "8000"]
