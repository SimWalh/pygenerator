"""
Created on Aug 28, 2009

@author: Claude Anderson

Draw color swatches showing all of the predefined TK colors, 
the colors used by TKiinter (and thus by zellegraphics)
Requires the graphics module, available from
   http://www.rose-hulman.edu/class/cs/resources/Python/graphics.html 
"""
from graphics import *

WIN_WIDTH = 1800
WIN_HEIGHT = 1200
ROW_PIXELS = 25  # Height of a swatch
COL_PIXELS = 100  # Width of a swatch
GRID_ROWS = WIN_HEIGHT / ROW_PIXELS  #  maximum number of rows of swatches
GRID_COLS = WIN_WIDTH / COL_PIXELS  #  number of columns of swatches
FONT_SIZE = 8


def upperLeft(col, row):
    "coordinates of upper left corner of this swatch"
    return Point(col * COL_PIXELS, row * ROW_PIXELS)


def lowerRight(col, row):
    "coordinates of upper left corner of this swatch"
    return upperLeft(col + 1, row + 1)
    # return Point((col + 1) * COL_PIXELS, (row + 1) * ROW_PIXELS)


def drawSwatch(col, row, colorName, win):
    """Draw this swatch in this color.  I cannot find a way to get the
       r,g, and b of a named TK color, or of a pixel on the screen, so I
       draw each color name in black and white, figuring that one or the 
       other should be readable """
    ul = upperLeft(col, row)
    lr = lowerRight(col, row)
    rect = Rectangle(ul, lr)
    rect.setFill(colorName)
    text = Text(
        Point(ul.getX() + COL_PIXELS / 2, ul.getY() + ROW_PIXELS / 4), colorName
    )
    text.setSize(FONT_SIZE)
    text2 = Text(
        Point(ul.getX() + COL_PIXELS / 2, ul.getY() + 3 * ROW_PIXELS / 4), colorName
    )
    text2.setSize(FONT_SIZE)
    text2.setFill("white")
    rect.draw(win)
    text.draw(win)
    text2.draw(win)


def main():
    win = GraphWin("Color Swatches", WIN_WIDTH, WIN_HEIGHT)
    colorList = tkColors
    length = len(colorList)
    index = 0
    row = 0
    while index < length and row < GRID_ROWS:
        col = 0
        while index < length and col < GRID_COLS:
            drawSwatch(col, row, colorList[index].strip(), win)
            index += 1
            col += 1
        row += 1
    win.getMouse()
    win.close()


# color list is hard-coded rather than read from a file so that this program
# can be distributed as a single file.

tkColors = [
    "alice blue",
    "AliceBlue",
    "antique white",
    "AntiqueWhite",
    "AntiqueWhite1",
    "AntiqueWhite2",
    "AntiqueWhite3",
    "AntiqueWhite4",
    "aquamarine",
    "aquamarine1",
    "aquamarine2",
    "aquamarine3",
    "aquamarine4",
    "azure",
    "azure1",
    "azure2",
    "azure3",
    "azure4",
    "beige",
    "bisque",
    "bisque1",
    "bisque2",
    "bisque3",
    "bisque4",
    "black",
    "blanched almond",
    "BlanchedAlmond",
    "blue",
    "blue1",
    "blue2",
    "blue3",
    "blue4",
    "blue violet",
    "BlueViolet",
    "brown",
    "brown1",
    "brown2",
    "brown3",
    "brown4",
    "burlywood",
    "burlywood1",
    "burlywood2",
    "burlywood3",
    "burlywood4",
    "cadet blue",
    "CadetBlue",
    "CadetBlue1",
    "CadetBlue2",
    "CadetBlue3",
    "CadetBlue4",
    "chartreuse",
    "chartreuse1",
    "chartreuse2",
    "chartreuse3",
    "chartreuse4",
    "chocolate",
    "chocolate1",
    "chocolate2",
    "chocolate3",
    "chocolate4",
    "coral",
    "coral1",
    "coral2",
    "coral3",
    "coral4",
    "cornflower blue",
    "CornflowerBlue",
    "cornsilk",
    "cornsilk1",
    "cornsilk2",
    "cornsilk3",
    "cornsilk4",
    "cyan",
    "cyan1",
    "cyan2",
    "cyan3",
    "cyan4",
    "dark blue",
    "DarkBlue",
    "dark cyan",
    "DarkCyan",
    "dark goldenrod",
    "DarkGoldenrod",
    "DarkGoldenrod1",
    "DarkGoldenrod2",
    "DarkGoldenrod3",
    "DarkGoldenrod4",
    "dark gray",
    "DarkGray",
    "dark green",
    "DarkGreen",
    "dark grey",
    "DarkGrey",
    "dark khaki",
    "DarkKhaki",
    "dark magenta",
    "DarkMagenta",
    "dark olive green",
    "DarkOliveGreen",
    "DarkOliveGreen1",
    "DarkOliveGreen2",
    "DarkOliveGreen3",
    "DarkOliveGreen4",
    "dark orange",
    "DarkOrange",
    "DarkOrange1",
    "DarkOrange2",
    "DarkOrange3",
    "DarkOrange4",
    "dark orchid",
    "DarkOrchid",
    "DarkOrchid1",
    "DarkOrchid2",
    "DarkOrchid3",
    "DarkOrchid4",
    "dark red",
    "DarkRed",
    "dark salmon",
    "DarkSalmon",
    "dark sea green",
    "DarkSeaGreen",
    "DarkSeaGreen1",
    "DarkSeaGreen2",
    "DarkSeaGreen3",
    "DarkSeaGreen4",
    "dark slate blue",
    "DarkSlateBlue",
    "dark slate gray",
    "DarkSlateGray",
    "DarkSlateGray1",
    "DarkSlateGray2",
    "DarkSlateGray3",
    "DarkSlateGray4",
    "dark slate grey",
    "DarkSlateGrey",
    "dark turquoise",
    "DarkTurquoise",
    "dark violet",
    "DarkViolet",
    "deep pink",
    "DeepPink",
    "DeepPink1",
    "DeepPink2",
    "DeepPink3",
    "DeepPink4",
    "deep sky blue",
    "DeepSkyBlue",
    "DeepSkyBlue1",
    "DeepSkyBlue2",
    "DeepSkyBlue3",
    "DeepSkyBlue4",
    "dim gray",
    "DimGray",
    "dim grey",
    "DimGrey",
    "dodger blue",
    "DodgerBlue",
    "DodgerBlue1",
    "DodgerBlue2",
    "DodgerBlue3",
    "DodgerBlue4",
    "firebrick",
    "firebrick1",
    "firebrick2",
    "firebrick3",
    "firebrick4",
    "floral white",
    "FloralWhite",
    "forest green",
    "ForestGreen",
    "gainsboro",
    "ghost white",
    "GhostWhite",
    "gold",
    "gold1",
    "gold2",
    "gold3",
    "gold4",
    "goldenrod",
    "goldenrod1",
    "goldenrod2",
    "goldenrod3",
    "goldenrod4",
    "gray",
    "gray0",
    "gray1",
    "gray2",
    "gray3",
    "gray4",
    "gray5",
    "gray6",
    "gray7",
    "gray8",
    "gray9",
    "gray10",
    "gray11",
    "gray12",
    "gray13",
    "gray14",
    "gray15",
    "gray16",
    "gray17",
    "gray18",
    "gray19",
    "gray20",
    "gray21",
    "gray22",
    "gray23",
    "gray24",
    "gray25",
    "gray26",
    "gray27",
    "gray28",
    "gray29",
    "gray30",
    "gray31",
    "gray32",
    "gray33",
    "gray34",
    "gray35",
    "gray36",
    "gray37",
    "gray38",
    "gray39",
    "gray40",
    "gray41",
    "gray42",
    "gray43",
    "gray44",
    "gray45",
    "gray46",
    "gray47",
    "gray48",
    "gray49",
    "gray50",
    "gray51",
    "gray52",
    "gray53",
    "gray54",
    "gray55",
    "gray56",
    "gray57",
    "gray58",
    "gray59",
    "gray60",
    "gray61",
    "gray62",
    "gray63",
    "gray64",
    "gray65",
    "gray66",
    "gray67",
    "gray68",
    "gray69",
    "gray70",
    "gray71",
    "gray72",
    "gray73",
    "gray74",
    "gray75",
    "gray76",
    "gray77",
    "gray78",
    "gray79",
    "gray80",
    "gray81",
    "gray82",
    "gray83",
    "gray84",
    "gray85",
    "gray86",
    "gray87",
    "gray88",
    "gray89",
    "gray90",
    "gray91",
    "gray92",
    "gray93",
    "gray94",
    "gray95",
    "gray96",
    "gray97",
    "gray98",
    "gray99",
    "gray100",
    "green",
    "green1",
    "green2",
    "green3",
    "green4",
    "green yellow",
    "GreenYellow",
    "grey",
    "grey0",
    "grey1",
    "grey10",
    "grey100",
    "grey11",
    "grey12",
    "grey13",
    "grey14",
    "grey15",
    "grey16",
    "grey17",
    "grey18",
    "grey19",
    "grey2",
    "grey20",
    "grey21",
    "grey22",
    "grey23",
    "grey24",
    "grey25",
    "grey26",
    "grey27",
    "grey28",
    "grey29",
    "grey3",
    "grey30",
    "grey31",
    "grey32",
    "grey33",
    "grey34",
    "grey35",
    "grey36",
    "grey37",
    "grey38",
    "grey39",
    "grey4",
    "grey40",
    "grey41",
    "grey42",
    "grey43",
    "grey44",
    "grey45",
    "grey46",
    "grey47",
    "grey48",
    "grey49",
    "grey5",
    "grey50",
    "grey51",
    "grey52",
    "grey53",
    "grey54",
    "grey55",
    "grey56",
    "grey57",
    "grey58",
    "grey59",
    "grey6",
    "grey60",
    "grey61",
    "grey62",
    "grey63",
    "grey64",
    "grey65",
    "grey66",
    "grey67",
    "grey68",
    "grey69",
    "grey7",
    "grey70",
    "grey71",
    "grey72",
    "grey73",
    "grey74",
    "grey75",
    "grey76",
    "grey77",
    "grey78",
    "grey79",
    "grey8",
    "grey80",
    "grey81",
    "grey82",
    "grey83",
    "grey84",
    "grey85",
    "grey86",
    "grey87",
    "grey88",
    "grey89",
    "grey9",
    "grey90",
    "grey91",
    "grey92",
    "grey93",
    "grey94",
    "grey95",
    "grey96",
    "grey97",
    "grey98",
    "grey99",
    "honeydew",
    "honeydew1",
    "honeydew2",
    "honeydew3",
    "honeydew4",
    "hot pink",
    "HotPink",
    "HotPink1",
    "HotPink2",
    "HotPink3",
    "HotPink4",
    "indian red",
    "IndianRed",
    "IndianRed1",
    "IndianRed2",
    "IndianRed3",
    "IndianRed4",
    "ivory",
    "ivory1",
    "ivory2",
    "ivory3",
    "ivory4",
    "khaki",
    "khaki1",
    "khaki2",
    "khaki3",
    "khaki4",
    "lavender",
    "lavender blush",
    "LavenderBlush",
    "LavenderBlush1",
    "LavenderBlush2",
    "LavenderBlush3",
    "LavenderBlush4",
    "lawn green",
    "LawnGreen",
    "lemon chiffon",
    "LemonChiffon",
    "LemonChiffon1",
    "LemonChiffon2",
    "LemonChiffon3",
    "LemonChiffon4",
    "light blue",
    "LightBlue",
    "LightBlue1",
    "LightBlue2",
    "LightBlue3",
    "LightBlue4",
    "light coral",
    "LightCoral",
    "light cyan",
    "LightCyan",
    "LightCyan1",
    "LightCyan2",
    "LightCyan3",
    "LightCyan4",
    "light goldenrod",
    "LightGoldenrod",
    "LightGoldenrod1",
    "LightGoldenrod2",
    "LightGoldenrod3",
    "LightGoldenrod4",
    "light goldenrod yellow",
    "LightGoldenrodYellow",
    "light gray",
    "LightGray",
    "light green",
    "LightGreen",
    "light grey",
    "LightGrey",
    "light pink",
    "LightPink",
    "LightPink1",
    "LightPink2",
    "LightPink3",
    "LightPink4",
    "light salmon",
    "LightSalmon",
    "LightSalmon1",
    "LightSalmon2",
    "LightSalmon3",
    "LightSalmon4",
    "light sea green",
    "LightSeaGreen",
    "light sky blue",
    "LightSkyBlue",
    "LightSkyBlue1",
    "LightSkyBlue2",
    "LightSkyBlue3",
    "LightSkyBlue4",
    "light slate blue",
    "LightSlateBlue",
    "light slate gray",
    "LightSlateGray",
    "light slate grey",
    "LightSlateGrey",
    "light steel blue",
    "LightSteelBlue",
    "LightSteelBlue1",
    "LightSteelBlue2",
    "LightSteelBlue3",
    "LightSteelBlue4",
    "light yellow",
    "LightYellow",
    "LightYellow1",
    "LightYellow2",
    "LightYellow3",
    "LightYellow4",
    "lime green",
    "LimeGreen",
    "linen",
    "magenta",
    "magenta1",
    "magenta2",
    "magenta3",
    "magenta4",
    "maroon",
    "maroon1",
    "maroon2",
    "maroon3",
    "maroon4",
    "medium aquamarine",
    "MediumAquamarine",
    "medium blue",
    "MediumBlue",
    "medium orchid",
    "MediumOrchid",
    "MediumOrchid1",
    "MediumOrchid2",
    "MediumOrchid3",
    "MediumOrchid4",
    "medium purple",
    "MediumPurple",
    "MediumPurple1",
    "MediumPurple2",
    "MediumPurple3",
    "MediumPurple4",
    "medium sea green",
    "MediumSeaGreen",
    "medium slate blue",
    "MediumSlateBlue",
    "medium spring green",
    "MediumSpringGreen",
    "medium turquoise",
    "MediumTurquoise",
    "medium violet red",
    "MediumVioletRed",
    "midnight blue",
    "MidnightBlue",
    "mint cream",
    "MintCream",
    "misty rose",
    "MistyRose",
    "MistyRose1",
    "MistyRose2",
    "MistyRose3",
    "MistyRose4",
    "moccasin",
    "navajo white",
    "NavajoWhite",
    "NavajoWhite1",
    "NavajoWhite2",
    "NavajoWhite3",
    "NavajoWhite4",
    "navy",
    "navy blue",
    "NavyBlue",
    "old lace",
    "OldLace",
    "olive drab",
    "OliveDrab",
    "OliveDrab1",
    "OliveDrab2",
    "OliveDrab3",
    "OliveDrab4",
    "orange",
    "orange1",
    "orange2",
    "orange3",
    "orange4",
    "orange red",
    "OrangeRed",
    "OrangeRed1",
    "OrangeRed2",
    "OrangeRed3",
    "OrangeRed4",
    "orchid",
    "orchid1",
    "orchid2",
    "orchid3",
    "orchid4",
    "pale goldenrod",
    "PaleGoldenrod",
    "pale green",
    "PaleGreen",
    "PaleGreen1",
    "PaleGreen2",
    "PaleGreen3",
    "PaleGreen4",
    "pale turquoise",
    "PaleTurquoise",
    "PaleTurquoise1",
    "PaleTurquoise2",
    "PaleTurquoise3",
    "PaleTurquoise4",
    "pale violet red",
    "PaleVioletRed",
    "PaleVioletRed1",
    "PaleVioletRed2",
    "PaleVioletRed3",
    "PaleVioletRed4",
    "papaya whip",
    "PapayaWhip",
    "peach puff",
    "PeachPuff",
    "PeachPuff1",
    "PeachPuff2",
    "PeachPuff3",
    "PeachPuff4",
    "peru",
    "pink",
    "pink1",
    "pink2",
    "pink3",
    "pink4",
    "plum",
    "plum1",
    "plum2",
    "plum3",
    "plum4",
    "powder blue",
    "PowderBlue",
    "purple",
    "purple1",
    "purple2",
    "purple3",
    "purple4",
    "red",
    "red1",
    "red2",
    "red3",
    "red4",
    "rosy brown",
    "RosyBrown",
    "RosyBrown1",
    "RosyBrown2",
    "RosyBrown3",
    "RosyBrown4",
    "royal blue",
    "RoyalBlue",
    "RoyalBlue1",
    "RoyalBlue2",
    "RoyalBlue3",
    "RoyalBlue4",
    "saddle brown",
    "SaddleBrown",
    "salmon",
    "salmon1",
    "salmon2",
    "salmon3",
    "salmon4",
    "sandy brown",
    "SandyBrown",
    "sea green",
    "SeaGreen",
    "SeaGreen1",
    "SeaGreen2",
    "SeaGreen3",
    "SeaGreen4",
    "seashell",
    "seashell1",
    "seashell2",
    "seashell3",
    "seashell4",
    "sienna",
    "sienna1",
    "sienna2",
    "sienna3",
    "sienna4",
    "sky blue",
    "SkyBlue",
    "SkyBlue1",
    "SkyBlue2",
    "SkyBlue3",
    "SkyBlue4",
    "slate blue",
    "SlateBlue",
    "SlateBlue1",
    "SlateBlue2",
    "SlateBlue3",
    "SlateBlue4",
    "slate gray",
    "SlateGray",
    "SlateGray1",
    "SlateGray2",
    "SlateGray3",
    "SlateGray4",
    "slate grey",
    "SlateGrey",
    "snow",
    "snow1",
    "snow2",
    "snow3",
    "snow4",
    "spring green",
    "SpringGreen",
    "SpringGreen1",
    "SpringGreen2",
    "SpringGreen3",
    "SpringGreen4",
    "steel blue",
    "SteelBlue",
    "SteelBlue1",
    "SteelBlue2",
    "SteelBlue3",
    "SteelBlue4",
    "tan",
    "tan1",
    "tan2",
    "tan3",
    "tan4",
    "thistle",
    "thistle1",
    "thistle2",
    "thistle3",
    "thistle4",
    "tomato",
    "tomato1",
    "tomato2",
    "tomato3",
    "tomato4",
    "turquoise",
    "turquoise1",
    "turquoise2",
    "turquoise3",
    "turquoise4",
    "violet",
    "violet red",
    "VioletRed",
    "VioletRed1",
    "VioletRed2",
    "VioletRed3",
    "VioletRed4",
    "wheat",
    "wheat1",
    "wheat2",
    "wheat3",
    "wheat4",
    "white",
    "white smoke",
    "WhiteSmoke",
    "yellow",
    "yellow1",
    "yellow2",
    "yellow3",
    "yellow4",
    "yellow green",
    "YellowGreen",
]


if __name__ == "__main__":
    main()