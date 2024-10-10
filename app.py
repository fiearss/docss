from flask import Flask, send_from_directory

app = Flask(__name__)

# Отображение index.html при запросе на корень сайта
@app.route('/')
def index():
    return send_from_directory('docs', 'index.html')

# Настройка маршрута для обслуживания всех статических файлов
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('docs', path)

if __name__ == '__main__':
    app.run(debug=True)