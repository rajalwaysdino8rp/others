# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY azure_blob_utilization.py .

RUN pip install azure-storage-blob

CMD ["python", "azure_blob_utilization.py"]
