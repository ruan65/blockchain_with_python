from web3 import Web3
from settings.vars import key, wallet

infura_url = f'https://mainnet.infura.io/v3/{key}'

web3 = Web3(Web3.HTTPProvider(infura_url))

print(f'is connected: {web3.isConnected()}\nlast block: {web3.eth.blockNumber}')

balance = web3.eth.getBalance(Web3.toChecksumAddress(f'{wallet}'))

print(f'balance: {web3.fromWei(balance, "ether")} eth')
