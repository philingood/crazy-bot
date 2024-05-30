FROM python:3.12-alpine3.19 as builder
RUN apk add --no-cache binutils=2.41-r0 docker-cli=25.0.5-r1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
WORKDIR /app/src
RUN pyinstaller --onefile bot.py


FROM alpine:3.19
WORKDIR /app
COPY --from=builder /app/src/dist/bot .
CMD ["./bot"]

ARG VERSION
ARG BUILD_DATE

LABEL maintainer="philingood"
LABEL version="1.0"
LABEL description="Telegram bot with AI"
LABEL image.tag="${IMAGE_TAG}"
