FROM python:3.14-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/
COPY tests/ ./tests/
COPY pyproject.toml .

# Create logs directory
RUN mkdir -p logs

# Set Python path
ENV PYTHONPATH=/app

# Run tests by default
CMD ["pytest", "tests/", "-v"]
