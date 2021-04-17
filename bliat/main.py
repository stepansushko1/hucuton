

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

data = []
with open('data.txt', 'r') as file:
    for line in file.readlines():
        data.append(line.strip().split(';'))


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/new", methods=["POST"])
def send_post():
    global data

    name = request.form.get('register')
    return render_template("all.html", content=data)


@app.route("/teacher/<string:teacher_name>")
def go_to_htos(teacher_name):
    global data
    our_person = None
    teacher_str = ' '.join(teacher_name.split('_'))
    for person in data:
        if person[0] == teacher_str:
            our_person = person
            break
    return render_template("page_of_teacher.html", teacher=our_person)

# for info in data:
#     name = '_'.join(person[0].splt()
#     @app.route(f"/{name}", methods=["GET", "POST"])
#     def go_to_htos():
#         return render_template("page_of_teacher.html")

if __name__ == "__main__":
    app.run(debug=True)
