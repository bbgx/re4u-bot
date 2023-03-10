FROM python:3.9-slim-buster

# Set up working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copy nodes file
COPY nodes.json .

# Change timezone
RUN apt update && apt install tzdata -y
ENV TZ="America/Sao_Paulo"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY ./src .

# Run the script
CMD ["python", "main.py"]
