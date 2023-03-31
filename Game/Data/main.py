from itertools import cycle
import random
import sys
import os
import pygame
from tkinter import Tk,messagebox
from pygame.locals import *

FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512
PIPEGAPSIZE  = 100 # gap between upper and lower part of pipe
BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

# list of all possible players (tuple of 3 positions of flap)
PLAYERS_LIST = (
    # red bird
    (
        'Game/Data/assets/sprites/redbird-upflap.png',
        'Game/Data/assets/sprites/redbird-midflap.png',
        'Game/Data/assets/sprites/redbird-downflap.png',
    ),
    # blue bird
    (
        'Game/Data/assets/sprites/bluebird-upflap.png',
        'Game/Data/assets/sprites/bluebird-midflap.png',
        'Game/Data/assets/sprites/bluebird-downflap.png',
    ),
    # yellow bird
    (
        'Game/Data/assets/sprites/yellowbird-upflap.png',
        'Game/Data/assets/sprites/yellowbird-midflap.png',
        'Game/Data/assets/sprites/yellowbird-downflap.png',
    ),
)

# list of backgrounds
BACKGROUNDS_LIST = (
    'Game/Data/assets/sprites/background-day.png',
    'Game/Data/assets/sprites/background-night.png',
)

# list of pipes
PIPES_LIST = (
    'Game/Data/assets/sprites/pipe-green.png',
    'Game/Data/assets/sprites/pipe-red.png',
)


try:
    xrange
except NameError:
    xrange = range

rsetting = open(os.getcwd()+"\\Game\\Data\\sap.dat","r")
setting = rsetting.readlines()
rsetting.close()
level=str(int(setting[0].strip())+1)
MITLICENSE="""The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

ABOUTSOLARTERM=["",
                "时间：2月3日~2月5日\n立春标志着万物闭藏的冬季已过去，开始进入风和日暖、万物生长的春季。在自然界，立春最显著的特点就是万物开始有复苏的迹象。时至立春，在我国的北回归线（黄赤交角）及其以南一带，可明显感觉到早春的气息。由于我国幅员辽阔，南北跨度大，各地自然节律不一，“立春”对于很多地区来讲只是入春天的前奏，万物尚未复苏，还处于万物闭藏的冬天。",
                "时间：2月18日~2月20日\n雨水节气的含义是降雨开始，降雨量极多以小雨或毛毛细雨为主，适宜的降水对农作物的生长很重要，它是农耕文化对于节令的反映。进入雨水节气，中国北方地区尚未有春天气息，南方大多数地方则是春意盎然，一幅早春的景象。",
                "时间：3月5日~3月6日\n惊蛰反映着自然界生物受节律变化影响而萌发、生长的状态。时至惊蛰，阳气上升、气温回暖、春雷乍动、雨水增多，万物生机盎然。农耕生产与大自然的节律息息相关，惊蛰节气在农耕上有着相当重要的意义，它是古代农耕文化对于自然节令的反映。",
                "时间：3月19日~3月22日\n春分在天文学上有重要意义，春分这天太阳直射赤道，南北半球昼夜平分，自这天以后太阳直射位置由赤道继续向北半球推移，北半球各地白昼开始长于黑夜，南半球与之相反。在气候上，也有比较明显的特征，春分后中国除青藏高原、东北地区、西北地区和华北地区北部外均进入了明媚的春天。",
                "时间：4月4日~4月5日\n清明节气因为节令期间“气清景明、万物皆显”而得名。清明是反映自然界物候变化的节气，这个时节阳光明媚、草木萌动、百花盛开，自然界呈现一派生机勃勃的景象。中国南方地区，此时已呈气清景明之象；北方地区开始断雪，气温上升，春意融融。",
                "时间：4月19日~4月21日\n谷雨取自“雨生百谷”之意，此时降水明显增加，田中的秧苗初插、作物新种，最需要雨水的滋润，降雨量充足而及时，谷类作物能茁壮成长。谷雨与雨水、小满、小雪、大雪等节气一样，都是反映降水现象的节气，是古代农耕文化对于节令的反映。",
                "时间：5月5日~5月7日\n立夏表示告别春天，是夏天的开始，因此又称“春尽日”。春生、夏长、秋收、冬藏。由于中国幅员辽阔、南北跨度大，各地自然节律不一。立夏时节，中国只有南岭以南地区呈现“绿树阴浓夏日长，楼台倒影入池塘”的夏季景象；而东北和西北的部分地区这时则刚刚有春天的气息。",
                "时间：5月20日~5月22日\n小满之名，有两层含义。第一，与气候降水有关。小满节气期间南方的暴雨开始增多，降水频繁；民谚云“小满小满，江河渐满”。小满中的“满”，指雨水之盈。第二， 与农业小麦有关。在北方地区小满节气期间降雨较少甚至无雨，这个“满”不是指降水，而是指小麦的饱满程度。",
                "时间：6月5日~6月7日\n“芒种”含义是“有芒之谷类作物可种，过此即失效”。这个时节气温显著升高、雨量充沛、空气湿度大，适宜晚稻等谷类作物种植。农事耕种以“芒种”这节气为界，过此之后种植成活率就越来越低。它是古代农耕文化对于节令的反映。",
                "时间：6月21日~6月22日\n夏至是太阳北行的转折点。夏至过后，太阳直射点开始从北回归线向南移动，北半球白昼开始逐渐变短。对于中国位于北回归线以北地区来说，夏至过后，正午太阳高度开始逐日降低；对于中国位于北回归线以南地区来说，正午太阳高度在夏至过后经南返，太阳再次直射后才开始逐日降低。",
                "时间：7月6日~7月8日\n暑，是炎热的意思，小暑为小热，还不十分热。小暑虽不是一年中最炎热的时节，但紧接着就是一年中最热的节气大暑，民间有“小暑大暑，上蒸下煮”之说。中国多地自小暑起进入雷暴最多的时节。",
                "时间：7月22日~7月24日\n“暑”是炎热的意思，大暑，指炎热之极。大暑相对小暑，更加炎热，是一年中阳光最猛烈、最炎热的节气，“湿热交蒸”在此时到达顶点。大暑气候特征：高温酷热、雷暴、台风频繁。大暑节气正值“三伏天”里的“中伏”前后，是一年中最热的时段。大暑时节阳光猛烈、高温潮湿多雨，虽不免有湿热难熬之苦，却十分有利于农作物成长，农作物在此期间成长最快。",
                "时间：8月7日~8月8日\n“立”，是开始之意；“秋”，意为禾谷成熟。整个自然界的变化是循序渐进的过程，立秋是阳气渐收、阴气渐长，由阳盛逐渐转变为阴盛的转折。在自然界，万物开始从繁茂成长趋向成熟。",
                "时间：8月22日~8月24日\n处暑，意即“出暑”，高温将逐渐退场。处暑后太阳直射点继续南移、太阳辐射减弱、副热带高压南退，随着太阳高度的继续降低，所带来的热力也随之减弱。处暑意味着酷热难熬的天气到了尾声，这期间天气虽仍热，但已是呈下降趋势。暑热消退是一个缓慢的过程，并不是暑气下降马上就凉爽了，真正开始有凉意一般要到白露之后。",
                "时间：9月7日~9月9日\n“白露”是反映自然界寒气增长的重要节气。由于冷空气转守为攻，白昼有阳光尚热，但傍晚后气温便很快下降，昼夜温差逐渐拉大。白露基本结束了暑天的闷热，天气渐渐转凉，寒生露凝。古人以四时配五行，秋属金，金色白，以白形容秋露，故名“白露”。",
                "时间：9月22日~9月24日\n秋分这天太阳几乎直射地球赤道，全球各地昼夜等长。秋分，“分”即为“平分”、“半”的意思，除了指昼夜平分外，还有一层意思是平分了秋季。秋分日后，太阳光直射位置南移，北半球昼短夜长，昼夜温差加大，气温逐日下降",
                "时间：10月7日~10月9日\n寒露，是深秋的节令，干支历戌月的起始。寒露是一个反映气候变化特征的节气。进入寒露，时有冷空气南下，昼夜温差较大，并且秋燥明显。寒露以后，北方冷空气已有一定势力，中国大部分地区在冷高压控制之下，雨季结束。受冷高压的控制，昼暖夜凉，白天往往秋高气爽。",
                "时间：10月23日~10月24日\n进入霜降节气后，深秋景象明显，冷空气南下越来越频繁。霜降不是表示“降霜”，而是表示气温骤降、昼夜温差大。就全国平均而言，“霜降”是一年之中昼夜温差最大的时节。",
                "时间：11月7日~11月8日\n立，建始也；冬，终也，万物收藏也。立冬，意味着生气开始闭蓄，万物进入休养、收藏状态。其气候也由秋季少雨干燥向阴雨寒冻的冬季气候过渡。立冬代表着冬季的开始，它是中国民间非常重视的季节节点之一，春耕夏耘、秋收冬藏，冬季是享受丰收、休养生息的季节。",
                "时间：11月22日~11月23日\n小雪是反映降水与气温的节气，它是寒潮和强冷空气活动频数较高的节气。小雪节气的到来，意味着天气会越来越冷、降水量渐增。“雪”是寒冷天气的产物，故以“小雪”比喻这个节气期间“气候寒未深且降水未大”的气候特征。“小雪”节气是反映气温与降水变化趋势的节气，并不是表示这个节气下很小量的雪，节气“小雪”与天气中的“小雪”没有必然联系。",
                "时间：12月6日~12月8日\n大雪节气是干支历子月的起始，标志着仲冬时节正式开始。大雪是反映气候特征的一个节气，大雪节气的特点是气温显著下降、降水量增多。“雪”是水汽遇冷的产物，代表寒冷与降水。大雪节气是一个气候概念，它代表的是大雪节气期间的气候特征，即气温与降水量（气象上将雨、雪、雹等从天空下降到地面的水汽凝结物都称为“降水”）。",
                "时间：12月21日~12月23日\n冬至是太阳直射点南行的极致，冬至这天太阳光直射南回归线，太阳光对北半球最为倾斜，太阳高度角最小，是北半球各地白昼最短、黑夜最长的一天。冬至也是太阳直射点北返的转折点，这天过后它将走“回头路”，太阳直射点开始从南回归线（23°26′S）向北移动，北半球（中国位于北半球）白昼将会逐日增长。",
                "时间：1月5日~1月7日\n冷气积久而寒，小寒是天气寒冷但还没有到极点的意思，它与大寒、小暑、大暑及处暑一样，都是表示气温冷暖变化的节气。小寒节气的特点就是寒冷，但是却还没有冷到极致。根据中国长期以来的气象记录，在北方地区小寒节气比大寒节气更冷，在北方有“小寒胜大寒”一说；但对于南方部分地区，全年最低气温仍然会出现在大寒节气内。",
                "时间：1月20日左右\n大寒同小寒一样，都是表示天气寒冷程度的节气，大寒是天气寒冷到极致的意思。大寒节气处在三九、四九时段，此时寒潮南下频繁，是一年中的最寒冷时节。大寒在岁终，冬去春来，大寒一过，又开始新的一个轮回。"]
SOLARTERMNAME=["","立春","雨水","惊蛰","春分","清明","谷雨","立夏","小满","芒种","夏至","小暑","大暑","立秋","处暑","白露","秋分","寒露","霜降","立冬","小雪","大雪","冬至","小寒","大寒"]
def main():
    root=Tk()
    root.withdraw()
    if level == "1":
        messagebox.showinfo("感谢","感谢游戏独立开发者Dong Nguyen\n感谢GitHub上的代码分享者sourabhv\n感谢Python，Pygame的开发者")
        messagebox.showinfo("MIT License",MITLICENSE)
        messagebox.showinfo("玩法教学：","1.空格\\鼠标左键飞翔\n2.失败后重新开始时再次按下空格\\左键")
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("第"+level+"关")

    # numbers sprites for score display
    IMAGES['numbers'] = (
        pygame.image.load('Game/Data/assets/sprites/0.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/1.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/2.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/3.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/4.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/5.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/6.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/7.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/8.png').convert_alpha(),
        pygame.image.load('Game/Data/assets/sprites/9.png').convert_alpha()
    )

    # game over sprite
    IMAGES['gameover'] = pygame.image.load('Game/Data/assets/sprites/gameover.png').convert_alpha()
    # message sprite for welcome screen
    IMAGES['message'] = pygame.image.load('Game/Data/assets/sprites/message.png').convert_alpha()
    # base (ground) sprite
    IMAGES['base'] = pygame.image.load('Game/Data/assets/sprites/base.png').convert_alpha()

    # sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['die']    = pygame.mixer.Sound('Game/Data/assets/audio/die' + soundExt)
    SOUNDS['hit']    = pygame.mixer.Sound('Game/Data/assets/audio/hit' + soundExt)
    SOUNDS['point']  = pygame.mixer.Sound('Game/Data/assets/audio/point' + soundExt)
    SOUNDS['swoosh'] = pygame.mixer.Sound('Game/Data/assets/audio/swoosh' + soundExt)
    SOUNDS['wing']   = pygame.mixer.Sound('Game/Data/assets/audio/wing' + soundExt)

    while True:
        # select random background sprites
        randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1)
        IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()

        # select random player sprites
        randPlayer = random.randint(0, len(PLAYERS_LIST) - 1)
        IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
        )

        # select random pipe sprites
        pipeindex = random.randint(0, len(PIPES_LIST) - 1)
        IMAGES['pipe'] = (
            pygame.transform.flip(
                pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(), False, True),
            pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(),
        )

        # hitmask for pipes
        HITMASKS['pipe'] = (
            getHitmask(IMAGES['pipe'][0]),
            getHitmask(IMAGES['pipe'][1]),
        )

        # hitmask for player
        HITMASKS['player'] = (
            getHitmask(IMAGES['player'][0]),
            getHitmask(IMAGES['player'][1]),
            getHitmask(IMAGES['player'][2]),
        )

        movementInfo = showWelcomeAnimation()
        crashInfo = mainGame(movementInfo)
        showGameOverScreen(crashInfo)


def showWelcomeAnimation():
    """Shows welcome screen animation of flappy bird"""
    # index of player to blit on screen
    playerIndex = 0
    playerIndexGen = cycle([0, 1, 2, 1])
    # iterator used to change playerIndex after every 5th iteration
    loopIter = 0

    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - IMAGES['player'][0].get_height()) / 2)

    messagex = int((SCREENWIDTH - IMAGES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.12)

    basex = 0
    # amount by which base can maximum shift to left
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()

    # player shm for up-down motion on welcome screen
    playerShmVals = {'val': 0, 'dir': 1}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)) or event.type == MOUSEBUTTONDOWN:
                # make first flap sound and return values for mainGame
                SOUNDS['wing'].play()
                return {
                    'playery': playery + playerShmVals['val'],
                    'basex': basex,
                    'playerIndexGen': playerIndexGen,
                }

        # adjust playery, playerIndex, basex
        if (loopIter + 1) % 5 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 4) % baseShift)
        playerShm(playerShmVals)

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))
        SCREEN.blit(IMAGES['player'][playerIndex],
                    (playerx, playery + playerShmVals['val']))
        SCREEN.blit(IMAGES['message'], (messagex, messagey))
        SCREEN.blit(IMAGES['base'], (basex, BASEY))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def mainGame(movementInfo):
    score = playerIndex = loopIter = 0
    playerIndexGen = movementInfo['playerIndexGen']
    playerx, playery = int(SCREENWIDTH * 0.2), movementInfo['playery']

    basex = movementInfo['basex']
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()

    # get 2 new pipes to add to upperPipes lowerPipes list
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]

    # list of lowerpipe
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    dt = FPSCLOCK.tick(FPS)/1000
    pipeVelX = -128 * dt

    # player velocity, max velocity, downward acceleration, acceleration on flap
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerMaxVelY =  10   # max vel along Y, max descend speed
    playerMinVelY =  -8   # min vel along Y, max ascend speed
    playerAccY    =   1   # players downward acceleration
    playerRot     =  45   # player's rotation
    playerVelRot  =   3   # angular speed
    playerRotThr  =  20   # rotation threshold
    playerFlapAcc =  -9   # players speed on flapping
    playerFlapped = False # True when player flaps


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)) or event.type == MOUSEBUTTONDOWN:
                if playery > -2 * IMAGES['player'][0].get_height():
                    playerVelY = playerFlapAcc
                    playerFlapped = True
                    SOUNDS['wing'].play()
        if int(level)<=6:
            if score==3:
                pygame.quit()
                root=Tk()
                root.withdraw()
                messagebox.showinfo("恭喜！","恭喜你完成了第"+level+"关的挑战！下面是节气介绍，要认真看哦！")
                messagebox.showinfo(SOLARTERMNAME[int(level)],ABOUTSOLARTERM[int(level)])
                wsetting=open(os.getcwd()+"\\Game\\Data\\sap.dat","w")
                wsetting.write(str(int(level)))
                wsetting.close()
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                sys.exit()
        elif int(level)<=12:
            if score==4:
                pygame.quit()
                root=Tk()
                root.withdraw()
                messagebox.showinfo("恭喜！","恭喜你完成了第"+level+"关的挑战！下面是节气介绍，要认真看哦！")
                messagebox.showinfo(SOLARTERMNAME[int(level)],ABOUTSOLARTERM[int(level)])
                wsetting=open(os.getcwd()+"\\Game\\Data\\sap.dat","w")
                wsetting.write(str(int(level)))
                wsetting.close()
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                sys.exit()
        elif int(level)<=18:
            if score==5:
                pygame.quit()
                root=Tk()
                root.withdraw()
                messagebox.showinfo("恭喜！","恭喜你完成了第"+level+"关的挑战！下面是节气介绍，要认真看哦！")
                messagebox.showinfo(SOLARTERMNAME[int(level)],ABOUTSOLARTERM[int(level)])
                wsetting=open(os.getcwd()+"\\Game\\Data\\sap.dat","w")
                wsetting.write(str(int(level)))
                wsetting.close()
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                sys.exit()
        elif int(level)<=24:
            if score==6:
                pygame.quit()
                root=Tk()
                root.withdraw()
                messagebox.showinfo("恭喜！","恭喜你完成了第"+level+"关的挑战！下面是节气介绍，要认真看哦！")
                messagebox.showinfo(SOLARTERMNAME[int(level)],ABOUTSOLARTERM[int(level)])
                wsetting=open(os.getcwd()+"\\Game\\Data\\sap.dat","w")
                wsetting.write(str(int(level)))
                wsetting.close()
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                sys.exit()


        # check for crash here
        crashTest = checkCrash({'x': playerx, 'y': playery, 'index': playerIndex},
                               upperPipes, lowerPipes)
        if crashTest[0]:
            return {
                'y': playery,
                'groundCrash': crashTest[1],
                'basex': basex,
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
                'playerRot': playerRot
            }

        # check for score
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                SOUNDS['point'].play()

        # playerIndex basex change
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 100) % baseShift)

        # rotate the player
        if playerRot > -90:
            playerRot -= playerVelRot

        # player's movement
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped = False

            # more rotation to cover the threshold (calculated in visible rotation)
            playerRot = 45

        playerHeight = IMAGES['player'][playerIndex].get_height()
        playery += min(playerVelY, BASEY - playery - playerHeight)

        # move pipes to left
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX

        # add new pipe when first pipe is about to touch left of screen
        if 3 > len(upperPipes) > 0 and 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # remove first pipe if its out of the screen
        if len(upperPipes) > 0 and upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        # print score so player overlaps the score
        showScore(score)

        # Player rotation has a threshold
        visibleRot = playerRotThr
        if playerRot <= playerRotThr:
            visibleRot = playerRot
        
        playerSurface = pygame.transform.rotate(IMAGES['player'][playerIndex], visibleRot)
        SCREEN.blit(playerSurface, (playerx, playery))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def showGameOverScreen(crashInfo):
    """crashes the player down and shows gameover image"""
    score = crashInfo['score']
    playerx = SCREENWIDTH * 0.2
    playery = crashInfo['y']
    playerHeight = IMAGES['player'][0].get_height()
    playerVelY = crashInfo['playerVelY']
    playerAccY = 2
    playerRot = crashInfo['playerRot']
    playerVelRot = 7

    basex = crashInfo['basex']

    upperPipes, lowerPipes = crashInfo['upperPipes'], crashInfo['lowerPipes']

    # play hit and die sounds
    SOUNDS['hit'].play()
    if not crashInfo['groundCrash']:
        SOUNDS['die'].play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                os.system("start "+os.getcwd()+"\\Game\\game.exe")
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)) or event.type == MOUSEBUTTONDOWN:
                if playery + playerHeight >= BASEY - 1:
                    return

        # player y shift
        if playery + playerHeight < BASEY - 1:
            playery += min(playerVelY, BASEY - playery - playerHeight)

        # player velocity change
        if playerVelY < 15:
            playerVelY += playerAccY

        # rotate only when it's a pipe crash
        if not crashInfo['groundCrash']:
            if playerRot > -90:
                playerRot -= playerVelRot

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        showScore(score)

        


        playerSurface = pygame.transform.rotate(IMAGES['player'][1], playerRot)
        SCREEN.blit(playerSurface, (playerx,playery))
        SCREEN.blit(IMAGES['gameover'], (50, 180))

        FPSCLOCK.tick(FPS)
        pygame.display.update()


def playerShm(playerShm):
    """oscillates the value of playerShm['val'] between 8 and -8"""
    if abs(playerShm['val']) == 8:
        playerShm['dir'] *= -1

    if playerShm['dir'] == 1:
         playerShm['val'] += 1
    else:
        playerShm['val'] -= 1


def getRandomPipe():
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10

    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]


def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) / 2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][digit].get_width()


def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collides with base or pipes."""
    pi = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player crashes into ground
    if player['y'] + player['h'] >= BASEY - 1:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][pi]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)

            if uCollide or lCollide:
                return [True, False]

    return [False, False]

def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """Checks if two objects collide and not just their rects"""
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False

def getHitmask(image):
    """returns a hitmask using an image's alpha."""
    mask = []
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask

if __name__ == '__main__':
    main()
