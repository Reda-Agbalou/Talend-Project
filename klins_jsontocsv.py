import os
import pandas as pd

# Specify the path to the directory containing JSON files
json_files_path = "C:\\Users\\RPC\\Desktop\\bi\\data\\jsonfiles_klines"

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through all files in the directory
for filename in os.listdir(json_files_path):
    if filename.endswith(".json"):
        file_path = os.path.join(json_files_path, filename)

        # Read JSON data into a Pandas DataFrame
        df = pd.read_json(file_path)

        # Add a new column 'symbol' with the name of the file (excluding extension)
        df['symbol'] = os.path.splitext(filename)[0]

        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Define new column names
new_column_names = ["Kline_open_time", "Open_price", "High_price", "Low_price", "Close_price", "Volume", "Kline_close_time", "Quote_asset_volume", "Number_of_trades", "Taker_buy_base_asset_volume", "Taker_buy_quote_asset_volume", "Ignore", "symbol"]

# Rename columns
final_df.columns = new_column_names

# Save the final DataFrame to a CSV file
csv_file_path = "C:/Users/RPC/Desktop/bi/data/csvfiles_klines/allklines.csv"
final_df.to_csv(csv_file_path, index=False)

print(f'Transformation complete. CSV file saved at: {csv_file_path}')
