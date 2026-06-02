import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from utils.preprocess import clean_text

import joblib


df = pd.read_csv(

    "dataset/UpdatedResumeDataSet.csv"

)


df["Resume"] = df["Resume"].apply(

    clean_text

)


x = df["Resume"]

y = df["Category"]


vectorizer = TfidfVectorizer()


x = vectorizer.fit_transform(

    x

)


model = LogisticRegression()


model.fit(

    x,

    y

)


joblib.dump(

    model,

    "model.pkl"

)

joblib.dump(

    vectorizer,

    "vectorizer.pkl"

)


print(

    "Training Complete"

)