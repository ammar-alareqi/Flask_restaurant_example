from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == "__main__":
    app.debug = True            # to refresh server when there is changes in code
    app.run(host='0.0.0.0', port=5000)