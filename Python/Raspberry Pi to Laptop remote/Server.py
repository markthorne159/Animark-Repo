import socket
import pyautogui
import time
import subprocess

class LaptopCapture():

    #Set self as host variable.
    #Set this to devices own IP address.
    Host = ''
    #Find devices IP to make it easier for remote to connect.
    DeviceIP = ''
    #Set unused port for connection
    Port = 9999
    #Integer variable for timers.
    Timer = 0

    def __init__(self):
        self.DeviceIP = self.GetIP()
        print "Setting up: %s" % self.DeviceIP

    def Setup(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((self.Host,self.Port))
        print 'Socket open on %s' % self.Host
        #Listen for a single connection.
        s.listen(1)

        conn, addr = s.accept()
        print "Received connection!"

        while True:
            #Setup a buffer to recieve commands.
            Command = conn.recv(1024)
            print Command
            self.Snap(Command)

    #Call this function to snap photo.
    def Snap(self,Command):
        
        #Split command to check for additional commands.
        Splits = Command.split(" ")
        print Splits

        #If multiple commands are sent then set other variables.
        if len(Splits) > 0:
            self.Timer = int(Splits[0])
            print "Sleeping for: %d" % self.Timer
            time.sleep(self.Timer)
            if "snap" in Splits:
                print "Command received!"
                #Use keyboard button to quickly take photo.
                pyautogui.press("space")
                print "Photo taken!"

    def GetIP(self):
        IP = subprocess.check_output("ipconfig")
        IP = IP.split("\n")

        for i in IP:
            if "adapter WiFi" in i:
                #print IP[IP.index(i) + 4]
                IP = IP[IP.index(i) + 4]
                return IP

Capturer = LaptopCapture()
Capturer.Setup()

            
