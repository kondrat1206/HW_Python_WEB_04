# Використаємо офіційний Python образ
FROM python:alpine3.18

# Встановимо змінну середовища
ENV APP_HOME /messages

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install -r /messages/requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 3000

# Задамо том для збереження даних на хост-машині
VOLUME /messages/storage

# Змінимо шлях до зберігання файлу в data.json
ENV DATA_FILE_PATH /messages/storage/data.json

# Запустимо наш застосунок всередині контейнера, використовуючи ENTRYPOINT
ENTRYPOINT ["python", "/messages/main.py", "--data-file", "/messages/storage/data.json"]
