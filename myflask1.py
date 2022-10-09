from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/hello/<Donna>')
def hello_name(Donna):
        return 'Hello %s!' % Donna

if __name__ == '__main__':
        app.run()
