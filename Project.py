from random import *
print("<=================================== WELCOME TO R RAILLINE ============================================>")
ticket=[]
def book():
    ch=int(input("How many ticket do u want to book? : "))
    date = input("Enter Departure Date (YYYY-MM-DD): ")
    start=input("Enter Starting station : ")
    end=input("Enter Ending Station : ")
    for i in range(ch):
        name=input("Traveller name : ")
        age=input("Enter travellers age : ")
        temp=[name,age,signup[1],date,start,end]
        ticket.append(temp)
        print(i+1," Ticket Booked")
    print("All tickets Booked. Now go to generate section and get your ticket")
    print("==================")
    m()
def cancel():
    l=len(ticket)
    for i in range(l):
        print(i+1,ticket[i],"\n")
    ch=int(input("Enter ticket number to cancel : "))
    ch=ch-1
    try:
        ticket.pop(ch)
        print("1 ticket cancelled")
        print("===============")
        m()
    except:
        print("Error Occured try again")
        print("=============")
        m()

#report issue
def issue():
    problem=input("Enter Your Issue : ")
    try:
        print("Report Submitted Successfully\n")
        m()
    except:
        print("Failed to submit\n")

def generate():
    l=len(ticket)
    for i in range(l):
        print(i+1,ticket[i],"\n")
    ch=int(input("How many tickets do u want to generate : "))
    for i in range(ch):
        co=int(input("Enter your ticket Number : "))
        t=ticket[co-1]
        print(t, "Ticket will be generated with these details.")
        name=t[0]
        age=t[1]
        phone=t[2]
        date=t[3]
        start=t[4]
        end=t[5]
        file=open("Rail_Ticket_"+name+".txt","w+")
        file.write("<-----------********----------->\nNOTE:-->Don't try to make a fake ticket. Tc will get to know if the ticket is fake or real.\nTicket id : "+str(i+1)+"\nName : "+name+"\nAge : "+age+"\nDeparture : "+date+"\nFrom : "+start+"\nTo :"+end+"\n<--------------************------------->")
        file.close()
        print(i+1, "Ticket generated.")
    print("Successfully generated all the tickets.")
    print("================")
    m()

def phone_up():
    ch=input("Enter Your new Phone Number : ")
    signup[1]=ch
    print("Successfully Updated")
    print("====================")
    m()

def password_up():
    ch=input("Enter Your new Password : ")
    signup[2]=ch
    print("Successfully Updated")
    print("====================")
    m()

def out():
    menu()

def delete():
    signup.clear()
    print("Account Deleted successfully")
    print("===================")
    menu()

def m():
    print("1. Book Ticket\n2. Cancel Ticket\n3. Generate Your Ticket\n4. Update Phone\n5. Update Password\n6. Logout\n7. Delete Account\n8. Report Issue")
    ch=int(input("Enter Your Choice : "))
    if(ch==1):
        book()
    elif(ch==2):
        cancel()
    elif(ch==3):
        generate()
    elif(ch==4):
        phone_up()
    elif(ch==5):
        password_up()
    elif(ch==6):
        out()
    elif(ch==7):
        delete()
    elif(ch==8):
        issue()
    else:
        print("Wrong input choosen try again")
        print("=================")
        m()

def login():
    phone=input("Enter your phone : ")
    password=input("Enter your password : ")
    if(phone==signup[1] and password==signup[2]):
        print("Logged in successfully")
        print("===========")
        m()
    else:
        print("Wrong Details")
        print("=============")
        menu()

def signup():
    global signup
    name=input("Enter your name : ")
    phone=input("Enter your Phone : ")
    password=input("Enter your Password : ")
    signup=[name,phone,password]
    r1=randrange(100,200)
    r2=randrange(100,200)
    print("Prove You are not robot ",r1,"+",r2)
    user_ans=int(input("Enter your Ans : "))
    if user_ans==r1+r2:
        print("Sign Up successful. Now login Please")
        print("================")
        menu()

def menu():
    print("1. Sign Up\n2. Login")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        signup()
    elif(ch==2):
        login()
    else:
        print("Wrong Choice")
        print("===============")
menu()
menu()
