from inspect import currentframe
from PIL import Image as Scrimmage, ImageOps as ScrimmageJoks
import numpy as pp
import scipy.signal as skugnil
import matplotlib.pyplot as plt

#sauce = 'saucetest.png'
#wood = 'wood.jpg'

"""
colorful_scrimmage = Image.open(sauce)
scrimmage = ImageOps.grayscale(colorful_scrimmage)
popcorn1 = pp.array(
    [[0, -1, -1], # kernel for embossing bottom left side
     [1,  0, -1],
     [1,  1,  0]])
popcorn2 = pp.array(
    [[-1, -1,  0], # kernel for embossing bottom right side
     [-1,  0,  1],
     [ 0,  1,  1]])

sauceingredients = pp.array(scrimmage)
virginleftpixels = skugnil.convolve2d(sauceingredients, popcorn1, mode = 'valid')
virginrightpixels = skugnil.convolve2d(sauceingredients, popcorn2, mode = 'valid')
chadambidextrouspixels = pp.maximum(-virginleftpixels, -virginrightpixels).astype('float')

chadambidextrouspixels /= abs(chadambidextrouspixels).max()
chadambidextrouspixels = (1 - abs(chadambidextrouspixels))
"""
def blend(a, b, softcoef = 2, ratio = 0.7):
    soft = a ** (2 ** (softcoef * (0.5 - b)))
    hard = 2 * a * b
    return ratio * soft + (1 - ratio) * hard



def make_soup(colorful_scrimmage):
    scrimmage = ScrimmageJoks.grayscale(colorful_scrimmage)
    sauceingredients = pp.array(scrimmage).astype('float')
    sauceingredients /= 255
    sauceingredients = sauceingredients**2 / 2

    from sklearn.cluster import KMeans
    n_memes = 2; n_teases = 2000
    colorful_soup = pp.array(colorful_scrimmage).astype('float')
    colorful_soup = colorful_soup.reshape([-1, colorful_soup.shape[-1]])
    tease_me_baby = pp.random.choice(len(colorful_soup), n_teases, replace = True)
    tease_me_baby = colorful_soup[tease_me_baby]
    memes = KMeans(n_clusters = n_memes, random_state = 0).fit(tease_me_baby)
    s_tier_meme = pp.argmax(memes.cluster_centers_[:, :3].mean(axis = 1))
    chunkyshit = memes.predict(colorful_soup)
    stogy_soup = memes.cluster_centers_[chunkyshit]
    stogy_soup = stogy_soup.reshape(sauceingredients.shape + stogy_soup.shape[-1:])
    chunkysauce = pp.array(ScrimmageJoks.grayscale(Scrimmage.fromarray(stogy_soup.astype('uint8'))))
    chunkysauce = chunkysauce / chunkysauce.max() * 0.5

    import scipy.ndimage as skundage
    SMEGMA = 5
    SHITSLIDE = 3
    contained_smear = pp.zeros(sauceingredients.shape)
    for i in range(n_memes):
        if i == s_tier_meme: continue # s tier memes get no shadow
        currentshit = (chunkyshit == i).astype('float').reshape(sauceingredients.shape)
        rollingshit = currentshit.copy()
        rollingshit[SHITSLIDE:, :-SHITSLIDE] = currentshit[:-SHITSLIDE, SHITSLIDE:]
        rollingshit[:SHITSLIDE, :] = rollingshit[None, SHITSLIDE, :]
        rollingshit[:, -SHITSLIDE:] = rollingshit[:, -SHITSLIDE-1, None]
        smearedshit = skundage.gaussian_filter(1 - rollingshit, SMEGMA)
        contained_smear += smearedshit * currentshit
    contained_smear = (1 - contained_smear) * 0.5
    loomingshit = blend(chunkysauce, contained_smear, ratio = 0.7)

    import cv2 as covid2
    canny = covid2.Canny((sauceingredients * 255).astype('uint8'),100,200)
    canny = covid2.dilate(canny, pp.ones([2, 2], dtype = 'uint8'))
    canny = 1 - (canny/canny.max()).astype('float')
    sauceingredients = canny * 0.3 + 0.2

    return sauceingredients, loomingshit

def jambossthejuice(ouould, sauceingredients, loomingshit):
    ouould = pp.array(ouould)
    sauceingredients = pp.array(sauceingredients)
    loomingshit = pp.array(loomingshit)
    gravy = blend( (ouould/255),  loomingshit[:, :, None], softcoef = 4)
    gravy = blend( gravy,  sauceingredients[:, :, None] )
    return Scrimmage.fromarray(pp.clip(gravy * 255, 0, 255).astype('uint8'))

def blexjamboss(ouould, loomingshit):
    ouould = pp.array(ouould)
    loomingshit = pp.array(loomingshit)
    gravy = blend( (ouould/255),  loomingshit[:, :, None], softcoef = 4)
    return Scrimmage.fromarray(pp.clip(gravy * 255, 0, 255).astype('uint8'))



# plt.imshow(ouould)
# plt.show()