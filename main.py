from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/user')
def json_example():
    nick = request.args.get('nickname')
    return coll.find({'_id': nick})
    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
