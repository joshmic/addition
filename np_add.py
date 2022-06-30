from flask import Flask
import numpy as np

import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/np_add",
    name="np_add",
    description="Adding two numbers together",
    #icon="add.png",
    inputs=[
        hs.HopsNumber("A","A","First number"),
        hs.HopsNumber("B","B","Second number"),
    ],
    outputs=[hs.HopsNumber("Sum","S","A + B")]
)

@app.route('/urlend')
def np_add(a, b):

    arr = np.array(a,b)

    result = np.add(arr)
    return result


if __name__ == "__main__":
    app.run()