print('Welcome to the second RPG text adventure in the Charlie B saga. The first was a demo, but this is the real deal.')
name = input('What is your name: ')
print('Hello', name , 'Please tell me what you chose for the last game, if you have not played the first, I suggest you go back and do so.')
weapon1 = input('What was the weapon you chose? Staff, Sword, or Bow? ')
if weapon1 == ('Staff')or weapon1 == ('staff') :
    print('The old woman says, Ah, a taste for the arcane this one, you may start out slow, but eventually, I see great things coming your way.')
elif weapon1 == ('Sword') or weapon1 == ('sword') :
    print('The old woman turns to you as you walk down the stairs, she says, "Ah, one for brute strength I see? Well, I sense that you will have a relativley easy journey, especially around the middle of your adventure, bot a good choice none the less.')
elif weapon1 == ('Bow') or weapon1 == ('bow') :
    print('You walk down the stairs as the old woman turns to you, she says "Oh, one for hiding in the bushes I see? Well, your journey shall start out quickly, but eventually become harder, but a good choice anyways.')
leaveCottage1 = input('Do you want to head out now? ')
if leaveCottage1 == ('Yes') or leaveCottage1 == ('yes') :
    print('You leave the cottage, that old woman was giving you the creeps, you finally head out, ready for your new adventure that the old woman was talking about, in the distance, you finally see civilization, it appears to be an old town,')
if leaveCottage1 == ('No') or leaveCottage1 == ('no') :
           print('You decide to stick around for a little bit, trying to discover more about the old woman, you and her talk for a long while, almost seeming to be days, when you finish talking, you decide to head out, but not after the old woman gives you a warning, "Do not go near the tall grass, it is where monsters can spri...')
           print('WRITERS NOTE: Sorry, I got my game notes mixed up again, that was the wrong game, now where is the damn...')
           print('Nope, not here...')
           print('Hmmmmmmm...')
           print('It has got to be around here somewherea...')
           print('.')
           print('..')
           print('...')
           print('AHA! There it is, sorry about that, here, what she really says is...')
           print('The old woman says to you, "Be wary of the enemies that lurk around every corner, you never know when you may encounter an opponent even you cannot handle." and she sends you on your way.')
           print('You finally head out, after the writer break down... but you see civilization ahead, it appears to be a run down town.')
direction1 = input('Do you want to head there? ')
if direction1 == ('Yes') or direction1 == ('yes') :
     print(' You head into the village, You see a sign that says welcome to Ol Village!')
     print("You look around, there is a Blacksmith's house, a wizard's caravan, a tavern, a hospital, and a huge castle directly to the left of the village.")
     olVillage1 = input('Where would you like to go? ')
if olVillage1 == ("Blacksmith's House") or olVillage1 == ('Blacksmith') or olVillage1 == ("Blacksmith's") or olVillage1 == ("blacksmith's") or olVillage1 == ('Blacksmith') or olVillage1 == ('blacksmith') or olVillage1 == ("blacksmith's house") or olVillage1 == ("Blacksmith's house") or olVillage1 == ("blacksmith's House") or olVillage1 == ('blacksmith house') or olVillage1 == ('Blacksmith House') :
     print("You walk into the blacksmith's house, a little bell rings above you, the blacksmith looks at you, his beard in full bloom.")
     blacksmithOl = input('What do you want to do? ')
if blacksmithOl == ('Buy') or blacksmithOl == ('buy') and  money <= 0 :
      print('''He looks you up and down, "Ye have no money t' buy with, come back when ye has something worth giving my time fer' ''')
elif blacksmithOl == ('Buy') or blacksmithOl == ('buy') and money <= 1 :
    print('''He looks you up and down, "Ah, y' has the coin, what do ye want?''')
    blacksmithOlShop = input('He has swords, bows, and armor, what do you want? ')
