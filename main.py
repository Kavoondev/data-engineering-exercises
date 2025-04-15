import pandas as pd

def process_data():
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    print("\nAverage age:", df['age'].mean())

if __name__ == "__main__":
    process_data()