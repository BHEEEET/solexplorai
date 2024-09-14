import requests
import json

# Solana mainnet RPC endpoint
url = "https://api.mainnet-beta.solana.com"
block = 289000000

# Define the request payload to get recent transactions
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBlock",
    "params":[
        block,
        {
        "encoding": "json",
        "maxSupportedTransactionVersion":0,
        "transactionDetails":"full",
        "rewards":False
      }
    ]
}

# Send the request to Solana's RPC API
response = requests.post(url, json=payload)
blockdata = response.json()

# print(json.dumps(blockdata, indent=4))

txs = blockdata["result"]["transactions"]

print(f'Total transactions (block {block}): {len(txs)}')

# print(json.dumps(txs, indent=4))

