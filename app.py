# Getting started : https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
from flask import Flask, render_template, request,json,jsonify
from flask_pymongo import PyMongo


app=Flask(__name__)
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
mongo = PyMongo(app)

@app.route('/')
def index():
	return render_template('index.html')

# The route path is given in the index.html as href of the html page. It does not however load the page
# This is the html side of the flask
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# signup method. What happens on clicking the signup button after filling the details.
# This is the restAPi side of flask
# We go to index.html from there we go to signUP.js file and that gets called on using this
@app.route('/signUp',methods=['POST'])
def signUp():
    # read the posted values from the UI
	# The 'inputName, etc. come from the html files.
	# The request command takes from the html, and gives to the variable

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']  # validate the received values

    output = mongo.db.users.insert({'name':_name})


    if _name and _email and _password:


        return json.dumps({'html': '<span>All fields good !!</span>'})

    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})




if __name__=='__main__':
	app.run(debug=True)