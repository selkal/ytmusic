
FROM python:3.9-alpine as builder

# Set build directory
WORKDIR /app

COPY . /app

RUN pip install -r ./requirements/docs.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

