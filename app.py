app = Flask(__name__)

@app.route('/')

def hello_world():

    return 'Zharbour'

if __name__ == "__main__":

    app.run()
