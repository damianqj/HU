def new_password(oldpassword,newpassword):
    if newpassword == oldpassword:
        return 'False'

    if len(newpassword) > 6:
        return 'True'

print(new_password('kaaskop','stoeptegel'))













