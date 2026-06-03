from pathlib import Path
import pandas as pd

folder=Path("data/raw")

files=folder.glob("*.csv")

for file in files:

    print("\n"+"="*40)

    print(file.name)

    df=pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nTypes:")
    print(df.dtypes)

    print("\nSample:")
    print(df.head())