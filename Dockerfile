FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir aiogram python-dotenv openai


CMD ["python", "bot.py"]
