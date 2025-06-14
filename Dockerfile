FROM python:3.12-slim
WORKDIR /app
COPY device_sim /app
CMD ["python", "simulate.py"]
