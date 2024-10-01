'''
Mintas Ivaska
Period 11 HCP
Program: Risk Game
Description: To replicate the risk game as much as possible that is on Nintendo Switch.
'''

#---------------------------References----------------------------#
# 1. Start Menu Background: https://maliks.bloooom.com/AlbumResources/1/Images/XLarge/6242863478679.jpg
#
# 2. Directions Background: https://cdn.akamai.steamstatic.com/steam/apps/1128810/header.jpg?t = 1609068923
#
# 3. Arrow Icon: https://www.subpng.com/png-i001cv/
#
# 4. Game Directions Taken and Modified From: https://www.hasbro.com/common/instruct/risk.pdf
#
# 5. Ted Klein Bergman for the blit_text() function
#
# 6. Game-in-Play Background Screen: https://wallpaper.dog/large/10810455.jpg
#
# 7. Tank Icon: https://www.google.com/url?sa = i&url = https%3A%2F%2Ficonscout.com%2Ficon%2Ftank-161&psig = AOvVaw287-ePT7wVQZg_s_7wKa8t&ust = 1621967123666000&source = images&cd = vfe&ved = 0CAIQjRxqFwoTCPD6rsz44vACFQAAAAAdAAAAABAD
#
# 8. Star Icon: https://www.google.com/url?sa = i&url = https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AStar_icon_stylized.svg&psig = AOvVaw3G1m2UOatpP0vPOZGz_oMN&ust = 1621967182576000&source = images&cd = vfe&ved = 0CAIQjRxqFwoTCKi55t_44vACFQAAAAAdAAAAABAD
#
# 9. Menu Background From: https://www.google.com/url?sa = i&url = https%3A%2F%2Ffutureoflife.org%2Fbackground%2Fbenefits-risks-of-artificial-intelligence%2F&psig = AOvVaw1UFjROl4C9gtQkqgKV9RTX&ust = 1621967569638000&source = images&cd = vfe&ved = 0CAIQjRxqFwoTCOjcspr64vACFQAAAAAdAAAAABAD
#
# 10. Player Setup Background: https://www.google.com/url?sa = i&url = https%3A%2F%2Fwww.dataversity.net%2Funderstanding-the-uses-of-artificial-intelligence%2F&psig = AOvVaw1VSynGTF_A_jImiH1KSaLL&ust = 1621967883109000&source = images&cd = vfe&ved = 0CAIQjRxqFwoTCODJ8rf74vACFQAAAAAdAAAAABAc
#
# 11. Background Music From: https://www.fesliyanstudios.com/royalty-free-music/downloads-c/suspenseful-music/25






#imports important modules
import pygame, sys, random, os

#initalizes pygame
pygame.init()

SF = 1

#sets the variables needed for pygame
w = int(600*SF)
h = int(480*SF)
size = (w, h)
surface  =  pygame.display.set_mode(size)

#sets the caption as RISK
pygame.display.set_caption("RISK")

#colors
BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)
LT_GREEN = (180, 255, 124)
GREEN = (137,  219,  140)
RISK_RED =  (234,  66,  36)
BLUE =  (71,  193,  220)
LT_BLUE = (0, 179, 223)
GRAY = (200, 200, 200)
ORANGE = (229, 131, 34)
YELLOW = (217,  221,  35)
BROWN = (156,  120,  5)
PURPLE = (163,  26,  166)
RED = (255, 0, 0)
DK_GREEN = (54,  133,  0)

#clock
clock = pygame.time.Clock()

#-----------country images variables neeeded----------------
STR_COLORS_LIST = ['_green', '_yellow', '_blue', '_brown', '_purple', '_red']   #cotains the colors that the users are playing as  
COLORS_LIST = [GREEN, YELLOW, BLUE, BROWN, PURPLE, RED]    #contains the actual color information for the colors

#contains all of the information needed to blit the country to the screen
COUNTRY_INFO_DICT = {'alaska':[.02*w, .105*h, .35*196, .35*200, random.choice(STR_COLORS_LIST), 0], 
                 'alberta':[.1*w, .175*h, .325*183, .325*149, random.choice(STR_COLORS_LIST), 1], 
                 'argentina':[.23*w, .67*h, .326*173, .326*362, random.choice(STR_COLORS_LIST), 0], 
                 'brazil':[.215*w, .545*h, .33*340, .33*326, random.choice(STR_COLORS_LIST), 0], 
                 'centralAfrica':[.4789*w, .647*h, .355*199, .355*195, random.choice(STR_COLORS_LIST), 0], 
                 'centralAmerica':[.12*w, .375*h, .33*173, .33*224, random.choice(STR_COLORS_LIST), 0], 
                 'cluster':[.37*w, .24*h, .332*148, .332*178, random.choice(STR_COLORS_LIST), 0], 
                 'eastAfrica':[.537*w, .587*h, .335*216, .335*320, random.choice(STR_COLORS_LIST), 0], 
                 'easternAustralia':[.88*w, .725*h, .335*191, .335*294, random.choice(STR_COLORS_LIST), 0], 
                 'easternCanada':[.25*w, .17*h, .335*168, .335*199, random.choice(STR_COLORS_LIST), 0], 
                 'easternUS':[.17*w, .26*h, .35*243, .35*230, random.choice(STR_COLORS_LIST), 0], 
                 'egypt':[.494*w, .52*h, .35*196, .35*123, random.choice(STR_COLORS_LIST), 0], 
                 'greenland':[.27*w, .035*h, .34*270, .34*270, random.choice(STR_COLORS_LIST), 0], 
                 'iceland':[.395*w, .18*h, .345*118, .345*84, random.choice(STR_COLORS_LIST), 0], 
                 'indonesia':[.755*w, .6375*h, .348*210, .348*177, random.choice(STR_COLORS_LIST), 0], 
                 'madagascar':[.61*w, .775*h, .349*99, .349*164, random.choice(STR_COLORS_LIST), 0], 
                 'newGuinnea':[.86*w, .63*h, .35*159, .35*121, random.choice(STR_COLORS_LIST), 0], 
                 'northAfrica':[.395*w, .485*h, .35*288, .35*311, random.choice(STR_COLORS_LIST), 0], 
                 'northernEurope':[.449*w, .25*h, .35*180, .35*183, random.choice(STR_COLORS_LIST), 0], 
                 'northwestTerritory':[.097*w, .087*h, .32*331, .32*154, random.choice(STR_COLORS_LIST), 0], 
                 'ontario':[.19*w, .18*h, .35*149, .35*203, random.choice(STR_COLORS_LIST), 0], 
                 'peru':[.1925*w, .569*h, .35*229, .35*240, random.choice(STR_COLORS_LIST), 0], 
                 'russia':[.514*w, .125*h, .35*288, .35*439, random.choice(STR_COLORS_LIST), 0], 
                 'sandinavia':[.455*w, .125*h, .35*182, .35*214, random.choice(STR_COLORS_LIST), 0], 
                 'southAfrica':[.4835*w, .73*h, .35*219, .35*267, random.choice(STR_COLORS_LIST), 0], 
                 'southernEurope':[.46*w, .35*h, .34*182, .34*201, random.choice(STR_COLORS_LIST), 0], 
                 'venezuela':[.19*w, .5*h, .355*245, .355*136, random.choice(STR_COLORS_LIST), 0], 
                 'westernAustralia':[.81*w, .74*h, .35*218, .35*253, random.choice(STR_COLORS_LIST), 0], 
                 'westernEurope':[.39*w, .35*h, .34*158, .34*223, random.choice(STR_COLORS_LIST), 0], 
                 'westernUS':[.11*w, .27*h, .34*186, .34*185, random.choice(STR_COLORS_LIST), 0], 
                 'afganistan':[.605*w, .28*h, .35*218, .35*227, random.choice(STR_COLORS_LIST), 0], 
                 'china':[.7*w, .3*h, .35*320, .35*297, random.choice(STR_COLORS_LIST), 0], 
                 'india':[.66*w, .395*h, .35*232, .35*334, random.choice(STR_COLORS_LIST), 0], 
                 'japan':[.89*w, .26*h, .35*112, .35*229, random.choice(STR_COLORS_LIST), 0], 
                 'kamataka':[.8035*w, .086*h, .358*282, .358*337, random.choice(STR_COLORS_LIST), 0], 
                 'middleEast':[.51*w, .4235*h, .35*308, .35*298, random.choice(STR_COLORS_LIST), 0], 
                 'mongolia':[.74*w, .255*h, .35*237, .35*190, random.choice(STR_COLORS_LIST), 0], 
                 'siberia':[.66*w, .05*h, .35*246, .35*417, random.choice(STR_COLORS_LIST), 0], 
                 'sk':[.73*w, .18*h, .36*221, .36*183, random.choice(STR_COLORS_LIST), 0], 
                 'southeastAsia':[.77*w, .467*h, .35*152, .35*207, random.choice(STR_COLORS_LIST), 0], 
                 'ural':[.645*w, .085*h, .35*177, .35*365, random.choice(STR_COLORS_LIST), 0], 
                 'yatusk':[.76*w, .07*h, .36*191, .36*189, random.choice(STR_COLORS_LIST), 0]}  

COUNTRY_INFO_KEYS_LIST = list(COUNTRY_INFO_DICT.keys())
COUNTRY_RECT_LIST = []

#background rect object
BACKGROUND_RECT = pygame.Rect(0, 0, w, h)

#start menu images
START_IMAGE = pygame.image.load('risk_menu.jpg').convert_alpha()
START_IMAGE = pygame.transform.scale(START_IMAGE, (BACKGROUND_RECT.width, BACKGROUND_RECT.height))

#country rect list
for i in range(len(COUNTRY_INFO_KEYS_LIST)):
    currentCountryInfoList = COUNTRY_INFO_DICT[COUNTRY_INFO_KEYS_LIST[i]]
    currentCountryRect = pygame.Rect(currentCountryInfoList[0], currentCountryInfoList[1], currentCountryInfoList[2], currentCountryInfoList[3])
    
    COUNTRY_RECT_LIST.append(currentCountryRect)
    
#directions menu images
DIRECTIONS_IMAGE = pygame.image.load('directions_background.jpg').convert_alpha()
DIRECTIONS_IMAGE = pygame.transform.scale(DIRECTIONS_IMAGE, (BACKGROUND_RECT.width, BACKGROUND_RECT.height))

#menu screen images
MENU_IMAGE = pygame.image.load('menu_background.jpg').convert_alpha()
MENU_IMAGE = pygame.transform.scale(MENU_IMAGE, (BACKGROUND_RECT.width, BACKGROUND_RECT.height))

#menu more information dictionary
MENU_OPTIONS_DICT = {'On':'Ceasefire Card On: The game will end when one player has conquered 30 territories.', 'Off':'Ceasefire Card Off: The Ceasefire Card is not active.', 'World Domination':'World Domination: Your mission is to conquer every territory to win.', 'Random':'Random: The computer will randomly choose players locations.',  'EXTRA':['Capitals: Your mission is to capture all of the opponents capitals to win.', 'Secret Mission: Each player will be given a secret mission to complete. The first player to complete their secret mission wins.']}

#gameInPlay screen images
PLAYERS_SCREEN_IMAGE = pygame.image.load('playersScreen_background.jpg').convert_alpha()
PLAYERS_SCREEN_IMAGE = pygame.transform.scale(PLAYERS_SCREEN_IMAGE, (BACKGROUND_RECT.width, BACKGROUND_RECT.height))
TANK_ICON = pygame.image.load('tank_icon.png').convert_alpha()
TANK_RECT = pygame.Rect(.815*w, .05*h, .1*w, .1*w)
TANK_RECT.center = (.815*w, .05*h)
TANK_ICON = pygame.transform.scale(TANK_ICON, (TANK_RECT.width, TANK_RECT.height))
STAR_ICON = pygame.image.load('star_icon.png').convert_alpha()
STAR_RECT = pygame.Rect(.925*w, .05*h, .0375*w, .0375*w)
STAR_RECT.center = (.925*w, .05*h)
STAR_ICON = pygame.transform.scale(STAR_ICON, (STAR_RECT.width, STAR_RECT.height))
GAME_IN_PLAY_BACKGROUND = pygame.image.load('dark_background.jpg').convert_alpha()
GAME_IN_PLAY_BACKGROUND = pygame.transform.scale(GAME_IN_PLAY_BACKGROUND,  (BACKGROUND_RECT.width,  BACKGROUND_RECT.height))

#string color converter dict
STR_COLOR_TO_COLOR_DICT = {'_green':GREEN, '_yellow':YELLOW, '_blue':BLUE, '_brown':BROWN, '_purple':PURPLE, '_red':RISK_RED}

#contains the names of the countries that are located in a certain continent
ASIA_COUNTRIES = ['middleEast', 'india', 'southeastAsia', 'china', 'afganistan', 'ural', 'siberia', 'yatusk', 'kamataka', 'sk', 'mongolia', 'japan']
EUROPE_COUNTRIES = ['iceland', 'cluster', 'westernEurope', 'southernEurope', 'northernEurope', 'russia', 'sandinavia']
NORTH_AMERICA_COUNTRIES = ['alaska', 'northwestTerritory',  'alberta', 'ontario', 'easternCanada', 'greenland', 'westernUS', 'easternUS', 'centralAmerica']
AFRICA_COUNTRIES = ['northAfrica', 'egypt', 'eastAfrica', 'centralAfrica', 'southAfrica', 'madagascar']
SOUTH_AMERICA_COUNTRIES = ['venezuela', 'brazil', 'peru', 'argentina']
AUSTRALIA_COUNTRIES = ['indonesia', 'newGuinnea', 'westernAustralia', 'easternAustralia']

#contains the bonus points that each contient has in this dict
CONTINENT_BONUS_POINT_DICT = {'australia':2, 'southAmerica':2,  'africa':3, 'northAmerica':5,  'europe':5,  'asia':7}

#card screen images
CHECK_MARK_IMAGE = pygame.image.load('check_mark.png').convert_alpha()
CHECK_MARK_IMAGE = pygame.transform.scale(CHECK_MARK_IMAGE, (int(.05*w), int(.05*h)))
CARDS_STAR_IMAGE = pygame.image.load('cards_star_image.png').convert_alpha()
CARDS_STAR_IMAGE = pygame.transform.scale(CARDS_STAR_IMAGE, (int(.1*w), int(.1*h)))

#directions screen images
PLAYER_HANDOVER_IMAGE = pygame.image.load('directions_images/playerHandoverScreen.PNG').convert_alpha()
DIRECTIONS_IMAGES_RECT = pygame.Rect(.09*w, .09*h, .75*w, .45*h)
PLAYER_HANDOVER_IMAGE = pygame.transform.scale(PLAYER_HANDOVER_IMAGE,  (DIRECTIONS_IMAGES_RECT.width, DIRECTIONS_IMAGES_RECT.height))
TRADE_CARDS_POPUP_IMAGE = pygame.image.load('directions_images/tradeTroopsPopup.PNG').convert_alpha()
TRADE_CARDS_POPUP_IMAGE = pygame.transform.scale(TRADE_CARDS_POPUP_IMAGE, (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
TRADE_CARDS_SCREEN_IMAGE = pygame.image.load('directions_images/tradeScreen.PNG').convert_alpha()
TRADE_CARDS_SCREEN_IMAGE = pygame.transform.scale(TRADE_CARDS_SCREEN_IMAGE, (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
DRAFT_POPUP_IMAGE = pygame.image.load('directions_images/draftPopup.PNG').convert_alpha()
DRAFT_POPUP_IMAGE = pygame.transform.scale(DRAFT_POPUP_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
ATTACK_PHASE_IMAGE = pygame.image.load('directions_images/attackPhase.PNG').convert_alpha()
ATTACK_PHASE_IMAGE = pygame.transform.scale(ATTACK_PHASE_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
ATTACK_PHASE_TRANSFER_TROOPS_IMAGE = pygame.image.load('directions_images/attackPhaseTransferTroops.PNG').convert_alpha()
ATTACK_PHASE_TRANSFER_TROOPS_IMAGE = pygame.transform.scale(ATTACK_PHASE_TRANSFER_TROOPS_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
END_ATTACK_PHASE_IMAGE = pygame.image.load('directions_images/endAttackPhase.PNG').convert_alpha()
END_ATTACK_PHASE_IMAGE = pygame.transform.scale(END_ATTACK_PHASE_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
END_FORTIFY_PHASE_IMAGE = pygame.image.load('directions_images/endFortifyPhase.PNG').convert_alpha()
END_FORTIFY_PHASE_IMAGE = pygame.transform.scale(END_FORTIFY_PHASE_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
FORTIFY_PHASE_IMAGE = pygame.image.load('directions_images/fortifyPhase.PNG').convert_alpha()
FORTIFY_PHASE_IMAGE = pygame.transform.scale(FORTIFY_PHASE_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
FORTIFY_POPUP_IMAGE = pygame.image.load('directions_images/fortifyPopup.PNG').convert_alpha()
FORTIFY_POPUP_IMAGE = pygame.transform.scale(FORTIFY_POPUP_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
DRAFT_SCREEN_IMAGE = pygame.image.load('directions_images/draftPhase.PNG').convert_alpha()
DRAFT_SCREEN_IMAGE = pygame.transform.scale(DRAFT_SCREEN_IMAGE, (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
ATTACK_POPUP_IMAGE = pygame.image.load('directions_images/attackPopup.PNG').convert_alpha()
ATTACK_POPUP_IMAGE = pygame.transform.scale(ATTACK_POPUP_IMAGE,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))
NOTE_IMAGES = pygame.image.load('directions_images/note.PNG').convert_alpha()
NOTE_IMAGES = pygame.transform.scale(NOTE_IMAGES,  (DIRECTIONS_IMAGES_RECT.width,  DIRECTIONS_IMAGES_RECT.height))

#sounds
EPIC_HERO_BACKGROUND_SOUND=pygame.mixer.music.load('sounds/imminent_threat.mp3')

#dict that contains the countries that the certain country is connected to
CONNECTED_COUNTRIES_DICT = {'alaska':('kamataka',  'northwestTerritory', 'alberta'), 
                          'northwestTerritory':('alaska', 'alberta', 'ontario', 'greenland'), 
                          'greenland':('northwestTerritory', 'ontario', 'easternCanada', 'iceland'), 
                          'alberta':('alaska', 'northwestTerritory', 'ontario','westernUS'), 
                          'ontario':('greenland', 'northwestTerritory', 'alberta', 'easternCanada', 'westernUS', 'easternUS'), 
                          'easternCanada':('greenland',  'ontario',  'easternUS'), 
                          'westernUS':('alberta',  'ontario', 'easternUS', 'centralAmerica'), 
                          'easternUS':('westernUS', 'ontario', 'easternCanada', 'centralAmerica'), 
                          'centralAmerica':('westernUS', 'easternUS', 'venezuela'), 
                          'venezuela':('peru', 'brazil','centralAmerica'), 
                          'peru':('brazil', 'venezuela', 'argentina'), 
                          'argentina':('peru', 'brazil'), 
                          'brazil':('venezuela', 'peru', 'argentina', 'northAfrica'), 
                          'northAfrica':('egypt', 'brazil', 'centralAfrica', 'eastAfrica'), 
                          'egypt':('northAfrica', 'southernEurope', 'middleEast', 'eastAfrica'), 
                          'centralAfrica':('northAfrica', 'eastAfrica', 'southAfrica'), 
                          'southAfrica':('centralAfrica', 'eastAfrica', 'madagascar'), 
                          'madagascar':('southAfrica', 'eastAfrica'), 
                          'eastAfrica':('egypt', 'northAfrica', 'centralAfrica', 'southAfrica', 'madagascar', 'middleEast'), 
                          'westernAustralia':('easternAustralia', 'indonesia'), 
                          'easternAustralia':('westernAustralia',  'newGuinnea'), 
                          'newGuinnea':('easternAustralia', 'indonesia'), 
                          'indonesia':('newGuinnea', 'westernAustralia', 'southeastAsia'), 
                          'iceland':('cluster', 'greenland', 'sandinavia'), 
                          'cluster':('iceland', 'westernEurope'), 
                          'westernEurope':('cluster', 'northernEurope', 'southernEurope', 'northAfrica'), 
                          'southernEurope':('northernEurope', 'westernEurope', 'russia', 'middleEast', 'egypt', 'northAfrica'), 
                          'northernEurope':('southernEurope', 'westernEurope', 'russia', 'sandinavia'), 
                          'russia':('southernEurope', 'northernEurope', 'sandinavia', 'middleEast', 'afganistan', 'ural'), 
                          'middleEast':('eastAfrica', 'egypt', 'southernEurope', 'europe', 'afganistan', 'india'), 
                          'india':('middleEast', 'afganistan', 'china', 'southeastAsia'), 
                          'southeastAsia':('india', 'indonesia', 'china'), 
                          'afganistan':('middleEast', 'india', 'china', 'ural', 'russia'), 
                          'china':('southeastAsia', 'india', 'mongolia', 'siberia', 'ural', 'afganistan'), 
                          'ural':('afganistan', 'russia', 'siberia', 'china'), 
                          'siberia':('ural', 'china', 'mongolia', 'sk', 'yatusk'), 
                          'mongolia':('sk', 'siberia', 'china', 'japan'), 
                          'japan':('mongolia', 'sk'), 
                          'sk':('kamataka', 'yatusk', 'siberia', 'mongolia'), 
                          'yatusk':('siberia', 'sk', 'kamataka'), 
                          'kamataka':('japan', 'mongolia', 'sk', 'yatusk', 'alaska'), 
                          'sandinavia':('russia', 'northernEurope', 'iceland')}

#main function
def main():
    mouseOverCountry = ''     #contains the name of the country that the mouse is touching
    gameOver = False      #tells if the game is over or not
    startScreen = True      #tells if the game should be displaying the start screen or not
    startScreenStartRect = getTextRect('START',  25,  .86*w,  .7*h,  BLACK)     #contains the rect object for where the start button is
    directionsRect = getTextRect('DIRECTIONS',  25,  .86*w,  .8*h,  BLACK)     #contains the rect object for where the directions rect is
    directionsScreen = False      #tells if the game should be displaying the directions screen or not
    exit = False          #tells if the program should quit
    exitRect = getTextRect('EXIT',  25,  .86*w,  .9*h, BLACK)     #contains the rect object for where the exit button is
    startScreenStartRect = getTextRect('START',  25,  .86*w,  .7*h,  BLACK)   #contains the rect object for the start button that is on the start screen
    directionsScreenBackColors = [RED, WHITE]     #contains the text and background colors for the back text on the directions screen
    startScreenStartColors = [RED, WHITE]   #contains the text and background colors for the start text that is on the start screen
    exitColors = [RED, WHITE]    #contains the text and background colors for the exit text
    directionsColors = [RED, WHITE]      #contains the text and background colors for the directions text
    directionsScreenStartColors = [RED, WHITE]    #contains the text and background colors for the start button on the directions screen
    directionsScreenStartRect = getTextRect('START',  25,  .9*w,  .9*h,  BLACK)     #contains the rect object for the start rect that is in the directions screen
    directionsScreenMenuColors = [RED, WHITE]      #contains the text and background colors for the menu button on the directions screen
    directionsScreenMenuRect = getTextRect('MENU',  25,  .5*w,  .9*h,  BLACK)     #contains the rect object for the menu button on the directions screen
    directionsScreenBackRect = getTextRect('BACK',  25,  .1*w,  .9*h,  BLACK)     #contains the rect object for the back button that is on the directions screen
    menuScreen = False    #tells if the program should be displaying the menu screen
    currentGameType = 'World Domination'      #contains the name of the current game type
    numOfPlayers = 2  #contains the number of players
    territoryAlocationsOption = 'Random'  #contains the str of what the territory allocation option is
    ceasefireCardOption = 'on'.title()    #oontains the str of whether the ceasefire card is on or off
    gameTypeRtArrowRect = getTextRect(' '*5+'>'+' '*5,  20,  .8*w,  .265*h,  BLACK,  LT_BLUE)  #contains the rect for the right arrow that is next to the game type text
    gameTypeLftArrowRect = getTextRect(' '*5+'<'+' '*5,  20,  .2*w,  .265*h,  BLACK,  LT_BLUE) #contains the rect for the left arrow that is next to the game type text
    gameTypeRtArrowColorsList = [BLACK, LT_BLUE]    #contains the text and background colors for the right arrow that is next to the game type text
    gameTypeLftArrowColorsList = [BLACK, LT_BLUE]   #contains the text and background colors for the left arrow that is next to the the game type text
    startScreenStartColors = [WHITE, BLACK]    #contains the text and background colors for the start button that is located on the start screen
    territoryAlocationsRtArrowRect = getTextRect(' '*5+'>'+' '*5,  20,  .8*w,  (.265+.065*2)*h,  BLACK,  LT_BLUE)  #contains the rect object for the right arrow that is next to the terriory allocations text
    territoryAlocationsLftArrowRect = getTextRect(' '*5+'<'+' '*5,  20,  .2*w,  (.265+.065*2)*h,  BLACK,  LT_BLUE) #contains the rect object for the left arrow that is next to the territory allocations text
    territoryAlocationsLftArrrowColorsList = [BLACK, LT_BLUE]  #contains the text and background colors of the left arrow that is next to the territroy allocations text
    territoryAlocationsRtArrowColorsList = [BLACK, LT_BLUE]    #contains the text and background colors of the right arrow that is next to the territory allocations text
    ceasefireCardRtArrowRect = getTextRect(' '*5+'>'+' '*5,  20,  .8*w,  (.265+.065*4)*h,  BLACK,  LT_BLUE)    #contains the rect object for the right arrow that is next to the ceasefire card text
    ceasefireCardLftArrowRect = getTextRect(' '*5+'<'+' '*5,  20,  .2*w,  (.265+.065*4)*h,  BLACK,  LT_BLUE)  #contains the rect object for the left arrow that is next to the ceasefire card text
    ceasefireCardRtArrowColorsList = [BLACK, LT_BLUE]  #contains the text and background colors for the right arrow that is next to the ceasefire card text
    ceasefireCardLftArrowColorsList = [BLACK, LT_BLUE] #contains the text and background colors for the left arrow that is next to the ceasefire card text
    menuScreenNextRect = getTextRect('NEXT',  25,  .9*w,  .95*h,  RED,  WHITE)    #contains the rect object for the next button that is located on the menu screen
    menuScreenNextColorsList = [RED, WHITE]    #contains the text and background colors for the next button that is located on the menu screen
    playersScreen = False     #contains the bool for whether the game should be displaying the players screen
    menuScreenBackRect = getTextRect('BACK',  25,  .1*w,  .95*h,  RED,  WHITE)    #contains the rect object for the back button that is located on the menu screen
    menuScreenBackColorsList = [RED, WHITE]    #contains the text and background colors for the back button that is located on the menu screen
    menuScreenDirectionsRect = getTextRect('DIRECTIONS',  25,  .5*w,  .95*h,  RED, WHITE)  #contains the rect object for the directions button that is located on the menu screen
    menuScreenDirectionsColorsList = [RED, WHITE]  #contains the text and background colors for the directions button that is on the menu screen  
    playerOptionsDict = {1:'On', 2:'On', 3:'On', 4:'Off', 5:'Off'}   #contains the text data for whether the player is on or off (!!! changed 3 to on...NEED TO FIX WHEN DONE TESTING)
    playersLftRtButtonRectAndColorsDict = {}
    #players left and right button rects and colors
    for i in range(1, 6):
        playersLftRtButtonRectAndColorsDict['player_right'+str(i)] = [[getTextRect(' '*5+'>'+' '*5,  20,  .8*w,  (.265+(.13*(i-1)))*h,  BLACK,  LT_BLUE)], [BLACK, LT_BLUE]]
        playersLftRtButtonRectAndColorsDict['player_left'+str(i)] = [[getTextRect(' '*5+'<'+' '*5,  20,  .2*w,  (.265+(.13*(i-1)))*h,  BLACK, LT_BLUE)], [BLACK, LT_BLUE]]  
    playersScreenButtonsRectAndColorsDict = {'back':[getTextRect('BACK',  25,  .1*w,  .95*h,  RED,  WHITE), [RED, WHITE]], 'start':[getTextRect('START',  25,  .9*w,  .95*h,  RED,  WHITE), [RED, WHITE]]}     #contains the rect object and colors for the buttons that are located on the player screen
    playersScreenErrorMessage = False #contains a bool whether or not the game should display the error message that there are not enough players
    countryInfoDict = dict(COUNTRY_INFO_DICT)     #exact copy of the COUNTRY_INFO_DICT that will be edited
    allowedColors = []        #contains a list of the colors that the players have chosen to use
    gameInPlayScreen = False  #contains a bool of whether or not the game in play screen should be showing up on the screen
    playerTurn = 1    #contains a number for which player's turn it is
    currentPhaseDict = {'draft':WHITE,  'attack':BLACK,  'fortify':BLACK}   #dict that contains the color that the phase should be displaying for it's text color
    nextPlayerScreen = False    #contains a bool of whether or not the player popup should be displayed
    gameInPlayScreen = False  #contains a bool of whether or not the game in play screen should be displayed
    arrowIcon = pygame.image.load('arrow_icon.png').convert_alpha()   #contains the arrow icon image
    arrowRect = pygame.Rect(.123*w, .27*h,  .05*w, .07*h)    #contains the arrow icon rect object
    nextPlayerScreenNextButtonRect = getTextRect('NEXT',  25,  .925*w,  .95*h,  BLACK,  WHITE)     #contains the rect object for the next button that is located on the nextPlayerScreen
    nextPlayerScreenNextButtonColorsList = [RED, WHITE]    #contains the color list for the next button that is located on the nextPlayerScreen
    nextPlayerScreenHelpButtonRect = getTextRect('HELP',  25,  .925*w,  .85*h,  RED, WHITE)    #contains the rect object for the help button that is located on the nextPlayerScreen
    nextPlayerScreenHelpButtonColorsList = [RED, WHITE]    #contains the colors list for the help button that is located on the nextPlayerScreen
    draftPopup = True #contains the bool of whether or not the draft popup should be showing up
    attackPopup = False   #contains the bool of whether or not the attack popup should be showing up
    fortifyPopup = False  #contains the bool of whether or not the foritfy popup should be showing up 
    draftTroops = 0   #contains the number of troops that the current player is allowed to draft
    popupButtonRect = getTextRect('CONTINUE',  25,  .5*w,  .7*h,  RED, WHITE)    #contains the rect object for the draft button that is located on the gameInPlayScreen
    popupButtonColorsList = [RED, WHITE]   #contains the colors for the button that is located on the gameInPlayScreen
    currentPhase = 'draft'    #contains the string of what the current phase is
    holdCountries = []    #contains the countries that should continue to be highlighted
    attackButtonRect = getTextRect('ATTACK!',  25,  .5*w,  .95*h,  RED,  WHITE)    #contains the rect object for the attack button that is located on the gameInPlayScreen
    attackButtonColorsList = [RED, WHITE]  #contains the colors that the attack button should be showing up as
    attackDiceValues = [6 for i in range(3)]    #contains the numbers of the attack dice
    defendDiceValues = [4, 6]    #contains the numbers of the defend dice
    diceDict = {1:pygame.image.load('dice_images/1.png').convert_alpha(),  2:pygame.image.load('dice_images/2.png'), 3:pygame.image.load('dice_images/3.png'), 4:pygame.image.load('dice_images/4.png'), 5:pygame.image.load('dice_images/5.png'), 6:pygame.image.load('dice_images/6.png')}    #contains the images for each of the numbers on the cube
    attack = False    #contains data about whether or not the player has pressed the attack button
    resultsList = []  #contains the information about whether the player won,  lost,  or tied the battle
    result = ''   #contains the str information about whether the player won,  lost,  or tied
    resultRect = getTextRect(result,  25,  .5*w,  .95*h,  RED,  WHITE) #contains the rect object for the result button that is located in the gameInPlayScreen
    resultColorsList = [RED,  WHITE]   #contains the colors for the rect object that is located in the gameInPlayScreen
    totalTransferTroops = 0   #contains the total number of troops that the player can transfer to their newly acquired territory
    transferButton = False    #contains a bool of whether or not the transfer button should be displayed onto the screen
    transferButtonRect = getTextRect(' > ',  25,  .775*w,  .95*h,  LT_BLUE,  BLACK)   #contains the rect object for the transfer button that is located on the gameInPlayScreen
    transferButtonColorsList = [LT_BLUE, BLACK]    #contains the colors for the transfer button that is located on the gameInPlayScreen
    totalTroops = 0   #contains the total number of troops that a territory had before any troops were transfered
    finishTransferTroopsRect = getTextRect('Transfer Troops: '+str(totalTransferTroops),  25,  .5*w,  .95*h,  BLACK,  LT_BLUE)     #contains the rect object for the transfer troops button that is located on the gameInPlayScreen
    finishTransferTroopsColorsList = [BLACK,  LT_BLUE]     #contains the colors for the finish transfer button that is located on the gameInPlayScreen
    endAttackPhaseButtonRect = getTextRect('END ATTACK PHASE',  25,  .5*w,  .95*h,  RED,  WHITE)   #contains the rect object for the end attack phase button that is located on the gameInPlayScreen
    endAttackPhaseButtonColorsList = [RED, WHITE]  #contains the colors for the end attack phase button that is located on the gameInPlayScreen
    fortifyHoldCountries = []     #contains the list of countries that the program should be showing in the fortify phase
    fortifyTroops = 0     #contains the total number of troops that the territory can transfer
    finishFortifyButtonColorsList = [BLACK,  LT_BLUE]  #contains the colors for the finish fortify button that is located on the gameInPlayScreen
    finishFortifyButtonRect = getTextRect('FORTIFY TROOPS: '+str(fortifyTroops)+' ',  25,  .5*w,  .95*h,  BLACK)    #contains the rect object for the finish fortify button that is located on the gameInPlayScreen
    increaseFortifyButtonRect = getTextRect(' > ',  25,  .775*w,  .95*h,  BLACK)  #contains the rect object for the increase foritfy button that is located on the gameInPlayScreen during the fortify phase
    increaseFortifyButtonColorsList = [LT_BLUE,  BLACK]    #contains the colors for the increase fortify button that is located on the gameInPlayScreen during the fortify phase
    endFortifyPhaseButtonRect = getTextRect('END FORTIFY PHASE',  25,  .5*w,  .95*h,  RED,  WHITE)     #contains the rect object for the endFortifyPhaseButton that is located on the gameInPlayScreen during the fortify phase
    endFortifyPhaseButtonColorsList = [RED,  WHITE]    #contains the colors for the endFortifyPhaseButton that is located on the gameInPlayScreen during the fortify phase
    changePageButtonRectsDict = {'next': getTextRect('NEXT PAGE',  25,  .7*w,  .9*h,  RED),  'last': getTextRect('LAST PAGE',  25,  .3*w,  .9*h,  RED, WHITE)}  #is a dict of all of the rects for the change page buttons
    changePageButtonColorsListDict = {'next':[RED, WHITE],  'last':[RED, WHITE]}     #contains the colors of each part of the dict
    directionsScreenPageNumber = 1    #contains the page number of the directions screen
    undoButtonRect = getTextRect('UNDO',  25,  .9*w,  .95*h,  BLACK)  #contains the rect object for the undo button that is located on the gameInPlayScreen
    undoButtonColorsList = [RED, WHITE]    #contains the colors list for the undo button
    fromHelpButton = False    #contains a bool of whether or not the player has come from the playerHandOver screen
    fortifyHoldCountriesTroopsList = [0 for i in range(2)]   #contains a list of the country that is supposed to be holding along with the number of troops that they have in the beginnnig
    gameOverButtonRect = getTextRect('EXIT',  25,  .5*w,  .7*h,  BLACK)   #contains the rect object for the gameOver button that occurs when the game is over
    gameOverButtonColorsList = [RED, WHITE]    #contains the game over button colors for the gameOver button that shows up when the game is over
    playerCardsDict = {}  #contains a dictionary of all of the cards that the player has
    firstTerritoryConquered = False   #contains a bool of whether or not the player has conquered the first territory
    cardsScreen = False   #contains a bool of whether or not the cardsScreen should be displayed
    numOfCardsSelected = 0    #contains an int of the nunber of cards that are selected
    finishTradeRect = getTextRect('TRADE '+str(numOfCardsSelected)+' STARS FOR '+str(getStarBonus(numOfCardsSelected))+' TROOPS'.upper(),  25,  .5*w,  .95*h,  RED,  WHITE)    #contains the rect object for the trade stars button
    finishTradeColorsList = [RED,  WHITE]  #contains the colors for the trade stars button
    lftTradeButtonRect = getTextRect('  <  ',  25,  .1*w,  .95*h,  RED,  WHITE)    #contains the rect object for the left trade button that is located on the cardsScreen
    lftTradeButtonColorsList = [RED, WHITE]    #contains the colors for the left trade button that is located on the cardsScreen
    rtTradeButtonRect = getTextRect('  >  ',  25,  .9*w,  .95*h,  RED,  WHITE)     #contains the rect object for the right trade buttno that is located on the cardsScreen
    rtTradeButtonColorsList = [RED, WHITE]     #contains the colors list foor the right trade button that is located on the cardsScreen
    tradePopup = True #contains a bool of whether or not the trade troops popup should show up
    pygame.mixer.music.play(-1)     #starts playing the background music
    
    #continues until exit is True
    while not exit:
        mousePos = pygame.mouse.get_pos()        #gets the current mouse position 
        
        #executes code for what happens if you click on a button
        for event in pygame.event.get():
            if (event.type  ==  pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit();
                sys.exit();
                
            #changes the variables if the user presses on a button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #contains mouse events for the startScreen
                if startScreen and not gameOver:                
                    if startScreenStartRect.collidepoint(mousePos):
                        startScreen = False
                        menuScreen = True
                    elif directionsRect.collidepoint(mousePos):
                        startScreen = False
                        directionsScreen = True
                    elif exitRect.collidepoint(mousePos):
                        exit = True
                
                #contains mouse events for the directionsScreen
                elif directionsScreen and not gameOver:
                    if directionsScreenBackRect.collidepoint(mousePos):
                        if not fromHelpButton:
                            startScreen = True
                            directionsScreen = False
                        else:
                            nextPlayerScreen = True
                            directionsScreen = False
                    elif directionsScreenMenuRect.collidepoint(mousePos):
                        if fromHelpButton:
                            nextPlayerScreen = True
                            directionsScreen = False
                        else:
                            menuScreen = True
                            directionsScreen = False
                    elif directionsScreenStartRect.collidepoint(mousePos):
                        if fromHelpButton:
                            directionsScreen = False
                            nextPlayerScreen = True
                        else:
                            directionsScreen = False
                            menuScreen = True
                    elif changePageButtonRectsDict['next'].collidepoint(mousePos):
                        if directionsScreenPageNumber<21:
                            directionsScreenPageNumber += 1
                    elif changePageButtonRectsDict['last'].collidepoint(mousePos):
                        if directionsScreenPageNumber>1:
                            directionsScreenPageNumber -= 1
                
                #contains mouse over events for the menuScreen
                elif menuScreen and not gameOver:
                    #game type arrows
                    if gameTypeRtArrowRect.collidepoint(mousePos):
                        if currentGameType.lower() == 'world domination':
                            currentGameType = 'Capitals'
                        elif currentGameType.lower() == 'capitals':
                            currentGameType = 'Secret Mission'
                        elif currentGameType.lower() == 'secret mission':
                            currentGameType = 'World Domination'
                    if gameTypeLftArrowRect.collidepoint(mousePos):
                        if currentGameType.lower() == 'world domination':
                            currentGameType = 'secret mission'.title()
                        elif currentGameType.lower() == 'capitals':
                            currentGameType = 'world domination'.title()
                        elif currentGameType.lower() == 'secret mission':
                            currentGameType = 'capitals'.title()
                    
                    #territory allocation arrows
                    if territoryAlocationsRtArrowRect.collidepoint(mousePos) or territoryAlocationsLftArrowRect.collidepoint(mousePos):
                        if territoryAlocationsOption == 'manual'.title():
                            territoryAlocationsOption = 'random'.title()
                        elif territoryAlocationsOption == 'random'.title():
                            territoryAlocationsOption = 'manual'.title()
                    
                    #ceasefire card arrows
                    if ceasefireCardRtArrowRect.collidepoint(mousePos) or ceasefireCardLftArrowRect.collidepoint(mousePos):
                        if ceasefireCardOption == 'on'.title():
                            ceasefireCardOption = 'off'.title()
                        elif ceasefireCardOption == 'off'.title():
                            ceasefireCardOption = 'on'.title()
                    
                    #next button
                    if menuScreenNextRect.collidepoint(mousePos):
                        if MENU_OPTIONS_DICT.get(currentGameType,  'Error') != 'Error' and MENU_OPTIONS_DICT.get(territoryAlocationsOption, 'Error') != 'Error':
                            menuScreen = False
                            playersScreen = True
                        
                    #back button
                    if menuScreenBackRect.collidepoint(mousePos):
                        menuScreen = False
                        startScreen = True
                    
                    #directions button
                    if menuScreenDirectionsRect.collidepoint(mousePos):
                        menuScreen = False
                        directionsScreen = True
                
                #contains mouse over events for the playersScreen
                elif playersScreen and not gameOver:
                    #player arrows
                    for i in range(1, 6):
                        #right arrows
                        if playersLftRtButtonRectAndColorsDict['player_right'+str(i)][0][0].collidepoint(mousePos):
                            if playerOptionsDict[i] == 'off'.title():
                                playerOptionsDict[i] = 'on'.title()
                            elif playerOptionsDict[i] == 'on'.title():
                                playerOptionsDict[i] = 'off'.title()
                        
                        #left arrows
                        if playersLftRtButtonRectAndColorsDict['player_left'+str(i)][0][0].collidepoint(mousePos):
                            if playerOptionsDict[i] == 'off'.title():
                                playerOptionsDict[i] = 'on'.title()
                            elif playerOptionsDict[i] == 'on'.title():
                                playerOptionsDict[i] = 'off'.title()    
                        
                        #back button
                        if playersScreenButtonsRectAndColorsDict['back'][0].collidepoint(mousePos):
                            menuScreen = True
                            playersScreen = False
                        
                        #start button
                        if playersScreenButtonsRectAndColorsDict['start'][0].collidepoint(mousePos):                            
                            numOfPlayers = 0
                            nextPlayerScreen = True
                            
                            #counts up how many players are on
                            for i in range(1, len(playerOptionsDict)+1):
                                if playerOptionsDict[i] == 'on'.title():
                                    numOfPlayers += 1
                                    
                            #adds the players onto the playerCardsDict
                            for i in range(numOfPlayers):
                                playerCardsDict[i+1] = 0
                            
                            #checks to make sure that there is at least 2 players
                            if numOfPlayers<3:
                                playersScreenErrorMessage = True
                                nextPlayerScreen = False
                            else:
                                playersScreenErrorMessage = False
                                playersScreen = False
                                
                                #creates the allowed colors list
                                for i in range(1, 6):
                                    if playerOptionsDict[i] == 'on'.title():
                                        if STR_COLORS_LIST[i] not in allowedColors:
                                            allowedColors.append(STR_COLORS_LIST[i])
                                
                                #changes the colors of the copy of the orginal country dict
                                countryInfoKeysColorsLeftList = list(countryInfoDict.keys())  #contains all of the keys in the country info dict that are left to use
                                
                                #gives each territory a random color from the allowedColors list
                                for i in range(numOfPlayers):
                                    for j in range(len(countryInfoDict.keys())//numOfPlayers):
                                        choice = random.choice(countryInfoKeysColorsLeftList)
                                        countryInfoDict[choice][4] = allowedColors[i]
                                        countryInfoKeysColorsLeftList.pop(countryInfoKeysColorsLeftList.index(choice))
                                        
                                #assigns troops a certain number of troops to each territory
                                countryInfoDict = assignTroops(countryInfoDict,  numOfPlayers,  allowedColors)                                
                                
                
                #contains mouse over events for the nextPlayerScreen
                elif nextPlayerScreen and not gameOver:
                    if nextPlayerScreenNextButtonRect.collidepoint(mousePos):
                        nextPlayerScreen = False
                        cardsScreen = True
                        tradePopup = True
                        
                    elif nextPlayerScreenHelpButtonRect.collidepoint(mousePos):
                        nextPlayerScreen = False
                        directionsScreen = True
                        fromHelpButton = True
                
                #contains mouse over events for the cardsScreen
                elif cardsScreen and not tradePopup and not gameOver:
                    if finishTradeRect.collidepoint(mousePos):
                        cardsScreen = False
                        gameInPlayScreen = True
                        draftTroops = (getNumOfCountryColors(numOfPlayers,  allowedColors,  countryInfoDict)[playerTurn-1]//3)+getContientBonus(playerTurn,  countryInfoDict,  allowedColors)+getStarBonus(numOfCardsSelected)
                        finishTradeColorsList=[RED,WHITE]
                        
                        playerCardsDict[playerTurn]-=numOfCardsSelected
                        
                        if draftTroops<3:
                            draftTroops=3
                        
                        draftPopup = True
                        finishFortifyButtonColorsList = [RED,  WHITE]
                        
                        
                    if lftTradeButtonRect.collidepoint(mousePos):
                        if numOfCardsSelected-1 >= 0:
                            numOfCardsSelected -= 1
                    
                    if rtTradeButtonRect.collidepoint(mousePos):
                        if numOfCardsSelected+1 <= playerCardsDict[playerTurn]:
                            numOfCardsSelected += 1
                        
                
                #contains mouse over events for the CONTINUE button
                elif (gameInPlayScreen or cardsScreen) and (draftPopup or fortifyPopup or attackPopup or tradePopup) and not gameOver:
                    if popupButtonRect.collidepoint(mousePos):
                        draftPopup = False
                        fortifyPopup = False
                        attackPopup = False
                        tradePopup = False
                
                #contains mouse over events for the gameInPlayScreen during the draft phase
                elif gameInPlayScreen and currentPhase == 'draft' and not draftPopup and not gameOver:
                    #adds one troop to the territory that the player has clicked on and removes one troop from the draftTroops variable
                    for i in range(len(COUNTRY_RECT_LIST)):
                        if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)):
                            draftTroops -= 1
                            countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5] += 1
                            
                            #changes the currentPhase if there are no more troops left to draft and sets the attackPopup to True
                            if draftTroops == 0:
                                currentPhase = 'attack'
                                attackPopup = True
                                currentPhaseDict['draft'] = BLACK
                                currentPhaseDict['attack'] = WHITE
                
                #contains mouse over events for the gameInPlayScreen during the attackPhase without the transferButton being used
                elif gameInPlayScreen and currentPhase == 'attack' and not attackPopup and not attack and not transferButton and not gameOver:
                    if len(holdCountries) == 0:
                        #country selecting in attack phase                        
                        for i in range(len(COUNTRY_RECT_LIST)):
                            if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5] >= 2:
                                holdCountries.append(COUNTRY_INFO_KEYS_LIST[i])
                                break
                            
                        #end attack phase button
                        if endAttackPhaseButtonRect.collidepoint(mousePos):
                            currentPhase = 'fortify'
                            fortifyPopup = True
                            mouseOverCountry = ''
                            holdCountries = []
                            currentPhaseDict['fortify'] = WHITE
                            currentPhaseDict['attack'] = BLACK
                            
                    elif len(holdCountries) == 1:
                        for i in range(len(COUNTRY_RECT_LIST)):
                            if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] not in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and (COUNTRY_INFO_KEYS_LIST[i] in CONNECTED_COUNTRIES_DICT[holdCountries[0]]):
                                holdCountries.append(COUNTRY_INFO_KEYS_LIST[i]) 
                                break
                    
                    elif len(holdCountries) == 2:
                        #attack button
                        if attackButtonRect.collidepoint(mousePos):
                            attack = True
                            resultsList = []
                            
                            if countryInfoDict[holdCountries[0]][5] >= 4:
                                attackDiceValues = [random.randint(1, 6) for i in range(3)]
                            elif countryInfoDict[holdCountries[0]][5] == 3:
                                attackDiceValues = [random.randint(1, 6) for i in range(2)]
                            elif countryInfoDict[holdCountries[0]][5] == 2:
                                attackDiceValues = [random.randint(1, 6) for i in range(1)]
                            
                            if countryInfoDict[holdCountries[1]][5] >= 2:
                                defendDiceValues = [random.randint(1, 6) for i in range(2)]
                            else:
                                defendDiceValues = [random.randint(1, 6)]
                                
                            
                            maxAttackDie = max(attackDiceValues)
                            maxDefendDie = max(defendDiceValues)
                            
                            if maxAttackDie>maxDefendDie:
                                countryInfoDict[holdCountries[1]][5] -= 1
                                resultsList.append('Won')
                            elif maxAttackDie <= maxDefendDie:
                                countryInfoDict[holdCountries[0]][5] -= 1    
                                resultsList.append('Lost')
                            
                            if len(defendDiceValues) == 2 and len(attackDiceValues) >= 2:
                                #second max attack die
                                tempAttackDieList = attackDiceValues.copy()
                                tempAttackDieList.remove(maxAttackDie)
                                secondMaxAttackDie = max(tempAttackDieList)
                                
                                #second max defend die
                                tempDefendDieList = defendDiceValues.copy()
                                tempDefendDieList.remove(maxDefendDie)
                                secondMaxDefendDie = max(tempDefendDieList)
                                
                                if secondMaxAttackDie>secondMaxDefendDie:
                                    countryInfoDict[holdCountries[1]][5] -= 1
                                    resultsList.append('Won')
                                elif secondMaxAttackDie <= maxDefendDie:
                                    countryInfoDict[holdCountries[0]][5] -= 1  
                                    resultsList.append('Lost')
                            #checks to see if the player has conquered the other territory
                            if countryInfoDict[holdCountries[-1]][5] <= 0:
                                totalTroops = countryInfoDict[holdCountries[0]][5]                            
                                countryInfoDict[holdCountries[1]][4] = countryInfoDict[holdCountries[0]][4]
                                transferButton = True
                                totalTransferTroops = 1
                                countryInfoDict[holdCountries[1]][5] = 1
                                countryInfoDict[holdCountries[0]][5] -= 1
                                
                                
                            #determines what the result is
                            if resultsList.count('Won')>resultsList.count('Lost'):
                                result = 'Won'
                            elif resultsList.count('Lost')>resultsList.count('Won'):
                                result = 'Lost'
                            elif resultsList.count('Lost') == resultsList.count('Won'):
                                result = 'Tie'
                            
                            resultRect = getTextRect(result,  25,  .5*w,  .95*h,  RED,  WHITE)
                    elif len(holdCountries)>2:
                        for i in range(len(holdCountries)-2):
                            holdCountries.pop(-1)
                        mouseOverCountry = ''
                    #undo button
                    if undoButtonRect.collidepoint(mousePos) and (len(holdCountries) == 1 or len(holdCountries) == 2):
                        holdCountries.pop(-1)
                
                #contains mouse over events for the gameInPlayScreen when the player has just attacked
                elif gameInPlayScreen and currentPhase == 'attack' and not attackPopup and attack and not transferButton and not gameOver:
                    if resultRect.collidepoint(mousePos):
                        attack = False
                        holdCountries = []
                        mouseOverCountry = ''
                    
                
                #contains mouse over events for the gameInPlayScreen with the transferButton
                elif gameInPlayScreen and currentPhase == 'attack' and not attackPopup and attack and transferButton and not gameOver:
                    if transferButtonRect.collidepoint(mousePos):
                        totalTransferTroops += 1
                        
                        if totalTransferTroops >= totalTroops:
                            totalTransferTroops = 1
                        
                        countryInfoDict[holdCountries[0]][5] = totalTroops-totalTransferTroops
                        countryInfoDict[holdCountries[1]][5] = totalTransferTroops   
                    elif finishTransferTroopsRect.collidepoint(mousePos):
                        gameOver = determineGameOver(ceasefireCardOption,  playerTurn,  countryInfoDict,  allowedColors) #determines whether the game is over or not     

                        if gameOver:
                            transferButtonColorsList = [RED, WHITE]
                            continue
                        
                        attack = False
                        transferButton = False
                        holdCountries = []
                        mouseOverCountry = ''
                        
                        #adds a card to the player if they have conquered a territory and it is the first territory that they have captured
                        if not firstTerritoryConquered and playerCardsDict[playerTurn]<10:
                            playerCardsDict[playerTurn] += 1
                            firstTerritoryConquered = True
                        
                        
                        if gameOver:
                            gameInPlayScreen = False
                
                #contains mouse over events for the gameInPlayScreen during the fortify phase
                elif gameInPlayScreen and currentPhase == 'fortify' and not fortifyPopup and not gameOver:
                    firstTerritoryConquered = False
                    if len(fortifyHoldCountries) == 0:
                        #country selecting in fortify phase                        
                        for i in range(len(COUNTRY_RECT_LIST)):
                            if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5] >= 2:
                                fortifyHoldCountries.append(COUNTRY_INFO_KEYS_LIST[i])
                                fortifyHoldCountriesTroopsList[0] = ([COUNTRY_INFO_KEYS_LIST[i], countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5]])
                                break
                                
                        #end fortify phase button
                        if endFortifyPhaseButtonRect.collidepoint(mousePos):
                            currentPhase = 'draft'
                            nextPlayerScreen = True
                            gameInPlayScreen = False
                            draftPopup = True
                            holdCountries = []
                            mouseOverCountry = ''
                            fortifyHoldCountries = []
                            currentPhaseDict['fortify'] = BLACK
                            currentPhaseDict['draft'] = WHITE
                            playerTurn, playerCardsDict=getNextPlayer(numOfPlayers, playerCardsDict, gameOver, playerTurn, countryInfoDict, allowedColors)
                            numOfCardsSelected=0
           
                          
                    elif len(fortifyHoldCountries) == 1:
                        for i in range(len(COUNTRY_RECT_LIST)):
                            if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and (COUNTRY_INFO_KEYS_LIST[i] in CONNECTED_COUNTRIES_DICT[fortifyHoldCountries[0]]):
                                fortifyHoldCountries.append(COUNTRY_INFO_KEYS_LIST[i]) 
                                fortifyHoldCountriesTroopsList[1] = ([COUNTRY_INFO_KEYS_LIST[i], countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5]])
                                fortifyTroops = 1
                                countryInfoDict[fortifyHoldCountries[0]][5] -= fortifyTroops
                                countryInfoDict[fortifyHoldCountries[1]][5] += fortifyTroops
                                break
                    elif len(fortifyHoldCountries) == 2:                       
                        if increaseFortifyButtonRect.collidepoint(mousePos):
                            if countryInfoDict[fortifyHoldCountries[0]][5]-1 >= 1:
                                fortifyTroops += 1
                            else:
                                fortifyTroops = 1
        
                            countryInfoDict[fortifyHoldCountries[0]][5] = fortifyHoldCountriesTroopsList[0][1]-fortifyTroops
                            countryInfoDict[fortifyHoldCountries[1]][5] = fortifyHoldCountriesTroopsList[1][1]+fortifyTroops
                        elif finishFortifyButtonRect.collidepoint(mousePos):
                            currentPhase = 'draft'
                            nextPlayerScreen = True
                            gameInPlayScreen = False
                            draftPopup = True
                            holdCountries = []
                            mouseOverCountry = ''
                            fortifyHoldCountries = []
                            playerTurn, playerCardsDict=getNextPlayer(numOfPlayers, playerCardsDict, gameOver, playerTurn, countryInfoDict, allowedColors)
                            currentPhaseDict['fortify'] = BLACK
                            currentPhaseDict['draft'] = WHITE    
                            numOfCardsSelected=0
                    
                    #undo button
                    if undoButtonRect.collidepoint(mousePos) and (len(fortifyHoldCountries) == 1 or len(fortifyHoldCountries) == 2):
                        if len(fortifyHoldCountries) == 2:
                            countryInfoDict[fortifyHoldCountries[0]][5] = fortifyHoldCountriesTroopsList[0][-1]
                            countryInfoDict[fortifyHoldCountries[-1]][5] = fortifyHoldCountriesTroopsList[1][1]  
                        fortifyHoldCountries.pop(-1)
                
                
                
                #contains mouse over events for when the game is over
                if gameOver:
                    if gameOverButtonRect.collidepoint(mousePos):
                        exit = True

        
        #adds the country to the mouseOverCountry list if it is the draft phase and it is their country and their mouse is hovering over it
        if gameInPlayScreen and currentPhase == 'draft' and not draftPopup and not fortifyPopup and not attackPopup and not gameOver and not startScreen and not directionsScreen and not menuScreen and not playersScreen and not nextPlayerScreen:
            for i in range(len(COUNTRY_RECT_LIST)):
                if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)):
                    mouseOverCountry = COUNTRY_INFO_KEYS_LIST[i]
                
        #changes the colors for the buttons in the start screen if the mouse is hovering over them
        elif not gameOver and startScreen and not directionsScreen and not exit and not menuScreen and not playersScreen and not nextPlayerScreen:
            if startScreenStartRect.collidepoint(mousePos):
                startScreenStartColors = [WHITE, BLACK]
            else:
                startScreenStartColors = [RED, WHITE]
            
            if directionsRect.collidepoint(mousePos):
                directionsColors = [WHITE, BLACK]
            else:
                directionsColors = [RED, WHITE]
                
            if exitRect.collidepoint(mousePos):
                exitColors = [WHITE, BLACK]
            else:
                exitColors = [RED, WHITE]
                
        
        #changes the button colors in the directions screen if the mouse hovers over the button
        elif directionsScreen and not gameOver and not startScreen and not menuScreen and not playersScreen and not nextPlayerScreen:
            if directionsScreenBackRect.collidepoint(mousePos):
                directionsScreenBackColors = [WHITE, BLACK]
            else:
                directionsScreenBackColors = [RED, WHITE]
            
            if directionsScreenStartRect.collidepoint(mousePos):
                directionsScreenStartColors = [WHITE, BLACK]
            else:
                directionsScreenStartColors = [RED, WHITE]
                
            if directionsScreenMenuRect.collidepoint(mousePos):
                directionsScreenMenuColors = [WHITE, BLACK]
            else:
                directionsScreenMenuColors = [RED, WHITE]
            
            #last button
            if changePageButtonRectsDict['last'].collidepoint(mousePos):
                changePageButtonColorsListDict['last'] = [WHITE, BLACK]
            else:
                changePageButtonColorsListDict['last'] = [RED, WHITE]
            
            #next button
            if changePageButtonRectsDict['next'].collidepoint(mousePos):
                changePageButtonColorsListDict['next'] = [WHITE, BLACK]
            else:    
                changePageButtonColorsListDict['next'] = [RED, WHITE]
        
        #changes the buttons colors on the menu screen
        elif not startScreen and not directionsScreen and menuScreen and not playersScreen and not nextPlayerScreen and not gameOver:
            if gameTypeLftArrowRect.collidepoint(mousePos):
                gameTypeLftArrowColorsList = [LT_BLUE, BLACK]
            else:
                gameTypeLftArrowColorsList = [BLACK, LT_BLUE]
          
            
            if gameTypeRtArrowRect.collidepoint(mousePos):
                gameTypeRtArrowColorsList = [LT_BLUE, BLACK]
            else:
                gameTypeRtArrowColorsList = [BLACK, LT_BLUE]
                
            if territoryAlocationsLftArrowRect.collidepoint(mousePos):
                territoryAlocationsLftArrrowColorsList = [LT_BLUE, BLACK]
            else:
                territoryAlocationsLftArrrowColorsList = [BLACK, LT_BLUE]
                
            if territoryAlocationsRtArrowRect.collidepoint(mousePos):
                territoryAlocationsRtArrowColorsList = [LT_BLUE, BLACK]
            else:
                territoryAlocationsRtArrowColorsList = [BLACK, LT_BLUE]
                
            if ceasefireCardRtArrowRect.collidepoint(mousePos):
                ceasefireCardRtArrowColorsList = [LT_BLUE, BLACK]
            else:
                ceasefireCardRtArrowColorsList = [BLACK, LT_BLUE]
        
            if ceasefireCardLftArrowRect.collidepoint(mousePos):
                ceasefireCardLftArrowColorsList = [LT_BLUE, BLACK]
            else:
                ceasefireCardLftArrowColorsList = [BLACK, LT_BLUE]
            
            #next button
            if menuScreenNextRect.collidepoint(mousePos):
                menuScreenNextColorsList = [WHITE, BLACK]
            else:
                menuScreenNextColorsList = [RED, WHITE]
                
            #back button
            if menuScreenBackRect.collidepoint(mousePos):
                menuScreenBackColorsList = [WHITE, BLACK]
            else:
                menuScreenBackColorsList = [RED, WHITE]
            
            #directions button
            if menuScreenDirectionsRect.collidepoint(mousePos):
                menuScreenDirectionsColorsList = [WHITE, BLACK]
            else:
                menuScreenDirectionsColorsList = [RED, WHITE]
        #players screen
        elif playersScreen and not startScreen and not menuScreen and not directionsScreen and not nextPlayerScreen and not gameOver:
            #player arrows
            for i in range(1, 6):
                #right arrows
                if playersLftRtButtonRectAndColorsDict['player_right'+str(i)][0][0].collidepoint(mousePos):
                    playersLftRtButtonRectAndColorsDict['player_right'+str(i)][-1] = [LT_BLUE, BLACK]
                else:
                    playersLftRtButtonRectAndColorsDict['player_right'+str(i)][-1] = [BLACK, LT_BLUE]
                
                #left arrows
                if playersLftRtButtonRectAndColorsDict['player_left'+str(i)][0][0].collidepoint(mousePos):
                    playersLftRtButtonRectAndColorsDict['player_left'+str(i)][-1] = [LT_BLUE, BLACK]
                else:
                    playersLftRtButtonRectAndColorsDict['player_left'+str(i)][-1] = [BLACK, LT_BLUE]
                
                #back button
                if playersScreenButtonsRectAndColorsDict['back'][0].collidepoint(mousePos):
                    playersScreenButtonsRectAndColorsDict['back'][-1] = [WHITE, BLACK]
                else:
                    playersScreenButtonsRectAndColorsDict['back'][-1] = [RED, WHITE]
                    
                #start button
                if playersScreenButtonsRectAndColorsDict['start'][0].collidepoint(mousePos):
                    playersScreenButtonsRectAndColorsDict['start'][-1] = [WHITE, BLACK]
                else:
                    playersScreenButtonsRectAndColorsDict['start'][-1] = [RED, WHITE]  
        #nextPlayerScreen
        elif nextPlayerScreen and not startScreen and not menuScreen and not directionsScreen and not gameOver:
            #checks the next button
            if nextPlayerScreenNextButtonRect.collidepoint(mousePos):
                nextPlayerScreenNextButtonColorsList = [WHITE, BLACK]
            else:
                nextPlayerScreenNextButtonColorsList = [RED, WHITE]
            
            #checks the help button    
            if nextPlayerScreenHelpButtonRect.collidepoint(mousePos):
                nextPlayerScreenHelpButtonColorsList = [WHITE, BLACK]
            else:
                nextPlayerScreenHelpButtonColorsList = [RED, WHITE]
        #CONTINUE button on the popups
        elif (gameInPlayScreen or cardsScreen) and (draftPopup or attackPopup or fortifyPopup or tradePopup) and not startScreen and not nextPlayerScreen and not menuScreen and not directionsScreen and not gameOver:
            if popupButtonRect.collidepoint(mousePos):
                popupButtonColorsList = [WHITE,  BLACK]
            else:
                popupButtonColorsList = [RED,  WHITE]
        #gameInPlayScreen during the attack phase
        elif gameInPlayScreen and currentPhase == 'attack' and not draftPopup and not fortifyPopup and not startScreen and not nextPlayerScreen and not menuScreen and not directionsScreen and not transferButton and not attack and not gameOver:
            if len(holdCountries) == 0:
                #countries button
                for i in range(len(COUNTRY_RECT_LIST)):
                    if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5] >= 2:
                        mouseOverCountry = COUNTRY_INFO_KEYS_LIST[i]
                        break
                
                #end attack button
                if endAttackPhaseButtonRect.collidepoint(mousePos):
                    endAttackPhaseButtonColorsList = [WHITE,  BLACK]
                else:
                    endAttackPhaseButtonColorsList = [RED,  WHITE]                
            elif len(holdCountries) == 1:
                for i in range(len(COUNTRY_RECT_LIST)):
                    if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] not in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors) and (COUNTRY_INFO_KEYS_LIST[i] in CONNECTED_COUNTRIES_DICT[holdCountries[0]])):
                        mouseOverCountry = COUNTRY_INFO_KEYS_LIST[i]
                        break
            elif len(holdCountries) == 2:    
                #attack button
                if attackButtonRect.collidepoint(mousePos):
                    attackButtonColorsList = [WHITE,  BLACK]
                else:
                    attackButtonColorsList = [RED,  WHITE]
            #undo button
            if len(holdCountries) == 1 or len(holdCountries) == 2:
                if undoButtonRect.collidepoint(mousePos):
                    undoButtonColorsList = [WHITE, BLACK]
                else:
                    undoButtonColorsList = [RED,  WHITE]
        #gameInPlayScreen during the attack phase when the player is attacking
        elif gameInPlayScreen and currentPhase == 'attack' and attack and not draftPopup and not attackPopup and not fortifyPopup and not startScreen and not nextPlayerScreen and not menuScreen and not directionsScreen and not transferButton and not gameOver:
            if resultRect.collidepoint(mousePos):
                resultColorsList = [WHITE,  BLACK]
            else:
                resultColorsList = [RED,  WHITE]
        #gameInPlayScreen during the attack phase with the transferButton activated
        elif gameInPlayScreen and currentPhase == 'attack' and transferButton and attack and not menuScreen and not directionsScreen and not draftPopup and not fortifyPopup and not startScreen and not nextPlayerScreen and not gameOver:
            #transfer right button
            if transferButtonRect.collidepoint(mousePos):
                transferButtonColorsList = [WHITE, BLACK]
            else:
                transferButtonColorsList = [BLACK,  LT_BLUE]
            
            #finish transfer button
            if finishTransferTroopsRect.collidepoint(mousePos):
                finishTransferTroopsColorsList = [WHITE, BLACK]
            else:
                finishTransferTroopsColorsList = [BLACK,  LT_BLUE]
        #gameInPlayScreen during the fortify phase
        elif gameInPlayScreen and currentPhase == 'fortify' and not (attack and attackPopup and draftPopup and fortifyPopup and menuScreen and directionsScreen and startScreen and nextPlayerScreen) and not gameOver:
            if len(fortifyHoldCountries) == 0:
                #countries collisions
                for i in range(len(COUNTRY_RECT_LIST)):
                    if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors)) and countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5] >= 2:
                        mouseOverCountry = COUNTRY_INFO_KEYS_LIST[i]            
                
                #end fortify phase button
                if endAttackPhaseButtonRect.collidepoint(mousePos):
                    endAttackPhaseButtonColorsList = [WHITE,  BLACK]
                else:
                    endAttackPhaseButtonColorsList = [RED,  WHITE]
            elif len(fortifyHoldCountries) == 1:
                for i in range(len(COUNTRY_RECT_LIST)):
                    if COUNTRY_RECT_LIST[i].collidepoint(mousePos) and (COUNTRY_INFO_KEYS_LIST[i] in getPlayerTerritoryNames(playerTurn,  countryInfoDict,  allowedColors) and (COUNTRY_INFO_KEYS_LIST[i] in CONNECTED_COUNTRIES_DICT[fortifyHoldCountries[0]])):
                        mouseOverCountry = COUNTRY_INFO_KEYS_LIST[i]        
            #fortify buttons
            elif len(fortifyHoldCountries) == 2:
                if finishFortifyButtonRect.collidepoint(mousePos):
                    finishFortifyButtonColorsList = [WHITE,  BLACK]
                else:
                    finishFortifyButtonColorsList = [BLACK,  LT_BLUE]
                
                if increaseFortifyButtonRect.collidepoint(mousePos):
                    increaseFortifyButtonColorsList = [WHITE,  BLACK]
                else:
                    increaseFortifyButtonColorsList = [BLACK,  LT_BLUE]
            
            #undo button
            if len(fortifyHoldCountries) == 1 or len(fortifyHoldCountries) == 2:
                if undoButtonRect.collidepoint(mousePos):
                    undoButtonColorsList = [WHITE, BLACK]
                else:
                    undoButtonColorsList = [RED,  WHITE] 
        #cardsScreen
        elif cardsScreen and not (nextPlayerScreen and gameInPlayScreen and startScreen and directionsScreen and menuScreen and tradePopup) and not gameOver:
            if finishTradeRect.collidepoint(mousePos):
                finishTradeColorsList = [WHITE, BLACK]
            else:
                finishTradeColorsList = [RED, WHITE]
                
            if lftTradeButtonRect.collidepoint(mousePos):
                lftTradeButtonColorsList = [WHITE, BLACK]
            else:
                lftTradeButtonColorsList = [RED, WHITE]
                
            if rtTradeButtonRect.collidepoint(mousePos):
                rtTradeButtonColorsList = [WHITE, BLACK]
            else:
                rtTradeButtonColorsList = [RED, WHITE]
        
        
        
        #gameOver events
        if gameOver:
            if gameOverButtonRect.collidepoint(mousePos):
                gameOverButtonColorsList = [WHITE, BLACK]
            else:
                gameOverButtonColorsList = [RED,  WHITE]

        #draws the screen 
        drawScreen(mouseOverCountry,  gameOver,  startScreen, startScreenStartColors, directionsColors, directionsScreen, exitColors, directionsScreenStartColors, directionsScreenMenuColors, directionsScreenBackColors, menuScreen, currentGameType, numOfPlayers, territoryAlocationsOption, ceasefireCardOption, gameTypeLftArrowColorsList, gameTypeRtArrowColorsList, territoryAlocationsLftArrrowColorsList, territoryAlocationsRtArrowColorsList, ceasefireCardLftArrowColorsList, ceasefireCardRtArrowColorsList, menuScreenNextColorsList, playersScreen, menuScreenBackColorsList, menuScreenDirectionsColorsList, playerOptionsDict, playersLftRtButtonRectAndColorsDict, playersScreenButtonsRectAndColorsDict, playersScreenErrorMessage, gameInPlayScreen, playerTurn, allowedColors, currentPhaseDict, nextPlayerScreen, countryInfoDict,  arrowIcon, arrowRect,  nextPlayerScreenNextButtonColorsList,  nextPlayerScreenHelpButtonColorsList,  draftPopup,  attackPopup,  fortifyPopup,  draftTroops,  popupButtonColorsList,  currentPhase,  holdCountries,  attackButtonColorsList,  attackDiceValues,  defendDiceValues,  diceDict,  attack,  result,  resultColorsList,  transferButton,  totalTransferTroops,  transferButtonColorsList,  finishTransferTroopsColorsList,  endAttackPhaseButtonColorsList,  fortifyHoldCountries,  fortifyTroops,  finishFortifyButtonColorsList,  increaseFortifyButtonColorsList,  changePageButtonColorsListDict,  directionsScreenPageNumber,  undoButtonColorsList,  gameOverButtonColorsList,  playerCardsDict,  cardsScreen,  numOfCardsSelected,  finishTradeColorsList,  lftTradeButtonColorsList,  rtTradeButtonColorsList,  tradePopup)
        
        #updates the screen and ticks the clock
        pygame.display.update() 
        clock.tick(60)


#------------------------- Functions-----------------------------------
#returns the next player that is going next and gameOver
def getNextPlayer(numOfPlayers,playerCardsDict, gameOver,playerTurn, countryInfoDict,allowedColors):
    if playerTurn < numOfPlayers:
        for i in range(1,numOfPlayers-playerTurn):
            if getNumTroops(playerTurn+i, countryInfoDict, allowedColors) == 0:
                playerCardsDict.pop(playerTurn+i)
        
    
    
    if playerTurn < numOfPlayers:
        if playerTurn+1 in playerCardsDict.keys():
            playerTurn+=1
            
        else:
            if playerTurn+2 in playerCardsDict.keys():
                playerTurn+=2
            elif playerTurn+3 in playerCardsDict.keys():
                playerTurn+=3
            elif playerTurn+4 in playerCardsDict.keys():
                playerTurn+=4
            else:
                if 1 in playerCardsDict.keys():
                    playerTurn=1
                elif 2 in playerCardsDict.keys():
                    playerTurn=2
                elif 3 in playerCardsDict.keys():
                    playerTurn=3
                elif 4 in playerCardsDict.keys():
                    playerTurn=4
                elif 5 in playerCardsDict.keys():
                    playerTurn=5
    else:
        if 1 in playerCardsDict.keys():
            playerTurn=1
        elif 2 in playerCardsDict.keys():
            playerTurn=2
        elif 3 in playerCardsDict.keys():
            playerTurn=3
        elif 4 in playerCardsDict.keys():
            playerTurn=4
        elif 5 in playerCardsDict.keys():
            playerTurn=5
        
    return playerTurn, playerCardsDict

#blits a message onto the screen at a certain location; returns the text bounds
def showMessage(words, size, X, Y, color, bg = None,  font = 'Consolas'):
    font = pygame.font.SysFont(font, int(size * SF), True, False)
    
    textImage = font.render(words, True, color)
    text = font.render(words, True, color, bg)
    
    textBounds = textImage.get_rect()
    textBounds.center = (X, Y)

    surface.blit(text, textBounds)
    
    return text, textBounds

#blits text onto the screen using the topleft x, y location
def topLeftShowMessage(words, size, X, Y, color, bg = None):
    font = pygame.font.SysFont("Consolas", int(size * SF), True, False)
    
    textImage = font.render(words, True, color)
    text = font.render(words, True, color, bg)
    
    textBounds = textImage.get_rect()
    textBounds.topleft = (X, Y)

    surface.blit(text, textBounds)
    
    return text, textBounds

def getTextRect(words, size, X, Y, color, bg = None):
    font = pygame.font.SysFont("Consolas", size, True, False)
    
    textImage = font.render(words, True, color)
    
    textBounds = textImage.get_rect()
    textBounds.center = (X, Y)
    
    return textBounds

def drawScreen(mouseOverCountry, gameOver, startScreen, startScreenStartColors, directionsColors, directionsScreen, exitColors, directionsScreenStartColors, directionsScreenMenuColors, directionsScreenBackColors,  menuScreen, currentGameType, numOfPlayers, territoryAlocationsOption, ceasefireCardOption, gameTypeLftArrowColorsList, gameTypeRtArrowColorsList, territoryAlocationsLftArrrowColorsList, territoryAlocationsRtArrowColorsList,  ceasefireCardLftArrowColorsList, ceasefireCardRtArrowColorsList, menuScreenNextColorsList, playersScreen, menuScreenBackColorsList, menuScreenDirectionsColorsList, playerOptionsDict, playersLftRtButtonRectAndColorsDict, playersScreenButtonsRectAndColorsDict, playersScreenErrorMessage, gameInPlayScreen, playerTurn, allowedColors, currentPhaseDict, nextPlayerScreen, countryInfoDict,  arrowIcon, arrowRect,  nextPlayerScreenNextButtonColorsList, nextPlayerScreenHelpButtonColorsList,  draftPopup,  attackPopup,  fortifyPopup,  draftTroops,  popupButtonColorsList,  currentPhase,  holdCountries,  attackButtonColorsList,  attackDiceValues,  defendDiceValues,  diceDict,  attack,  result,  resultColorsList,  transferButton,  totalTransferTroops,  transferButtonColorsList,  finishTransferTroopsColorsList,  endAttackPhaseButtonColorsList,  fortifyHoldCountries,  fortifyTroops,  finishFortifyButtonColorsList,  increaseFortifyButtonColorsList,  changePageButtonColorsListDict,  directionsScreenPageNumber,  undoButtonColorsList,  gameOverButtonColorsList,  playerCardsDict,  cardsScreen,  numOfCardsSelected,  finishTradeColorsList,  lftTradeButtonColorsList,  rtTradeButtonColorsList,  tradePopup):
    surface.fill(WHITE)
    
    #start screen
    if startScreen and not directionsScreen and not gameOver and not menuScreen and not playersScreen:
        #blits the background image if the start screen should be displayed
        surface.blit(START_IMAGE, BACKGROUND_RECT)
        
        #displays the start,  directions,  and exit buttons onto the screen
        showMessage('START',  25,  .86*w,  .7*h,  startScreenStartColors[0],  startScreenStartColors[-1])
        showMessage('DIRECTIONS',  25,  .86*w,  .8*h,  directionsColors[0], directionsColors[-1])
        showMessage('EXIT',  25,  .86*w,  .9*h,  exitColors[0], exitColors[-1])
    
    #directions screen
    elif directionsScreen and not gameOver and not startScreen and not menuScreen and not playersScreen:
        surface.blit(DIRECTIONS_IMAGE, BACKGROUND_RECT)
        showMessage('BACK',  25,  .1*w,  .9*h,  directionsScreenBackColors[0],  directionsScreenBackColors[-1])
        showMessage('START',  25,  .9*w,  .9*h,  directionsScreenStartColors[0],  directionsScreenStartColors[-1])
        showMessage('MENU',  25,  .5*w,  .9*h,  directionsScreenMenuColors[0],  directionsScreenMenuColors[-1])
        
        if directionsScreenPageNumber == 1:
            #introduction
            showMessage('introduction'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')  
            blit_text('In the classic World Domination RISK game of military strategy,  you are battling to conquer the world. To win,  you must launch daring attacks,  defend yourself on all fronts,  and sweep across vast continents with boldness and cunning. But remember,  the dangers,  as well as the rewards,  are high. Just when the world is within your grasp,  your opponent might strike and take it all away!',  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 2:
            showMessage('game board'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')
            blit_text("The game board is a map of 6 continents divided into 42 territories. Each continent is a different color and contains from 1 to 4 troops.",  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 3:
            showMessage('object of the game'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')
            blit_text("The object of the game is to conquer the world by occupying every territory on the board,  thus eliminating all your opponents.",  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 4:
            showMessage('Gameplay'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')
            blit_text("On your turn,  try to capture territories by defeating armies. But be careful: Winning battles will depend on careful planning,  quick decisions and bold moves. You will have to place your forces wisely,  attack at just the right time and fortify your defenses against all enemies.\nEach of your turns consists of four steps,  in this order: \n1. Trading in troops. \n2. Getting and placing new armies \n3. Attacking,  if you choose to,  by rolling the dice \n4. Fortifying your position.",  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 5:
            showMessage('continents'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')
            blit_text("At the beginning of your turn you will receive armies for each continent you control. (To control a continent,  you must occupy all its territories at the start of your turn.)",  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 6:
            showMessage('attacking part 1'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')            
            blit_text("The object of an attack is to capture a territory by defeating all the opposing armies already on it. The battle is fought by a roll of the dice. Study the board. Do you want to attack?",  (.05*w, .1*h),  BLACK,  WHITE)
        elif directionsScreenPageNumber == 7:
            showMessage('attacking part 2'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                        
            blit_text('If you choose to attack,  you must follow these rules: You may only attack a territory that is adjacent (touching) to one of your own,  or connected to it by a dashed line. Examples: Greenland may attack the Northwest Territory,  Ontario,  Quebec and Iceland. North Africa may attack Egypt,  Western Europe and Brazil. At the western and eastern edges of the board,  Alaska is considered adjacent to,  and may attack,  Kamchatka. You must always have at least two armies in the territory you are attacking from. You may continue attacking one territory until you have eliminated all armies on it,  or you may shift your attack from one territory to another,  attacking each as often as you like and attacking as many territories as you like during one turn.',  (.05*w, .1*h), BLACK, WHITE,  'Arial', 20)
        elif directionsScreenPageNumber == 8:
            showMessage('Capturing territories'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                        
            blit_text('As soon as you defeat the last opposing army on a territory,  you capture that territory and must occupy it immediately. To do so,  move in as many territories as you want as long as they add up to the total number of troops that the territory had before. Remember: In most cases,  moving as many armies as you can to the front is advantageous,  because armies left behind can not help you when you are attacking. Also remember you must always leave at least one army behind on the territory you attacked from. During the game,  every territory must always be occupied by at least one army. You may end your attack(s) at any time.',  (.05*w, .1*h), BLACK, WHITE)
        elif directionsScreenPageNumber == 9:
            showMessage('fortifying'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                        
            blit_text('No matter what you have done on your turn,  you may,  if you wish,  end your turn by fortifying your position. You are not required to win a battle or even to try an attack to do so. Some players refer to this as the free move. To fortify your position,  move as many armies as you would like from one (and only one) of your territories into one (and only one) of your adjacent territories. Remember to move troops towards borders where they can help in an attack! In moving your armies from one territory to another,  you must leave at least one army behind.',  (.05*w, .1*h), BLACK, WHITE)
        elif directionsScreenPageNumber == 10:
            showMessage('Tips'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            blit_text("Keep 3 strategy hints in mind as you play: add armies,  fortify,  and conquer whole continents: You will earn more armies that way. Watch your enemies: If they are building up forces on adjacent territories or continents,  they may be planning an attack. Beware! Fortify borders adjacent to enemy territories for better defense if a neighbor decides to attack you.",  (.05*w,  .1*h),  BLACK,  WHITE,  font = 'Arial')
        elif directionsScreenPageNumber == 11:
            showMessage('Player Handover Screen'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(PLAYER_HANDOVER_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('The image displayed above is an image of the Player Handover Screen. The player that is next is highlited in Red with the arrow pointing to their box. Each of the player boxes are color coded to colors that each player picked at the beginning of the game. Under the Contienents text,  it contains information about how many continents each player holds. Under the Territories text,  the number of territories each player controls is displayed. Under the Troops text,  it contains the number of troops that each player has. The NEXT button in the bottom right corner will continue the game. The HELP button takes the player back to the Directions.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 14)
        elif directionsScreenPageNumber == 12:
            showMessage('Trade Cards Popup'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(TRADE_CARDS_POPUP_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('This is the popup that will show up after you select NEXT from the Player Handover Screen. This popup describes how to trade cards. When you are ready to move on,  select the CONTINUE button.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 20)
        elif directionsScreenPageNumber == 13:
            showMessage('Trade Cards Screen'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(TRADE_CARDS_SCREEN_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('This screen contains the cards that you may trade in for extra troops. You obtain cards by conquering at least one territory during your turn. Select the < at the bottom of the screen to decrease the number of cards that are selected. Select the > at the bottom of the screen to increase the number of cards that are selected. When you are ready to trade in your cards for bonus troops,  select the TRADE 0 STARS FOR 0 TROOPS button.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)  
        elif directionsScreenPageNumber == 14:
            showMessage('Draft Troops Popup'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(DRAFT_POPUP_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('This popup appears after you have selected the TRADE 0 STARS FOR 0 TROOPS button. It lists the number of troops that you have recieved from continents,  territories,  and cards. It also displays the total number of troops that you are allowed to draft. Select CONTINUE when you are ready to move on.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)
        elif directionsScreenPageNumber == 15:
            showMessage('Draft Troops Screen'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(DRAFT_SCREEN_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('During the Draft Phase,  add troops to a territory by moving your mouse over it and clicking the left mouse button. This will give the territory that you are selecting another troop. The total number of troops that still need to be drafted are posted at the bottom of the screen. When there is no more troops left to draft,  the game will automatically move to the Attack Phase.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17) 
        elif directionsScreenPageNumber == 16:
            showMessage('Attack Popup'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(ATTACK_POPUP_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('The Attack Phase Popup appears after you have finished drafting troops in the draft phase. It contains information about what to do during the draft phase. When you are finished with the Attack Phase Popup,  select CONTINUE.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)   
        elif directionsScreenPageNumber == 17:
            showMessage('Attack Phase'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(ATTACK_PHASE_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('During the attack phase,  you may attack as many territories as you would like,  but you are not required to conquer any territories. During the attack phase,  you must first select one of your own territories that you would like to attack from that has more than 1 troop. After that,  select an enemy territory to attack. The two territories will be shown in the bottom left corner. When you are ready to attack,  select ATTACK. After you have attacked,  you must select the WON or LOST button in order to attack again. When you are finished attacking,  select the END ATTACK PHASE at the bottom of the screen. If you accidentally selected a territory,  then you may select the UNDO button located at the bottom of the screen to unselect the last territory.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 13)   
        elif directionsScreenPageNumber == 18:
            showMessage('Attack Phase Transfer Troops'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(ATTACK_PHASE_TRANSFER_TROOPS_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('If you have conquered a territory that you have attacked,  you will be asked to transfer troops to that new territory. You may select the > button to transfer more troops. When you are ready to finish the transfer,  select the TRANSFER TROOPS button that is located at the bottom of the screen. The territories that you are using to transfer are located at the bottom left corner of the screen.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)
        elif directionsScreenPageNumber == 19:
            showMessage('Fortify Popup'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(FORTIFY_POPUP_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('The Fortify Popup contains information about how to fortify your territories. When you are finished,  select the CONTINUE button.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)   
        elif directionsScreenPageNumber == 20:
            showMessage('Fortify Phase'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(FORTIFY_PHASE_IMAGE,  DIRECTIONS_IMAGES_RECT)
            blit_text('In the fortify phase,  you may move troops from one adjacent territory to another. You may only fortify one territory,  however you are not required to fortify. The selected territories are highlighted in green and placed in the bottom left corner of the screen. Select the > button to increase the amount of troops that you want to transfer. Select the FORTIFY TROOPS button when you are finished. If you want to deselect a territory,  you may press the UNDO button.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)     
        elif directionsScreenPageNumber == 21:
            showMessage('Notes'.upper(),  35,  .5*w,  .05*h,  WHITE,  BLACK,  font = 'Consolas')                                    
            surface.blit(NOTE_IMAGES,  DIRECTIONS_IMAGES_RECT)
            blit_text('At the top of the screen,  the current phase is in White text. The current player turn is in the top left corner of the screen highlighted by their color that they picked at the start of the game. The number of troops for the current player is located to the right of the tank icon in the top right corner of the screen. The total number of extra troops that you have not used is located in the top right hand corner of the screen next to the star icon.',  (.05*w,  .55*h),  BLACK,  WHITE,  'Arial', 17)             
            
        
        
        #next button
        showMessage('NEXT PAGE',  25,  .7*w,  .9*h,  changePageButtonColorsListDict['next'][0], changePageButtonColorsListDict['next'][-1])
        
        #back button
        showMessage('LAST PAGE',  25,  .3*w,  .9*h,  changePageButtonColorsListDict['last'][0], changePageButtonColorsListDict['last'][-1])
        
        
    #menuScreen
    elif menuScreen and not startScreen and not directionsScreen and not playersScreen:
        surface.blit(MENU_IMAGE, BACKGROUND_RECT)
        showMessage('RISK MENU',  50,  .2*w,  .1*h,  WHITE, LT_BLUE)     #title
        
        #game type
        showMessage('GAME TYPE',  30,  .15*w,  .2*h,  WHITE,  LT_BLUE)   #title
        showMessage(' '+str(currentGameType)+' ',  20,  .5*w,  .265*h,  BLACK, LT_BLUE)
        showMessage(' '*5+'>'+' '*5,  20,  .8*w,  .265*h,  gameTypeRtArrowColorsList[0],  gameTypeRtArrowColorsList[-1])
        showMessage(' '*5+'<'+' '*5,  20,  .2*w,  .265*h,  gameTypeLftArrowColorsList[0],  gameTypeLftArrowColorsList[-1])       
        
        #territory allocations
        showMessage('territory allocations'.upper(),  30,  .32*w,  (.265+.065)*h,  WHITE,  LT_BLUE)  #title
        showMessage(' '*5+str(territoryAlocationsOption)+' '*5,  20,  .5*w,  (.265+.065*2)*h,  BLACK, LT_BLUE)
        showMessage(' '*5+'>'+' '*5,  20,  .8*w,  (.265+.065*2)*h,  territoryAlocationsRtArrowColorsList[0],  territoryAlocationsRtArrowColorsList[-1])
        showMessage(' '*5+'<'+' '*5,  20,  .2*w,  (.265+.065*2)*h,  territoryAlocationsLftArrrowColorsList[0],  territoryAlocationsLftArrrowColorsList[-1])        
        
        #ceasefire card
        showMessage('ceasefire card'.upper(),  30,  .22*w,  (.265+.065*3)*h,  WHITE,  LT_BLUE)   #title
        showMessage(' '*7+str(ceasefireCardOption)+' '*7,  20,  .5*w,  (.265+.065*4)*h,  BLACK, LT_BLUE)
        showMessage(' '*5+'>'+' '*5,  20,  .8*w,  (.265+.065*4)*h,  ceasefireCardRtArrowColorsList[0],  ceasefireCardRtArrowColorsList[-1])
        showMessage(' '*5+'<'+' '*5,  20,  .2*w,  (.265+.065*4)*h,  ceasefireCardLftArrowColorsList[0],  ceasefireCardLftArrowColorsList[-1])    
        
        #information box and text
        pygame.draw.rect(surface, LT_BLUE, (0, .6*h, w, h), 0)
        topLeftShowMessage(MENU_OPTIONS_DICT.get(currentGameType,  'Error: This game mode is currently unavailable.'),  13,  .025*w,  .65*h,  WHITE)
        topLeftShowMessage(MENU_OPTIONS_DICT.get(territoryAlocationsOption,  'Error: This feature is currently unavailable.'),  13,  .025*w,  .75*h,  WHITE)
        topLeftShowMessage(MENU_OPTIONS_DICT[ceasefireCardOption],  13,  .025*w,  .85*h,  WHITE)  
        
        #next button
        showMessage('NEXT',  25,  .9*w,  .95*h,  menuScreenNextColorsList[0],  menuScreenNextColorsList[-1])
        
        #back button
        showMessage('BACK',  25,  .1*w,  .95*h,  menuScreenBackColorsList[0],  menuScreenBackColorsList[-1])
        
        #directions button
        showMessage('DIRECTIONS',  25,  .5*w,  .95*h,  menuScreenDirectionsColorsList[0], menuScreenDirectionsColorsList[-1])
        
    #playersScreen
    elif playersScreen and not startScreen and not directionsScreen and not menuScreen:
        #background
        surface.blit(PLAYERS_SCREEN_IMAGE, BACKGROUND_RECT)
        showMessage('PLAYER SETUP',  50,  .275*w,  .1*h,  WHITE, LT_BLUE)     #main title
        
        #player titles
        for i in range(1, 6):
            #player titles
            showMessage('PLAYER '+str(i),  30,  .15*w,  (.2+((.065*2)*(i-1)))*h,  WHITE,  LT_BLUE)   #title
            
            #player info
            showMessage(' '*5+str(playerOptionsDict[i])+' '*5,  20,  .5*w,  (.265+(.13*(i-1)))*h,  BLACK,  LT_BLUE)
        
        #players arrows
        for i in range(1, 6):
            showMessage(' '*5+'>'+' '*5,  20,  .8*w,  (.265+(.13*(i-1)))*h,  playersLftRtButtonRectAndColorsDict['player_right'+str(i)][-1][0],  playersLftRtButtonRectAndColorsDict['player_right'+str(i)][-1][-1])
            showMessage(' '*5+'<'+' '*5,  20,  .2*w,  (.265+(.13*(i-1)))*h,  playersLftRtButtonRectAndColorsDict['player_left'+str(i)][-1][0], playersLftRtButtonRectAndColorsDict['player_left'+str(i)][-1][-1]) 
            
        #player colors
        for i in range(1, 6):
            pygame.draw.rect(surface, COLORS_LIST[i], (.95*w, (.247+(.13*(i-1)))*h, .035*w, .035*w))
        
        #bottom box
        pygame.draw.rect(surface, LT_BLUE, (0, .85*h, w, h), 0)         
        
        #next button
        showMessage('START',  25,  .90*w,  .95*h,  playersScreenButtonsRectAndColorsDict['start'][-1][0],  playersScreenButtonsRectAndColorsDict['start'][-1][-1])
        
        #back button
        showMessage('BACK',  25,  .1*w,  .95*h,  playersScreenButtonsRectAndColorsDict['back'][-1][0],  playersScreenButtonsRectAndColorsDict['back'][-1][-1])
        
        #bottom messages
        if playersScreenErrorMessage:
            showMessage('You do not have enough players. Please select more.',  13,  .5*w,  .875*h,  WHITE)
        else:
            showMessage('Please turn on the players with your favorite colors.',  13,  .5*w,  .875*h,  WHITE)
    
    #game in play screen
    elif gameInPlayScreen and not directionsScreen and not menuScreen and not startScreen and not playersScreen and not nextPlayerScreen and not cardsScreen:
        surface.blit(GAME_IN_PLAY_BACKGROUND,  BACKGROUND_RECT)
        blitAllImages(mouseOverCountry,  countryInfoDict,  currentPhase,  draftTroops,  holdCountries,  fortifyHoldCountries)     #blits the country images onto the screen   
        
        numTerritoryBlitX=.025*w
        numTerritoryBlitY=.275*h
        for i in range(numOfPlayers):
            showMessage(' '+str(len(getPlayerTerritoryNames(i+1, countryInfoDict, allowedColors)))+' ', 15, numTerritoryBlitX, numTerritoryBlitY, BLACK, STR_COLOR_TO_COLOR_DICT[allowedColors[i]])
            numTerritoryBlitY+=.05*h
        
        #player turn
        showMessage('PLAYER '+str(playerTurn),  20,  .1*w,  .05*h,  BLACK,  STR_COLOR_TO_COLOR_DICT[allowedColors[playerTurn-1]])
        
        #phase
        showMessage(' '*2+'DRAFT'+' '*2,  20,  .35*w,  .05*h,  currentPhaseDict['draft'],  YELLOW)
        showMessage(' '*2+'ATTACK'+' '*2,  20,  .5*w,  .05*h,  currentPhaseDict['attack'], RISK_RED)
        showMessage(' '*2+'FORTIFY'+' '*2,  20,  .675*w,  .05*h,  currentPhaseDict['fortify'], DK_GREEN)
        
        #number of troops icon and text
        pygame.draw.rect(surface,  ORANGE, (.775*w, .03*h, .125*w, .045*h))     #draws the background rect
        surface.blit(TANK_ICON, TANK_RECT)      #blits the tank image
        showMessage(str(getNumTroops(playerTurn,  countryInfoDict,  allowedColors)),  20,  .875*w,  .05*h,  BLACK,  ORANGE) #number of troops txt
        
        #stars icon and text
        pygame.draw.rect(surface, LT_GREEN, (.9*w, .03*h, .125*w, .045*h))
        surface.blit(STAR_ICON, STAR_RECT)
        showMessage(str(getStarBonus(playerCardsDict[playerTurn])),  20,  .975*w,  .05*h,  BLACK,  LT_GREEN)
        
        
        if draftPopup:
            #draws the background rect
            pygame.draw.rect(surface,  YELLOW,  (.25*w,  .25*h,  .5*w,  .5*h))
            
            #draws the titles
            showMessage('PLAYER '+str(playerTurn),  20,  .5*w,  .3*h,  BLACK)
            topLeftShowMessage('FROM TERRITORIES:',  15,  .275*w,  .35*h,  BLACK)
            topLeftShowMessage('FROM CONTIENT BONUS:',  15,  .275*w,  .4*h,  BLACK)
            topLeftShowMessage('TRADE IN BONUS:',  15,  .275*w,  .45*h,  BLACK)
            topLeftShowMessage('_'*34,  15,  .275*w,  .5*h,  BLACK)        
            topLeftShowMessage('TOTAL:',  15,  .275*w,  .55*h,  BLACK)
            
            #draws the values
            topLeftShowMessage(str(getNumOfCountryColors(numOfPlayers,  allowedColors,  countryInfoDict)[playerTurn-1]//3),  15,  .7*w,  .35*h,  BLACK)
            topLeftShowMessage(str(getContientBonus(playerTurn,  countryInfoDict,  allowedColors)),  15,  .7*w,  .4*h,  BLACK)
            topLeftShowMessage(str(getStarBonus(numOfCardsSelected)),  15,  .7*w,  .45*h,  BLACK)
            topLeftShowMessage(str(draftTroops),  15,  .7*w,  .55*h,  BLACK)
            
            #draft button
            showMessage('CONTINUE',  25,  .5*w,  .7*h,  popupButtonColorsList[0], popupButtonColorsList[-1])
        elif attackPopup:
            #draws the background rect
            pygame.draw.rect(surface,  RED,  (.25*w,  .25*h,  .5*w,  .5*h))
            
            #displays the main message
            showMessage('ATTACK PHASE',  20,  .5*w,  .3*h,  BLACK)
            
            #displays the description
            topLeftShowMessage('First: Select your own territory',  15,  .275*w,  .35*h,  BLACK)
            topLeftShowMessage("Then: Select an enemy territory",  15,  .275*w,  .4*h,  BLACK)
            topLeftShowMessage("Finally: Select ATTACK",  15,  .275*w,  .45*h,  BLACK)
            topLeftShowMessage('Finished: Select END ATTACK PHASE',  15,  .275*w,  .5*h,  BLACK)
            
            #continue button
            showMessage('CONTINUE',  25,  .5*w,  .7*h,  popupButtonColorsList[0], popupButtonColorsList[-1])            
        elif fortifyPopup:
            #draws the background rect
            pygame.draw.rect(surface,  GREEN,  (.25*w,  .25*h,  .5*w,  .5*h))
            
            #displays the main message
            showMessage('FORTIFY PHASE',  20,  .5*w,  .3*h,  BLACK)
            
            #displays the description
            topLeftShowMessage('Fist: Select your own territory',  15,  .275*w,  .35*h,  BLACK)
            topLeftShowMessage("Then: Select adjacent own territory",  15,  .275*w,  .4*h,  BLACK)
            topLeftShowMessage('Third: Adjust troops',  15,  .275*w,  .45*h,  BLACK)
            topLeftShowMessage('Finally: Select FORTIFY TROOPS',  15,  .275*w,  .5*h,  BLACK)
            
            #continue button
            showMessage('CONTINUE',  25,  .5*w,  .7*h,  popupButtonColorsList[0], popupButtonColorsList[-1])                
            
        elif currentPhase == 'draft':
            showMessage('DRAFT TROOPS REMAINING: '+str(draftTroops),  20,  .5*w, .95*h,  BLACK,  WHITE)     #blits the number of draftTroops that are remaining
        elif currentPhase == 'attack' and len(holdCountries) == 2:
            if not attack and not transferButton:
                #attack button
                showMessage('ATTACK!',  25,  .5*w,  .95*h,  attackButtonColorsList[0],  attackButtonColorsList[-1])
            elif attack and transferButton:
                #button
                showMessage(' > ',  25,  .775*w,  .95*h,  transferButtonColorsList[0],  transferButtonColorsList[-1])
                
                #message
                showMessage('Transfer Troops: '+str(totalTransferTroops),  25,  .5*w,  .95*h,  finishTransferTroopsColorsList[0],  finishTransferTroopsColorsList[-1])                
            elif attack and not transferButton:
                #need to work on main first before I can blit anything onto the screen
                showMessage(result,  25,  .5*w,  .95*h,  resultColorsList[0],  resultColorsList[-1])
        
                #attack dice
                attackDiceRect = pygame.Rect(.2*w,  .925*h,  .05*w,  .05*h)
                for i in range(len(attackDiceValues)):
                    diceDict[attackDiceValues[i]] = pygame.transform.scale(diceDict[attackDiceValues[i]], (attackDiceRect.width,  attackDiceRect.height))
                    surface.blit(diceDict[attackDiceValues[i]],  attackDiceRect)
                    pygame.draw.rect(surface, BLACK, attackDiceRect, 2)                    
                    attackDiceRect.centerx += .05*w
                    
                #defend dice
                defendDiceRect = pygame.Rect(.65*w, .925*h,  .05*w,  .05*h)
                for i in range(len(defendDiceValues)):
                    diceDict[defendDiceValues[i]] = pygame.transform.scale(diceDict[defendDiceValues[i]], (defendDiceRect.width,  defendDiceRect.height))
                    surface.blit(diceDict[defendDiceValues[i]],  defendDiceRect)
                    pygame.draw.rect(surface, BLACK, defendDiceRect, 2)
                    defendDiceRect.centerx += .05*w      
        elif currentPhase == 'attack' and len(holdCountries) == 0:
            showMessage('END ATTACK PHASE',  25,  .5*w,  .95*h,  endAttackPhaseButtonColorsList[0],  endAttackPhaseButtonColorsList[-1])
        elif currentPhase == 'fortify' and len(fortifyHoldCountries) == 2:
            showMessage(' > ',  25,  .775*w,  .95*h,  increaseFortifyButtonColorsList[0],  increaseFortifyButtonColorsList[-1])
            showMessage('FORTIFY TROOPS: '+str(fortifyTroops)+' ',  25,  .5*w,  .95*h,  finishFortifyButtonColorsList[0],  finishFortifyButtonColorsList[-1]) 
        elif currentPhase == 'fortify' and len(fortifyHoldCountries) == 0:
            showMessage('END FORTIFY PHASE',  25,  .5*w,  .95*h,  endAttackPhaseButtonColorsList[0],  endAttackPhaseButtonColorsList[-1])
        
        if (currentPhase == 'attack' and (len(holdCountries) == 1 or len(holdCountries) == 2) and not attack) or (currentPhase == 'fortify' and (len(fortifyHoldCountries) == 1 or len(fortifyHoldCountries) == 2)):
            showMessage('UNDO',  25,  .9*w,  .95*h,  undoButtonColorsList[0], undoButtonColorsList[-1])
            
    
    #draws the screen for the nextPlayerScreen
    elif nextPlayerScreen and not gameInPlayScreen and not startScreen and not directionsScreen and not playersScreen:
        #fills the background
        surface.fill(LT_BLUE)
        
        #blits the screen title
        showMessage('PLAYER HANDOVER:',  40,  .3*w,  .05*h,  BLACK,  WHITE)
        
        #player turn background rect
        pygame.draw.rect(surface, RED, (.01*w,  (.1+(.18*(playerTurn-1)))*h,  .88*w,  .2*h))
        
        #player titles
        for i in range(1, numOfPlayers+1):
            nPSMessagesHeight = .18*(i-1)
            
            #outside rect
            pygame.draw.rect(surface,  STR_COLOR_TO_COLOR_DICT[allowedColors[i-1]],  (.1*w,  (.12+nPSMessagesHeight)*h, .75*w, .15*h))                       
            
            #player title
            showMessage('PLAYER '+str(i),  25,  .2*w,  (.15+nPSMessagesHeight)*h,  BLACK)   #title
        
            #contient data                    
            showMessage('CONTINENTS',  20,  .25*w,  (.21+nPSMessagesHeight)*h,  BLACK)                    
            showMessage(str(getNumContinent(i,  countryInfoDict,  allowedColors))+' / 6',  15,  .25*w,  (.25+nPSMessagesHeight)*h,  BLACK)                
        
            #territory data
            showMessage('TERRITORIES',  20,  .5*w,  (.21+nPSMessagesHeight)*h,  BLACK)
            showMessage(str(getNumOfCountryColors(numOfPlayers,  allowedColors,  countryInfoDict)[i-1]),  15,  .5*w,  (.25+nPSMessagesHeight)*h,  BLACK)
            
            #troop data
            showMessage('TROOPS',  20,  .75*w,  (.21+nPSMessagesHeight)*h,  BLACK)
            showMessage(str(getNumTroops(i,  countryInfoDict,  allowedColors)), 15,  .75*w, (.25+nPSMessagesHeight)*h, BLACK)  
        
        #blits the arrow icon onto the screen that shows whose turn it is
        tempRect = pygame.Rect(.015*w, (.15+(.18*(playerTurn-1)))*h,  .075*w, .075*w)
        arrowIcon = pygame.transform.scale(arrowIcon, (tempRect.width, tempRect.height))
        surface.blit(arrowIcon,  tempRect) 
        
        #next button
        showMessage('NEXT',  25,  .925*w,  .95*h,  nextPlayerScreenNextButtonColorsList[0],  nextPlayerScreenNextButtonColorsList[-1])
        
        #help button
        showMessage('HELP',  25,  .925*w,  .85*h,  nextPlayerScreenHelpButtonColorsList[0], nextPlayerScreenHelpButtonColorsList[-1])
    #cardsScreen
    elif cardsScreen and not gameInPlayScreen and not startScreen and not directionsScreen and not nextPlayerScreen:
        #blit the background image
        surface.fill(LT_BLUE)
        
        #blit the title
        showMessage('PLAYER '+str(playerTurn)+' CARDS',  30,  .5*w,  .05*h,  BLACK)
        
        #blits the cards
        for i in range(playerCardsDict[playerTurn]):
            blitX = (.1+(.175*i))*w
            blitY = .15*h
            
            if i >= 5:
                blitY += .4*h
                blitX = (.1+(.175*(i-5)))*w

            pygame.draw.rect(surface,  ORANGE,  (blitX,  blitY, .15*w, .3*h), 0)
            pygame.draw.rect(surface,  BLACK,  (blitX,  blitY, .15*w, .3*h), 6)
            
            surface.blit(CARDS_STAR_IMAGE,  pygame.Rect(blitX+(.025*w), blitY+(.1*h), .1*w, .1*h))
            
        #blits the check marks
        for i in range(numOfCardsSelected):
            if i<5:
                surface.blit(CHECK_MARK_IMAGE, pygame.Rect(((.1+(.175*i))*w), .15*h, .05*w, .05*h))
            else:
                surface.blit(CHECK_MARK_IMAGE, pygame.Rect(((.1+(.175*(i-5)))*w), .55*h, .05*w, .05*h))
                
        #bottom button
        showMessage('TRADE '+str(numOfCardsSelected)+' STARS FOR '+str(getStarBonus(numOfCardsSelected))+' TROOPS'.upper(),  25,  .5*w,  .95*h,  finishTradeColorsList[0],  finishTradeColorsList[-1])
        showMessage('  <  ',  25,  .1*w,  .95*h,  lftTradeButtonColorsList[0],  lftTradeButtonColorsList[-1])
        showMessage('  >  ',  25,  .9*w,  .95*h,  rtTradeButtonColorsList[0],  rtTradeButtonColorsList[-1])
        
        #displays the trade popup
        if tradePopup:
            #draws the background rect
            pygame.draw.rect(surface,  ORANGE,  (.25*w,  .25*h,  .5*w,  .5*h))
            
            #displays the main message
            showMessage('trade troops'.upper(),  20,  .5*w,  .3*h,  BLACK)
            
            #displays the description
            topLeftShowMessage('Select the > to increase selection',  15,  .275*w,  .35*h,  BLACK)
            topLeftShowMessage("Select the < to decrease selection",  15,  .275*w,  .4*h,  BLACK)
            topLeftShowMessage('Select the bottom button to finish',  15,  .275*w,  .45*h,  BLACK)
            
            #continue button
            showMessage('CONTINUE',  25,  .5*w,  .7*h,  popupButtonColorsList[0], popupButtonColorsList[-1])   
        
        
    
    
    #draws the screen when the game is over
    if gameOver:
        pygame.draw.rect(surface, BLACK, (.25*w, .25*h,  .5*w, .5*h))
        showMessage('GAME OVER',  20,  .5*w,  .3*h,  WHITE)
        showMessage('PLAYER '+str(playerTurn)+' WINS!',  35,  .5*w,  .5*h,  WHITE)
        
        #exit button
        showMessage('EXIT',  25,  .5*w,  .7*h,  gameOverButtonColorsList[0], gameOverButtonColorsList[-1])        
        

#determines whether or not the game is over
def determineGameOver(ceasefireCardOption,  player,  countryInfoDict,  allowedColors):
    if ceasefireCardOption == 'on'.title():
        if len(getPlayerTerritoryNames(player,  countryInfoDict,  allowedColors)) >= 30:
            return True
    else:
        if len(getPlayerTerritoryNames(player,  countryInfoDict,  allowedColors)) == len(countryInfoDict):
            return True
    return False


#gets the star bonus troops
def getStarBonus(numOfCards):
    if numOfCards<2:
        return 0
    elif numOfCards == 2:
        return 2
    elif numOfCards == 3:
        return 4
    elif numOfCards == 4:
        return 7
    elif numOfCards == 5:
        return 10
    elif numOfCards == 6:
        return 13
    elif numOfCards == 7:
        return 17
    elif numOfCards == 8:
        return 21
    elif numOfCards == 9:
        return 25
    elif numOfCards == 10:
        return 30
    
#gets and returns the contient bonus
def getContientBonus(playerNum,  countryInfoDict,  allowedColors):
    continentBonus = 0
    continentNamesList = getContientNames(playerNum,  countryInfoDict,  allowedColors)
    
    for continentName in continentNamesList:
        continentBonus += CONTINENT_BONUS_POINT_DICT[continentName]
    
    return continentBonus
#gets and returns the names of the contients that the certain player has
def getContientNames(playerNum,  countryInfoDict,  allowedColors):
    #intializes the important variables
    continentNamesList = []
    territoryNames = getPlayerTerritoryNames(playerNum,  countryInfoDict,  allowedColors)
    
    #gets a copy of the countries lists
    africaCountries = AFRICA_COUNTRIES.copy()
    asiaCountires = ASIA_COUNTRIES.copy()
    northAmericaCountries = NORTH_AMERICA_COUNTRIES.copy()
    australiaCountries = AUSTRALIA_COUNTRIES.copy()
    europeCountries = EUROPE_COUNTRIES.copy()
    southAmericaCountries = SOUTH_AMERICA_COUNTRIES.copy()
    
    #removes the name of all the countries that the player has
    for name in territoryNames:
        if name in africaCountries:
            africaCountries.remove(name)
        elif name in asiaCountires:
            asiaCountires.remove(name)
        elif name in northAmericaCountries:
            northAmericaCountries.remove(name)
        elif name in australiaCountries:
            australiaCountries.remove(name)
        elif name in europeCountries:
            europeCountries.remove(name)
        elif name in southAmericaCountries:
            southAmericaCountries.remove(name)
    
    #adds the name of the continent to the continentNamesList list if the player has all of the countries in that continent
    if len(africaCountries) == 0:
        continentNamesList.append('africa')
    if len(asiaCountires) == 0:
        continentNamesList.append('asia')
    if len(northAmericaCountries) == 0:
        continentNamesList.append('northAmerica')
    if len(australiaCountries) == 0:
        continentNamesList.append('australia')
    if len(europeCountries) == 0:
        continentNamesList.append('europe')
    if len(southAmericaCountries) == 0:
        continentNamesList.append('southAmerica')
    
    return continentNamesList    

#assigns troops to the countryInfoDict
def assignTroops(countryInfoDict,  numOfPlayers,  allowedColors):
    #finds the total number of troops that each player recieves
    if numOfPlayers == 2:
        totalTroops = 'ERROR - Needs fixing'
    else:
        totalTroops = 35-(5*(numOfPlayers-3))
        
    
    #creates the playerTerritoryNamesList
    playerTerritoryNamesList = []
    
    for i in range(numOfPlayers):
        playerTerritoryNamesList.append(getPlayerTerritoryNames(i+1,  countryInfoDict,  allowedColors))
    
    #sets up the allTroopsList
    allTroopsList = []
    for i in range(numOfPlayers):
        allTroopsList.append([0 for i in range(len(playerTerritoryNamesList[i]))])
    
    #creates the allTroopsList
    for i in range(numOfPlayers):
        #adds a value to each value of the allTroopsList that is between 1 and 3
        for j in range(len(allTroopsList[i])):
            allTroopsList[i][j] = random.randint(1, 3)
        
        total = sum(allTroopsList[i])
        numExtra = total-totalTroops
        
        while numExtra>0:
            index = random.randint(0,  len(allTroopsList[i])-1)
            
            if allTroopsList[i][index]>1:
                allTroopsList[i][index] -= 1
                numExtra -= 1
        while numExtra<0:
            index = random.randint(0,  len(allTroopsList[i])-1)
            
            if numOfPlayers == 5:
                if allTroopsList[i][index]<4:
                    allTroopsList[i][index] += 1
                    numExtra += 1                
            elif allTroopsList[i][index]<3:
                allTroopsList[i][index] += 1
                numExtra += 1
    
    for i in range(numOfPlayers):
        for j in range(len(playerTerritoryNamesList[i])):
            countryInfoDict[playerTerritoryNamesList[i][j]][5] = allTroopsList[i][j]    
    
    return countryInfoDict

#gets and returns the number of countries that the player occupies
def getNumContinent(playerNum,  countryInfoDict, allowedColors):
    #intializes the important variables
    totalContinents = 0
    territoryNames = getPlayerTerritoryNames(playerNum,  countryInfoDict,  allowedColors)
    
    #gets a copy of the countries lists
    africaCountries = AFRICA_COUNTRIES.copy()
    asiaCountires = ASIA_COUNTRIES.copy()
    northAmericaCountries = NORTH_AMERICA_COUNTRIES.copy()
    australiaCountries = AUSTRALIA_COUNTRIES.copy()
    europeCountries = EUROPE_COUNTRIES.copy()
    southAmericaCountries = SOUTH_AMERICA_COUNTRIES.copy()
    
    #removes the name of all the countries that the player has
    for name in territoryNames:
        if name in africaCountries:
            africaCountries.remove(name)
        elif name in asiaCountires:
            asiaCountires.remove(name)
        elif name in northAmericaCountries:
            northAmericaCountries.remove(name)
        elif name in australiaCountries:
            australiaCountries.remove(name)
        elif name in europeCountries:
            europeCountries.remove(name)
        elif name in southAmericaCountries:
            southAmericaCountries.remove(name)
    
    #adds 1 to the totalContinents if there is nothing left in the contient that the player does not have
    if len(africaCountries) == 0:
        totalContinents += 1
    if len(asiaCountires) == 0:
        totalContinents += 1
    if len(northAmericaCountries) == 0:
        totalContinents += 1
    if len(australiaCountries) == 0:
        totalContinents += 1
    if len(europeCountries) == 0:
        totalContinents += 1
    if len(southAmericaCountries) == 0:
        totalContinents += 1
    
    return totalContinents

#gets and returns a list of all the names of the territories that the player occupies
def getPlayerTerritoryNames(playerNum,  countryInfoDict,  allowedColors):
    territoryNamesList = []
    
    for i in range(len(countryInfoDict)):
        for j in range(len(allowedColors)):
            if countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][4] == allowedColors[playerNum-1]:
                if COUNTRY_INFO_KEYS_LIST[i] not in territoryNamesList:
                    territoryNamesList.append(COUNTRY_INFO_KEYS_LIST[i])
                
    return territoryNamesList


#gets and returns the total number of troops for the certain player
def getNumTroops(playerNum,  countryInfoDict,  allowedColors):
    territoryNamesList = getPlayerTerritoryNames(playerNum,  countryInfoDict,  allowedColors)
    numOfTroops = 0
    
    for i in range(len(territoryNamesList)):
        numOfTroops += countryInfoDict[territoryNamesList[i]][5]
        
    return numOfTroops

def moveText(dictName,  textRect):
    if dictName == 'alaska':
        textRect.centery -= .02*h
    elif dictName == 'northwestTerritory':
        textRect.centery += .025*h
    elif dictName == 'argentina':
        textRect.centerx -= .0175*w
        textRect.centery -= .01*h
    elif dictName == 'madagascar':
        textRect.centerx += .0015*w
    elif dictName == 'indonesia':
        textRect.centerx += .0125*w
    elif dictName == 'easternAustralia':
        textRect.centerx += .02*w
    elif dictName == 'cluster':
        textRect.centerx += .015*w
        textRect.centery += .01*h
    elif dictName == 'mongolia':
        textRect.centery += .02*h
    elif dictName == 'japan':
        textRect.centerx += .015*w
    elif dictName == 'kamataka':
        textRect.centery -= .06*h
        textRect.centerx += .01*w
    elif dictName == 'peru':
        textRect.centerx -= .005*w
    elif dictName == 'centralAmerica':
        textRect.centery -= .01*h
    elif dictName == 'westernEurope':
        textRect.centerx += .01*w
    elif dictName == 'southernEurope':
        textRect.centery -= .01*h
    elif dictName == 'iceland':
        textRect.centery += .005*h
    
    return textRect

#blits all of the country images onto the screen
def blitAllImages(mouseOverCountry,  countryInfoDict,  currentPhase,  draftTroops,  holdCountries,  fortifyHoldCountries):
    highlightedCountry = []
    
    for i in range(len(COUNTRY_INFO_KEYS_LIST)):
        dictName = COUNTRY_INFO_KEYS_LIST[i]
        countryDimensions = COUNTRY_INFO_DICT.get(dictName,  'Error')        
        name = 'country_images/'+str(dictName)+str(countryDimensions[4])+'.png'
        
        countryImage = pygame.image.load(name).convert_alpha()
        countryRect = pygame.Rect(countryDimensions[0], countryDimensions[1], countryDimensions[2]*SF, countryDimensions[3]*SF)     
        
        
        if COUNTRY_INFO_KEYS_LIST[i] == mouseOverCountry or COUNTRY_INFO_KEYS_LIST[i] in holdCountries or COUNTRY_INFO_KEYS_LIST[i] in fortifyHoldCountries:
            countryRect.width += 20*SF
            countryRect.height += 20*SF
            highlightedCountry.append([countryImage,  countryRect,  COUNTRY_INFO_KEYS_LIST[i]])
        
        
        
        countryImage = pygame.transform.scale(countryImage, (countryRect.width, countryRect.height))
        
        surface.blit(countryImage, countryRect)
        
        textRect = moveText(dictName,  countryRect.copy())

        showMessage(str(countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][5]),  20,  textRect.centerx,  textRect.centery,  BLACK,  None,  'Trebuchet MS')    #blits the number of troops on each territory
        
    #blits the highlighted country
    if len(highlightedCountry) != 0:
        for i in range(len(highlightedCountry)):  
            highlightedCountry[i][0] = pygame.transform.scale(highlightedCountry[i][0], (highlightedCountry[i][1].width,  highlightedCountry[i][1].height))
            surface.blit(highlightedCountry[i][0], highlightedCountry[i][1])
            
            textRect = moveText(highlightedCountry[i][2],  highlightedCountry[i][1].copy())
            
            showMessage(str(countryInfoDict[highlightedCountry[i][-1]][5]),  20,  textRect.centerx,  textRect.centery,  BLACK,  None,  'Trebuchet MS') #blits the number of troops on each territory
            
            if highlightedCountry[i][2] in holdCountries:
                pygame.draw.rect(surface,  RED,  (highlightedCountry[i][1].topleft[0],  highlightedCountry[i][1].topleft[-1],  highlightedCountry[i][1].width,  highlightedCountry[i][1].height), 6)

                if highlightedCountry[i][2] == holdCountries[0]:
                    tempRect = pygame.Rect(.025*w, (.8-.25)*h,  .15*w, .15*h)
                    showMessage('FROM:',  20,  tempRect.topleft[0]+(.5*tempRect.width),  tempRect.topleft[-1]-(.025*h),  BLACK,  WHITE)
                else:
                    tempRect = pygame.Rect(.025*w, .8*h,  .15*w, .15*h)  
                    showMessage('TO:',  20,  tempRect.topleft[0]+(.5*tempRect.width),  tempRect.topleft[-1]-(.025*h),  BLACK,  WHITE)                     
                
                tempImage = highlightedCountry[i][0].copy()
                tempImage = pygame.transform.scale(tempImage,  (tempRect.width,  tempRect.height))
                surface.blit(tempImage, tempRect)
                 
                showMessage(str(countryInfoDict[highlightedCountry[i][-1]][5]),  20,  tempRect.centerx,  tempRect.centery,  BLACK,  None,  'Trebuchet MS') #blits the number of troops on each territory
            elif highlightedCountry[i][2] in fortifyHoldCountries:
                pygame.draw.rect(surface,  GREEN,  (highlightedCountry[i][1].topleft[0],  highlightedCountry[i][1].topleft[-1],  highlightedCountry[i][1].width,  highlightedCountry[i][1].height), 6)
                
                if highlightedCountry[i][2] == fortifyHoldCountries[0]:
                    tempRect = pygame.Rect(.025*w, (.8-.25)*h,  .15*w, .15*h)
                    showMessage('FROM:',  20,  tempRect.topleft[0]+(.5*tempRect.width),  tempRect.topleft[-1]-(.025*h),  BLACK,  WHITE)
                else:
                    tempRect = pygame.Rect(.025*w, .8*h,  .15*w, .15*h)  
                    showMessage('TO:',  20,  tempRect.topleft[0]+(.5*tempRect.width),  tempRect.topleft[-1]-(.025*h),  BLACK,  WHITE)                     
                
                tempImage = highlightedCountry[i][0].copy()
                tempImage = pygame.transform.scale(tempImage,  (tempRect.width,  tempRect.height))
                surface.blit(tempImage, tempRect)
                showMessage(str(countryInfoDict[highlightedCountry[i][-1]][5]),  20,  tempRect.centerx,  tempRect.centery,  BLACK,  None,  'Trebuchet MS') #blits the number of troops on each territory                
    else:
        highlightedCountry = []
    
    
    
    

#gets and returns a list of how many countries that each player has
def getNumOfCountryColors(numOfPlayers, allowedColors, countryInfoDict):
    numOfColorCountriesList = [0]*numOfPlayers

    for i in range(len(countryInfoDict)):
        for j in range(len(allowedColors)):
            if countryInfoDict[COUNTRY_INFO_KEYS_LIST[i]][4] == allowedColors[j]:
                numOfColorCountriesList[j] += 1  
                
    return numOfColorCountriesList

#blits a big line of text seperated into lines
def blit_text(text,  pos,  color = WHITE, bg = None, font = 'Arial', size = 22):
    font = pygame.font.SysFont(font, int(size * SF), 1)
    words  =  [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space  =  font.size(' ')[0]  # The width of a space.
    max_width,  max_height  =  surface.get_size()
    max_width -= w/28
    max_height -= h/1.5
    x,  y  =  pos
    
    pygame.draw.rect(surface, bg,  (x, y, (.975*w)-x, (.86*h)-y), 0)
    
    for line in words:
        for word in line:
            word_surface  =  font.render(word,  0,  color, bg)
            word_width,  word_height  =  word_surface.get_size()
            if x + word_width  >=  max_width:
                x  =  pos[0]  # Reset the x.
                y  +=  word_height  # Start on new row.
            surface.blit(word_surface,  (x,  y))
            x  +=  word_width + space
        x  =  pos[0]  # Reset the x.
        y  +=  word_height  # Start on new row.
       
main()