from flask import Flask, send_file, request, jsonify
from threading import Thread
import socket
import json
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Получаем текущую директорию
        current_directory = os.path.dirname(os.path.realpath(__file__))
        
        index_file_path = os.path.join(current_directory, 'index.html')
        nf_file_path = os.path.join(current_directory, 'error.html')
        

        # Отправляем содержимое файла index.html
        return send_file(index_file_path)
    except FileNotFoundError:
        return send_file(nf_file_path)

@app.route('/<path:filename>')
def serve_file(filename):
    try:
        # Получаем текущую директорию
        current_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Объединяем текущую директорию с запрошенным именем файла
        file_path = os.path.join(current_directory, filename)
        nf_file_path = os.path.join(current_directory, 'error.html')

        # Отправляем файл клиенту
        return send_file(file_path)
    except FileNotFoundError:
        return send_file(nf_file_path)

@app.route('/message', methods=['POST'])
def message():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    comp_file_path = os.path.join(current_directory, 'completed.html')
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        try:
            username = request.form.get('username')
            message = request.form.get('message')
            # Создание клиентского сокета
            udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Подготовка данных в формате JSON
            message_dict = {'username': username, 'message': message}
            json_data = json.dumps(message_dict).encode('utf-8')

            # Отправка данных на сервер
            udp_client_socket.sendto(json_data, ('localhost', 5000))

            # Закрытие соединения
            udp_client_socket.close()

            return send_file(comp_file_path)
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid content type'})


# Папка для хранения файлов
storage_folder = 'storage'
os.makedirs(storage_folder, exist_ok=True)

# Путь к файлу JSON
json_file_path = os.path.join(storage_folder, 'data.json')
if not os.path.isfile(json_file_path):
    # Создать пустой словарь
    data = {}

    # Открыть файл JSON для записи
    with open(json_file_path, 'w') as json_file:
        # Записать пустой словарь в файл JSON
        json.dump(data, json_file)

    print(f"Создан файл JSON по пути: {json_file_path}")
else:
    print(f"Файл JSON уже существует по пути: {json_file_path}")

def save_to_json(data):
    try:
        with open(json_file_path, 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = {}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    existing_data[timestamp] = data

    with open(json_file_path, 'w') as file:
        json.dump(existing_data, file, indent=2)

def run_flask_app():
    app.run(host='0.0.0.0', port=3000)

def run_socket_server():
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind(('localhost', 5000))

    print('UDP server is listening on port 5000...')

    while True:
        # Получение данных
        data, addr = udp_server_socket.recvfrom(1024)

        # Декодирование байтов в строку
        message = data.decode('utf-8')

        try:
            # Преобразование строки JSON в словарь
            message_dict = json.loads(message)
            
            # Сохранение в JSON-файл
            save_to_json(message_dict)

            print(f"Received and saved message: {message_dict}")
        except json.JSONDecodeError:
            print("Invalid JSON format received.")

# Запуск Flask в одном потоке
flask_thread = Thread(target=run_flask_app)
flask_thread.start()

# Запуск socket server в другом потоке
socket_thread = Thread(target=run_socket_server)
socket_thread.start()

# Ожидание завершения потоков
flask_thread.join()
socket_thread.join()
