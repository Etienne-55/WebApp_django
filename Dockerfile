FROM python:3.11-slim

WORKDIR /STOCK_PROJECT

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Code to run container --> docker run -p 8000:8000 mydjangoapp