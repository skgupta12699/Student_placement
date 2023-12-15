from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)

@app.route("/")
def my_fun():
    print("Hellow")
    return render_template("file.html")

@app.route('/predict', methods= ["post"])
def iris_pred():
    with open("model.pkl","rb") as model:
        ml_model = pickle.load(model)
    
    data = request.form
    cgpa = eval(data["cgpa"])
    iq = eval(data["iq"])
    profile_score = eval(data["profile_score"])

    result = ml_model.predict([[cgpa,iq,profile_score]])
    
    if result[0] == 0:
        student = "Not Placed"
    if result[0] == 1:
        student = "Placed"  

    return student

if __name__ == "__main__":
    app.run()

