#Class Password
# Author Scott Harrington
# Last Edit 3/14/2018
class Password:
    currentPassword=''
    boolAdmin= False

#
#
#
#
    def __init__(self, c:str):
        self.currentPassword= c
        self.boolAdmin = False
    
# createPassword
# take an input password and sets it to be the current password
# pre - currentPassword is whate ever it currently is 
# post - currentPassword = what ever password was
    def createPassword(self, password):
        self.currentPassword = password
        return password
        
#edit password
# edits the current password 
# pre - admin selects edit password
# post-  password has been edited to newPassword 
    def editPassword(self, currentPasswordCheck, newPassword, newPasswordCheck):
#Checks to see if admin is enabled
        if(self.boolAdmin == True):
#Checks to make sure admin is admin when changing password
            if(currentPasswordCheck == self.currentPassword):
# Checks to see if first enterd password is the same as the second entered password       
                if(newPassword == newPasswordCheck):
                   return self.createPassword(newPassword)# set the new password to be the current password
                else:
                    return
            else:
                return
        else:
            return
# enableAdmin
# enables admin for the person logged in
#pre - user not logged in 
#post- person is logged in as admin
    def enableAdmin(self, passwordEntered):
        if (passwordEntered == self.currentPassword):
             self.boolAdmin = True
             return True
            
        else:
            return False
