import pytest

from ..vote import *


DEFAULT_CANDIDATES = [
    'potato',
    'carrot',
    'cheese'
]


@pytest.fixture
def electionSetup():
    return Election(DEFAULT_CANDIDATES)


def addSingleVote(election):
    oldVoteNumber = len(election.votes)
    vote = Vote({
        DEFAULT_CANDIDATES[0]: 0,
        DEFAULT_CANDIDATES[1]: 2,
        DEFAULT_CANDIDATES[2]: 6
    })
    election.addVote(vote)

    assert len(election.votes) == oldVoteNumber + 1

    election.addVote({
        DEFAULT_CANDIDATES[0]: 0,
        DEFAULT_CANDIDATES[1]: 2,
        DEFAULT_CANDIDATES[2]: 6
    })

    assert len(election.votes) == oldVoteNumber + 2


def replaceVotes(election):
    replacementVote = Vote({
        DEFAULT_CANDIDATES[0]: 6,
        DEFAULT_CANDIDATES[1]: 0,
        DEFAULT_CANDIDATES[2]: 0
    })

    try:
        election.votes = [replacementVote]
    except AttributeError:
        pass
    else:
        assert False


def addAndChangeSingleVote(election):
    vote = Vote({
        DEFAULT_CANDIDATES[0]: 0,
        DEFAULT_CANDIDATES[1]: 2,
        DEFAULT_CANDIDATES[2]: 6
    })
    voteId = election.addVote(vote)
    election.votes[voteId].grades[DEFAULT_CANDIDATES[1]] = 3  # carrot: 2 -> 3
    
    assert election.votes[voteId].grades[DEFAULT_CANDIDATES[1]] == 3


def changeCandidates(election):
    election.candidates = ['rottenPotato', 'badApple']
    
    assert election.candidates == DEFAULT_CANDIDATES


def testElection(electionSetup):
    addSingleVote(electionSetup)  # should succeed
    changeCandidates(electionSetup)  # should fail
    replaceVotes(electionSetup)  # should fail
    addAndChangeSingleVote(electionSetup)  # should succeed
