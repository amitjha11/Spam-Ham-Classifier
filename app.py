from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    message=request.form["message"]
    value=model.predict([message])
    if value==[0]:
        return render_template('index.html', prediction_text=" is Not a Spam")
    else:
         return render_template('index.html', prediction_text= "It is a Spam")


if __name__ == "__main__":
    app.run(debug=True)