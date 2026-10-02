from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
