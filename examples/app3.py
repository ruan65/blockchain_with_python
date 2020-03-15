from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

print(f'is connected: {web3.isConnected()} block number: {web3.eth.blockNumber}')

account_1 = '0xFDf85ef3b65806CdA3b33ff36f57D7fbC1717357'
account_2 = '0xc7fbc7a572bCdf91972E465C9a5D47F626fD01e5'

private_key = '1a93f9b73935978188667b722cf86d83adbfe9a1e403ef93a3a03726ddd0c72c'

# get the nonce
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction

tx = {
    "nonce": nonce,
    "to": account_2,
    "value": web3.toWei(0.05, 'ether'),
    "gas": 2000000,
    "gasPrice": web3.toWei('50', 'gwei')
}
# sign a transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send a transaction
tx_cache = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get a transaction cache
print(f'transaction hash: {web3.toHex(tx_cache)}')
