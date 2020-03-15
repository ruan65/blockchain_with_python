from web3 import Web3
from props.vars import key, wallet

infura_url = f'https://mainnet.infura.io/v3/{key}'

web3 = Web3(Web3.HTTPProvider(infura_url))

latest = web3.eth.blockNumber
# print(f'is connected: {web3.isConnected()}\nlast block: {latest}')

# for i in range(5):
#     print(f'{web3.eth.getBlock(latest - 1)}')

b_hash = '0xbcd625f17fd2afd0d697115e250f8968f2323aa273615110b3c4b959ba799d85'

print(web3.eth.getTransactionByBlock(b_hash, 0))


