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

# Define environment variables
ENV Question_FILE=/app/questions
ENV Solution_FILE=/app/solutions
ENV evalmessage="YourMessageHere"

# Run script
RUN bash main.sh