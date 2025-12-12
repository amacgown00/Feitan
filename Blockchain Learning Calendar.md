# __1.5-Month Accelerated Calendar (6 Weeks)__  
__Protocol / Core Engineering Technical Writer Track__

__Focus areas:__ Blockchain foundations, cryptography, Python scripting, RPC, Solidity, Rust, Go, reading specs.

## WEEK 1 — Blockchain Foundations + Environment Setup
__MON__
- Set up GitHub Codespace \
<a href="https://docs.github.com/en/codespaces" target="_blank">Github Codespace Guide</a>
- Create a "protocol-learning" repo
- Start: Blockchain basics \
  <a href="https://www.preethikasireddy.com/post/how-does-ethereum-work-anyway" target="_blank">How Does Ethereum Work Anyway</a>

__TUE__

- Read: What is a blockchain? \
<a href="https://www.ibm.com/topics/blockchain" target="_blank">IBM Blockchain</a>
- Read: Blocks, Merkle trees, hashes \
<a href="https://www.geeksforgeeks.org/merkle-tree-cryptography/" target="blank">Merkle Tree Cyroptography</a>

__WED__

- Read: How Ethereum works\
<a href="https://ethereum.org/en/developers/docs/" target="_blank">Ethereum Docs</a>
- In Codespace: create a folder /notes-week1/

__THU__

- Learn: Transactions + gas\
https://ethereum.org/en/developers/docs/gas/
- Start writing your own explanation of "How a blockchain works"

__FRI__

- Learn: Private keys & wallets\
https://andersbrownworth.com/blockchain/public-private-keys/
- Codespace task: Implement SHA-256 hash in Python (hashlib)

__SAT__

- Watch crashes-course overview\
https://www.youtube.com/watch?v=bBC-nXj3Ng4
- Summarize Bitcoin vs Ethereum

__SUN__

REST or review day

## WEEK 2 — Cryptography + Python Transaction Signing
__MON__

- Learn Elliptic Curve Cryptography basics\
https://cryptobook.nakov.com/elliptic-curve-cryptography/ecc-introduction

- Codespace: pip install ecdsa

__TUE__

- Learn how digital signatures work\
https://www.section.io/engineering-education/elliptic-curve-cryptography/

__WED__

- Codespace Python task:
  - generate keypair
  - sign message
  - verify signature\
(Use <mark>ecdsa</mark> library)

__THU__

Read: Ethereum accounts & signing
https://ethereum.org/en/developers/docs/accounts/

Try Python: sign a dummy Ethereum-style message

FRI

Learn JSON-RPC
https://www.jsonrpc.org/specification

Test calling RPC endpoints with Python requests

SAT

Read: What is an RPC node?
https://ethereum.org/en/developers/docs/nodes-and-clients/

Codespace: write Python script to call eth_blockNumber

SUN

REST or catch-up

📅 WEEK 3 — Solidity Fundamentals + Smart Contract Interaction
MON

Read: Solidity basics
https://docs.soliditylang.org/en/latest/

Set up Remix IDE in browser:
https://remix.ethereum.org/

TUE

Deploy a simple contract in Remix

Study: functions, events, storage
https://ethereum.org/en/developers/docs/smart-contracts/

WED

Codespace: write Python script to call a smart contract read method

Use web3.py
https://web3py.readthedocs.io/

THU

Read: ABI, bytecode
https://docs.soliditylang.org/en/latest/abi-spec.html

Document how ABI works (portfolio piece)

FRI

Write a technical explanation:
“How a smart contract call works from RPC → EVM execution”

SAT

Review & practice testnets:
https://chainlist.org/

SUN

REST

📅 WEEK 4 — Rust Essentials (for blockchain clients)
MON

Install Rust
https://www.rust-lang.org/learn/get-started

(Works inside Codespace!)

TUE

Learn Rust basics (Variables, ownership)
https://doc.rust-lang.org/book/

WED

Learn: Structs, Enums, Pattern Matching
https://doc.rust-lang.org/book/ch06-00-enums.html

THU

Write small Rust programs in Codespace

hash a string

read + parse JSON

FRI

Read code from real blockchain client:
▸ Ethereum Rust client (“Reth”)
https://github.com/paradigmxyz/reth

SAT

Take notes: consensus, block validation in Reth

SUN

REST

📅 WEEK 5 — Go Essentials (for blockchain clients)
MON

Install Go
https://go.dev/doc/install

(in Codespace)

TUE

Go basics
https://go.dev/tour/welcome/1

WED

Learn: goroutines, channels
https://gobyexample.com/goroutines

THU

Read real client code (Go-Ethereum “geth”)
https://github.com/ethereum/go-ethereum

FRI

Document: “How geth handles incoming transactions”

SAT

Codespace: Write Go code
▸ fetch latest block via RPC
▸ parse transaction count

SUN

REST

📅 WEEK 6 — Consensus, Specs, and Portfolio Assembly
MON

Read: Nakamoto Consensus
https://bitcoin.org/bitcoin.pdf

TUE

Read: Ethereum PoS consensus
https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/

WED

Read and summarize an EIP
https://eips.ethereum.org/

THU

Portfolio piece:
“Explain EIP-1559 in plain English”
https://eips.ethereum.org/EIPS/eip-1559

FRI

Create a “Protocol Technical Writer Portfolio” repo

Put notes

Add 3 specs rewrites

Add 3 technical blog-style docs

Add Python/Rust/Go scripts

SAT

Prepare final writing sample

“How an Ethereum transaction travels through mempool → block inclusion”

SUN

Done 🎉
