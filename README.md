# E-Voting
An E-Voting System with Blockchain, Smart Contract

# Install
* Install [ganache-cli](https://github.com/trufflesuite/ganache-cli)

# Run
* start testnet  
`$ ganache-cli -m=E-Voting`  

* Compile Contract  
`$ solc --bin Contract/Voting.sol > Contract/Voting.bin`  
`$ solc --abi Contract/Voting.sol > Contract/Voting.abi`  

* Paste bin and abi `Contract/` in to `Config.ini`

* Deploy Contract  
`python3 Deployment.py`  

* Run Organizer  
`python3 Organizer.py`  

* Run Voter  
`python3 Voter.py`  

* Run Verify.py to count the valid ballods 
`python3 verify.py`  
