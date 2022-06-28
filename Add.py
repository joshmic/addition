from flask import Flask
import ghhops_server as hs

import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/add",
    name="Add",
    description="Adding two numbers together",
    icon="add.png",
    inputs=[
        hs.HopsNumber("A","A","First number"),
        hs.HopsNumber("B","B","Second number"),
    ],
    outputs=[hs.HopsNumber("Sum","S","A + B")]
)

def add(a, b):
    return a + b 

if __name__ == "__main__":
    app.run()