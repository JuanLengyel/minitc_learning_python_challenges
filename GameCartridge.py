class GameCartridge:

    SEVERE_DETRIMENTAL_ACTION = -3.5
    MODERATE_DETRIMENTAL_ACTION = -2.0
    LIGHT_DETRIMENTAL_ACTION = -0.5
    SEVERE_BENEFICIAL_ACTION = 3.3
    MODERATE_BENEFICIAL_ACTION = 1.7
    LIGHT_BENEFICIAL_ACTION = 0.5

    def __init__(self, gameName, savedData, size, status):
        self.__gameName = gameName
        self.__savedData = savedData
        self.__size = size
        self.__status = status
    
    def getGameName(self):
        return self.__gameName
    def getSavedData(self):
        return self.__savedData
    def getSize(self):
        return self.__size
    def getStatus(self):
        return self.__status

    def setGameName(self, gameName):
        self.__gameName = gameName
    def setSavedData(self, savedData):
        self.__savedData = savedData
    def setSize(self, size):
        self.__size = size
    def setStatus(self, status):
        self.__status = status

    def loadGameData(self):
        self.setStatus(self.getStatus() + LIGHT_DETRIMENTAL_ACTION)

        if self.__status < 0.6:
            raise ValueError("Cartridge status ({0}) is way to low to work. Try blowing it!".format(self.__status))

        return self.getSavedData()

    def blowCartridge(self):
        self.setStatus(self.getStatus() + LIGHT_BENEFICIAL_ACTION)