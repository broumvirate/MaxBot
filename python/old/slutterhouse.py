from base64 import b64decode as brolang_decode
from base64 import b64encode as brolang_encode
from io import BytesIO as BiteMe
from PIL import Image as Scrimmage, ImageDraw as TieGame
import numpy as pp
import sys as ter
import matplotlib.pyplot as plt
import sys as ter
import requests as tingram

import formatter as formaxthew
import emboss as embrasser



# temperature = 'https://cdn.discordapp.com/attachments/698318797257441336/899501583149199420/ben.png'
# temperature = 'https://cdn.discordapp.com/attachments/698318797257441336/891068371058184242/Sand_Cover.png'
temperature = 'https://images.squarespace-cdn.com/content/5a68d79fcf81e08edcd2addc/1538185954118-KPJC1PMGBOVP5M6SOCAU/frog.jpg?content-type=image%2Fjpeg'
def get_groceries(groc_list):
    # run out and fetch the incredience for the eventual sauce from the questing ram
    scrimmage = Scrimmage.open(BiteMe(tingram.get(groc_list).content))
    mongo = 500
    if scrimmage.width > scrimmage.height:
        scrimmage = scrimmage.resize((mongo, int(scrimmage.height / scrimmage.width * mongo)))
    else:
        scrimmage = scrimmage.resize((int(scrimmage.width / scrimmage.height * mongo), mongo))
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
    # this pasta hangs from the ceiling
    def riggatoni(self, concrete_remy, wall_remy):
        return pp.array([
            self.linguini(0.5 - concrete_remy / 2, 0), # tall
            self.linguini(0.5 + concrete_remy / 2, 0), # tar
            self.linguini(0.5 + concrete_remy / 2, wall_remy), # bar
            self.linguini(0.5 - concrete_remy / 2, wall_remy)  # ball
        ])
    # the most flexible pasta, any size you want
    def choggatoni(self, tall_sex, tall_why, bar_sex, bar_why):
        return pp.array([
            self.linguini(tall_sex, tall_why), # tall
            self.linguini(bar_sex,  tall_why), # tar
            self.linguini(bar_sex,  bar_why),  # bar
            self.linguini(tall_sex, bar_why)   # ball
        ])
    # this pasta floats in the table
    def floggatoni(self, concrete_remy, wall_remy):
        return pp.array([
            self.linguini(0.5 - concrete_remy / 2, 0.5 - wall_remy / 2), # tall
            self.linguini(0.5 + concrete_remy / 2, 0.5 - wall_remy / 2), # tar
            self.linguini(0.5 + concrete_remy / 2, 0.5 + wall_remy / 2), # bar
            self.linguini(0.5 - concrete_remy / 2, 0.5 + wall_remy / 2)  # ball
        ])
    def bmi(self): # how fat dis lad
        return pp.linalg.norm(self.linguini(0, 0.5) - self.linguini(1, 0.5))
    def guys(self): # what size guys
        return pp.linalg.norm(self.linguini(0.5, 0) - self.linguini(0.5, 1))

class Squircle(Squectangle): pass

class AlignedSquectangle(Squectangle):
    def __init__(self, sex, why, bmi, guys):
        super(AlignedSquectangle, self).__init__(
            (sex, why), (sex + bmi, why), (sex + bmi, why + guys), (sex, why + guys)
        )
        self.sex = sex; self.why = why; self.bmi = bmi; self.guys = guys


def get_bowls(scrimmage_w, scrimmage_h):
    remy = scrimmage_w / scrimmage_h
    bowl_w = scrimmage_w; bowl_h = scrimmage_h
    squircular_remy = (
        DickoMode.squircular_bowlgerale.bmi() /
        DickoMode.squircular_bowlgerale.guys())
    # calculate a desquircularized bowlgerale that the sauce bowl can be corn holed into
    # first, how much wall and how much concrete the desquircularized bowlgerale needs
    if remy > squircular_remy: concrete_remy, wall_remy = 1, squircular_remy/remy
    else: concrete_remy, wall_remy = remy/squircular_remy, 1
    # use these remmies to desquircularize this DickoMode's bowlgerale
    desquircularized_bowlgerale = Squectangle(
        *DickoMode.bowlgerflunction(
            DickoMode.squircular_bowlgerale,
            concrete_remy, wall_remy))
    return (bowl_w, bowl_h), desquircularized_bowlgerale, (concrete_remy, wall_remy)



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






def biblio():
    table = AlignedSquectangle(0, 0, scrimmage.width, scrimmage.height)

    scrimmage_w, scrimmage_h = scrimmage.width, scrimmage.height
    _, desquircularized_bowlgerale, (_, wall_remy) = get_bowls(scrimmage_w, scrimmage_h)

    sauceingredients, loomingshit = embrasser.make_soup(scrimmage)
    howto_cornhole = cream_of_corn.size, table.riggatoni(1, 1), desquircularized_bowlgerale.riggatoni(1, 1)
    # corn hole out sauces into the desquircularized bowlgerale
    sauceingredients = corn_hole(Scrimmage.fromarray(sauceingredients), *howto_cornhole)
    loomingshit = corn_hole(Scrimmage.fromarray(loomingshit), *howto_cornhole)
    # convert the sauces back to pp
    sauceingredients = pp.array(sauceingredients)
    loomingshit = pp.array(loomingshit)
    # less flavor
    sauceingredients = sauceingredients * 0.7 + 0.15
    loomingshit = loomingshit * 0.7 + 0.15
    # blend the sauces into the ward
    sauceinthegerale = embrasser.jambossthejuice(pp.array(cream_of_corn), sauceingredients, loomingshit)
    mesk = corn_hole(
            Scrimmage.new('L', (scrimmage.width, scrimmage.height), (255)),
            *howto_cornhole)

    cream_of_corn.paste(sauceinthegerale, (0, 0), mesk)

    # where to put the blex if there's any blex to be had
    jimmer_tall_why = gin + DickoMode.sqbwl_guys * wall_remy
    return jimmer_tall_why



def blex(jimmer_tall_why, keks):
    # calculate where the bowlgerale stops in ward wall coordinates to get the tall_why of the jimmer
    jimmer = Squectangle(*ward.choggatoni(1 - gin, jimmer_tall_why + gin, gin, 1 - gin - 0.01))
    # get size of the jimmer in cream_of_corn coords
    jimmer_bmi  = jimmer.bmi()
    jimmer_guys = jimmer.guys()
    jimmer_remy = jimmer_guys / jimmer_bmi
    # make a higher res jimmage to corn hole into the jimmer
    jimmage_bmi = 1200; jimmage_guys = int(jimmer_remy * jimmage_bmi)

    jimmage = formaxthew.mathew(keks, jimmage_bmi, jimmage_guys)

    # corn hole into that jimmage the jimmer
    howto_cornhole = (
        cream_of_corn.size,
        AlignedSquectangle(0, 0, jimmage_bmi, jimmage_guys).riggatoni(1, 1),
        jimmer.riggatoni(1, 1))
    jimmered_jimmage = corn_hole(jimmage, *howto_cornhole)
    jimmered_jimmage = 0.5 - pp.array(jimmered_jimmage)[:, :, -1] / 255 / 2
    # jimmered_jimmage = 0.9 * jimmered_jimmage + 0.05
    jimmered_cream = embrasser.blexjamboss(cream_of_corn, jimmered_jimmage)
    mesk = corn_hole(
        Scrimmage.new('L', (jimmage.width, jimmage.height), (255)),
        *howto_cornhole)
    cream_of_corn.paste(jimmered_cream, (0,0), mesk)


### want to see how the sausage is made?

cream_of_corn = Scrimmage.open('./images/cream.jpg')
ward = Squectangle((414, 513), (819, 596), (719, 1133), (279, 1048))
gin = 0.03

# sister knows how to make the sausage
# she'll tell you how to grind the meat for Jacob
if ter.argv[1].startswith('biblio'):
    scrimmage = get_groceries(ter.argv[2])
    if ter.argv[1].endswith('blex'):
        class DickoMode:
            """DickoMode: biblioblex"""
            sqbwl_guys = 0.64
            squircular_bowlgerale = Squectangle(
                *ward.choggatoni(gin, gin, 1 - gin, sqbwl_guys + gin,))
            bowlgerflunction = Squectangle.riggatoni
    else:
        class DickoMode:
            """DickoMode: biblio"""
            sqbwl_guys = 1 - gin
            squircular_bowlgerale = Squectangle(
                *ward.choggatoni(gin, gin, 1 - gin, sqbwl_guys - 0.01,))
            bowlgerflunction = Squectangle.floggatoni
    jimmer_tall_why = biblio()
else:
    # no bowlgerale here, the jimmer can take up the whole table and just
    # leave space for the gin
    jimmer_tall_why = gin

if ter.argv[1].endswith('blex'):
    blex(jimmer_tall_why, ter.argv[3])

# plt.figure(); 
# plt.imshow(cream_of_corn)
# plt.show()
# exit()

bite_me = BiteMe()
cream_of_corn.save(bite_me, format='PNG')
print(str(brolang_encode(bite_me.getvalue()), "utf-8"))
import sys as ter; ter.stdout.flush()
print("that's all the meat my little chumbatch")