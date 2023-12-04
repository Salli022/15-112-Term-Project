import random

class Player:
    
    def __init__(self,width,height):
        self.setHeightandWidthofCanvasPlayer(width,height)
        self.X = self.canvaswidth//4 * 3
        self.canServe = False
        self.gamesWon = 0
        self.gameScore = 0
        self.receivingDuece = True
        self.receivingAD = False
        self.servingDuece = False
        self.servingAD = False
        self.restart()
    
    def restart(self):
        self.Y = 800
        self.canHitBall = False
        self.Swung = False
        self.Hit = False
        self.movingLeft = False
        self.movingRight = False
        self.canHitServe = False

    def setXandY(self,ballx,bally):
        if self.canServe:
            self.X = ballx - 50
            self.Y = bally
        else:
            if self.receivingAD:
                self.X = random.randint(self.canvaswidth//6 + 30, self.canvaswidth//2 )
            else:
                self.X = random.randint(self.canvaswidth//2, self.canvaswidth//6 * 5 - 30)

    def setHeightandWidthofCanvasPlayer(self,width,height):
        self.canvasheight = height
        self.canvaswidth = width

    def moveUp(self):
        if self.Y >= self.canvasheight//2 and self.canServe == False:
            self.Y -= 5
        self.movingLeft = False
        self.movingRight = False
        self.Swung = False

    def moveDown(self):
        if self.canServe == False:
            self.Y += 5
        self.movingLeft = False
        self.movingRight = False
        self.Swung = False

    def moveRight(self):
        self.X += 5
        self.movingLeft = False
        self.movingRight = True
        self.Swung = False


    def moveLeft(self):
        self.X -= 5
        self.movingLeft = True
        self.movingRight = False
        self.Swung = False

    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y

    def swung(self):
        self.Swung = True

    def hitshot(self):
        self.Hit = True
    
    def opponentHitShot(self):
        self.Hit = False

    def canhitball(self):
        self.canHitBall = True

    def cannotServeMethod(self):
        self.canServe = False

    def cannothitball(self):
        self.canHitBall = False

    def serveTime(self):
        self.canServe = True
    
    def opponentServeTime(self):
        self.canServe = False
    
    def pointWon(self):
        if self.gameScore == 0 or self.gameScore == 15:
            self.gameScore += 15
        elif self.gameScore == 30:
            self.gameScore += 10
        elif self.gameScore == 40 or self.gameScore == 'AD':
            self.gameScore = 0
            self.gamesWon += 1

    def restartPoints(self):
        self.gameScore = 0

    def gotoAD(self):
        self.gameScore = 'AD'
    
    def gotoDuece(self):
        self.gameScore = 40
    
    def ballinmotion(self):
        self.Hit = True
        self.canServe = False

    def canHitServeMethod(self, ballY):
        if ballY < self.Y and self.Y - ballY < 100:
            self.canHitServe = True

    def servingADMethod(self):
        self.servingDuece = False
        self.servingAD = True
        self.receivingDuece = False
        self.receivingAD = False
    
    def servingDueceMethod(self):
        self.servingDuece = True
        self.servingAD = False
        self.receivingDuece = False
        self.receivingAD = False
    
    def receivingDeuceMethod(self):
        self.receivingDuece = True
        self.receivingAD = False
        self.servingDuece = False
        self.servingAD = False

    def receivingADMethod(self):
        self.receivingDuece = False
        self.receivingAD = True
        self.servingDuece = False
        self.servingAD = False
    
    def restartPointsGame(self):
        self.gamesWon = 0
        self.gameScore = 0