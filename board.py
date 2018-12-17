from operator import attrgetter


class Board(object):
    def __init__(self):
        self.tokens = [[], [], [], [], [], [], [], [], [], []]

    def current_tokens(self):
        return len([token for token in self.tokens if token != []])

    def available_tokens(self):
        return {self.tokens.index(token): token for token in self.tokens if token != []}

    def add_token(self, token):
        self.tokens[0] = token

    def move_token(self, start_place):
        token_to_move = self.tokens[start_place]
        next_empty = self.tokens[start_place:].index(next(token for token in self.tokens[start_place:] if token == [])) + start_place
        self.tokens[next_empty] = token_to_move
        token_to_move.price = 9 - next_empty
        self.tokens[start_place] = []

    def remove_token(self, token):
        index_to_remove = self.tokens.index(token)
        self.tokens[index_to_remove] = []

    def get_cheapest_token(self):
        try:
            return min([token for token in self.tokens if token != []], key=attrgetter('price'))
        except:
            return None

    def get_most_expensive_token(self):
        most_expensive_token = max([token for token in self.tokens if token != []], key=attrgetter('price'))
        most_expensive_token_index = self.tokens.index(most_expensive_token)
        return most_expensive_token, most_expensive_token_index

    def display_available_actions(self):
        available_actions = []
        if self.current_tokens() < 3:
            available_actions.append({'d': '(d)raw a token.'})
        if self.current_tokens() > 0:
            available_actions.append({'b': '(b)uy a token from the board.'})
        if self.current_tokens() > 1:
            available_actions.append({'m': '(m)ove a token on the board.'})
        return available_actions

    def __str__(self):
        return '----------------\n' + \
               '\n'.join(['{}: {}'.format(9-self.tokens.index(token), str(token)) for token in self.tokens if token != []]) + \
               '\n----------------'

