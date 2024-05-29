FROM python:3.12-alpine as builder
RUN apk add --no-cache binutils
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir aiogram python-dotenv openai pyinstaller docker
RUN pyinstaller --onefile bot.py


FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/dist/bot .
CMD ["./bot"]

ARG VERSION
ARG BUILD_DATE

LABEL maintainer="philingood"
LABEL version="1.0"
LABEL description="Telegram bot with AI"
LABEL image.tag="${IMAGE_TAG}"
