FROM python:3.10-slim

LABEL maintainer="Jeferson F Silva <jeferson0993@gmail.com>"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ncbi-blast+ \
    wget \
    psortb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

RUN mkdir -p /app/data /app/results

ENTRYPOINT ["python", "pipeline.py"]
