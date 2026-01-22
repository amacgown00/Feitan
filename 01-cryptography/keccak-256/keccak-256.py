from eth_hash.auto import keccak
message = b"hello ethereum"
digest = keccak(message)

print("Input:", message)
print("Keccak-256:", digest.hex())