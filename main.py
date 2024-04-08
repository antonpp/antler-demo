from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    city = request.args.get('city')
    return f"Welcome to {city}!!!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)