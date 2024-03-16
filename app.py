from flask import Flask

app= Flask(__name__)
@app.route("/")
def home():
 return "Hello hjj "


app.run(host='0.0.0.0',debug=True)

  