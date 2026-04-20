# Use a lightweight Python image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies (including the akeyless SDK)
RUN pip install --no-cache-dir -r requirements.txt

# Copy both scripts to the container
COPY get_akeyless_secret.py .
COPY get_akeyless_secret_SDK.py .

# By default, run the new SDK-based script
CMD ["python", "get_akeyless_secret_SDK.py"]