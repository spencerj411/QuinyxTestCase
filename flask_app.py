from flask import Flask # include the flask library 
import requests

app = Flask(__name__) 

@app.route("/") 
def index(): 
   return "Hello, World!"

@app.route("/getJokes")
def get_jokes():
      list_of_jokes = ""
      for i in range(10):
         response = requests.get("http://api.icndb.com/jokes/random/")
         list_of_jokes += "{}. {} <br />".format(i+1, response.json()['value']['joke'])
      return list_of_jokes

if __name__ == '__main__': 
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000
