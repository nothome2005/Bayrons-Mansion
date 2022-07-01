from flask import Flask, request
import pymongo
from time import sleep
import requests
from fake_useragent import UserAgent
from threading import Thread

ua = UserAgent()
client = pymongo.MongoClient("mongodb+srv://Fit4a:S8Lqaagemi98rTt@cluster0.dzzqz.mongodb.net/Godot?retryWrites=true&w=majority")
db = client.Godot
coll = db.Secrets_of_Bayron_Mansion


def ping_timer():
    while True:
        requests.get('https://bayronsmansion.herokuapp.com/user?nickname=super4', headers={'User-Agent': ua.random})
        print('Herok wake up!')
        sleep((60*15))
    print('Heroku sleep!')
    
th = Thread(target=ping_timer)
th.start()


# create the Flask app
app = Flask(__name__)


@app.route('/user')
def json_example():
    nick = request.args.get('nickname')
    for value in coll.find({'_id': nick}):
        pass
    try:
        type(value)
        return '1'
    except UnboundLocalError:
        return '0'

@app.route('/achivement')
def example():
    nick = request.args.get('nickname')
    achiv = request.args.get('achivement')
    for value in coll.find({'_id': nick}):
        pass
    try:
        type(value)
        coll.update_one({'_id': nick}, {'$set': {achiv: 1}})
        return '1'
    except UnboundLocalError:
        return '0'    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
