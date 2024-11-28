# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY ./src /app/src
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the main script
CMD ["python", "/app/src/main.py"]
