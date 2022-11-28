from flask import Flask


import sys
from flask import Flask
from housing.exception import HousingException
from housing.logger import logging

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing Custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established. "

if __name__== "__main__":
    app.run()