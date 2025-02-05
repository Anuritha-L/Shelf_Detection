# Use official Python image as base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure required directories exist
RUN mkdir -p uploads processed

# Expose the port Flask runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "main.py"]
