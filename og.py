

import os #[+] Importing os

def linux():
    os.system("clear")
    print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("            Nmap Devil Scan                                 ")
    print("            Author: MrDestroyer [Mohammad Zim]              ")
    print("            Best tool for Nmap Scan                         ")
    print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print("")
    print("                  Scan List                                 ") 
    print("")
    print("------------------------------------------------------------")
    print("[1]Basic Scan")
    print("[2]Intense Scan")
    print("[3]Ping Scan")
    print("[4]Quick Scan")
    print("[5]Intense Scan v2(All TCP ports)")
    print("[6]Quick Scan Plus")
    print("[7]Quick traceroute")
    print("[8]Exit")
    print("-------------------------------------------------------------")


def loop():
    while True:
        linux()
        ask = input("[*]choose:-> ")

        if ask=="1":
            os.system("clear")
            ip = input("Enter Target ip: ")
            os.system("clear")
            os.system(f"nmap {ip}")
        elif ask=="2":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -A -T4 -v {ip}")
        elif ask=="3":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -sn {ip}")
        elif ask=="4":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -T4 -F {ip}")
        elif ask=="5":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -p 1-65535 -T4 -A -v {ip}")
        elif ask=="6":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -sV -T4 -O -F --version-light {ip}")
        elif ask=="7":
            os.system("clear")
            ip = input("Enter target ip: ")
            os.system("clear")
            os.system(f"nmap -sn --traceroute {ip}")
        elif ask=="8":
            break
        else:
            print("[*]Wrong Input!")
            linux()



def windows():
    os.system("cls")
    print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("            Nmap Devil Scan                                 ")
    print("            Author: MrDestroyer [Mohammad Zim]              ")
    print("            Best tool for Nmap Scan                         ")
    print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    print("")
    print("")
    print("                  Scan List                                 ") 
    print("")
    print("------------------------------------------------------------")
    print("[1]Basic Scan")
    print("[2]Intense Scan")
    print("[3]Ping Scan")
    print("[4]Quick Scan")
    print("[5]Intense Scan v2(All TCP ports)")
    print("[6]Quick Scan Plus")
    print("[7]Quick traceroute")
    print("[8]Exit")
    print("-------------------------------------------------------------")

hack = True
def loop2():

    while hack:
        windows()
        ask2 = input("[*]choose:-> ")
        if ask2=="1":
                os.system("cls")
                ip = input("Enter Target ip: ")
                os.system("clear")
                os.system(f"nmap {ip}")
                windows()
        elif ask2=="2":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("clear")
                os.system(f"nmap -A -T4 -v {ip}")
                windows()
        elif ask2=="3":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("cls")
                os.system(f"nmap -sn {ip}")
                windows()
        elif ask2=="4":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("cls")
                os.system(f"nmap -T4 -F {ip}")
                windows()
        elif ask2=="5":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("cls")
                os.system(f"nmap -p 1-65535 -T4 -A -v {ip}")
                windows()
        elif ask2=="6":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("cls")
                os.system(f"nmap -sV -T4 -O -F --version-light {ip}")
                windows()
        elif ask2=="7":
                os.system("cls")
                ip = input("Enter target ip: ")
                os.system("cls")
                os.system(f"nmap -sn --traceroute {ip}")
                windows()
        elif ask2=="8":
                break
        else:
                print("[*]Wrong Input!")
                windows()



q = input("Enter your os name: ")
if q == "kali linux" or "linux" or "parrot os" or "ubuntu linux" or "ubuntu" or "parrot security os":
    loop()
elif q=="windows" or "window":
    loop2()
else:
    print("[+]Wrong input !")



