allPurposeSheep = "Choose a card in your hand. Play this card as a copy of the card you choose."
beFruitful = "Duplicate one of your sheep cards."
crowding = "Release all but two sheep cards."
dominion = "Choose any number of sheep cards in the field. Add their values and then replace them with one sheep card of equal or lesser value."
fallingRock = "Release one Sheep card."
fillTheEarth = "Place as many 1 sheep cards as you like in the field."
flourish = "Choose one of your sheep cards and receive three sheep cards of one rank lower."
goldenHooves = "Raise the rank of as many sheep cards as you like, except for your higest-ranking sheep card."
inspiration = "Look through the deck and add one card of your choice to your hand, and then re-shuffle the deck."
lightning = "Release one of your highest-ranking Sheep."
meteor = "Remove this card from the game, and then release three sheep cards."
multiply = "Place one 3 sheep card in the field."
plague = "Release all sheep cards of one rank."
planningSheep = "Remove one card in you hand from the game."
sheepDog = "Release one card from your hand."
shephion = "Release seven sheep cards."
slump = "Release half of your sheep cards (round down)."
storm = "Release two sheep cards."
wolves = "Reduce the rank of your highest-ranking sheep card by one. If your highest-ranking sheep card is 1, release it."

eventos  = [allPurposeSheep, crowding, fallingRock, fillTheEarth, flourish]
eventos += [goldenHooves, inspiration, lightning, meteor, multiply, plague]
eventos += [planningSheep, sheepDog, shephion, slump, storm, wolves]
eventos += [beFruitful] * 3 + [dominion] * 2

negras, mano, descarte, campo = 1, [], [], [1]
