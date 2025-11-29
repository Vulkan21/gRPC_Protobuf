FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY recommendations.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. recommendations.proto

COPY marketplace.py .

CMD ["python", "marketplace.py"]



