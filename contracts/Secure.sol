pragma solidity >=0.4.25 <0.6.0;

contract SecureElection
{
    int bjp_votes;
    int congress_votes;
    int aap_votes;
    int nota_votes;
    constructor() public
    {
        bjp_votes = 0;
        congress_votes = 0;
        aap_votes = 0;
        nota_votes = 0;
    }
    function get_bjp_votes() public view  returns(int)
    {
        return bjp_votes;
    }
    function get_congress_votes() public view  returns(int)
    {
        return congress_votes;
    }
    function get_aap_votes() public view  returns(int)
    {
        return aap_votes;
    }
    function get_nota_votes() public view  returns(int)
    {
        return nota_votes;
    }
    function vote(int vote_num) public
    {
        if(vote_num==1)
        {
            bjp_votes++;
        }
        else if(vote_num==2)
        {
            congress_votes++;
        }
        else if(vote_num==3)
        {
            aap_votes++;
        }
        else if(vote_num==0 )
        {
            nota_votes++;
        }
    }

}