from core.file_manager import FileManager
from models.message import Message
from models.notification import Notification
import random

class MessageRepository:
    def __init__(self):
        self.fm = FileManager()
        self.msgFile = "messages.csv"
        self.notifFile = "notifications.csv"

    def send_message(self, sender, receiver, content):
        msgID = random.randint(1000, 9999)
        newMSG = Message(msgID, sender, receiver, content)
        msgColumns = ["messageID", "sender", "receiver", "content", "time"]
        self.fm.append_csv(self.msgFile, newMSG.Dict(), msgColumns)
        self.createNotif(receiver, f"New message from {sender}")

    def createNotif(self, userEmail, text):
        notifID = random.randint(1000, 9999)
        newNotif = Notification(notifID, userEmail, text)
        notifColumns = ["notifID", "userEmail", "message"]
        self.fm.append_csv(self.notifFile, newNotif.Dict(), notifColumns)
        
    def getMSG(self, userEmail):
        allMSGs = self.fm.read_csv(self.msgFile)
        MsgList = []
        for msg in allMSGs:
            if msg['receiver'] == userEmail:
                MsgList.append(msg)
                
        return MsgList

    def getNotif(self, userEmail):
        allNotifs = self.fm.read_csv(self.notifFile)
        NotifList = []
        for notif in allNotifs:
            if notif['userEmail'] == userEmail:
                NotifList.append(notif)
                
        return NotifList