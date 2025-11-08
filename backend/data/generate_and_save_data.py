import pandas as pd
import numpy as np
np.random.seed(42)
n = 1200
sqft = np.random.normal(1500, 500, n).clip(300, 5000)
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 4, n)
lot_size = np.random.normal(5000, 2000, n).clip(200, 20000)
year_built = np.random.randint(1950, 2021, n)
price = 60 * sqft + 12000 * bedrooms + 9000 * bathrooms + 1.8 * lot_size - 180 * (2021 - year_built)
price = price + np.random.normal(0, 35000, n)
df = pd.DataFrame({
    'sqft': sqft.round(0).astype(int),
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'lot_size': lot_size.round(0).astype(int),
    'year_built': year_built,
    'price': price.round(2)
})
df.to_csv('backend/data/housing.csv', index=False)
print('Saved synthetic dataset to backend/data/housing.csv; rows:', len(df))
