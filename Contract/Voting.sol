pragma solidity ^0.5.0;
contract Voting {
    address organizer;
    uint blindMessageID;
    
    struct Ballot{
        string VoteString;
        string signedVoteString;
    }
    
    Ballot [] public ballots;
    
    event newBlindMessage(uint id, string msg);
    event newSignedBlindMessage(uint id, string msg);
    
    modifier isOrganizer() {
        require(msg.sender == organizer);
        _;
    }
    
    modifier isVoter() {
        _;
    }
    
    constructor ()
        public
    {
        organizer = msg.sender;
        blindMessageID = 0;
    }
    
    function sendBlindMessage (string memory msg) 
        public
        isVoter
        returns (uint id)
    {
        id = blindMessageID;
        blindMessageID = blindMessageID + 1;
        emit newBlindMessage(id, msg);
    }
    
    function sendSignedBlindMessage (uint id, string memory msg) 
        public
        isOrganizer
    {
        id = blindMessageID;
        blindMessageID = blindMessageID + 1;
        emit newSignedBlindMessage(id, msg);
    }
    
    function sendBallot (string memory VoteString,string memory signedVoteString) 
        public
    {
        ballots.push(Ballot({
            VoteString: VoteString,
            signedVoteString: signedVoteString
        }));
    }
}
