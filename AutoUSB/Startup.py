import sys
import os
# Program Name          AutoUSB
# Program Purpose       To make a program that will make folders for a usb automatically.
# Program Date          2/03/2021 Justin Foss
print("Users System:",sys.platform)
ST=input("Press enter to start.")
print()
USBdir=input("Input the path to your usb.: ")
os.chdir(USBdir)
os.mkdir("Home")
os.mkdir("Work")
os.chdir("Home")
os.mkdir("Movies")
os.mkdir("Games")
os.mkdir("Misc")
os.chdir("..")
os.chdir("Work")
wkDir=int(input("How many work folders do you want? (Includes WorkFolder0): "))
wkDirMx=0
wkDirNum=-1
while wkDirMx<=wkDir:
    wkDirNum += 1
    os.mkdir("WorkFolder"+str(wkDirNum))
    wkDirMx+=1

os.chdir("..")
f=open("Worked.txt","w+")
f.write("Congrates it is finished.\n")
f.write("It worked if you are seeing this.\n")
f.write("You can delete this. I hope you like this little tool.\n")
f.write("I just made this in my free time.")# End Of Code