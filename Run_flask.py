from flask import Flask ,request,render_template

app=Flask(__name__)

@app.route("/tuna / <value>")
def tuna(value):
    return render_template("main.html" , name = name)

@app.route("/good")
def good():
    return render_template("main.html")

if __name__=="__main__":
    app.run(debug=True)
