import joblib

#laod the model

model = joblib.load(open('diabetes_79.pkl','rb'))

result = model.predict([[1,1,1,1,1,1,1,1]])

if result[0]==1:
    print("diabetic")
else:
    print('not diabetic')