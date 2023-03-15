FROM python:3.10-slim-buster

# Create a non-root user
RUN useradd --create-home appuser

# Set up working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copy nodes file
COPY nodes.json .

# Copy sonar file
COPY sonar-project.properties .

# Change timezone
RUN apt update && apt install -y --no-install-recommends tzdata
ENV TZ="America/Sao_Paulo"

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY ./src .

# Set ownership of the working directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Run the script
CMD ["python", "main.py"]
