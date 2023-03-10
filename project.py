import time,sys,os,maskpass,pyfiglet
from yachalk import chalk
from InquirerPy import inquirer
msg="WELCOME TO THE BAKERY MANAGEMENT SYSTEM"
print(pyfiglet.figlet_format(msg, font="digital"))
for char in msg:
    sys.stdout.write(chalk.blue.bg_magenta.bold.italic.underline(char))
    time.sleep(0.05)
time.sleep(0.2)   
import pandas as pd
import matplotlib.pyplot as plt
print()
n1=0
n7=input(chalk.bg_cyan_bright('ENTER YOUR NAME:\n'))
n8=0

n8=maskpass.advpass(prompt=chalk.bg_cyan_bright("ENTER THE PASSWORD:"),mask="*")

while n8!='qwerty':
    print(chalk.rgb(255,87,51).bold("TRY AGAIN!!!!"))
    
    n8=maskpass.advpass(prompt=chalk.bg_cyan_bright("ENTER THE PASSWORD:"),mask="*")

    print("---------------------------------------------------------------------------------------------------------------------------")
    # print("---------------------------------------------------------------------------------------------------------------------------")
    # print("---------------------------------------------------------------------------------------------------------------------------")
    while n1!="Exit The System":  
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------------------------------------------")
        n1 = inquirer.select(
        message="SELECT YOUR CHOICE",
        choices=["The Sales Report", "The List of Items in Shop", "Update the List of Items in Shop", "Profit Calculator","The Maximum,Minimum,Total of the Sales","Exit The System"],
        ).execute()

        print("---------------------------------------------------------------------------------------------------------------------------")

        if n1=="The Sales Report":
            df=pd.read_csv("Book11.csv")
            df.plot(kind='bar',color='Yellow',edgecolor='Black',linestyle='dashed',linewidth=1)
            ticks = df.index.tolist()
            plt.xticks(ticks,df.Months)
            plt.title('MONTHLY SALES REPORT')
            plt.ylabel('Sales(in Rs)')
            plt.xlabel('Months')
            plt.grid(True)
            plt.show()

        elif n1=="The List of Items in Shop":
            print("---------------------------------------------------------------------------------------------------------------------------")
            # print("---------------------------------------------------------------------------------------------------------------------------")
            n2=inquirer.select(message="SELECT YOUR CHOICE",choices=["CAKES", "SNACKS" , "BEVERAGES"],).execute()
            print("---------------------------------------------------------------------------------------------------------------------------")

            if n2=="CAKES":
                Cakes=pd.read_csv("cakes.csv")
                print(Cakes)
            elif n2=="SNACKS":
                Snacks=pd.read_csv("snacks.csv")
                print(Snacks)
            elif n2=="BEVERAGES":
                Beverages=pd.read_csv("B1.csv")
                print(Beverages)
                # print("---------------------------------------------------------------------------------------------------------------------------")
            else:
                print(chalk.red_bright('VALUE ERROR! PLEASE CHECK'))  
                # print("---------------------------------------------------------------------------------------------------------------------------")      
                
        elif n1=="Update the List of Items in Shop":
            import os
            # print("---------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------")
            n3=inquirer.select(message="SELECT YOUR CHOICE",choices=["CAKES","SNACKS","BEVERAGES"],).execute()
            print("---------------------------------------------------------------------------------------------------------------------------")

            if n3=="CAKES":
                os.system("start cakes.csv")
            elif n3=="SNACKS":
                os.system("start snacks.csv")
            elif n3=="BEVERAGES":
                os.system("start B1.csv")
                print("---------------------------------------------------------------------------------------------------------------------------")
            else:
                print(chalk.red_bright('VALUE ERROR! PLEASE CHECK'))    
                
        elif n1=="Profit Calculator":
            # print("---------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------")
            n3=inquirer.select(message="SELECT YOUR CHOICE",choices=["To Get the Net Profit", "To Get Profit Per Item"],).execute()
            # print("---------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------")

            if n3=="To Get the Net Profit":
                c1=int(input(chalk.bg_cyan_bright("Enter the Number of Cakes Sold:\n")))
                c2=int(input(chalk.bg_cyan_bright("Enter the Number of Snacks Sold:\n")))
                c3=int(input(chalk.bg_cyan_bright("Enter the Number of Beverages Sold:\n")))
                print(chalk.bg_blue("Net Profit= Rs",(c1*50)+(c2*20)+(c3*60)))
                # print("---------------------------------------------------------------------------------------------------------------------------")
                # print("---------------------------------------------------------------------------------------------------------------------------")
            elif n3=="To Get Profit Per Item":
                n4=inquirer.select(message="SELECT YOUR CHOICE",choices=["CAKES","SNACKS","BEVERAGES"],).execute()

                if n4=="CAKES":
                    n5=int(input(chalk.bg_cyan_bright("Enter the Number of Cakes Sold:\n")))
                    print(chalk.bg_blue("Net Profit is=Rs",n5*50))
                    # print("---------------------------------------------------------------------------------------------------------------------------")
                    # print("---------------------------------------------------------------------------------------------------------------------------")
                elif n4=="SNACKS":
                    n6=int(input(chalk.bg_cyan_bright("Enter the Number of Snacks Sold:\n")))
                    print(chalk.bg_blue("Net Profit is=Rs",n6*20))
                    # print("---------------------------------------------------------------------------------------------------------------------------")
                    # print("---------------------------------------------------------------------------------------------------------------------------")
                elif n4=="BEVERAGES":
                    n7=int(input(chalk.bg_cyan_bright("Enter the Number of Beverages Sold:\n")))
                    print(chalk.bg_blue("Net Profit is=Rs",n7*60))
                    # print("---------------------------------------------------------------------------------------------------------------------------")
                    # print("---------------------------------------------------------------------------------------------------------------------------")
            else:
                print(chalk.red_bright('VALUE ERROR! PLEASE CHECK'))
                print("---------------------------------------------------------------------------------------------------------------------------")

        elif n1=="The Maximum,Minimum,Total of the Sales":
            print("---------------------------------------------------------------------------------------------------------------------------")
            df = pd.read_excel("Book1.xlsx")    
            print(chalk.bg_blue("Net Sales:Rs",df["Sales"].sum()))
            time.sleep(0.4)
            print()
            print(chalk.bg_blue("Maximum Sales with Month:\n",df.max()))
            time.sleep(0.4)
            print()
            print(chalk.bg_blue("Minimum Sales With Month:\n",df.min()))
            # print("---------------------------------------------------------------------------------------------------------------------------")
            
        elif n1=="Exit The System":
            os.system('cls')
            time.sleep(1)
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print(chalk.magenta("THANK YOU"),chalk.rgb(255,0,255).bold.italic(n7),chalk.magenta("FOR USING B.M.S......."))
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------------------------------------")
        else:
            print(chalk.red_bright('VALUE ERROR! PLEASE CHECK'))

    if n8!='qwerty':
        print(chalk.rgb(255,87,51).bold("TRY AGAIN!!!!"))
        



            
