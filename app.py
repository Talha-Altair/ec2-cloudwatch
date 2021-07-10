from flask import Flask, render_template
import json
import watchtower, flask, logging
import random

app = Flask(__name__)

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(watchtower.CloudWatchLogHandler())

                                 
@app.route('/')
def start():

    num = random.randint(0,10000)

    # print(f"Current random number is {num}")
    logger.info(f"Current random number is {num}")
    if num%2 == 0:
      # print(f"current number is even")
      logger.info(f"current number is even")
    else:
      # print(f"current number is odd")
      logger.info(f"current number is odd")

    return render_template('index.html',num=num)
    

if __name__== "__main__":
  app.run(host="0.0.0.0",port=7000, debug=True)


  