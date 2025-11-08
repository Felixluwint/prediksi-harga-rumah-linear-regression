import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
os.makedirs('backend/model', exist_ok=True)
df = pd.read_csv('backend/data/housing.csv')
X = df[['sqft','bedrooms','bathrooms','lot_size','year_built']].values
y = df['price'].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
joblib.dump(model, 'backend/model/model.pkl')
joblib.dump(scaler, 'backend/model/scaler.pkl')
print('Trained LinearRegression model')
print(f'MSE: {mse:.2f}, R2: {r2:.4f}')
print('Saved model to backend/model/model.pkl and scaler to backend/model/scaler.pkl')
