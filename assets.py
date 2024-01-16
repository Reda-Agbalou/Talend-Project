import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    balances = data.get("balances", [])
    non_zero_balances = [balance for balance in balances if float(balance['free']) != 0 or float(balance['locked']) != 0]

    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['asset', 'free', 'locked']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for balance in non_zero_balances:
            writer.writerow({'asset': balance['asset'], 'free': balance['free'], 'locked': balance['locked']})

if __name__ == "__main__":
    json_file_path = "c:\\Users\\RPC\\Desktop\\bi\\data\\binance_account_info.json"  
    csv_file_path = "c:\\Users\\RPC\\Desktop\\bi\\data\\M3aaaalem.csv"  

    json_to_csv(json_file_path, csv_file_path)


