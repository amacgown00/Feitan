from eth_hash.auto import keccak
message = b"hello ethereum"
digest = keccak(message)

print("Input:", message)
print("Keccak-256:", digest.hex())


"""
This shows how to implement the Keccak-256 algorithm from 
the eth_hash library so you don't have to download an Ethereum client.


Ethereum uses Keccak-256, an algorithm that creates hashes for:
- Addresses
- Transactions
- Public and private keys
- Blocks

- Keccak-256 is different from SHA3-256. 

- Ethereum started using Keccak before SHA-3 was finalized and continues to use it for consistency.  

- Protocol documentation 
- What it is
- Why it exists
- How it's used
- what output looks like 
"""