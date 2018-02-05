import apt

BooleanApplication = {"nmap":False}

#Checks for what dependancies are installed
def ApplicationCheck(BooleanApplication):
    cache = apt.Cache()
    ApplicationList = []
    for Application in BooleanApplication.keys():
        if cache[Application].is_installed:
            BooleanApplication[Application] = True
    return BooleanApplication
BooleanApplication = ApplicationCheck(BooleanApplication)
