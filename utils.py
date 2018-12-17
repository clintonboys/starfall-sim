import json
import random
from token import Token


def load_tokens(num_tokens):
    with open('tokens.json') as f:
        game_tokens = json.load(f)
    token_list = []
    for token in game_tokens:
        token_list.append(Token(token['stars'], token['comets'], token['planets'],
                                token['moons'], token['cloud'], token['black_holes']))
    return random.sample(token_list, num_tokens)
