def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    elif employed == True and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False
    elif employed == False and vacation == True:
        return False

# L1: Set Alarm