import datetime
import subprocess
import time
import pyautogui
import pygetwindow

class Funcs:
    def __init__(self):
        self.FoundWindow = False
        self.Resetting = False

        self.MaxTimeoutSeconds = 15

        self.ClashIcon = "Images\ClashIcon.png"
        self.ClearAll = "Images\ClearAll.png"#      
        self.FindNewMembers = "Images\FindNewMembers.png"
        self.ClanWars = "Images\ClanWars.png"
        self.ClanWarLeague = "Images\ClanWarLeague.png"
        self.TrophyPushing = "Images\TrophyPushing.png"
        self.Search = "Images\Search.png"
        self.Invite = "Images\Invite.png"
        self.Back = "Images\Back.png"
        self.UnknownPlayer = r"Images\UnknownPlayer.png"
        self.HomeVillage = r"Images\HomeVillage.png"
        
    def gettime(self):
        current_time = datetime.datetime.now()
        time_string = "[" + current_time.strftime("%H:%M:%S") + "] "
        return time_string

    def print_log(self, txt):
        SendMsg = self.gettime() + txt + "\n"
        print(SendMsg)
        with open("error_log.txt", 'a') as log_file:  # Log to error_log.txt
            log_file.write(SendMsg)
    
    def WaitUntilImage(self, path, conf=0.7, gray=False):
        Timeout = 0
        while (pyautogui.locateCenterOnScreen(path, grayscale=gray, confidence=conf) is None):
            if Timeout >= self.MaxTimeoutSeconds:
                self.print_log("Max timeout reached by: " + path)
                self.ResetBlueStacks()
                break
            time.sleep(1)
            Timeout +=1
        return pyautogui.locateCenterOnScreen(path, grayscale=gray, confidence=conf)

    def CheckWindow(self):
        if (pygetwindow.getWindowsWithTitle("BlueStacks App Player")):
            self.FoundWindow = True
            return True
        else:
            self.FoundWindow = False
            return False
        
    def CheckImage(self, path, conf=0.7, gray=False):
        img = pyautogui.locateCenterOnScreen(path, grayscale=gray, confidence=conf)
        if img is None:
            return False
        return img
    
    def Click(self, image, amt=1):
        if not image: return
        for i in range(0,amt):
            time.sleep(0.5)
            pyautogui.click(image.x, image.y)
        
    def ResetBlueStacks(self):

        window = pygetwindow.getWindowsWithTitle("BlueStacks App Player")[0]
        try:
            window.activate()
        except Exception as e:
            self.print_log("Error: " + str(e))
        newwindow = pygetwindow.getActiveWindow()
        newwindow.maximize()
        self.WaitUntilImage(self.ClashIcon)
        pyautogui.hotkey('ctrlleft', 'shiftleft', '5')
        img = self.WaitUntilImage(self.ClearAll)
        self.Click(img)
        img = self.WaitUntilImage(self.ClashIcon)
        self.Click(img)
        time.sleep(1)
        self.Resetting = False
    
    def CheckReload(self, event=None):
        img = self.CheckImage(self.Reload)
        if img:
            self.Click(img)
            self.print_log("Had me reload, there was possibly an error...")
            return True
        return False


    def Start(self):
        if self.Resetting: return

    def Scroll(self):
        pyautogui.moveTo(900, 700)
        time.sleep(0.1)
        for i in range(0,3):
            if self.CheckImage(self.HomeVillage): self.Click(self.WaitUntilImage(self.Back))
            pyautogui.scroll(-1)
            pyautogui.scroll(-1)
            time.sleep(0.1)

    def ScrollUp(self):
        for i in range(0,10):
            if self.CheckImage(self.HomeVillage): self.Click(self.WaitUntilImage(self.Back))
            pyautogui.mouseDown(955, 530)
            pyautogui.moveTo(955, 1000)
            pyautogui.mouseUp()
            time.sleep(0.5)

    def SendInvite(self):
        time.sleep(0.2)
        if self.CheckImage(self.UnknownPlayer): 
            self.Click(self.WaitUntilImage(self.Back))
            return
        if self.CheckImage(self.HomeVillage): 
            self.Click(self.WaitUntilImage(self.Invite))
            self.Click(self.WaitUntilImage(self.Back))
    
    def StartInvite(self, Even):
        if self.CheckImage(self.HomeVillage): self.Click(self.WaitUntilImage(self.Back))
        self.Click(self.WaitUntilImage(self.ClanWarLeague))
        self.Click(self.CheckImage(self.Search))

        while not self.CheckImage(self.Search, gray=True): time.sleep(0.5)

        for i in range(0,4):
            pyautogui.click(910, 539)
            self.SendInvite()
            pyautogui.click(956, 664)
            self.SendInvite()
            pyautogui.click(957, 785)
            self.SendInvite()
            pyautogui.click(956, 908)
            self.SendInvite()
            pyautogui.click(956, 1015)
            self.SendInvite()
            time.sleep(1)
            self.Scroll()
            time.sleep(1)
        if self.CheckImage(self.HomeVillage): self.Click(self.WaitUntilImage(self.Back))
        self.ScrollUp()


if __name__ == "__main__":
    self = Funcs()
    #self.ResetBlueStacks()
    self.Click(self.WaitUntilImage(self.FindNewMembers))
    CurrentlyOn = 0
    Even = False
    self.Click(self.WaitUntilImage(self.ClanWars))
    time.sleep(0.5)
    self.Click(self.WaitUntilImage(self.TrophyPushing))
    self.Click(self.CheckImage(self.Search))
    while True:
        Even = False
        if CurrentlyOn % 2 == 0: Even = True
        time.sleep(0.5)
        self.StartInvite(Even)
        