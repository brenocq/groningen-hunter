FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y curl wget gnupg unzip && \
    apt-get clean

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable=126.0.6478.114-1 && \
    apt-get clean

# Copy requirements file
COPY requirements.txt .

# Install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY src src

# Forward stdout
ENV PYTHONUNBUFFERED=1

# Run groningen hunter
CMD ["python", "src/main.py"]
