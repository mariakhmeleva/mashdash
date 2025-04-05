from flask import Flask
from lab_requests_11 import lab3_blueprint  # Импортируем Blueprint

app = Flask(__name__)
app.register_blueprint(lab3_blueprint, url_prefix='/lab3')  # Регистрируем с префиксом /lab3

if __name__ == '__main__':
    app.run(debug=True)