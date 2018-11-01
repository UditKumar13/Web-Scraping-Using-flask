from flask import Flask ,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("main.html" )

@app.route("/good")
def good():
    return render_template("main.html")

if __name__=="__main__":
    app.run(debug=True)
