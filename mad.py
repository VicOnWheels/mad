from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Coucou PGUI ça va ?'

if __name__ == '__main__':
    app.run(debug=True)
