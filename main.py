from flask import Flask, send_from_directory, render_template_string

web = Flask(__name__)


@web.route("/")
@web.route("/<path:path>")
def index(path=""):
    try:
        # Возвращаем HTML-файл
        with open("html/contacts.html", "r", encoding="utf-8") as file:
            html = file.read()
        return render_template_string(html)
    except FileNotFoundError:
        return "Страница не найдена", 404


@web.route("/css/<path:filename>")
def css_files(file):
    return send_from_directory("css", file)


if __name__ == "__main__":
    web.run(debug=True, host="localhost", port=5000)
