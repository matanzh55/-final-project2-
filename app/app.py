from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to your MongoDB instance
client = MongoClient('mongodb://root:3yGWpZ7jeS@34.78.116.136:27017/')
db = client['matan_project']
collection = db['links']

@app.template_filter('zip_lists')
def zip_lists(a, b):
    return zip(a, b)

@app.route('/')
def index():

   # Retrieve links from MongoDB
    links = collection.find_one()['links']
    
    # Define labels for the links
    labels = ['LinkedIn', 'GitHub', 'GitLab']

    # Render the HTML template and pass the links as variables
    return render_template('index.html', links=links, labels=labels)

if __name__ == '__main__':
     app.run(host="0.0.0.0",port=5001,debug=True)
