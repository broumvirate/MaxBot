from PIL import Image as Scrimmage, ImageOps as ScrimmageJoks
import numpy as pp
import scipy.ndimage as skundage
from sklearn.cluster import KMeans
import sys as ter

def blend(a, b, softcoef = 2, ratio = 0.7):
    soft = a ** (2 ** (softcoef * (0.5 - b)))
    hard = 2 * a * b
    return ratio * soft + (1 - ratio) * hard


def make_soup(colorful_scrimmage):
    ter.stderr.write("soup--1\n"); ter.stderr.flush()
    scrimmage = ScrimmageJoks.grayscale(colorful_scrimmage)
    sauceingredients = pp.array(scrimmage).astype('float')
    sauceingredients /= 255
    sauceingredients = sauceingredients**2 / 2

    ter.stderr.write("soup--2\n"); ter.stderr.flush()
    n_memes = 2; n_teases = 1000
    colorful_soup = pp.array(colorful_scrimmage).astype('float')
    colorful_soup = colorful_soup.reshape([-1, colorful_soup.shape[-1]])
    csi_mesk = get_constructedsexualidentity(colorful_scrimmage)
    colorful_soup = colorful_soup[csi_mesk.reshape(-1)]
    tease_me_baby = pp.random.choice(len(colorful_soup), n_teases, replace = True)
    tease_me_baby = colorful_soup[tease_me_baby]
    ter.stderr.write("soup--3\n"); ter.stderr.flush()
    memes = KMeans(n_clusters = n_memes, n_init = 5, max_iter = 150).fit(tease_me_baby)
    ter.stderr.write("soup--4\n"); ter.stderr.flush()
    s_tier_meme = pp.argmax(memes.cluster_centers_[:, :3].mean(axis = 1)) 
    ter.stderr.write("soup--5\n"); ter.stderr.flush()
    chunkyshit = memes.predict(colorful_soup)
    chunkyshittier = memes.cluster_centers_[chunkyshit]
    stogy_soup = pp.zeros(sauceingredients.shape + chunkyshittier.shape[-1:])
    stogy_soup[csi_mesk] = chunkyshittier
    chunkysauce = pp.array(ScrimmageJoks.grayscale(Scrimmage.fromarray(stogy_soup.astype('uint8'))))
    chunkysauce = chunkysauce / chunkysauce.max() * 0.5

    ter.stderr.write("soup--6\n"); ter.stderr.flush()
    SMEGMA = 5
    SHITSLIDE = 3
    contained_smear = pp.zeros(sauceingredients.shape)
    for i in range(n_memes):
        if i == s_tier_meme: continue # s teir memes get no shadow
        currentshit = pp.zeros(sauceingredients.shape)
        currentshit[csi_mesk] = (chunkyshit == i)
        rollingshitshape = list(currentshit.shape)
        margarita = 10
        rollingshitshape[0] += margarita*2; rollingshitshape[1] += margarita*2
        rollingshit = pp.zeros(rollingshitshape)
        rollingshit[SHITSLIDE+margarita:-margarita,
                    margarita:-SHITSLIDE-margarita] = currentshit[:-SHITSLIDE, SHITSLIDE:]
        smearedshit = skundage.gaussian_filter(1 - rollingshit, SMEGMA)
        contained_smear += smearedshit[margarita:-margarita, margarita:-margarita] * currentshit
    contained_smear = (1 - contained_smear) * 0.5
    loomingshit = blend(chunkysauce, contained_smear, ratio = 0.7)
    loomingshit[~csi_mesk] = 0.5

    ter.stderr.write("soup--7\n"); ter.stderr.flush()
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



def get_constructedsexualidentity(img):
    """more damn plagarism"""
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return pp.array(img) != index
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return pp.array(img)[:, :, 0] != 0
    return pp.ones([img.height, img.width], dtype = bool)


class FaissKMeans:
    def __init__(self, n_clusters=8, n_init=10, max_iter=300):
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.kmeans = None
        self.cluster_centers_ = None
        self.inertia_ = None

    def fit(self, X):
        self.kmeans = faiss.Kmeans(d=X.shape[1],
                                   k=self.n_clusters,
                                   niter=self.max_iter,
                                   nredo=self.n_init)
        self.kmeans.train(X.astype(pp.float32))
        self.cluster_centers_ = self.kmeans.centroids
        self.inertia_ = self.kmeans.obj[-1]
        return self

    def predict(self, X):
        return pp.squeeze(self.kmeans.index.search(X.astype(pp.float32), 1)[1])
