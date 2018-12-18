providerURL = ""

Config = dict(
    organizerAddress = "",
    voterAddress = "",
)

voterConfig = dict(
    voterChoice = 1,
    voterPrivateKey = "",
)

organizerConfig = dict(
    blindPrivateKeyExponent = ,
    voterPrivateKey = "",
)

contractAddress = ""

contractABI = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "VoteString",
				"type": "string"
			},
			{
				"name": "signedVoteString",
				"type": "string"
			}
		],
		"name": "sendBallot",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "msg",
				"type": "string"
			}
		],
		"name": "sendBlindMessage",
		"outputs": [
			{
				"name": "id",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "id",
				"type": "uint256"
			},
			{
				"name": "msg",
				"type": "string"
			}
		],
		"name": "sendSignedBlindMessage",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "exponent",
				"type": "string"
			},
			{
				"name": "modulus",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"name": "msg",
				"type": "string"
			}
		],
		"name": "newBlindMessage",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": False,
				"name": "msg",
				"type": "string"
			}
		],
		"name": "newSignedBlindMessage",
		"type": "event"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ballots",
		"outputs": [
			{
				"name": "VoteString",
				"type": "string"
			},
			{
				"name": "signedVoteString",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "blindPublicKey",
		"outputs": [
			{
				"name": "exponent",
				"type": "string"
			},
			{
				"name": "modulus",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]