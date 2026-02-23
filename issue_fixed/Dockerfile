FROM python:3.14-slim

WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["bash"]
