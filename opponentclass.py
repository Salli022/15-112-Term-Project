import random
from ballclass import * 

class Opponent:
    
    def __init__(self, width, height):
        self.setHeightandWidthofCanvasOpponent(width, height)
        self.X = 0
        self.Y = 0
        self.gamesWon = 0
        self.gameScore = 0
        self.canServe = True
        self.servingDuece = True
        self.servingAD = False
        self.receivingDuece = False
        self.receivingAD = False
        self.restart()
    
    def restart(self):
        self.Hit = False
        self.canHitBall = False
        self.dx = 0 
        self.BackHand = False
        self.ForeHand = False
        self.MovingRight = False
        self.MovingLeft = False
        self.StandingStill = True
        self.previousdx = 0
        self.canHitServe = False


    def setXandY(self, ballx, bally):
        if self.canServe:
            self.X = ballx 
            self.Y = bally - 60
        else:
            if self.receivingAD:
                self.X = random.randint(self.canvaswidth//6 + 30, self.canvaswidth//2 - 30)
                self.Y = 40
            else:
                self.X = random.randint(self.canvaswidth//2 + 30, self.canvaswidth//6 * 5 - 30)
                self.Y = 40


    def setHeightandWidthofCanvasOpponent(self,width,height):
        self.canvasheight = height
        self.canvaswidth = width

    def hitShot(self):
        self.Hit = True

    def playerhitshot(self):
        self.Hit = False
        self.canServe = False

    def ballinmotion(self):
        self.Hit = True
        self.canServe = False
    
    def canhitball(self):
        self.canHitBall = True

    def canthitball(self):
        self.canHitBall = False
    
    def movingRightMethod(self):
        self.dx = 3
        self.BackHand = False
        self.ForeHand = False
        self.MovingRight = True
        self.MovingLeft = False
        self.StandingStill = False
        self.X += self.dx

    def movingLeftMethod(self):
        self.dx = -3
        self.BackHand = False
        self.ForeHand = False
        self.MovingLeft = True
        self.MovingRight = False
        self.StandingStill = False
        self.X += self.dx

    def movingForewardMethod(self):
        self.Y += 4

    def movingBackwardMethod(self):
        self.Y -= 4

    def standingStillMethod(self):
        if self.dx == 3:
            self.previousdx = 3
        elif self.dx == -3:
            self.previousdx = -3
        self.dx = 0
        self.BackHand = False
        self.ForeHand = False

        self.X += self.dx

    def determineTypeOfShot(self):
        if self.previousdx == 0:
            pass
        elif self.dx == 3 or self.previousdx == 3:
            self.hitBackHand()
        elif self.dx == -3 or self.previousdx == -3:
            self.hitForeHand()

    def hitBackHand(self):
        self.BackHand = True

    def hitForeHand(self):
        self.ForeHand = True
    
    def canServeMethod(self):
        self.canHitServe = True
    
    def cannotServeMethod(self):
        self.canHitServe = False
    
    def serveTime(self):
        self.canServe = True
    
    def playerServeTime(self):
        self.canServe = False
    
    def canHitServeMethod(self, ballY):
        if ballY > self.Y and ballY - self.Y < 40:
            self.canHitServe = True

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
    
    

