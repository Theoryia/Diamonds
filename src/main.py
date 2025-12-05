import pandas as pd
import numpy as np

df = pd.read_csv('src/data/diamonds.csv')

def avg_column(column):
    return np.mean(df[column]) 

def max_column(column):
    return np.max(df[column]) 

def max_column_price(column):
    max_idx = df[column].idxmax()
    return df.loc[max_idx,['price','carat']]

def min_column_price(column):
    max_idx = df[column].idxmax()
    return max_idx

def main():
    print(f"Carat: {avg_column('carat')}")
    print(f"Depth: {avg_column('depth')}") 
    print(f"Price: {avg_column('price')}") 
    print(min_column_price('price'))
    
    price, carat = max_column_price('price')
    print(f"Price: ${price} for Carat: {carat}")

main()


