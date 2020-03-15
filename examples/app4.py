from web3 import Web3
import json

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

print(
    f'is connected: {web3.isConnected()} block number: {web3.eth.blockNumber}\ndefault account: {web3.eth.defaultAccount}')

abi = json.loads(
    '[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

address = web3.toChecksumAddress('0x5D114B98a5dCCc183554F66c177E79e55011eb0A')

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Hash Hash Hi there friends').transact()

# print(tx_hash)

web3.eth.waitForTransactionReceipt(tx_hash)

print(f'updated greeting: {contract.functions.greet().call()}')
