# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install required Python packages
RUN pip install qrcode[pil]

# Command to run the Python script
CMD ["python", "generate_qr.py"]
