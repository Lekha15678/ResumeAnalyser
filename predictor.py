import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_resume(text):

    vec = vectorizer.transform([text])

    prediction = model.predict(vec)

    print("Prediction =", prediction)

    return prediction[0]