FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir aiogram python-dotenv openai


CMD ["python", "bot.py"]
