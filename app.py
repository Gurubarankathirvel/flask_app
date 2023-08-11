from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #decorator
def hello_world():
    numbers=[11,13,14,20]
    return render_template('index.html',numbers=numbers)
if __name__=="__main__":
    app.run(debug=True)
