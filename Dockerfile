# установка базового образа (host OS)
FROM python:3.10.2-slim
# установка рабочей директории в контейнере
RUN mkdir -p "/app"

RUN apt-get update && apt-get install libpython3.9-dev gcc -y

RUN apt-get install libcairo2-dev pkg-config -y

RUN pip install pyTelegramBotAPI beautifulsoup4

WORKDIR /app

# копирование содержимого локальной директории src в рабочую директорию
COPY main/ .
# команда, выполняемая при запуске контейнера
CMD [ "python", "./main.py" ]