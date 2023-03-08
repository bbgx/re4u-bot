FROM python:3.9-slim-buster

# Set up working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copy nodes file
COPY nodes.json .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY ./src .

# Run the script
CMD ["python", "main.py"]
