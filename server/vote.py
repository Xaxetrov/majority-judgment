from uuid import uuid4


class Election:
    def __init__(self, candidates=[], choiceNumber=6):
        self._candidates = candidates
        self._choiceNumber = choiceNumber
        self._results = []
        self._votes = {}

    @property
    def candidates(self):
        return self._candidates

    @candidates.setter
    def candidates(self, newCandidates):
        if not self._votes:
            self._candidates = newCandidates

    @property
    def choiceNumber(self):
        return self._choiceNumber

    @property
    def votes(self):
        return self._votes
            
    def addVote(self, vote):
        voteId = uuid4()
        try:
            vote.id = voteId
        except AttributeError:  # If vote is not an object but a dict (grades) instead
            vote = Vote(vote)  # Construct vote with grades
            vote.id = voteId
        self._votes[voteId] = vote
        return voteId

    def checkAndAddVote(self, vote):
        try:
            grades = vote.grades
        except AttributeError:  # If vote is not an object but a dict (grades) instead
            vote = Vote(vote)  # Construct vote with grades
            grades = vote.grades
        return self.addVote(vote) if all((grade < self._choiceNumber for grade in grades)) else None


    @property
    def results(self):
        return self._results

    def updateResults(self):
        results = {(candidate, [0] * self._choiceNumber) for candidate in self._candidates}
        for vote in self._votes:
            print(vote)


class Vote:
    def __init__(self, grades={}):
        self._id = None
        self.grades = grades

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, newId):
        if self._id is None:
            self._id = newId

def getVote(request):
    return 'Get vote'

def postVote(request):
    return 'Post vote'
