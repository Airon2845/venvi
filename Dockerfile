FROM python:3.9-slim
WORKDIR /workspace
COPY venvi.py .
CMD ["python", "venvi.py"]
