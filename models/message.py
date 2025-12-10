from datetime import datetime

class Message:
    def __init__(self, messageID, sender, receiver, content, time=None):
        self.messageID = messageID
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.time = str(datetime.now())

    def Dict(self):
        data = {}
        data["messageID"] = self.messageID
        data["sender"] = self.sender
        data["receiver"] = self.receiver
        data["content"] = self.content
        data["time"] = self.time
        return data