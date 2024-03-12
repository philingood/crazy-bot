FROM python:3.12-alpine as builder
RUN apk add --no-cache binutils
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir aiogram python-dotenv openai pyinstaller docker
RUN pyinstaller --onefile bot.py


FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/dist/bot /app/bot
ENV OPENAI_API_KEY ${OPENAI_API_KEY}
ENV BOT_TOKEN ${BOT_TOKEN}
ENV PAY_TOKEN ${PAY_TOKEN}

CMD ["./bot"]