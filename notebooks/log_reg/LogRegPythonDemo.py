
# coding: utf-8

# # Load Python Libraries

from sklearn2pmml import PMMLPipeline, sklearn2pmml
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from sklearn.externals import joblib
import time

# # Load datafile with 123,419 reviews containing text and sentiment (0,1) from .csv file

df = pd.read_csv('5_4_3_all_data.csv', header = 0 )

# # Display dataframe head and shape

df.head()

print(df.shape)

# # Assign the review text and the sentiment to separate input and label dataframes, then assign the raw values to X, Y

input_X = df['review']
label_Y = df['sentiment']

X = input_X.values
Y = label_Y.values


# # Create a CountVectorizer object using Sklearn's CountVectorizer
# ### After creating the CountVectorizer object, we perform a fit and transform on our input_X in a single method call. The transform uses the CountVectorizer algorithm to convert our review data that is held in our input_X into a document term matrix. Next we use a fit to learn a dictionary of all of the transformed tokens.


tic = time.time()
vect = CountVectorizer(min_df = 1, max_features = 900)
X = vect.fit_transform(X)
toc = time.time()
print("Total time in seconds elapsed :", (toc-tic))


# # Create a Logistic Regression Model using Sklearn's Linear Model Library

model = LogisticRegression()


tic = time.time()
model.fit(X, Y)
toc = time.time()
print("Total time in seconds elapsed :", (toc - tic))


# # Create a PMML Pipeline object and add the Logistic Regression to it


tic = time.time()
myPMMLPipeline = PMMLPipeline([
    ("classifier", model)
])
toc = time.time()
print("Total time in seconds elapsed :", (toc-tic))


# # Export PMML Pipeline with Logistic Regression model to .pmml file for use in SparkML

tic = time.time()
sklearn2pmml(myPMMLPipeline, "LogisticRegressionCountVectorizerModel.pmml", with_repr = True)
toc = time.time()
print("Total time in seconds elapsed :", (toc - tic))


# # Test prediction


singleReview = ["i love this app  it keeps me up to date on how much and what is in my acct i could never be without this app after having had it  i have been blessed to never once had a problem so far and ive been using it for around six months now  im never giving it up"]
vectorizedSentence = vect.transform(singleReview)


# # Display the transformed review

print(vectorizedSentence.data)


# # Make a prediction on the vectorized review text

print(myPMMLPipeline.predict_proba(vectorizedSentence))


# # Export model to Pickle and Joblib

pickle_file = open("pickleFile.pkl", 'wb')
pickle.dump(model, pickle_file)
pickle_file.close()

joblib_file = "joblibLRModel.sav"
joblib.dump(model,joblib_file)
