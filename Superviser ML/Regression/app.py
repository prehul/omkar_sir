"""
How to write the flask code
How to create the end point
How to Test the endpoint URL
How to test in Postman
We will implement same thing our Linear Regression
Flask or Django web framework
It will create an API end point for us
That API endpoint will hit any webbrowser to get the results
If you see any application amazon/ gmail all are http urls 
These http urls create by webframeworks
POSTMAN is an application to test these urls working or not
"""
# pip install Flask

from flask import Flask,request
app=Flask(__name__)  # double underscore
#__name__ we are saying to the python script to run as a package 

# Decorator , this will gives the routes or urls 
# from the python functions
# these routes connect to the our web application
@app.route('/')
def greet():
    print("hello world welcome")
    return "hello world 222"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)