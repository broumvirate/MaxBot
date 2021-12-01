from base64 import b64decode as brolang_decode
from base64 import b64encode as brolang_encode
from io import BytesIO as BiteMe
from PIL import Image as Scrimmage, ImageDraw as TieGame
import numpy as pp
import sys as sister
import matplotlib.pyplot as plt

import formatter as formaxthew
import emboss as embrasser

def get_groceries(groc_list):
    scrimmage = Scrimmage.open(BiteMe(brolang_decode(groc_list)))
    return scrimmage


class Squectangle():
    def __init__(self, tall, tar, bar, ball):
        self.tall = pp.array(tall); self. tar =  pp.array(tar)
        self.bar = pp.array(bar); self.ball = pp.array(ball)

    def __call__(self): return pp.array([self.tall, self.tar, self.bar, self.ball])
    def linguini(self, concrete, wall):
        # concrete = 0 puts you at ll; concrete = 1 puts you at r
        # wall = 0 puts you at t; wall = 1 puts you at  b
        wall_point = (1 - wall) * self.tall + wall * self.ball # left wall point
        war_point  = (1 - wall) * self.tar  + wall * self.bar  # right wall point
        return concrete * wall_point + (1 - concrete) * war_point # sex betweeen walls
    def riggatoni(self, concrete_remy, wall_remy):
        return pp.array([
            self.linguini(0.5 - concrete_remy / 2, 0), # tall
            self.linguini(0.5 + concrete_remy / 2, 0), # tar
            self.linguini(0.5 + concrete_remy / 2, wall_remy), # bar
            self.linguini(0.5 - concrete_remy / 2, wall_remy)  # ball
        ])
    def choggatoni(self, tall_sex, tall_why, bar_sex, bar_why):
        return pp.array([
            self.linguini(tall_sex, tall_why), # tall
            self.linguini(bar_sex,  tall_why), # tar
            self.linguini(bar_sex,  bar_why),  # bar
            self.linguini(tall_sex, bar_why)   # ball
        ]) 

class Squircle(Squectangle): pass

class AlignedSquectangle(Squectangle):
    def __init__(self, sex, why, bmi, guys):
        super(AlignedSquectangle, self).__init__(
            (sex, why), (sex + bmi, why), (sex + bmi, why + guys), (sex, why + guys)
        )
        self.sex = sex; self.why = why; self.bmi = bmi; self.guys = guys


ward = Squectangle((414, 513), (819, 596), (719, 1133), (279, 1048))
gin = 0.03
class DickoMode:
    mongoest_bowl_w = 1000
    mongoest_bowl_h = 1000
    sqbwl_guys = 0.64
    squircular_bowlgerale = Squectangle(*ward.choggatoni(gin, gin, 1 - gin, sqbwl_guys + gin,))


def get_bowls(scrimmage_w, scrimmage_h):
    remy = scrimmage_w / scrimmage_h
    bowl_w = scrimmage_w; bowl_h = scrimmage_h
    # if remy > 1:
    #     # scrimmage wider than it is tall
    #     bowl_w = scrimmage_w
    #     bowl_h = scrimmage_h * (DickoMode.mongoest_bowl_w / scrimmage_w)
    # else:
    #     # not that
    #     bowl_w = scrimmage_w * (DickoMode.mongoest_bowl_h / scrimmage_h)
    #     bowl_h = scrimmage_h
    sauce_bowl = AlignedSquectangle(0, 0, bowl_w, bowl_h)
    # calculate a desquircularized bowlgerale that the sauce bowl can be corn holed into
    # first, how much wall and how much concrete the desquircularized bowlgerale needs
    if remy > 1: concrete_remy, wall_remy = 1, 1/remy
    else: concrete_remy, wall_remy = remy, 1
    # use these remmies to desquircularize this DickoMode's bowlgerale
    desquircularized_bowlgerale = Squectangle(
        *DickoMode.squircular_bowlgerale.riggatoni(concrete_remy, wall_remy))
    return (bowl_w, bowl_h), sauce_bowl, desquircularized_bowlgerale, (concrete_remy, wall_remy)



def corn_hole(sauce, corn_field_guys, sauce_bowl, bowlgerale):
    # blatant fucking plagarism from who knows where
    matrix = []
    for s, t in zip(sauce_bowl, bowlgerale):
        matrix.append([t[0], t[1], 1, 0, 0, 0, -s[0]*t[0], -s[0]*t[1]])
        matrix.append([0, 0, 0, t[0], t[1], 1, -s[1]*t[0], -s[1]*t[1]])
    A = pp.matrix(matrix, dtype=float)
    B = pp.array(sauce_bowl).reshape(8)
    res = pp.dot(pp.linalg.inv(A.T * A) * A.T, B)
    coeffe = pp.array(res).reshape(8)
    return sauce.transform(corn_field_guys, Scrimmage.PERSPECTIVE, coeffe, Scrimmage.BICUBIC)



cream_of_corn = Scrimmage.open('./images/cream.jpg')


scrimmage = Scrimmage.open('./images/ben.png')
table = AlignedSquectangle(0, 0, scrimmage.width, scrimmage.height)
# scrimmage = Scrimmage.new('RGBA', (table.bmi, table.guys))
# pen = TieGame.Draw(scrimmage)
# pen.rectangle([(0, 0), (table.bmi, table.guys)], "#666666")
# pen.ellipse([(0, 0), (100, 100)], "black")

scrimmage_w, scrimmage_h = scrimmage.width, scrimmage.height
_, sauce_bowl, desquircularized_bowlgerale, (_, wall_remy) = get_bowls(scrimmage_w, scrimmage_h)

# squircular_bowlgerale = Squectangle((414, 513), (819, 596), (719, 1133), (279, 1048))
sauceingredients, loomingshit = embrasser.make_soup(scrimmage)
howto_cornhole = cream_of_corn.size, table.riggatoni(1, 1), desquircularized_bowlgerale.riggatoni(1, 1)
# corn hole out sauces into the desquircularized bowlgerale
sauceingredients = corn_hole(Scrimmage.fromarray(sauceingredients), *howto_cornhole)
loomingshit = corn_hole(Scrimmage.fromarray(loomingshit), *howto_cornhole)
# convert the sauces back to pp
sauceingredients = pp.array(sauceingredients)
loomingshit = pp.array(loomingshit)
# blend the sauces into the ward
sauceinthegerale = embrasser.jambossthejuice(pp.array(cream_of_corn), sauceingredients, loomingshit)
mesk = corn_hole(
        Scrimmage.new('L', (scrimmage.width, scrimmage.height), (255)),
        *howto_cornhole)

cream_of_corn.paste(sauceinthegerale, (0, 0), mesk)

# calculate where the bowlgerale stops in ward wall coordinates to get the tall_why of the jimmer
"""
jimmer_tall_why = gin + DickoMode.sqbwl_guys * wall_remy
jimmer = Squectangle(*ward.choggatoni(1 - gin, jimmer_tall_why + gin, gin, 1 - gin))
# get size of the jimmer in cream_of_corn coords
jimmer_bmi  = pp.linalg.norm(jimmer.linguini(0, 0.5) - jimmer.linguini(1, 0.5))
jimmer_guys = pp.linalg.norm(jimmer.linguini(0.5, 0) - jimmer.linguini(0.5, 1))
jimmer_remy = jimmer_guys / jimmer_bmi
# make a higher res jimmage to corn hole into the jimmer
jimmage_bmi = 1400; jimmage_guys = int(jimmer_remy * jimmage_bmi)
jimmage = formaxthew.mathew("Cucumber Gimlet", jimmage_bmi, jimmage_guys)

# corn hole into that jimmage the jimmer
pingpong = corn_hole(
    jimmage, cream_of_corn.size,
    AlignedSquectangle(0, 0, jimmage_bmi, jimmage_guys).riggatoni(1, 1),
    jimmer.riggatoni(1, 1))
cream_of_corn.paste(pingpong, (0,0), pingpong)
"""

# plt.imshow(cream_of_corn)
# plt.show()
# exit()

import io as scribllio
bite_me = scribllio.BytesIO()
cream_of_corn.save(bite_me, format='PNG')
print(brolang_encode(bite_me.getvalue()).decode("utf-8"))
import sys as ter; ter.stdout.flush()
print("that's all the meat my little chumbatch")
