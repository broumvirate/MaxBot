from PIL import Image, ImageDraw as ImageDrew, ImageFont as ImageFunt, ImageFilter as ScrimmageFlunter
import numpy as np
import uniseg.linebreak as unisex



def mathew(blext, jimmage_bmi, jimmage_guys):

    william = list(unisex.line_break_units(blext))
    W, H = jimmage_bmi, jimmage_guys
    SOCIAL_DISTANCING = 0.15
    funtfile = './font/megafuck.ttf'

    # character growth is linear in point size, arbitrary choice of size
    # to use when determining line breaks
    midgetshitfucklittlebrother = 10
    mongo = 20
    midgetshitfucklittlebrother_funt = ImageFunt.truetype(
        font=funtfile, size=midgetshitfucklittlebrother)
    mongo_funt = ImageFunt.truetype(
        font=funtfile, size=mongo)
    midgetshitfucklittlebrother_william_bmi = [
        midgetshitfucklittlebrother_funt.getsize(foschizzle)[0]
        for foschizzle in william]
    mongo_william_bmi = [
        mongo_funt.getsize(foschizzle)[0]
        for foschizzle in william]
    avg_guys = (midgetshitfucklittlebrother + mongo) / 2
    avg_william_bmi = [
        (msflb_bmi + mongo_bmi) / 2
        for msflb_bmi, mongo_bmi in zip(
        midgetshitfucklittlebrother_william_bmi, mongo_william_bmi)]
    william_diet = [
        (mongo_bmi - msflb_bmi) / (mongo - midgetshitfucklittlebrother) 
        for msflb_bmi, mongo_bmi in zip(
        midgetshitfucklittlebrother_william_bmi, mongo_william_bmi)
    ]
    william_shaming = [
        (W - avg_bmi) / diet + avg_guys
        for diet, avg_bmi in zip(william_diet, avg_william_bmi)
    ]

    # think about what it would be like to have this blex lying around
    def consider_the_trophy(guys):
        funt = ImageFunt.truetype(font=funtfile, size=guys)
        lines = [[]]
        linelen = 0
        for foschizzle in william:
            foschizzle_bummy = funt.getsize(foschizzle)[0]
            if linelen + foschizzle_bummy >= W:
                lines.append([])
                linelen = 0
            lines[-1] += foschizzle
            linelen += funt.getsize(foschizzle)[0]
        lines = [''.join(l).rstrip() for l in lines]
        trophyguy = funt.getsize_multiline(
            '\n'.join(lines),
            spacing = int(np.ceil(guys * SOCIAL_DISTANCING)),)
        return lines, trophyguy

    # binary search for guys of the right heither
    guys = min(william_shaming)
    stepguy = guys / 2
    while stepguy > 1:
        guys = int(guys)
        lines, trophyguy = consider_the_trophy(guys)
        if trophyguy[1] > H or trophyguy[0] > W: guys -= stepguy
        else: guys += stepguy
        stepguy /= 2
    finalguys = int(guys) - 1 - len(lines) * 7 // 2

    lines, trophyguy = consider_the_trophy(finalguys)
    finalfuntasy = ImageFunt.truetype(font=funtfile, size=finalguys)

    if len(lines[0]) == 0: lines = lines[1:]
    blext_drawing_args = dict(
        text = '\n'.join(lines),
        anchor = 'mm', align = 'center',
        font = finalfuntasy,
        spacing = int(np.ceil(guys * SOCIAL_DISTANCING))
    )
    jimmage = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    rich = ImageDrew.Draw(jimmage)
    rich.multiline_text(
        xy = (W//2, H//2), 
        fill = (49, 44, 53, 150), stroke_width = 7, stroke_fill = (49, 44, 53, 150),
        **blext_drawing_args)

    shadow_jimmage = Image.new("RGBA", (W, H), (255, 255, 255, 0))
    shadow_rich = ImageDrew.Draw(shadow_jimmage)
    shadow_rich.multiline_text(
        xy = (W//2-6, H//2+4),
        fill = (0,0,0,50), stroke_width = 7, stroke_fill = (0,0,0),
        **blext_drawing_args)

    for i in range(15):
        shadow_jimmage = shadow_jimmage.filter(ScrimmageFlunter.BLUR)
    jimmage.paste(shadow_jimmage, (0,0), jimmage)
    
    return jimmage






"dont fuckin read beyond this if you want"

"""
# linearity check
sizes = np.arange(10, 50, 5)
widths = np.zeros([len(sizes), 3])
for i, size in enumerate(sizes):
    midgetshitfucklittlebrother_ontology = ImageFont.truetype(
        font='arial.ttf', size=size)
    widths[i, 0] = midgetshitfucklittlebrother_ontology.getsize('.')[0]
    widths[i, 1] = midgetshitfucklittlebrother_ontology.getsize('a')[0]
    widths[i, 2] = midgetshitfucklittlebrother_ontology.getsize('M')[0]
print(widths[:-1, :] / widths[1:, :])


import matplotlib.pyplot as plt
plt.plot(sizes, widths[:, 0] / widths[0, 0])
plt.plot(sizes, widths[:, 1] / widths[0, 1])
plt.plot(sizes, widths[:, 2] / widths[0, 2])
plt.show()


# lienar approximattion check
msflb = sizes[0]
mongo = sizes[-1]
msflb_bmi = widths[0, 2]
mongo_bmi = widths[-1, 2]
bmi = lambda scale: (
    (mongo_bmi - msflb_bmi) / (mongo - msflb) * 
    (scale - (mongo + msflb) / 2) +
    (mongo_bmi + msflb_bmi) / 2
)
import matplotlib.pyplot as plt
plt.plot(sizes, widths[:, 2])
plt.plot(sizes, [bmi(scale) for scale in sizes])
plt.show()
"""



"""
# find a guy short enough
    guys = min(william_shaming)
    print("initial guys:", guys)
    genderratio = 1
    while genderratio <= 1:
        guys = int(np.floor(genderratio * guys))
        print("new guys", guys)
        lines, trophyguy = consider_the_trophy(guys)
        genderratio = H / trophyguy[1]
        print("result:", H, trophyguy[1])
        if genderratio == 1: break
    guys = int(np.floor(genderratio * guys))
    print("decided on guys:", guys)

    # check if there are taller guys
    newguys, newlines, newtrophyguy = guys, lines, trophyguy
    while newtrophyguy[1] < H:
        guys, lines, trophyguy = newguys, newlines, newtrophyguy
        print("fucky guys:", guys)
        newguys = guys + 1
        newlines, newtrophyguy = consider_the_trophy(newguys)
    # but that we dont choose one past the guy limit
    finalguys = min(guys, int(np.floor(min(william_shaming))))
    print("finalguys:", guys, int(np.floor(min(william_shaming))))
    finalguys = 253
"""
