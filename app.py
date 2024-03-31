from flask import Flask,render_template,jsonify


Matieres =[
  {
    "id": 1,
    "title" : "Noraniya",
    "description" :"Noraniya is based in good ways to read the coran ",
      },

  {
    "id": 2,
    "title" : "Arabe",
    "description" :"Arabe langage by alphabet and vocabulary  ",
      },
  {
    "id": 3,
    "title" : "Tarbiya",
    "description" :"Tarbiya islamiya means how pratice our religion  ",
      },
]

app= Flask(__name__)
@app.route("/")
def home():
 return render_template("home.html",matieres=Matieres)
  
@app.route("/api/matieres")
def list_matieres():
  return jsonify(Matieres)

app.run(host='0.0.0.0',debug=True)

  