from flask import Flask
import requests

import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

r = requests.get('https://www.clipartmax.com/png/full/79-791760_plus-addition-sign-circle-vector-1-icon-png.png')

@hops.component(
    "/add",
    name="Add",
    description="Adding two numbers together",
    icon=r,
    inputs=[
        hs.HopsNumber("A","A","First number"),
        hs.HopsNumber("B","B","Second number"),
    ],
    outputs=[hs.HopsNumber("Sum","S","A + B")]
)

@app.route('/urlend')
def add(a, b):
    return a + b 

if __name__ == "__main__":
    app.run()