class Court:

    def __init__(self):
        self.court = 'normal'
        self.changeAfterBounce = 0

    def changeToClay(self):
        self.court = 'clay'
        self.changeAfterBounce = -.25

    def changeToGrass(self):
        self.court = 'grass'
        self.changeAfterBounce = .1

    def changeToRubber(self):
        self.court = 'grass'
        self.changeAfterBounce = .2
    
    def changeToNormal(self):
        self.court = 'normal'
        self.changeAfterBounce = 0