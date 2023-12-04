import random
import time

class Ball:
    def __init__(self):
        self.changedVelocityAfterBounce = 0
        self.startY = 100
        self.ballSize = 5
        self.ballColor = 'red'
        self.direction = 1
        self.x = 0
        self.dx = 0
        self.canvasheight = 0
        self.canvaswidth = 0
        self.scoreminimax = 0
        self.numofFaults = 0
        self.DueceSide = True
        self.ADSide = False
        self.courtImpact = 0
        self.Faultrestart()

    def Faultrestart(self):
        self.Fault = False
        self.shotType = 'topspin'
        self.initialVelocity = 600
        self.startingVelocity = 600
        self.changeinY = 0
        self.dy = .5
        self.velocityY = 0
        self.gravity = -10
        self.time = 1
        self.positiony = 150
        self.initialpositiony = 500
        self.updatedPosition = self.initialpositiony//100
        self.goingUp = True
        self.numofBounce = 0
        self.holdBallPeriod = 0
        self.onGround = False
        self.ballHit = False
        self.stopBallMovement = False
        self.hitNet = False
        self.ballinAirForServe = False
        self.outofBounds = False

    def restart(self):
        self.Faultrestart()
        self.numofFaults = 0
        

    def setHeightandWidth(self,width,height):
        self.canvasheight = height
        self.canvaswidth = width
    
    #randomize the original x and dx of the ball
    def randomizeX(self):
        self.x = random.randint(self.canvaswidth//6 + 200, self.canvaswidth//2)
        self.dx = 1 + random.random() * 4

    #opponent hit the ball. this is where the simple game AI is implement, as the 
    #minimaxSimple function is able to determine the most optimal shot to be played
    #based off the locations of the players
    def opponentHit(self, playerX, playerY, opponentX, opponentY, ballX, ballY):
        self.minimaxSimple(playerX, playerY, opponentX, opponentY, ballX, ballY)
        if self.shotType == 'slice':
            self.playerHitSlice()
        elif self.shotType == 'lob':
            self.playerHitLob()
        elif self.shotType == 'topspin':
            self.playerHitTopSpin()

    def HoldPeriodAfterBounce(self):
        self.dy = 0
        self.holdBallPeriod += 1
    
    def changeBallSize(self):
        if self.direction == 1:
            if self.ballSize < 8:
                self.ballSize += .03
        else:
            if self.ballSize > 4:
                self.ballSize -= .03
    
    def changeBallMovementY(self):
        if self.goingUp == True:
            self.dy += self.changeinY
        else:
            self.dy -= self.changeinY
        self.startY += (self.dy * self.direction)
    
    #the ball moving on the game screen, modeling the physics of the ball but not the part of the 
    #code modeling the real time velocity and postion of the ball. that is later on
    #line 123 shows the courtImpact making an impact on the velocity of the ball after a bounce, 
    #just like real life
    def changeMotion(self, person, court):
        if self.numofBounce < 2:
            self.changeBallSize()
            self.changeBallMovementY()
            if self.dy <= 0:
                self.holdBall()
                self.ballColor = 'green'
                self.time = 1
                self.numofBounce += 1

                if self.numofBounce == 1 and self.shotType == 'serve' and self.ADSide == True and (not(self.canvaswidth//6 + 15 < self.x < self.canvaswidth//2 + 5) or 
                                                 not(self.canvasheight//6 - 15 < self.startY < self.canvasheight//6 * 5 + 15)):
                    self.Fault = True
                    self.numofFaults += 1
                    self.stopBallMovementMethod()
                elif self.numofBounce == 1 and self.shotType == 'serve' and self.DueceSide == True and (not(self.canvaswidth//2 - 5  < self.x < self.canvaswidth//6 * 5 - 15 ) or 
                                                 not(self.canvasheight//6 - 15 < self.startY < self.canvasheight//6 * 5 + 15)):
                    self.Fault = True
                    self.numofFaults += 1
                    self.stopBallMovementMethod()
                elif person == 'opp' and self.numofBounce == 1 and (not(self.canvaswidth//6 - 20 < self.x < self.canvaswidth//6 * 5 + 20 ) or 
                                                 not(self.canvasheight//6 - 50 < self.startY < self.canvasheight//6 * 5 + 30)):
                    self.outofBounds = True
                    self.stopBallMovementMethod()
                elif person == 'player' and self.numofBounce == 1 and (not(self.canvaswidth//6 - 10 < self.x < self.canvaswidth//6 * 5 + 10 ) or 
                                                 not(self.canvasheight//6 - 50 < self.startY < self.canvasheight//6 * 5 + 30)):
                    self.outofBounds = True
                    self.stopBallMovementMethod()

                if self.numofBounce == 1:
                    self.initialVelocity = (self.startingVelocity // 4) * (self.changedVelocityAfterBounce + self.courtImpact)
                    if court == 'clay':
                        self.dx *= 1.15
            self.x += self.dx
            self.changeY()
            self.time+=1
        else:
            self.stopBallMovement = True

    
    def holdBall(self):
        self.onGround = True
    
    def stopBallMovementMethod(self):
        self.ballHit = False
        self.stopBallMovement = True

    #determining the real time of the ball using simple physics formula. the ball has an actual
    #position and characteristics that determines if the ball can clear the net and if the player 
    #can hit the ball when its a lob
    def changeY(self):
        if self.stopBallMovement == False:
            self.velocityY = self.initialVelocity + self.time * self.gravity
            tempposition = self.positiony
            self.positiony = self.initialpositiony + (self.velocityY * self.time +
                                        0.5 * self.gravity * self.time**1.1)
            if self.positiony > tempposition:
                self.goingUp = True
            else:
                self.goingUp = False
            self.updatedPosition = self.positiony//100

    def setColor(self,color):
        self.ballColor = color

    def playerHitTopSpin(self):
        self.initialVelocity = 650
        self.time = 1
        self.shotType = 'topspin'
        self.goingUp = True
        self.changeinY = .5
        self.dy = .5
        self.changedVelocityAfterBounce = 3
        self.initialposition = 500
        self.direction *= -1
        self.numofBounce = 0

    def playerHitSlice(self):
        self.initialVelocity = 550
        self.time = 1
        self.shotType = 'slice'
        self.goingUp = True
        self.changeinY = .5
        self.dy = .5
        self.changedVelocityAfterBounce = 1.5
        self.initialposition = 500
        self.direction *= -1
        self.numofBounce = 0

    def playerHitLob(self):
        self.initialVelocity = 950
        self.time = 1
        self.shotType = 'lob'
        self.goingUp = True
        self.changeinY = .25
        self.dy = .5
        self.changedVelocityAfterBounce = 3
        self.initialposition = 500
        self.direction *= -1
        self.numofBounce = 0
        
    def topSpinShot(self):
        self.shotType = 'topspin'
        self.changeinY = .5
        self.ballHit = True
        self.changedVelocityAfterBounce = 3

    def serveShot(self, velocity):
        self.shotType = 'serve'
        self.changeinY = .75
        self.ballHit = True
        self.changedVelocityAfterBounce = 3
        self.initialVelocity = velocity
        self.initialposition = 500
        self.numofBounce = 0

    def getBallX(self):
        return self.x
    
    def getBallY(self):
        return self.startY

    #set the ball's dx
    def setBalldx(self, location,  min, max):
        if location > self.canvaswidth//4 * 3:
            if 0 > min:
                max, min = 0, min
            else:
                max,min = min, 0
        elif location < self.canvaswidth // 4:
            min = 0 

        self.dx = min + random.random() * (max-min)

    def checkIfHitNet(self,minVal,maxVal):
        if minVal <= self.startY <= maxVal and abs(self.updatedPosition) < 60 and self.goingUp and self.shotType != 'serve':
            self.hitNet = True
        if self.hitNet == True:
            self.stopBallMovementMethod()

    #these two functions are used when the ball is going up and down for the serve
    def goingUpForServe(self, val):
        self.ballinAirForServe = True
        self.startY -= val
    
    def goingDownForServe(self, val):
        self.startY += val

    def setX(self, val):
        self.x = val
    
    def setforUpdatedServer(self,direction, startY):
        self.direction = direction
        self.startY = startY

    #updating the ball properties based on if its Duece or AD side
    def Duece(self):
        self.DueceSide = True
        self.ADSide = False
        self.x = random.randint(self.canvaswidth//6 + 200, self.canvaswidth//2 - 100)
        self.dx = 2 + random.random() * 4
        
    
    def AD(self):
        self.ADSide = True
        self.DueceSide = False
        self.x = random.randint(self.canvaswidth//2 + 100, self.canvaswidth//6 * 5 - 200)
        self.dx = -6 + random.random() * 4
        
    def setSize(self,value):
        self.ballSize = value


    #the one layer minimax function that runs through all the possible shots that can be played
    #and chooses the best one, there is a slight room of error when determinig the score so that the 
    # computer doesn't hit the pure optimal shot everytime. 
    def minimaxSimple(self, playerX, playerY, opponentX, opponentY, ballX, ballY):
        currMax = 0
        currMaxShot = None
        currMaxDirection = 0
        shots = ['topspin', 'slice', 'lob']
        directions = range(-5,5)
        for shot in shots:
            for direction in directions:
                self.determineShotScore(playerX, playerY, opponentX, opponentY, shot, direction, ballX, ballY)
                if self.scoreminimax >= currMax or currMaxShot == None:
                    currMax = self.scoreminimax
                    currMaxShot = shot
                    currMaxDirection = direction
        self.shotType = currMaxShot
        self.dx = currMaxDirection + random.random()
                

    def determineShotScore(self, playerX, playerY, opponentX, opponentY, shot, direction, ballX, ballY):
        if shot == 'topspin':
            if (not(self.canvaswidth//6 + 75 < ballX + direction * 37 < self.canvaswidth//6 * 5 - 75) or 
                    not(self.canvasheight//2 + 50 < ballY + 515 < self.canvasheight//6 * 5 - 50)):
                    self.scoreminimax = 0
                    newpositionx = 0
            else:
                newposition = (ballX + direction * 37, ballY + 511.5)
                newpositionx = newposition[0]
                newpositiony = newposition[1]
                self.scoreminimax = self.distance(playerX, playerY, newpositionx, newpositiony)
        elif shot == 'slice':
            if (not(self.canvaswidth//6 + 75 < ballX + direction * 25 < self.canvaswidth//6 * 5 - 75) or 
                    not(self.canvasheight//2 + 50 < ballY + 250 < self.canvasheight//6 * 5 - 50)):
                self.scoreminimax = 0
                newpositionx = 0
            else:
                newposition = (ballX + direction * 25, ballY + 250)
                newpositionx = newposition[0]
                newpositiony = newposition[1]
                self.scoreminimax = self.distance(playerX, playerY, newpositionx, newpositiony)
        elif shot == 'lob':
            if (not(self.canvaswidth//6 + 75 < ballX + direction * 75 < self.canvaswidth//6 * 5 - 75) or 
                    not(self.canvasheight//2 + 50 < ballY + 650 < self.canvasheight//6 * 5 - 50)):
                self.scoreminimax = 0
                newpositionx = 0
            else:
                newposition = (ballX + direction * 55, ballY + 600)
                newpositionx = newposition[0]
                newpositiony = newposition[1]
                self.scoreminimax = self.distance(playerX, playerY, newpositionx, newpositiony)

    def distance(self,x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2) ** .5
    
    def FaultMethod(self):
        self.Fault = True
        self.numofFaults += 1
        self.outofBounds = True
        self.stopBallMovementMethod()

    #the impact that the court makes on the ball
    def changeCourtImpact(self,val):
        self.courtImpact = val



    
    



