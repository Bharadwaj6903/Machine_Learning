from flask import Flask 
app = Flask(__name__)

@app.route("/",methods =['GET',"POSt"])
def index():
    return "Starting Machine Learning"
 
if __name__=='__main__':
    app.run(debug=True) 