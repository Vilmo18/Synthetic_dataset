import pickle

model = pickle.load(open("detection.pkl", "rb"))
prediction = model.predict([[15901200-2000,0,0,1]])
print(prediction[0])
