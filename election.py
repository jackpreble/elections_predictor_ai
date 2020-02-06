class Election:

    def __init__(self, year, state, party, totalVotes):
        self.year = year
        self.state = state
        self.party = party
        self.totalVotes = totalVotes

    def add_candidate(self, candidate):
        self.party.append(candidate)

    def __str__(self):
        to_print = str(self.year) + ' ' + self.state + ' ' + str(self.party) + ' ' + str(self.totalVotes)
        for candidate in self.party:
            to_print += '\n' + str(candidate)
        return to_print

    #def election_winner(self):
        #for election in election_results:
            #if election[1] == election[1] and election[0] == election[0]:
    def __eq__(self, other):
        if isinstance(other, Election):
            return self.year == other.year and self.state == other.state
        return False

    def __lt__(self, other):
        if self.state == other.state:
            return self.year < other.year
        else:
            return self.state < other.state

    '''def __le__(self, other):
        if self.state == other.state:
            return self.year <= other.year
        else:
            return self.state <= other.state'''

    def __gt__(self, other):
        if self.state == other.state:
            return self.year > other.year
        else:
            return self.state > other.state