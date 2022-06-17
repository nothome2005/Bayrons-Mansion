from flask import Flask, request
import pymongo

client = pymongo.MongoClient("mongodb+srv://Fit4a:S8Lqaagemi98rTt@cluster0.dzzqz.mongodb.net/Godot?retryWrites=true&w=majority")
db = client.Godot
coll = db.Secrets_of_Bayron_Mansion

# create the Flask app
app = Flask(__name__)


@app.route('/user')
def json_example():
    language = request.args.get('nickname')
    return '''<h1>The language value is: {}</h1>'''.format(language)
    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
