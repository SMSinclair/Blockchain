import json
import requests
import sys

if len(sys.argv)==3:
    command = sys.argv[1]
    name = sys.argv[2]

    if command == 'save' or command == 'change':
        with open("user_id.txt", "w") as f:
            f.write(name)

elif len(sys.argv)==2:
    name = sys.argv[1]

elif len(sys.argv)==1:
    # Load ID
    f = open("user_id.txt", "r")
    name = f.read()
    f.close()

elif len(sys.argv)>3:
     print("ERROR: too many arguments!")
     exit()

node = "http://localhost:5000"

r = requests.get(url=node + "/chain")
    # Handle non-json response
try:
    data = r.json()
except ValueError:
    print("Error: Non-json response")
    print("Response returned:")
    print(r)
    exit()


current_balance = 0
user_transactions = []

for item in data['chain']:
    for transaction in item['transactions']:
        if transaction['recipient']==name:
            user_transactions.append((transaction['sender'], transaction['recipient'], transaction['amount']))
            current_balance = current_balance + transaction['amount']

for item in user_transactions:
    print(f'{item[0]} sent {item[2]} coins to {item[1]}.')
print(f'The balance for {name} is {current_balance}.')
