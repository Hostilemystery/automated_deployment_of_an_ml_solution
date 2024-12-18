FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install build dependencies and Python dev tools
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]