from modelo.forms import *

class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state