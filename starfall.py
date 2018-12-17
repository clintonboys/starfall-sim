#!/usr/bin/python
from utils import load_tokens
from player import Player
from board import Board


def main():
    print 'Welcome to Starfall simulator version 1!\n'
    player1 = Player(1, True)
    player2 = Player(2, False)
    board = Board()
    tokens = load_tokens(17)
    active_player = player1
    inactive_player = player2
    x = 1
    while len(tokens) + board.current_tokens() > 1:
        print 'Turn ', x, ' (player {})'.format(active_player.id)
        print ' Tokens remaining: ', len(tokens)
        if not active_player.is_human:
            cheapest_token = board.get_cheapest_token()
            if len(tokens) > 0 and ((board.current_tokens() == 0) or (board.tokens[0] == [] and board.current_tokens() < 3)):
                print ' Player {} draws a token.\n'.format(active_player.id)
                token = tokens[0]
                board.add_token(token)
                del tokens[0]
            elif ((board.current_tokens() < 3 and board.tokens[0] != []) or
                  (board.current_tokens() == 3 and cheapest_token.price >= cheapest_token.value) or
                  (len(tokens) == 0 and cheapest_token.price >= cheapest_token.value) or
                  (active_player.stardust < cheapest_token.price)):
                print ' Player {} moves a token.\n'.format(active_player.id)
                active_player.play_token(board)
            elif (cheapest_token.price < cheapest_token.value):
                active_player.acquire_token(cheapest_token, board)
        else:
            print ' Your tokens: '
            print '  ' + '\n  '.join([str(token) for token in active_player.tokens])
            print ' Stardust : {}'.format(active_player.stardust)
            print ' Choose your action: '
            available_actions = board.display_available_actions()
            action = raw_input('\n'.join([action.values()[0] for action in available_actions]) + '\n..$ ')
            if action == 'd':
                print ' Player {} draws a token.\n'.format(active_player.id)
                token = tokens[0]
                board.add_token(token)
                del tokens[0]
            elif action == 'b':
                available_tokens = board.available_tokens()
                print ' Choose a token to buy: '
                token_to_buy = raw_input('  ' + '\n  '.join(['({}): {}'.format(9 - token_index, available_tokens[token_index])
                                                       for token_index in available_tokens.keys()]) + '\n..$')
                active_player.acquire_token(available_tokens[9-int(token_to_buy)], board)
            elif action == 'm':
                print ' Player {} moves a token.\n'.format(active_player.id)
                active_player.play_token(board)
        active_player, inactive_player = inactive_player, active_player
        print board
        x += 1
    print '-- GAME OVER!'
    p1score = player1.get_score(player2)
    p2score = player2.get_score(player1)
    if p1score > p2score:
        print '----\nPLAYER 1 WINS!'
    elif p2score > p1score:
        print '----\nPLAYER 2 WINS!'
    else:
        print '----\nSCORES TIED!'


if __name__ == '__main__':
  main()
