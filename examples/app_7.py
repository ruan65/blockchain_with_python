from web3 import Web3
from props.vars import key, wallet

infura_url = f'https://mainnet.infura.io/v3/{key}'

web3 = Web3(Web3.HTTPProvider(infura_url))

latest = web3.eth.blockNumber
print(f'is connected: {web3.isConnected()}\nlast block: {latest}')

account = web3.eth.account.create()

key_store = account.encrypt('foobar')

decrypted = web3.eth.account.decrypt(key_store, 'foobar')

