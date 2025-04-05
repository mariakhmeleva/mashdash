from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def labs():
    return '''<!DOCTYPE html>
<body >
    <header>
        НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных
    </header>
    <main>
        <h1>Лабораторные работы по WEB-программированию</h1>
        <div>
        <a href="/number/">Лабораторная работа 3</a><br>
        </div>
    </main>
</body>
</html>
'''