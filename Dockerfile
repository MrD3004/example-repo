# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your Python script into the container
COPY finance_calculator.py .

# Set the default command to run the script
CMD ["python", "finance_calculator.py"]