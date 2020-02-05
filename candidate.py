class Candidate:

    def __init__(self, name, party, numVotes):
        self.name = name
        self.party = party
        self.numVotes = numVotes

    def __str__(self):
        return self.name + ', ' + self.party + ': ' + str(self.numVotes)