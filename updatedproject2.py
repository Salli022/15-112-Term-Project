from cmu_graphics import *
from ballclass import *
from opponentclass import *
from playerclass import *
from courtclass import *
from PIL import Image
import os, pathlib
import math
import random


ball = Ball()
opponent = Opponent(1000,1000)
player = Player(1000,1000)
court = Court()

def onAppStart(app):
    createImages(app)
    app.width = 1000
    app.height = 1000
    ball.setHeightandWidth(app.width,app.height)
    ball.randomizeX()
    app.gameScreen = False
    app.homeScreen = True
    app.directionsScreen = False
    app.chooseCourtScreen = False
    app.outsidecourtColor = rgb(201, 85, 2)
    app.insidecourtColor = rgb(3, 143, 40)
    app.drawFaultScreen = False
    app.wonGame = False
    app.lostGame = False
    newPoint(app)
    
def newPoint(app):
    ball.restart()
    player.restart()
    opponent.restart()
    opponent.setXandY(ball.x, ball.startY)
    player.setXandY(ball.x,ball.startY)
    app.stepsPerSecond = 27
    app.timer = 0
    app.timer1 = 0
    app.timerserve = 0
    app.timerhitserve = 0
    app.drawFaultScreen = False


def redoServe(app):
    ball.Faultrestart()
    player.restart()
    opponent.restart()
    opponent.setXandY(ball.x, ball.startY)
    player.setXandY(ball.x,ball.startY)
    app.stepsPerSecond = 27
    app.timer = 0
    app.timer1 = 0
    app.timerserve = 0
    app.timerhitserve = 0
    app.drawFaultScreen = False


def createImages(app):

    #all images drawn from characters in 
    # https://www.retrogames.cz/play_013-NES.php?language=EN
    # words created by https://fontmeme.com/retro-fonts/
    #ball created by https://www.google.com/search?q=retro+animated+tennis+ball&sca_esv=586055818&udm=2&source=lnms&sa=X&ved=0ahUKEwiMnIb7yueCAxWlhIkEHdagAWMQ0pQJCO4H&biw=1710&bih=952&dpr=2#vhid=EDuHbQq1pIw4bM&vssid=mosaic

    #player sprites 
    app.imagemovingLeft = Image.open("images/playermoveandhit/player1.png")
    app.imagestill = Image.open("images/playermoveandhit/player.png")
    app.imagemovingRight = Image.open("images/playermoveandhit/player2.png")
    app.imageforehand1 = Image.open("images/playermoveandhit/player3.png")
    app.imageforehand2 = Image.open("images/playermoveandhit/player7.png")
    app.imageforehand3 = Image.open("images/playermoveandhit/player8.png")
    app.imageforehand4 = Image.open("images/playermoveandhit/player9.png")
    app.imagebackhand1 = Image.open("images/playermoveandhit/player4.png")
    app.imagebackhand2 = Image.open("images/playermoveandhit/player5.png")
    app.imagebackhand3 = Image.open("images/playermoveandhit/player6.png")
    app.imageserve1 = Image.open("images/playerserve/playerserve1.png")
    app.imageserve2 = Image.open("images/playerserve/playerserve2.png")
    app.imageserve3 = Image.open("images/playerserve/playerserve3.png")
    app.imageserve4 = Image.open("images/playerserve/playerserve5.png")
    app.imageserve5 = Image.open("images/playerserve/playerserve4.png")
    app.imageserve6 = Image.open("images/playerserve/playerserve6.png")

    app.imagemovingLeft = CMUImage(app.imagemovingLeft)
    app.imagestill = CMUImage(app.imagestill)
    app.imagemovingRight = CMUImage(app.imagemovingRight)
    app.imageforehand1 = CMUImage(app.imageforehand1)
    app.imageforehand2 = CMUImage(app.imageforehand2)
    app.imageforehand3 = CMUImage(app.imageforehand3)
    app.imageforehand4 = CMUImage(app.imageforehand4)
    app.imagebackhand1 = CMUImage(app.imagebackhand1)
    app.imagebackhand2 = CMUImage(app.imagebackhand2)
    app.imagebackhand3 = CMUImage(app.imagebackhand3)
    app.imageserve1 = CMUImage(app.imageserve1)
    app.imageserve2 = CMUImage(app.imageserve2)
    app.imageserve3 = CMUImage(app.imageserve3)
    app.imageserve4 = CMUImage(app.imageserve4)
    app.imageserve5 = CMUImage(app.imageserve5)

    #opponent sprites

    app.imageoppserve1 = Image.open("images/oppserve/oppserve1.png")
    app.imageoppserve2 = Image.open("images/oppserve/oppserve2.png")
    app.imageoppserve3 = Image.open("images/oppserve/oppserve3.png")
    app.imageoppserve4 = Image.open("images/oppserve/oppserve4.png")
    app.imageoppserve5 = Image.open("images/oppserve/oppserve5.png")

    app.imageoppleft = Image.open("images/oppmoveandhit/opponent1.png")
    app.imageoppbackhand1 = Image.open("images/oppmoveandhit/opponent.png")
    app.imageoppbackhand2 = Image.open("images/oppmoveandhit/opponent2.png")
    app.imageoppbackhand3 = Image.open("images/oppmoveandhit/opponent3.png")
    app.imageoppstill = Image.open("images/oppmoveandhit/opponent4.png")
    app.imageoppright = Image.open("images/oppmoveandhit/opponent5.png")
    app.imageoppforehand3 = Image.open("images/oppmoveandhit/opponent6.png")
    app.imageoppforehand1 = Image.open("images/oppmoveandhit/opponent7.png")
    app.imageoppforehand2 = Image.open("images/oppmoveandhit/opponent8.png")
    app.imageoppleft = CMUImage(app.imageoppleft)
    app.imageoppbackhand1 = CMUImage(app.imageoppbackhand1)
    app.imageoppbackhand2 = CMUImage(app.imageoppbackhand2)
    app.imageoppbackhand3 = CMUImage(app.imageoppbackhand3)
    app.imageoppright = CMUImage(app.imageoppright)
    app.imageoppforehand3 = CMUImage(app.imageoppforehand3)
    app.imageoppforehand2 = CMUImage(app.imageoppforehand2)
    app.imageoppforehand1 = CMUImage(app.imageoppforehand1)
    app.imageoppstill = CMUImage(app.imageoppstill)
    app.imageoppserve1 = CMUImage(app.imageoppserve1)
    app.imageoppserve2 = CMUImage(app.imageoppserve2)
    app.imageoppserve3 = CMUImage(app.imageoppserve3)
    app.imageoppserve4 = CMUImage(app.imageoppserve4)
    app.imageoppserve5 = CMUImage(app.imageoppserve5)

    #other 
    app.imagecomputerscorecard = Image.open("images/other/computerscore.png")
    app.imageuserscorecard = Image.open("images/other/userscore.png")
    app.imagejudgetowards = Image.open("images/other/judgetowards.png")
    app.imagejudgeaway = Image.open("images/other/judgeaway.png")
    app.imagetitlescreen = Image.open("images/other/titlescreen.png")
    app.imageball = Image.open("images/other/balltitlescreen.png")
    app.imagedirections = Image.open("images/other/directions.png")
    app.imagestart = Image.open("images/other/start.png")
    app.imagecomputerscorecard = CMUImage(app.imagecomputerscorecard)
    app.imageuserscorecard = CMUImage(app.imageuserscorecard)
    app.imagejudgetowards = CMUImage(app.imagejudgetowards)
    app.imagejudgeaway = CMUImage(app.imagejudgeaway)
    app.imagetitlescreen = CMUImage(app.imagetitlescreen)
    app.imageball = CMUImage(app.imageball)
    app.imagedirections = CMUImage(app.imagedirections)
    app.imagestart = CMUImage(app.imagestart)

def redrawAll(app):
    if app.wonGame:
        drawRect(0,0,app.width,app.height, fill = 'green')
        drawLabel("You Won!!!!!", app.width//2, 300, size = 80, bold = True)
        drawLabel("Press r to go back to the home screen", app.width//2, 600, size = 20)
        drawLabel(str(player.gamesWon) + "-"+ str(opponent.gamesWon), app.width//2, 450, size = 60, bold = True)
    elif app.lostGame:
        drawRect(0,0,app.width,app.height, fill = 'red')
        drawLabel("You Lost :(", app.width//2, 300, size = 80, bold = True)
        drawLabel("Press r to go back to the home screen", app.width//2, 600, size = 20)
        drawLabel(str(player.gamesWon) + "-"+ str(opponent.gamesWon), app.width//2, 450, size = 60, bold = True)
    elif app.homeScreen:
        drawRect(0,0,app.width,app.height, fill = rgb(5,169,86))
        drawImage(app.imageball, 200, 375, width = 600, height = 600)
        drawImage(app.imagetitlescreen, app.width//9, 100, width = 800, height = 300)
        drawRect(app.width//2, 600, 410, 110, fill = 'white', align = 'center')
        drawRect(app.width//2, 600, 400, 100, fill = 'black', align = 'center')
        drawRect(app.width//2, 800, 610, 160, align = 'center', fill = 'white')
        drawRect(app.width//2, 800, 600, 150, align = 'center')
        drawImage(app.imagedirections, 300, 550, width = 400, height = 100)
        drawImage(app.imagestart, 200, 725, width = 600, height = 150)
        drawImage(app.imageoppbackhand2, 50, 550, width = 120, height = 160)
        drawImage(app.imageforehand3, 850, 550, width = 120, height = 160)
    elif app.directionsScreen:
        drawRect(0,0,app.width,app.height, fill = rgb(5,169,86))
        drawLabel('''Welcome to Retro Tennis!!!!''', app.width//2, 100, size = 50, bold = True)
        drawLabel(" This is a simple game where you are tasked with beating the computer at tennis!!", app.width//2, 200, size = 25, bold = True)
        drawLabel("Make sure you look over the controls. The first person to win a set wins the game!!! Good Luck!!", app.width//2, 275, size = 20, bold = True)
        drawLabel("Up Key ----------------------------- Move User Up", app.width//2, 400, size = 35, bold = True, italic = True)
        drawLabel("Down Key ----------------------------- Move User Down", app.width//2, 475, size = 35, bold = True, italic = True)
        drawLabel("Right Key ----------------------------- Move User Right" , app.width//2, 550, size = 35, bold = True, italic = True)
        drawLabel("Left Key ----------------------------- Move User Left", app.width//2, 625, size = 35, bold = True, italic = True)
        drawLabel("1 ----------------------------- Topspin Shot", app.width//2, 700, size = 35, bold = True, italic = True)
        drawLabel("2 ----------------------------- Slice Shot", app.width//2, 775, size = 35, bold = True, italic = True)
        drawLabel("3 ----------------------------- Lob Shot", app.width//2, 850, size = 35, bold = True, italic = True)
        drawLabel("Space ----------------------------- Hit Serve", app.width//2, 925, size = 35, bold = True, italic = True)
        drawLabel("Press r to go back to home screen", app.width//2, 325, size = 15, bold = True, italic = True)
    elif app.chooseCourtScreen:
        drawRect(0,0,app.width,app.height, fill = rgb(5,169,86))
        drawLabel("Choose Your Court!!!",app.width//2, 100, size = 50, bold = True)
        drawLabel("Clay : Ball moves slower", app.width//4, 250, bold = True, size = 25)
        drawLabel("Hard: Ball moves at normal speed", app.width//4, 450, bold = True, size = 25)
        drawLabel("Grass : Ball moves a bit faster", app.width//4, 650, bold = True, size = 25)
        drawLabel("Rubber : Ball moves much faster", app.width//4, 850, bold = True, size = 25)
        drawRect(app.width//4 * 3, 250, 410, 110, fill = 'white', align = 'center')
        drawRect(app.width//4 * 3, 250, 400, 100, align = 'center', fill = rgb(240,104,52) )
        drawRect(app.width//4 * 3, 450, 410, 110, fill = 'white', align = 'center')
        drawRect(app.width//4 * 3, 450, 400, 100, align = 'center', fill = rgb(3, 143, 40))
        drawRect(app.width//4 * 3, 650, 410, 110, fill = 'white', align = 'center')
        drawRect(app.width//4 * 3, 650, 400, 100, align = 'center', fill = rgb(153,200,92))
        drawRect(app.width//4 * 3, 850, 410, 110, fill = 'white', align = 'center')
        drawRect(app.width//4 * 3, 850, 400, 100, align = 'center', fill = rgb(86,121,143))
        drawLabel("Start", 750, 850, size = 50, fill = 'white')
        drawLabel("Start", 750, 650, size = 50, fill = 'white')
        drawLabel("Start", 750, 450, size = 50, fill = 'white')
        drawLabel("Start", 750, 250, size = 50, fill = 'white')
    elif app.gameScreen:
        #background
        drawRect(0,0, app.width, app.height, fill = app.outsidecourtColor)
        drawRect(app.width//6+15,app.height//8, (app.width//6 * 5 - app.width//6 - 30), 
                app.height//8 * 7 - app.height//8, fill = app.insidecourtColor)
        drawLine(app.width//6 + 5, app.height//8 * 7, app.width//6 + 20, app.height//8, fill = app.insidecourtColor,
                lineWidth = 20)
        drawLine(app.width//6 * 5 - 5, app.height//8 * 7, app.width//6 * 5 - 20, app.height//8, fill = app.insidecourtColor,
                lineWidth = 20)

        #code for drawing the court
        drawLine(app.width//6, app.height//8 * 7, app.width//6 * 5, app.height//8 * 7, fill = 'white', 
                lineWidth = 13)
        drawLine(app.width//6, app.height//8 * 7, app.width//6 + 15, app.height//8, fill = 'white',
                lineWidth = 13)
        drawLine(app.width//6 * 5, app.height//8 * 7, app.width//6 * 5 - 15, app.height//8, fill = 'white',
                lineWidth = 13)
        drawLine(app.width//6 + 15, app.height//8, app.width//6 * 5 - 15, app.height//8, fill = 'white',
                lineWidth = 13)

        #drawing lines on court 
        drawLine(app.width//2, app.height//8 * 2.5, app.width//2, app.height//2 - 40, fill = 'white')
        drawLine(177.188 , app.height//8 * 2.5, 818.75, app.height//8 * 2.5, fill = 'white')
        drawLine(app.width//2, app.height//2 + 40, app.width//2, app.height//2+ 40 - (app.height//8 * 2.5 - app.height//2 + 40),
                fill = 'white')
        drawLine(169.64,app.height//2+ 40 - (app.height//8 * 2.5 - app.height//2 + 40), 826.29
                , app.height//2+ 40 - (app.height//8 * 2.5 - app.height//2 + 40), fill = 'white' )
        
        #code for drawing the net
        startingpointx = app.width//8
        endingpointx = app.width//8 * 7
        startingpointy = app.height//2 - 40
        endingpointy = app.height //2 + 40 
        for x in range(1,30):
            drawLine(startingpointx + x * ((endingpointx - startingpointx)//30), startingpointy, 
                    startingpointx + x * ((endingpointx - startingpointx)//30), endingpointy)
        
        for y in range(1,10):
            drawLine(startingpointx, startingpointy + y * ((endingpointy - startingpointy)//10), 
                    endingpointx, startingpointy + y * (endingpointy - startingpointy)//10)
        drawRect(app.width//2, app.height//2, 3 * app.width//4, 80, align = 'center', fill = None, border = 'white',
                borderWidth = 5 )
        drawRect(app.width//2 - (3 * app.width//8), app.height//2 - 40, 10, 80)
        drawRect(app.width//2 + (3 * app.width//8) - 10, app.height//2 - 40, 10, 80)

        #drawing Scoreboard
        drawRect(0,app.height-85, 305,85, fill = 'white')
        drawRect(0, app.height - 80, 300, 80)
        drawLine(0,app.height-(85/2 - 5), 300, app.height-(85/2 - 5), fill = 'white')
        for x in range(3):
            drawLine(x * (300/3), app.height - 85 , x * (300/3), app.height, fill = 'white')
        drawImage(app.imagecomputerscorecard, 0 , app.height - 60, width = 100, height = 80)
        drawImage(app.imageuserscorecard, 0 , app.height - 90, width = 100, height = 60)
        drawLabel(str(player.gamesWon), 150, app.height - (85/1.4), fill = 'white', size = 30)
        drawLabel(str(player.gameScore), 250, app.height - (85/1.4), fill = 'white', size = 30)
        drawLabel(str(opponent.gamesWon), 150, app.height - (85/4.5), fill = 'white', size = 30)
        drawLabel(str(opponent.gameScore), 250, app.height - (85/4.5), fill = 'white', size = 30)

        #code for drawing the ball
        if ball.onGround:
            if player.Hit:
                drawLine(ball.x - 10, ball.startY + 10, ball.x - 20, ball.startY + 20)
                drawLine(ball.x + 10, ball.startY + 10, ball.x + 20, ball.startY + 20 )
            else:
                drawLine(ball.x - 10, ball.startY - 10, ball.x - 20, ball.startY - 20)
                drawLine(ball.x + 10, ball.startY - 10, ball.x + 20, ball.startY - 20)
            drawCircle(ball.x, ball.startY, ball.ballSize, fill = rgb(223,255,7))
        elif (ball.hitNet or (ball.numofBounce == 2 and ball.Fault == False) or 
            (ball.outofBounds and ball.Fault == False) or ball.Fault or ball.onGround):
            drawCircle(ball.x, ball.startY, ball.ballSize, fill = 'red')
        else:
            drawCircle(ball.x, ball.startY, ball.ballSize, fill = rgb(223,255,7))

        #draw Player and Opponent
        drawPlayer(app)
        drawOpponent(app)

        #draw the judge
        drawJudge(app)
        


def drawJudge(app):
    if ball.startY <= app.height//2:
        drawImage(app.imagejudgeaway, 900, app.height//2 - 100, width = 80, height = 160)
    else:
        drawImage(app.imagejudgetowards, 900, app.height//2 - 100, width = 70, height = 160)

def drawPlayer(app):
    if player.canServe and app.timerserve < 100:
        drawPlayerServe(app)
    elif player.movingLeft == True and player.Swung == True and app.timer < 15:
        drawhitBackhand(app)
    elif player.movingRight == True and player.Swung == True and app.timer < 20:
        drawhitForehand(app)
    elif player.movingLeft == True :
        drawImage(app.imagemovingLeft, player.X, player.Y, width = 60, height = 80)
    elif player.movingRight == True:
        drawImage(app.imagemovingRight, player.X, player.Y, width = 60, height = 80)
    else:
        drawImage(app.imagestill, player.X, player.Y, width = 50, height = 70)

def drawOpponent(app):
    if opponent.canServe and app.timerserve < 30:
        drawOpponentServe(app)
    elif opponent.StandingStill == True and opponent.Hit == False:
        drawImage(app.imageoppstill, opponent.X, opponent.Y, width = 35, height = 80)
    elif opponent.MovingRight == True and opponent.canHitBall == False:
        drawImage(app.imageoppleft, opponent.X, opponent.Y, width = 60, height = 80)
    elif opponent.MovingLeft == True and opponent.canHitBall == False:
        drawImage(app.imageoppright, opponent.X, opponent.Y, width = 60, height = 80)
    elif opponent.StandingStill == True and opponent.canHitBall and app.timer1 < 15:
        drawoppForehand(app)
    elif opponent.BackHand and opponent.canHitBall == True and app.timer1 < 15:
        drawoppBackhand(app)
    elif opponent.ForeHand and opponent.canHitBall == True and app.timer1 < 15:
        drawoppForehand(app)
    else:
        drawImage(app.imageoppstill, opponent.X, opponent.Y, width = 35, height = 80)

def drawPlayerServe(app):
    if ball.ballinAirForServe == False and player.canHitServe == False:
        drawImage(app.imageserve1, player.X, player.Y, width = 60, height = 80)
    elif ball.ballinAirForServe == True and player.canHitServe == False:
        drawImage(app.imageserve2, player.X, player.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and player.canHitServe and app.timerserve % 100 < 33:
        drawImage(app.imageserve3, player.X, player.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and player.canHitServe and app.timerserve % 100 < 66:
        drawImage(app.imageserve4, player.X, player.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and player.canHitServe:
        drawImage(app.imageserve5, player.X, player.Y, width = 60, height = 80)

def drawOpponentServe(app):
    if ball.ballinAirForServe == False and opponent.canHitServe == False:
        drawImage(app.imageoppserve1, opponent.X, opponent.Y, width = 60, height = 80)
    elif ball.ballinAirForServe == True and opponent.canHitServe == False:
        drawImage(app.imageoppserve2, opponent.X, opponent.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and opponent.canHitServe and app.timerserve % 30 < 10:
        drawImage(app.imageoppserve3, opponent.X, opponent.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and opponent.canHitServe and app.timerserve % 30 < 20:
        drawImage(app.imageoppserve4, opponent.X, opponent.Y, width = 60, height = 80)
    elif ball.ballinAirForServe and opponent.canHitServe:
        drawImage(app.imageoppserve5, opponent.X, opponent.Y, width = 60, height = 80)
    
def drawoppForehand(app):
    if app.timer1 % 15 < 5:
        drawImage(app.imageoppforehand1, opponent.X, opponent.Y, width = 60, height = 80)
    elif app.timer1 % 15 < 10:
        drawImage(app.imageoppforehand2, opponent.X, opponent.Y, width = 60, height = 80)
    else:
        drawImage(app.imageoppforehand3, opponent.X, opponent.Y, width = 60, height = 80)

def drawoppBackhand(app):
    if app.timer1 % 15 < 5:
        drawImage(app.imageoppbackhand1, opponent.X, opponent.Y, width = 60, height = 80)
    elif app.timer1 % 15 < 10:
        drawImage(app.imageoppbackhand2, opponent.X, opponent.Y, width = 60, height = 80)
    else:
        drawImage(app.imageoppbackhand3, opponent.X, opponent.Y, width = 60, height = 80)

def drawhitBackhand(app):
    if app.timer % 15 < 5:
        drawImage(app.imagebackhand1, player.X, player.Y, width = 60, height = 80)
    elif app.timer % 15 < 10:
        drawImage(app.imagebackhand2, player.X, player.Y, width = 60, height = 80)
    else:
        drawImage(app.imagebackhand3, player.X, player.Y, width = 60, height = 80)

def drawhitForehand(app):
    if app.timer % 20 < 5:
        drawImage(app.imageforehand2, player.X, player.Y, width = 60, height = 80)
    elif app.timer % 20 < 10:
        drawImage(app.imageforehand3, player.X, player.Y, width = 60, height = 80)
    elif app.timer % 20 < 15:
        drawImage(app.imageforehand1, player.X, player.Y, width = 60, height = 80)
    else:
        drawImage(app.imageforehand4, player.X, player.Y, width = 50, height = 80)

def onStep(app):
    if app.gameScreen:
        if player.gamesWon >= 6 and player.gamesWon - opponent.gamesWon >= 2:
            app.wonGame = True
            app.gameScreen = False
        elif opponent.gamesWon >= 6 and opponent.gamesWon - player.gamesWon >= 2:
            app.lostGame = True
            app.gameScreen = False
        #timers needed for the sprites to change between actions
        app.timerhitserve += 1
        app.timer += .5
        app.timer1 += .5

        if ball.ballinAirForServe:
            app.timerserve += 1
        
        #player serving
        if player.canServe:
            ballMovingForServe(app)
            ball.setX(player.X)
            if player.canHitServe:
                ball.serveShot(425)
                app.timerhitserve = 0
                app.timerserve = 0
            if player.canHitServe and ball.shotType == 'serve':
                player.ballinmotion()
            if ball.ballinAirForServe and ball.startY == 800:
                ball.FaultMethod()

        #opponent serving   
        if opponent.canServe:
            ballMovingForServe(app)
            opponent.canHitServeMethod(ball.startY)
            if opponent.canHitServe:
                ball.serveShot(500)
                app.timerhitserve = 0
            if ball.startY > app.height//6:
                opponent.ballinmotion()

        #check if the point needs to end
        checkifFault(app)
        checkifBallHitNet(app)
        checkifDoubleBounce(app)
        checkifOutofBounds(app)
        
        #opponent moving and opponent hitting ball
        if player.Hit == True and opponent.Hit == False:
            checkOppponentMovement(app)
            checkifBallHitOpponent(app)
            if opponent.canHitBall:
                app.timer1 = 0
                ball.opponentHit(player.X, player.Y, opponent.X, opponent.Y, ball.x, ball.startY)
                player.opponentHitShot()
                opponent.hitShot()
                opponent.determineTypeOfShot()

        #ball motion
        if ball.ballHit == True:
            checkifBallHit(app)
            if ball.holdBallPeriod < 2 and ball.onGround == True:
                ball.HoldPeriodAfterBounce()
            else:
                ball.onGround = False
                if player.Hit:
                    ball.changeMotion("player", court.court)
                else:
                    ball.changeMotion("opp",court.court)

#ball movement while serving 
def ballMovingForServe(app):
    if player.canServe:
        if 20 < app.timerhitserve < 50 and app.timerhitserve % 5 == 0:
            ball.goingUpForServe(20)
        elif 50 < app.timerhitserve < 80 and app.timerhitserve % 5 == 0:
            ball.goingDownForServe(20) 
    elif opponent.canServe:
        if 10 < app.timerhitserve < 80 and app.timerhitserve % 10 == 0:
            ball.goingUpForServe(20)
        elif app.timerhitserve < 160 and app.timerhitserve % 10 == 0:
            ball.goingDownForServe(20)
    

def checkifBallHitNet(app):
    ball.checkIfHitNet(app.height//2 - 40, app.height //2 + 40)
    if ball.hitNet:
        if opponent.Hit:
            changeScoreforPlayer(app)
        else:
            changeScoreforComputer(app)
        determineServer(app)
        newPoint(app)

#determining which person is serving the next point        
def determineServer(app):
    if (opponent.gamesWon + player.gamesWon) % 2 == 0:
        opponent.serveTime()
        player.opponentServeTime()
        ball.setforUpdatedServer(1,100)
        ball.setSize(5)
        if opponent.servingDuece:
            opponent.servingADMethod()
            player.receivingADMethod()
            ball.AD()
        else:
            opponent.servingDueceMethod()
            player.receivingDeuceMethod()
            ball.Duece()
    else:
        player.serveTime()
        opponent.playerServeTime()
        ball.setSize(7)
        ball.setforUpdatedServer(-1,800)
        if player.servingDuece:
            player.servingADMethod()
            opponent.receivingADMethod()
            ball.AD()
        else:
            player.servingDueceMethod()
            opponent.receivingDeuceMethod()
            ball.Duece()

def checkifFault(app):
    if ball.Fault:
        ball.stopBallMovementMethod()
        if ball.numofFaults == 1:
            if player.servingAD or player.servingDuece:
                player.serveTime()
                ball.setforUpdatedServer(-1,800)
            else:
                opponent.serveTime()
                ball.setforUpdatedServer(1,100)
            if ball.DueceSide:
                ball.Duece()
            else:
                ball.AD()
            redoServe(app)
        elif ball.numofFaults == 2:
            if opponent.Hit:
                changeScoreforPlayer(app)
            else:
                changeScoreforComputer(app)
            determineServer(app)
            newPoint(app)
    

def checkifDoubleBounce(app):
    if ball.numofBounce == 2 and ball.Fault == False:
        if opponent.Hit:
            changeScoreforComputer(app)
        else:
            changeScoreforPlayer(app)
        determineServer(app)
        newPoint(app)
    
def checkifOutofBounds(app):
    if ball.outofBounds and ball.Fault == False:
        if opponent.Hit:
            changeScoreforPlayer(app)
        else:
            changeScoreforComputer(app)
        determineServer(app)
        newPoint(app)

# methods for changing the score for player and opponent
def changeScoreforPlayer(app):
    if player.gameScore == 40 and opponent.gameScore == 40:
        player.gotoAD()
    elif opponent.gameScore == 'AD':
        opponent.gotoDuece()
    else:
        player.pointWon()
    if player.gameScore == 0:
        opponent.restartPoints()

def changeScoreforComputer(app):
    if player.gameScore == 40 and opponent.gameScore == 40:
        opponent.gotoAD()
    elif player.gameScore == 'AD':
        player.gotoDuece()
    else:
        opponent.pointWon()
    if opponent.gameScore == 0:
        player.restartPoints()
    
#making sure the opponent moves towards the ball and upwards and forewards dependent on the shot
def checkOppponentMovement(app):
    if opponent.X < ball.x:
        opponent.movingRightMethod()
    elif abs(opponent.X - ball.x) < 5:
        opponent.standingStillMethod()
    else:
        opponent.movingLeftMethod()

    if ball.shotType == 'topspin':
        if opponent.Y > 100:
            opponent.movingBackwardMethod()
    elif ball.shotType == 'slice':
        if opponent.Y < app.height//8 * 2.5:
            opponent.movingForewardMethod()
    elif ball.shotType == 'lob':
        if opponent.Y > 100:
            opponent.movingBackwardMethod()

#checking if the opponent can hit the ball
def checkifBallHitOpponent(app):
    if ball.updatedPosition < 100:
            if distance(ball.x, ball.startY, opponent.X, opponent.Y) < 60:
                opponent.canhitball()
            else:
                opponent.canthitball()

#checking if the player can hit the ball
def checkifBallHit(app):
    if player.Swung == True:
        if ball.updatedPosition < 100:
            if distance(ball.getBallX(), ball.getBallY(), player.X, player.Y) < 70:
                player.canhitball()
            else:
                player.cannothitball()
        else:
            player.cannothitball()

def onKeyPress(app,key):
    if app.directionsScreen or app.chooseCourtScreen or app.lostGame or app.wonGame:
        if key == 'r':
            app.directionsScreen = False
            app.chooseCourtScreen = False
            app.homeScreen = True
            app.lostGame = False
            app.wonGame = False
            opponent.restartPointsGame()
            player.restartPointsGame()
    # if app.gameScreen:
    #     #hitting a serve
    #     if key == 'space':
    #         player.canHitServeMethod(ball.startY)
    #     #topspin shot
    #     if key == '1':
    #         app.timer = 0
    #         player.swung()
    #         checkifBallHit(app)
    #         if player.canHitBall == True and player.Hit == False:
    #             ball.playerHitTopSpin()
    #             determineDirectionofBall(app)
    #             opponent.playerhitshot()
    #             player.hitshot()
    #     #slice shot
    #     elif key == '2':
    #         app.timer = 0
    #         player.swung()
    #         checkifBallHit(app)
    #         if player.canHitBall == True and player.Hit == False:
    #             ball.playerHitSlice()
    #             opponent.playerhitshot()
    #             determineDirectionofBall(app)
    #             player.hitshot()
    #     #lob shot
    #     elif key == '3':
    #         app.timer = 0
    #         player.swung()
    #         checkifBallHit(app)
    #         if player.canHitBall == True and player.Hit == False:
    #             ball.playerHitLob()
    #             determineDirectionofBall(app)
    #             opponent.playerhitshot()
    #             player.hitshot()

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** .5

#determinng the direction of the ball after the player hits the ball
def determineDirectionofBall(app):
    if player.movingRight == True:
        distancetoBall = distance(ball.getBallX(), ball.getBallY(), player.getX() + 30, player.getY() - 30)
    elif player.movingLeft == True:
        distancetoBall = distance(ball.getBallX(), ball.getBallY(), player.getX() - 30, player.getY() - 30)
    else:
        distancetoBall = distance(ball.getBallX(), ball.getBallY(), player.getX(), player.getY())
    if distancetoBall < 30:
        if opponent.X <= app.width//2:
            ball.setBalldx(player.X,.5, (app.width//6 * 5 - 15 - player.X)//150)
        else:
            ball.setBalldx(player.X, (app.width//6 + 15 - player.X)//150, -.5)
    elif distancetoBall < 40:
        ball.setBalldx(player.X,-3,3)
    elif distancetoBall < 70:
        ball.setBalldx(player.X, -3.5,3.5)
    else:
        ball.setBalldx(player.X, -4,4)

def onMousePress(app, mouseX, mouseY):
    if app.homeScreen:
        if 300 <= mouseX <= 700 and 550 <= mouseY <= 650:
            app.directionsScreen = True
            app.homeScreen = False
        elif 200 <= mouseX <= 800 and 725 <= mouseY <= 825:
            app.homeScreen = False
            app.chooseCourtScreen = True

    elif app.chooseCourtScreen:
        if (550 <= mouseX <= 950) and (200 <= mouseY <= 300):
            app.chooseCourtScreen = False
            app.gameScreen = True
            court.changeToClay()
            ball.changeCourtImpact(court.changeAfterBounce)
            app.outsidecourtColor = rgb(240,104,52)
            app.insidecourtColor = rgb(240,104,52)
        elif (550 <= mouseX <= 950) and (400 <= mouseY <= 500):
            app.chooseCourtScreen = False
            app.gameScreen = True
            court.changeToNormal()
            ball.changeCourtImpact(court.changeAfterBounce)
            app.outsidecourtColor = rgb(201, 85, 2)
            app.insidecourtColor = rgb(3, 143, 40)
        elif (550 <= mouseX <= 950) and (600 <= mouseY <= 700):
            app.chooseCourtScreen = False
            app.gameScreen = True
            court.changeToGrass()
            ball.changeCourtImpact(court.changeAfterBounce)
            app.insidecourtColor = rgb(129,200,62)
            app.outsidecourtColor = rgb(153,200,92)
        elif (550 <= mouseX <= 950) and (800 <= mouseY <= 900):
            app.chooseCourtScreen = False
            app.gameScreen = True
            court.changeToRubber()
            ball.changeCourtImpact(court.changeAfterBounce)
            app.outsidecourtColor = rgb(94,144,179)
            app.insidecourtColor = rgb(86,121,143)


def onKeyHold(app,keys):
    if app.gameScreen:
        if 'up' in keys:
            player.moveUp()
        elif 'down' in keys:
            player.moveDown()
        elif 'right' in keys:
            player.moveRight()
        elif 'left' in keys:
            player.moveLeft()
            
        if 'space' in keys:
            player.canHitServeMethod(ball.startY)
        #topspin shot
        if '1' in keys:
            app.timer = 0
            player.swung()
            checkifBallHit(app)
            if player.canHitBall == True and player.Hit == False and player.canServe == False:
                ball.playerHitTopSpin()
                determineDirectionofBall(app)
                opponent.playerhitshot()
                player.hitshot()
        #slice shot
        elif '2' in keys:
            app.timer = 0
            player.swung()
            checkifBallHit(app)
            if player.canHitBall == True and player.Hit == False and player.canServe == False:
                ball.playerHitSlice()
                opponent.playerhitshot()
                determineDirectionofBall(app)
                player.hitshot()
        #lob shot
        elif '3' in keys:
            app.timer = 0
            player.swung()
            checkifBallHit(app)
            if player.canHitBall == True and player.Hit == False and player.canServe == False:
                ball.playerHitLob()
                determineDirectionofBall(app)
                opponent.playerhitshot()
                player.hitshot()
        
    

def main():
    runApp()

main()
