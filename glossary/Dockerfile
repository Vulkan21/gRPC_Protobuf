FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY glossary.json .
COPY glossary_api.py .
COPY static/ ./static/

CMD ["uvicorn", "glossary_api:app", "--host", "0.0.0.0", "--port", "8000"]



