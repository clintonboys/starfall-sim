import math

class Player(object):
    def __init__(self, player_id, is_human):
        self.id = player_id
        self.stardust = 7 + 5 * 5
        self.tokens = []
        self.is_turn = False
        self.score = 0
        self.is_human = is_human

    def acquire_token(self, token, board):
        print ' Player {} acquires token [{}S {}P {}M {}C {} cloud]\n ' \
              '   for {} stardust ({} remaining)\n'.format(self.id, token.stars, token.planets, token.moons,
                                                      token.comets, token.cloud, token.price, self.stardust)
        self.tokens.append(token)
        self.stardust -= token.price
        board.remove_token(token)

    def play_token(self, board):
        _, current_index = board.get_most_expensive_token()
        board.move_token(current_index)

    def is_turn(self):
        self.is_turn = True

    def is_not_turn(self):
        self.is_turn = False

    def get_score(self, player2):
        my_stars = sum([token.stars for token in self.tokens])
        their_stars = sum([token.stars for token in player2.tokens])
        star_pts = 0
        if my_stars > their_stars:
            star_pts = 10
        elif their_stars < my_stars:
            star_pts = -5
        self.score += star_pts
        num_planets = sum([token.planets for token in self.tokens])
        self.score += num_planets
        num_moons = sum([token.moons for token in self.tokens])
        planet_moon_diff = num_planets - num_moons
        if planet_moon_diff >= 0:
            moon_pts = num_moons*3
            self.score += num_moons*3
        else:
            self.score += (num_planets - planet_moon_diff)*3
            moon_pts = (num_planets - planet_moon_diff)*3
        num_black_holes = sum([token.black_holes for token in self.tokens])
        black_hole_pts = 0
        if num_black_holes == 1:
            black_hole_pts = -5
        elif num_black_holes >= 2:
            black_hole_pts = 15
        self.score += black_hole_pts
        num_comets = sum([token.comets for token in self.tokens])
        comet_pts = 0
        if num_comets == 1:
            comet_pts = 3
        elif num_comets == 2:
            comet_pts = 8
        elif num_comets == 3:
            comet_pts = 15
        elif num_comets == 4:
            comet_pts = 24
        elif num_comets >= 5:
            comet_pts = 7*num_comets
        self.score += comet_pts
        num_clouds = len([token.cloud for token in self.tokens if token.cloud != 'no'])
        self.score += num_clouds*2
        distinct_cloud_colours = len(set([token.cloud for token in self.tokens]))
        cloud_bonus = 0
        if distinct_cloud_colours == 3:
            cloud_bonus = 4
        elif distinct_cloud_colours == 4:
            cloud_bonus += 9
        elif distinct_cloud_colours == 5:
            cloud_bonus += 16
        self.score += cloud_bonus
        self.score += math.ceil((float(self.stardust))/2.0)
        print 'Player {} SCORE SUMMARY: '.format(self.id)
        print ' Stars:      {} ({} pts)'.format(my_stars, star_pts)
        print ' Planets:     {} ({} pts)'.format(num_planets, 5*num_planets)
        print ' Moons:       {} ({} pts)'.format(num_moons, moon_pts)
        print ' Comets:      {} ({} pts)'.format(num_comets, comet_pts)
        print ' Clouds:      {} ({} pts)'.format(num_clouds, num_clouds*2 + cloud_bonus)
        print ' Black holes: {} ({} pts)'.format(num_black_holes, black_hole_pts)
        print ' Remaining stardust: {} ({} pts)'.format(self.stardust, math.ceil((float(self.stardust))/2.0))
        print 'TOTAL: {}\n'.format(self.score)
        return self.score
