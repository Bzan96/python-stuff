'''
Dog 10
Cat 5
Hamster 2
Fish 7
Snake 1
Eagle 3
'''

# Can't just use it, it only works in a browser or similar.
# Need to look for a good solution, eg. openbrowser or maybe tkinter?

import pygal

piechart = pygal.Pie()
piechart.title = "Favourite Pets"
piechart.add("Dog", 10)
piechart.add("Cat", 5)
piechart.add("Hamster", 2)
piechart.add("Fish", 7)
piechart.add("Snake", 1)
piechart.add("Eagle", 3)
piechart.render()



barchart = pygal.Bar()
barchart.title = "Favourite NHL Teams"
barchart.add("Penguins", 15)
barchart.add("Flyers", 1)
barchart.add("Blackhawks", 14)
barchart.add("Kings", 12)
barchart.add("Canadiens", 10)
barchart.add("Maple Leafs", 9)
barchart.add("Senators", 2)
barchart.add("Blue Jackets", 2)
barchart.render()