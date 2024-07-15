from web3 import Web3

# Connect to the Ganache network using Web3
ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set the Ethereum address and private key of the admin
admin_address = '0x5F7d25C7094EA9Cb8EC896a11e3491a3bD4A4Db7'  # Replace with the admin's address
admin_private_key = '0x3b1d4766cf4bf230a98dff63c5b3c65e6da48a3513291507ae1ae05fd63baf04'  # Replace with the admin's private key

# Set the contract address and ABI
contract_address = '0x17D9486181F99d50EE87984CD95eC0A8b363B15a'
contract_abi = ''' [
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "adminAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "candidates",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "id",
          "type": "uint256"
        },
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "uint256",
          "name": "voteCount",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "candidatesCount",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "electionStarted",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "voters",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "string[]",
          "name": "_candidateNames",
          "type": "string[]"
        }
      ],
      "name": "startElection",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_candidateId",
          "type": "uint256"
        }
      ],
      "name": "vote",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getElectionStatus",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getElectionResults",
      "outputs": [
        {
          "internalType": "string[]",
          "name": "",
          "type": "string[]"
        },
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "endElection",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getCandidateIdsAndNames",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        },
        {
          "internalType": "string[]",
          "name": "",
          "type": "string[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "clearCandidates",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]'''
vadd = ["0xC431E8eaBE890AddF4eF9eE5517e6f26F69683a4",
        "0xd3286B6E13D3D116763190E1FF8d52bcac25A2D1",
        "0x83f88b4d0378e95D5a892F51A92015505903bd36",
        "0x82880688ECA05D8372D900A5795D45297312AaC5",
]

vpvt=["0xd564b69ba0b6fe160ded84de30d4b5e3b348fba3b0a01af12314865ef836e0e8",
      "0x262f47604d357a195c5859c4e97d0cf798d190b036b1998d66be2e2483702f6c",
      "0x815a1719644f72a96b00bbe2bc4a0240ba064f5998d9ceb6d2989fd4c0cd1713",
      "0x3ab2caa246f4baa6b13a7e7bced76da721426f8cfda6656394c758d78d6786a1",
]
# Create an instance of the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def start_election(candidate_names):
    # Ensure that the provided candidate names list is not empty
    assert len(candidate_names) > 0, "Candidate names list cannot be empty"

    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Check if the election has already started
    election_started = contract.functions.getElectionStatus().call()
    if election_started:
        print("Election has already started. Please end the current election before starting a new one.")
        return

    # Start the election by calling the startElection function in the contract
    transaction = contract.functions.startElection(candidate_names).build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)


def vote(candidate_id, vid):
    voter_private_key = vpvt[int(vid[10])]
    # Ensure the candidate ID is valid
    candidates_count = contract.functions.candidatesCount().call()
    assert candidate_id > 0 and candidate_id <= candidates_count, "Invalid candidate ID"

    # Unlock the voter's account
    voter_address = web3.eth.account.from_key(voter_private_key).address

    # Check if the voter has already voted
    has_voted = contract.functions.voters(voter_address).call()
    if has_voted:
        print("Voter has already voted")
        return

    # Vote for the candidate by calling the vote function in the contract
    transaction = contract.functions.vote(candidate_id).build_transaction({
        'from': voter_address,
        'nonce': web3.eth.get_transaction_count(voter_address),
        'gas': 200000
    })
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=voter_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)


def get_election_status():
    # Retrieve the current election status from the contract
    election_status = contract.functions.getElectionStatus().call()
    return election_status


def get_election_results():
    # Retrieve the election results from the contract
    candidate_names, vote_counts = contract.functions.getElectionResults().call()
    results = list(zip(candidate_names, vote_counts))
    return results


def end_election():
    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Check if the election has already ended
    election_ended = contract.functions.getElectionStatus().call()
    if not election_ended:
        print("Election has not started yet or has already ended.")
        return

    # End the election by calling the endElection function in the contract
    transaction = contract.functions.endElection().build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)

def get_candidate_ids_and_names():
    # Retrieve the number of candidates from the contract
    candidates_count = contract.functions.candidatesCount().call()

    # Retrieve the candidate IDs and names from the contract
    candidate_ids = []
    candidate_names = []
    for i in range(1, candidates_count + 1):
        candidate = contract.functions.candidates(i).call()
        candidate_ids.append(candidate[0])
        candidate_names.append(candidate[1])

    # Combine the candidate IDs and names into a list of tuples
    candidates = list(zip(candidate_ids, candidate_names))

    return candidates

def clear_candidates():
    # Ensure that the election has not started
    election_started = contract.functions.getElectionStatus().call()
    if election_started:
        print("Cannot clear candidates while the election is ongoing.")
        return

    # Unlock the admin account
    web3.eth.defaultAccount = admin_address

    # Clear all candidate IDs and names by calling the clearCandidates function in the contract
    transaction = contract.functions.clearCandidates().build_transaction({
        'from': admin_address,
        'nonce': web3.eth.get_transaction_count(admin_address),
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=admin_private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(transaction_hash)

