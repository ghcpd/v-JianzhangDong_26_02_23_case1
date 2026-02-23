FROM python:3.14.2-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

COPY . .

RUN mkdir -p logs

ENV PYTHONUNBUFFERED=1
ENV SMART_APP_NAME="smart-report-service"
ENV SMART_DEBUG="true"
ENV SMART_LOG_LEVEL="info"

CMD ["python", "-m", "pytest", "tests/", "-v", "--tb=short"]
