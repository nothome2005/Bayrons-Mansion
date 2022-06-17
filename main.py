from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/user')
def json_example():
    language = request.args.get('nickname')
    return '''<h1>The language value is: {}</h1>'''.format(language)
    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
