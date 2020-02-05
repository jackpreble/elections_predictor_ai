class Election:

    def __init__(self, year, state, special, totalVotes):
        self.year = year
        self.state = state
        self.special = special
        self.candidates = []
        self.totalVotes = totalVotes

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def __str__(self):
        to_print = str(self.year) + ' ' + self.state + ' ' + str(self.special) + ' ' + str(self.totalVotes)
        for candidate in self.candidates:
            to_print += '\n' + str(candidate)
        return to_print

    #def election_winner(self):
        #for election in election_results:
            #if election[1] == election[1] and election[0] == election[0]: