import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_excel("Student_Performance.xlsx")
print(df.isna().any())
df.info()
df = df.drop(columns = ['Extracurricular Activities'])
df.info()

# TRAINING THE MODEL
x = df[['Hours Studied','Previous Scores','Sleep Hours','Sample Question Papers Practiced']]
y = df[['Performance Index']]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

# TESTING THE MODEL PERFORMANCE ON TEST DATA
result = model.predict(X_test)
print(result)
r2accuracy = model.score(X_test,y_test)
print(f"r2Accuracy is {r2accuracy}")

# TESTING THE MODEL ON CUSTOM DATA
test = {'Hours Studied':8,
                     'Previous Scores':50,
                     'Sleep Hours':6,
                     'Sample Question Papers Practiced':9}


df1 = pd.DataFrame(test,index=[0])
predict = model.predict(df1)
print(predict)

joblib.dump(model, 'Student_Performance_Model.joblib')