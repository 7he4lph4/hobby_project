		if dice == 1:
			desc = f'but you realize you\'re walking in circles and that you\'re just lost.'
		elif dice == 2:
			desc = f'and come across a humanoid skeleton.'
		elif dice == 3:
			desc = f'and see something written in dwarvish on the walls: ||\'You are being watched\'||'
		elif dice == 4:
			desc = f'and find a small node of coal worth **{roll("1d24mi6")}sp** Make a **DC8 STR check** to break it out and add the silver directly to your pouch.'
		elif dice == 5:
			desc = f'but you get to a dead end and trace your steps back'
		elif dice == 6:
			desc = f'and come across a bunch of rocks and boulders. They seem worthless.'
		elif dice == 7:
			desc = f'and you find some brown fungi. Make a **DC14 Nature check** {roll("1d8mi3")}gp. Add the gold directly to your pouch'
		elif dice == 8:
			desc = f'and you find some yellow small fungi. You easily collect them, they are worth **{roll("1d36mi18")}sp**. Add the silver directly to your pouch'
		elif dice == 9:
			desc = f'but you come across some rats running away from something, you get an unnerving feeling creeping upon you.'
		elif dice == 10:
			desc = f'and you find a wooden door. It is locked. Make a **DC14 Thieves\' Tools check** if you have one with `!tool thi dex`. Or maybe even break it open? **Make a DC18 STR check**. If you get past, you get deeper into this cave system.'
		elif dice == 11:
			desc = f'and you come across a small iron node worth **{roll("1d12mi8")}gp**. Make a **DC8 STR check** to add the gold directly to your pouch'
		elif dice == 12:
			desc = f'and find some skulls tied to a rope hanging from the ceiling. If you succeed on a **DC15 Investigation check**. You can identify that most are humanoid besides 2 others that are from beasts. You are unsure if you wanna continue your journey deeper.'
		elif dice == 13:
			desc = f'but you come across two giant bats sleeping from the ceiling. Make a **DC10 Stealth check** to pass unnoticed!'
		elif dice == 14:
			desc = f'and you come across a mediocre sized node of coal worth **{roll("1d96mi32")}sp**. Make a **DC10 STR check** to add the silver direcly to your pouch'
		elif dice == 15:
			desc = f'and you come across a larger part of this cavern and the ground is mostly covered in white fungi. As you step into the cavern, make a **DC13 Stealth Check**, on failure the fungi start screaming and force you to go different way.'
		elif dice == 16:
			desc = f'and you come across a burning camp-fire that seems deserted. You feel the unnerving sensation of being watched!'
		elif dice == 17:
			desc = f'and you come across some vines leading upwards deeper into this cave system. Make a **DC10 Athletics Check** to climb up.'
		elif dice == 18:
			desc = f'and find a treasure chest. Add **{roll("1d20mi7")}gp** to your pouch'
		elif dice == 19:
			desc = f'but you come across a wooden barricade that blocks the way further into the cave. (It has **AC 14** and **30HP**, destroy it down however you like).'
		elif dice == 20:
			desc = f'and you find some geodes worth **{roll("1d20mi10")}sp**. Add the silver directly to your pouch' 
		elif dice == 21:
			desc = f'but you fall down a small 10ft deep pit. Make **DC10 Acrobatics check** to avoid it.' 
		elif dice == 22:
			desc = f'and you find an abandoned mine-cart rail running deeper into the caves.'
		elif dice == 23:
			desc = f'and you find some bloody daggers laying around.'
		elif dice == 24:
			desc = f'and you find some loot scattered around including a Potion of Healing and a pouch with **15gp** in it. You also see a note saying: \'Take whatever you need, and maybe leave something behind for those following\'.'
		elif dice == 25:
			desc = f'when you faintly make out the whispers and murmuring of a ritual being cast.'
		elif dice == 26:
			desc = f'but some rocks fall from above. Make a DC10 **DEX SAVE** or type `!hp -d4 [Bludgeoning]`'
		elif dice == 27:
			desc = f'but you only find a water source running deeper into the cave.'
		elif dice == 28:
			desc = f'and you find a rope leading a steep way down, far deeper into the cave.'
		elif dice == 29:
			desc = f'and you discover a mediocre node of coal on the wall worth **{roll("1d96mi32")}sp**. Make a **DC10 STR check** to add the silver directly to your pouch.'
		elif dice == 30:
			desc = f'but you come to a hollow cave with some empty sheets of paper on the ground.'
		elif dice == 31:
			desc = f'and you find a perfectly symmetrical room, odd.'
		elif dice == 32:
			desc = f'but you suddenly get envoloped in sheer darkness as you watch your most dreaded nightmare come lumbering out of the shadows, towards you. Make a **DC16 WIS Saving throw**, on success, you realize it was an illusion to ward off explorers'
		elif dice == 33:
			desc = f'and you find a statue resembling a fiend. On a successful **DC14 Religion Check**, you remember that you can offer an skull in exchange for **15gp**'
		elif dice == 34:
			desc = f'but you\'ve accidentally walked into a Stirge\'s nest. **Make a DC13 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 35:
			desc = f'but a **crawling claw** tries to reach out and grab your foot, as you turn around you see 5 more...' 
		elif dice == 36:
			desc = f'and you find a small node of gold!. Make a **DC8 STR check** to add **{roll("1d25mi10")}gp** directly to your pouch.'
		elif dice == 37:
			desc = f'and you come across a large room with a high ceiling and you can see some torches lit along the wall.'
		elif dice == 38:
			desc = f'and you find a dead end Make **DC 14 Arcana Check** to discover that it is just an illusion and behind it the cave network continues.' 
		elif dice == 39:
			desc = f'but you enter an room with gruesome bones with rotting flesh laying around, you have a really bad feeling that something terrible has happened here.'
		elif dice == 40:
			desc = f'but you find three rotting corpses with their hands ripped off.'
		elif dice == 41:
			desc = f'and you come across a mediocre iron node on the floor worth **{roll("1d26mi14")}gp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 42:
			desc = f'and you find a sentient fishing rod that talks to you in a funny voice.'
		elif dice == 43:
			desc = f'and you find four chairs and a table with a book on it, titled \'How to Have Fun in a Cave\' and two bottles of fine mead.'
		elif dice == 44:
			desc = f'but as you go deeper two giant centipedes crawl out of a hole in the side of the cave! {disengage}'
		elif dice == 45:
			desc = f'but you enter a room full of thick purplish gas. Make a **DC 15 CON Saving throw** or become poisoned and roll all ability checks at disadvantage for 30 minutes.'
		elif dice == 46:
			desc = f'and you find a gemstone with an magical aura in the wall worth **{roll("1d50mi30")}gp**. Make a **DC15 STR check** to add the gold directly to your pouch.'
		elif dice == 47:
			desc = f'and you enter a strange room where the floor is made out of glass letting you see all that\'s going on inside the tavern!'
		elif dice == 48:
			desc = f'and you find a small node of coal worth **{roll("1d24mi6")}sp** Make a **DC 8 Strength Check** to retreive it and add the silver directly to your pouch.'
		elif dice == 49:
			desc = f'and you see a cultist going further into one of the three ways. You also find some lavender scented candles on the floor.'
		elif dice == 50:
			desc = f'but you come across a Spectator that telepathically tells you: \'Leave this part of the Cavern and let me rest!\' **Make a DC15 Perception Check** to notice a crate with 3 Potions of Healing behind the Spectator.'
		elif dice == 51:
			desc = f'and somebody tells you through telepathy: \'Tread carefully\''
		elif dice == 52:
			desc = f'but you fall into a pit with a glowing aura and mysteriously wake up in the tavern!' 
		elif dice == 53:
			desc = f'and you find an amethyst stuck in the floor! **Make a DC 12 Strength Check** to retrieve it, on success add **45gp** directly to your pouch!'
		elif dice == 54:
			desc = f'and you come across a perfectly refreshing fountain. If you drink from it, the water stops flowing and type: `!hp + 2d4+2`.'
		elif dice == 55:
			desc = f'and you discover a small node of iron worth **{roll("1d12mi8")}gp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 56:
			desc = f'and you discover a large node of coal worth **{roll("1d2mi10")}gp**. Make a **DC12 STR check** to Add the gold directly to your pouch.'
		elif dice == 57:
			desc = f'and you discover a mediocre node of iron worth **{roll("1d26mi14")}gp**! **Make a DC10 Strength Check** to add the gold directly to your pouch..'
		elif dice == 58:
			desc = f'and you find a coupon wedged between some rocks for a free drink and meal from Denzel! You can skip paying for two orders with this!'
		elif dice == 59:
			desc = f'but you find an empty room with two exits, you notice a gelatinous cube right in the center of the room!'
		elif dice == 60:
			desc = f'and in surprise, you find a massive node of gold worth **{roll("1d140mi100")}gp**. Make a **DC12 STR check with Advantage** to add the gold directly to your pouch.'
		elif dice == 61:
			desc = 	f'and you find a statue resembling you. The statue animates after a minute and roams around the world for one day, spreading lies and rumours about you, it has **3 HP** and you can kill it to prevent it leaving the caves. (If you choose to RP it, use the tupperbot NPC to RP the statue: `tul!help` for more info!'
		elif dice == 62:
			desc = 	f'but you come across some chains tied to the wall, that seem broken. You get an anxious-inducing feeling.'
		elif dice == 63:
			desc = 	f'and you come across some barrels with some old rations aswell as unlit torches.'
		elif dice == 64:
			desc = 	f'but you come across an exact copy of the <#745568550676070420>?'
		elif dice == 65:
			desc = 	f'and you find a small node of copper worth **{roll("1d34mi12")}sp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 66:
			desc = 	f'and you find a mediocre node of copper worth **{roll("1d8mi3")}gp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 67:
			desc = 	f'and you come across a room with a magical pickaxe, that you can use 5 times to skip an strength check until it breaks.'
		elif dice == 68:
			desc = 	f'but you come across an room dimly lit with an table in the centre and you see 3 goblins and a hobgoblin drinking. Make a **DC8 Stealth check** to pass unnoticed!'
		elif dice == 69:
			desc = 	f'but you come across some deep footprints that seem to belong to a dragon! There might be one in here!'
		elif dice == 70:
			desc = 	f'and you come across a black dragon\'s scale worth **{roll("1d20mi12")}gp** aswell as some footprints of a dragon. You are getting a bad feeling about this.'
		elif dice == 71:
			desc = 	f'but you find a room with some burnt down bookshelves as well as some charred skeletons. You are unsure if you want to continue your journey onwards.'
		elif dice == 72:
			desc = 	f'and you venture deeper into this abyss only to realise a living **`!monster Shadow`** has been following you! {disengage}'
		elif dice == 73:
			desc = 	f'despite going forward and exploring, you seem to find yourself in the same location you left from!'
		elif dice == 74:
			desc = 	f'but you come across three `!monster Kenku` talking about how they robbed someone in Wittiga. You can notice they got a coin pouch with 30gp. **Make a DC14 Stealth Check** to pass unnoticed {disengage}'
		elif dice == 75:
			desc = 	f'but you find a steep slide deeper into the cave. If you try to slide, make a DC12 **DEX SAVE** to not get hurt or type `!hp -d4 [Bludgeoning]`'
		elif dice == 76:
			desc = 	f'but you come across a batch of `!monster violet fungus`. After closer inspection they seem to be alive! {disengage}'
		elif dice == 77:
			desc = 	f'but you walk into a tight hallway. You might need to squeeze to get through!'
		elif dice == 78:
			desc = 	f'and you find a small node of copper worth **{roll("1d34mi12")}sp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 79:
			desc = 	f'and you find an empty room. Make a **DC15 Perception Check** to discover a hidden stash containing **{roll("1d30mi8")}gp**, add the gold directly to your pouch.'
		elif dice == 80:
			desc = 	f'but you see a bugbear talking to a goblin. Make a **DC12 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 81:
			desc = 	f'and you come across a **`!monster Cavelight Moss`**! {disengage}'
		elif dice == 82:
			desc = 	f'and you come across two **`!monster Bugbear`** talking with a table and a pouch of gold containing **{roll("1d22mi12")}gp**! {disengage}'
		elif dice == 83:
			desc = 	f'and you come across a mediocre node of copper worth **{roll("1d8mi3")}gp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 84:
			desc = 	f'and you surprisingly find a massive node of copper worth **{roll("1d24mi12")}gp**. Make a **DC12 STR check** to add the gold directly to your pouch.' 
		elif dice == 85:
			desc = 	f'but you come across four **`!monster Hobgoblin`** with a crate of swords worth **{roll("1d50mi30")}gp**! Make a **DC15 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 86:
			desc = 	f'and you come across a mediocre node of iron worth **{roll("1d26mi14")}gp**! But it is getting mined by two **`!monster Goblin`** and a **`!monster Bugbear`** watching over them. Make a **DC13 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 87:
			desc = 	f'but you come across two **`!monster Ghoul`** feasting on some dead cultists, which have **{roll("1d200mi70")}sp** in their pouches. Make a **DC14 Stealth Check** to pass unnoticed. {disengage}'
		elif dice == 88:
			desc = 	f'and you find a small node of silver worth **{roll("1d45mi20")}sp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 89:
			desc = 	f'and you find a mediocre node of silver worth **{roll("1d12mi5")}gp**. Make a **DC10 STR check** to add the gold directly to your pouch.'
		elif dice == 90:
			desc = 	f'and you find a small node of silver worth **{roll("1d45mi20")}sp**. Make a **DC8 STR check** to add the gold directly to your pouch.'
		elif dice == 91:
			desc = 	f'but you come across a beautiful part of the cavern with lots of different fungi and moss covering the walls in different colours.'
		elif dice == 92:
			desc = 	f'and you find a underground lake. The waters look uninviting.'
		elif dice == 93:
			desc = 	f'and you come across a statue resembling a deity. Make a **DC12 Religion check** to find out that you get **20gp** if you offer a piece of coal.'
		elif dice == 94:
			desc = 	f'but you trigger a spiked net trap above you! Make a DC13 **DEX SAVE** to not get hurt or type `!hp -d4 [Piercing]`'
		elif dice == 95:
			desc = 	f'but you come across a longer cave hall. As you step further into it.. A giant boulder falls behind you and rolls towards you! Make a **DC14 Athletics Check** to not get hurt or type `!hp -5 [bludgeoning]`'
		elif dice == 96:
			desc = 	f'and make a **DC12 Perception Check** to find a silver ring on the floor worth **{roll("1d25mi8")}gp**.'
		elif dice == 97:
			desc = 	f'but you come across three **`!monster Gray Ooze`** that are digesting a some corpses. You also notice two unharmed potions. Make a **DC12 Arcana Check** to find out that these are Potions of Heroism. {disengage}' 
		elif dice == 98:
			desc = 	f'and you find a crate of alchemist supplies. Maybe you can sell it?'
		elif dice == 99:
			desc = 	f'and you come across a heavy armored door. You also notice it is magically locked aswell. Make a **DC32 STR check** to burst it open or make a **DC24 Thieves\' Tools check** if you have one with `!tool thi dex`. You can dispel the magic lock with a fitting spell and reduce the Difficulty of those Checks by 8.'
