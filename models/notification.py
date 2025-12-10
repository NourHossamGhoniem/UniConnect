class Notification:
    def __init__(self, notifID, userEmail, message, isRead="False"):
        self.notifID = notifID
        self.userEmail = userEmail
        self.message = message

    def Dict(self):
        data = {}
        data["notifID"] = self.notifID
        data["userEmail"] = self.userEmail
        data["message"] = self.message
        return data
