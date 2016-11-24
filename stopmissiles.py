import getpass
print("Are you sure you want to stop the missiles from launching?? [yes|no]")
blah = ""
while(blah != "no"):
    blah = getpass.getpass("")
    if(blah == "yes"):
        print("Are you crazy?")
        print("Are you sure you want to stop the missiles from launching?? [yes|no]")
