from datetime import datetime

# Get Credentials
# 8/13/2025
# AUX-441

class Get_Credentials:
    def Credentials(self):
        try:
            Sender = input("Enter Sender Email Please :")
            Password = input("Enter Sender Password Please :")
            Receiver = input("Enter Receiver Email Please :")
            return Sender, Password, Receiver
        except Exception as e:
            print(f"Failed to Get Credentials : {e}")
            return None

