from pathlib import Path
import pandas as pd

data_directory = Path("data/raw")

csv_files = data_directory.glob("*.csv")

for csv_file in csv_files:
    print("\n" + "=" * 40)
    print(csv_file.name)
    
    data_frame = pd.read_csv(csv_file)
    
    print("Shape:")
    print(data_frame.shape)
    
    print("\nColumns:")
    print(data_frame.columns)
    
    print("\nTypes:")
    print(data_frame.dtypes)
    
    print("\nSample:")
    print(data_frame.head())