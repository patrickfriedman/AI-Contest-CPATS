# Dockerfile
FROM python:3.9

# Set workdir
WORKDIR /app

# Copy all files
COPY . /app

# Install requirements
RUN pip install -r requirements.txt

# Make script executable
RUN chmod +x main.sh

# Run script
CMD ["./main.sh"]
