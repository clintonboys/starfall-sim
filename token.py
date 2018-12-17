import math


class Token(object):
    def __init__(self, stars, comets, planets, moons, cloud, black_holes):
        self.stars = stars
        self.comets = comets
        self.planets = planets
        self.moons = moons
        self.cloud = cloud
        self.has_cloud = 1 if self.cloud != 'no' else 0
        self.black_holes = black_holes
        self.value = math.ceil(float(self.stars * 0.4) + float(self.comets * 0.6) + float(self.planets * 1.4) +
                               float(self.moons * 0.5) + float(self.has_cloud))
        self.price = 9

    def __str__(self):
        attributes = {'Star': self.stars, 'Comet': self.comets, 'Planet': self.planets,
                      'Moon': self.moons, 'Black hole': self.black_holes}
        has_cloud = True if self.cloud != 'no' else False
        pretty_print = ''
        for attribute, value in attributes.iteritems():
            if value > 0:
                if attribute == 'Black hole':
                    pretty_print += '; {}'.format(attribute)
                else:
                    if value > 1:
                        pretty_print += '; {} {}s'.format(value, attribute)
                    else:
                        pretty_print += '; 1 {}'.format(attribute)
        if has_cloud:
            pretty_print += '; {} cloud'.format(self.cloud)
        return pretty_print[2:]
