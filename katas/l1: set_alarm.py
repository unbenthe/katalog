def set_alarm(employed, vacation):
    if employed == True:
        if vacation == True:
            return False
        if vacation == False:
            return True
    if employed == False:
        return False


#Eu esqueço que a ordem é importante pros katas e isso me custa tempo, precioso tempo que não retorna quando perdido
