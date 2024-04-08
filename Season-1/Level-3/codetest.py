import os
from flask import Flask, request

app = Flask(__name__)

class TaxPayer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def get_prof_picture(self, path=None):
        if not path:
            pass

        # Используем функцию save_path() для защиты от атак на обход пути
        path = save_path(path)

        if not path:
            return None

        with open(path, 'rb') as pic:
            picture = bytearray(pic.read())

        return path

    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")

        # Используем функцию save_path() для защиты от атак на обход пути
        path = save_path(path)

        if not path:
            return None

        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        return path

# Определяем функцию save_path() вне класса TaxPayer
def save_path(path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.normpath(os.path.join(base_dir, path))
    if base_dir != os.path.commonpath([base_dir, filepath]):
        return None
    return filepath

# Этот кусок кода не связан с упражнением, он просто для Flask приложения
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
    TaxPayer('foo', 'bar').save_path(request.args["path"])

if __name__ == "__main__":
    app.run()