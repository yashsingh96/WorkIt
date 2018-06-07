from _bisect import bisect
from colorsys import rgb_to_hsv

import pylab
from PIL import Image
from cv2.cv2 import imread
from matplotlib import patches
from sklearn.cluster import KMeans


def main():
    image = Image.open("monochromatic.png")
    # im = Image.open("monochromatic.png")
    # pixels = list(im.getdata())
    #
    # width, height = im.size
    #
    # hsl_pixels = []
    #
    # for pixel in pixels:
    #     # print(pixel)
    #     h, l, s = rgb_to_hls(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
    #     hsl_pixels.append((int(round(h * 359)), int(round(l * 100)), int(round(s * 100))))
    #
    # hue_vals = [15, 45, 65, 165, 180, 265, 300, 340, 360]
    # colour_vals = 'ROYGCBPVR'
    #
    # for i in range (0, height):
    #     str = ""
    #     for j in range (0, width):
    #         curr_colour = colour_vals[bisect(hue_vals, hsl_pixels[width * j + i][0])]
    #         str +=  curr_colour
    #
    #     print(str)
    #

    # backgroundColor = (0,) * 3
    # pixelSize = 80
    #
    # image = Image.open('monochromatic.png')
    # image = image.resize((round(image.size[0] / pixelSize), round(image.size[1] / pixelSize)), Image.NEAREST)
    # w,h = image.size
    # image = image.crop((w/5, h/5, w*4/5, h*3/5))
    #
    # print(image.size)
    # imgdata = list(image.getdata())

    return


def get_colours(img, plot):
    height, width, dim = img.shape

    img_vec = pylab.np.reshape(img, [height * width, dim])

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(img_vec)

    unique_l, counts_l = pylab.np.unique(kmeans.labels_, return_counts=True)
    sort_ix = pylab.np.argsort(counts_l)
    sort_ix = sort_ix[::-1]

    fig = pylab.plt.figure()
    ax = fig.add_subplot(111)
    x_from = 0.05

    hsl_colours = []

    for cluster_center in kmeans.cluster_centers_[sort_ix]:
        cluster_center = [int(cluster_center[0]), int(cluster_center[1]), int(cluster_center[2])]
        hsl_colours.append(rgb_to_hsv(cluster_center[2] / 255, cluster_center[1] / 255, cluster_center[0] / 255))

        ax.add_patch(patches.Rectangle((x_from, 0.05), 0.29, 0.9, alpha=None,
                                       facecolor='#%02x%02x%02x' % (
                                           cluster_center[2], cluster_center[1], cluster_center[0])))
        x_from = x_from + 0.4

    if plot:
        pylab.plt.show()

    return hsl_colours


def get_common_colours(src, plot=False):
    img = imread(src)
    height, width, dim = img.shape

    img = img[int(height / 4):int(3 * height / 4), int(width / 3):int(2 * width / 3), :]
    height, width, dim = img.shape

    # img_top = img[0:int(height * 2 / 5), 0:width, :]
    # top_colours = get_colours(img_top, plot)
    #
    # img_bottom = img[int(height * 2 / 5):height, 0:width, :]
    # bottom_colours = get_colours(img_bottom, plot)

    colours = get_colours(img, plot)

    return colours


def monochromatic(colours):
    # print(colours)
    hue_vals = [-10, -5, -2, 15, 45, 65, 165, 180, 265, 300, 340, 360]
    colour_vals = '0GROYGCBPVR'

    curr_colour = None

    for colour in colours:
        H, S, L = colour
        H = H * 360
        S = S * 100
        L = L * 100

        if S <= 10:
            H = -3

        if L <= 10:
            continue

        if L > 97:
            continue

        if curr_colour is None:
            curr_colour = bisect(hue_vals, H)

        elif curr_colour != bisect(hue_vals, H):
            return False

    return True


def offspring(colours):
    hue_vals = [-10, -5, -2, 15, 45, 65, 165, 180, 265, 300, 340, 360]

    colour1, colour2 = colours
    return abs(colour1[0]*359 - colour2[0]*359) < 80


def analogous(colours):
    return False


def matches(colours):

    does_match = False

    # monochromatic
    if monochromatic(colours):
        print(colours)
        print("hi")
        return True

    # analogous
    if analogous(colours):
        return True

    # offspring
    if offspring(colours):
        return True

    return False


def classification(colour):
    H, S, L = colour


if __name__ == "__main__":
    main()
