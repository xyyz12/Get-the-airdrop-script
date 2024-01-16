
import requests
import json


def get_airdrop_amount(self, from_address):
    address =from_address.lower()
    url = f'https://https://www.zksyncpepe.com/resources/amounts/{address}.json'
    try:
        response = requests.get(url, Timeout = 5)
        amount = response.json()[0]
        return int(amount)
    except:
        print(f'查询地址{address}时出错：{e}')
        return 0
    
def get_proof(self, address):    
    headers = {
        
        
        
    
        }

def claim(self, web3, proof, amount):
    contract_address = '0x95702a335e3349d197036acb04beca1b4997a91a'
    to_address = web3.to_checksum_address(contract_address)
    abi = [{
      "constant": False,
      "inputs": [
          {"name":"proof","type":"bytes32[]"}, 
          {"name":"amount","type":"uint256"}
        ],
      "name": "claim",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    }]
    contract = web3.eth.contract(address=to_address, abi=abi)
    return contract.functions.claim(proof, amount)




def claim_pepe(self, from_address, private_key):
    #1. 获取空投数量
    airdrop_amount = self.get_airdrop_amount(from_address)
    if airdrop_amount == 0:
        print(f'地址{from_address}没有空投')
        return False

    print(f'地址{from_address}有{airdrop_amount}个zkpep空投')

    #2. 获取空投证明
    print('获取证明中......')
    proof = self.get_proof(from_address)
    if proof == False:
        print(f'地址{from_address}获取空投证明失败')
        return False
    
    #3. 发送交易领取空投
    print('开始领取空投......')
    try:
        amount = self.web3.to_wei(airdrop_amount, 'ether')
        func = self.claim(self.web3, proof, amount)
        return self.helper.call_contract_function(from_address, private_key, func)
    except Exception as e:
        print(f'地址{from_address}领取空投失败：{e}')
        return False
    
    
if __name__ == '__main__':
    claim_pepe()
    

