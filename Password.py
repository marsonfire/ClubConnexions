#Class Password
# Author Scott Harrington
# Last Edit 3/14/2018
class _Password:
    currentPassword='temp'
    boolAdmin = False


# createPassword
# take an input password and sets it to be the current password
# pre - currentPassword is whate ever it currently is 
# post - currentPassword = what ever password was
    def createPassword(password):
        currentPassword = password
        
#edit password
# edits the current password 
# pre - admin selects edit password
# post-  password has been edited to newPassword 
    def editPassword(currentPasswordCheck, newPassword, newPasswordCheck):
#Checks to see if admin is enabled
        if(boolAdmin == True):
#Checks to make sure admin is admin when changing password
            if(currentPasswordCheck == currentPassword):
# Checks to see if first enterd password is the same as the second entered password       
                if(newPassword == newPasswordCheck):
                    createPassword(newPassword)# set the new password to be the current password
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
    def enableAdmin(passwordEntered):
        if (passwordEntered == currentPassword):
            boolAdmin = True
            return
        else:
            return
