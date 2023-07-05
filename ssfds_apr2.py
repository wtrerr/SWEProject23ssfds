import sqlite3
import os



conn=sqlite3.connect("ssfds.db")

cursor=conn.cursor()
'''
########################################
sql queries

for making table
ACCOUNTS

CREATE TABLE accounts(
    username VARCHAR(32) PRIMARY KEY,
    password VARCHAR(20) NOT NULL,
    acc_name VARCHAR(32) NOT NULL,
    type DOUBLE NOT NULL
);
------
trial accounts i used
    root root1234 trial1 1
    root root5678 trial2 1

------
insert account into accounts

"INSERT INTO accounts (username, password, acc_name,type) VALUES();".format(username,password,acc_name,type)


######################################
'''
showtables="SELECT name FROM sqlite_master WHERE type='table';"

make_accounts="""CREATE TABLE accounts(
    username VARCHAR(32) PRIMARY KEY,
    password VARCHAR(20) NOT NULL,
    acc_name VARCHAR(32) NOT NULL,
    type DOUBLE NOT NULL
);"""


make_foods="""CREATE TABLE foods(
    food_code VARCHAR(9) PRIMARY KEY,
    food_item VARCHAR(32) NOT NULL,
    plate_price double NOT NULL,
    plates integer NOT NULL,
    lat integer NOT NULL,
    long integer NOT NULL
);"""

def show_table(table):
    
    cursor.execute("SELECT * FROM {};".format(table))
    conn.commit()
    rows=(cursor.fetchall())
    for entry in rows:
        print(entry)

def signup():
    print("signing up")
    while True:
        username=''
        password=''
        acc_name=''
        type=0
        
        confirm=0
        while(len(username)==0 or len(username)>32 or confirm=='0'):
            username=input("Please enter your USERNAME (1-32 characters): \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
        
        confirm=0
        while(len(password)==0 or len(password)>20 or len(password)<8 or confirm=='0'):
            password=input("Please enter your PASSWORD (8-20 characters): \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(len(acc_name)==0 or len(acc_name)>32 or confirm=='0'):
            acc_name=input("Please enter your ACCOUNT NAME (8-20 characters): \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(type==0 or confirm=='0'):
            type=input("Define ACCOUNT TYPE (1 for Restaurant, 2 for Individual, 3 for NGO: \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            if type==2.0:
                type=0.8
            elif type==3.0:
                type=0.6
            if (type!=1.0 or type!=0.8 or type!=0.6):
                confirm=0
                
        try:
            add_account="INSERT INTO accounts (username, password, acc_name,type) VALUES(?,?,?,?);"
            cursor.execute(add_account,(username,password,acc_name,type))
            conn.commit()
            print("added ACCOUNT to DATABASE")
            break
        except sqlite3.IntegrityError:
            print("Username already exists, try another")
            continue
    
    
def login():
    print("logging in")
    username=''
    password=''
    exist=False
    
    while(not exist):
        username=''
        password=''
        exist=False   
        confirm=0
        while(len(username)==0 or len(username)>32 or confirm=='0'):
            username=input("Please enter your USERNAME (1-32 characters): \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(len(password)==0 or len(password)>20 or len(password)<8 or confirm=='0'):
            password=input("Please enter your PASSWORD (8-20 characters): \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
        
        user_exists="SELECT * from accounts WHERE username=? AND password=?;"
        cursor.execute(user_exists,(username,password))
        conn.commit()
        results=cursor.fetchall()
        exist=False if results==[] else True
        if(not exist):
            print("user does not exist, please re-enter redentials")
            pass
        else:
            print("{user} logged in".format(user=results[0][0]))
            return((results[0]))

    
    pass #delete when made


def del_acc(username,password):
    print(username)
    delete_user="DELETE FROM accounts WHERE username=? and password=?;"
    deleted_accs=cursor.execute(delete_user,(username,password))
    conn.commit()
    print("affected {} rows".format(deleted_accs.rowcount))
    

    
    
    pass #delete when made      


def delete():
    print("deleting accoun")
    username=''
    password=''
    exist=False
    username=''
    password=''
    exist=False   
    confirm=0
    while(len(username)==0 or len(username)>32 or confirm=='0'):
        username=input("Please enter your USERNAME (1-32 characters): \t")
        confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
        
    confirm=0
    while(len(password)==0 or len(password)>20 or len(password)<8 or confirm=='0'):
        password=input("Please enter your PASSWORD (8-20 characters): \t")
        confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
    
    user_exists="SELECT * from accounts WHERE username=? AND password=?;"
    cursor.execute(user_exists,(username,password))
    conn.commit()
    results=cursor.fetchall()
    exist=False if results==[] else True
    del_acc(username,password)

    
    pass #delete when made 


def add_dish():
    print("adding dish")
    while True:
        food_item=''
        plate_price=0.0
        plates=0
        lats=0
        longs=0
        
        confirm=0
        while(len(food_item)==0 or confirm=='0'):
            food_item=input("Please enter name of food item: \t")
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
        
        confirm=0
        while(plate_price<=0 or confirm==0):
            plate_price=(float)(input("Please enter plate price: \t"))
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(plates<=0 or confirm==0):
            plates=(int)(input("Please enter number of available plates: \t"))
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(confirm==0):
            lats=(int)(input("Please enter lat cooking location of food item: \t"))
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
        
        confirm=0
        while (confirm==0):
            longs=(int)(input("Please enter long cooking location of food item: \t "))
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        food_code=food_item[0:2]+(str(lats))+(str(longs))
                    
        add_to_dish="INSERT INTO foods(food_code,food_item,plate_price,plates,lat,long) VALUES (?,?,?,?,?,?);"
        cursor.execute(add_to_dish,(food_code,food_item,plate_price,plates,lats,longs))
        conn.commit()
        print("added DISH to DATABASE")
        break
    
    
    
    pass #delete when done


def view_foods(identity):
    print("viewing foods")
    user_lats=0
    user_longs=0
    
    confirm=0
    while(confirm==0):
        user_lats=input("Please enter your lat location: \t")
        confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
    
    confirm=0
    while (confirm==0):
        user_longs=input("Please enter your long location: \t ")
        confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
   
    get_dist_dishes="""SELECT *,(SQRT((({}-lat)*({}-lat)) + ( ({}-long)*({}-long) ))) as distance FROM foods WHERE distance <=10;
                    
    """.format(user_lats,user_lats,user_longs,user_longs)
    cursor.execute(get_dist_dishes)
    got_dishes=cursor.fetchall()
    print(got_dishes)
    
    
    pass #delete when done


def order_dish(type,distance):
    food_code=''
    quantity=0
    final_price=0
    keep_ordering=True
    
    while(keep_ordering):
        confirm=0
        while(len(food_code)==0 or confirm=='0'):
            food_code=input("Please enter food_code of food ordering: \t" )
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
        confirm=0
        while(quantity==0 or confirm=='0'):
            quantity=(int)(input("Please enter number of plates to order: \t" ))
            confirm=input("are you sure?(enter 1 for yes, 0 for no): \t")
            
            
        check_available="SELECT * FROM foods WHERE food_code=?;"
        cursor.execute(check_available,(food_code,))
        fooditem=cursor.fetchall()
        if(fooditem==[]):
            print("food item doesnt exist")
            confirm=0
            continue
        elif(fooditem[0][3]<quantity):
            print("order less")
            confirm=0
            continue
        else:
            cost=fooditem[0][2]
            new_quantity=(fooditem[0][3])-quantity
            final_price+=(cost*quantity)
            cursor.execute("UPDATE foods SET plates=? WHERE food_code=?",(new_quantity,food_code))
            conn.commit()
            keep_ordering=input("Keel ordering?(1/0): \t")
            keep_ordering= False if keep_ordering=='0' else True
            
    print("Final cost is {}".format(final_price))
           

def rest_options():
    while (True):
        option=-1
        option=(int)(input("As a RESTAURANT, your options are\nView Dishes (1)\nAdd Dishes (2)\nExit (0)\nEnter your option: "))
        if option==0:
            return
        elif option==1:
            print("The Schema for entries (food_code,food_name,price_per_plate,plates,lat,long)")
            show_table("foods")
            continue
        elif option==2:
            add_dish()
            continue
        else:
            print("enter valid option")
            continue
            

def indi_options():
    while (True):
        option=-1
        option=(int)(input("As an INDIVIDUAL, your options are\nView Dishes (1)\nAdd Dishes (2)\nOrder Dishes (3)\nExit (0)\nEnter your option: "))
        if option==0:
            return
        elif option==1:
            print("The Schema for entries (food_code,food_name,price_per_plate,plates,lat,long)")
            show_table("foods")
            continue
        elif option==2:
            add_dish()
            continue
        
        elif option==3:
            order_dish(2,10)
        else:
            print("Please enter valid option")
            continue
            
def ngo_options():
    while (True):
        option=-1
        option=(int)(input("As an NGO, your options are\nView Dishes (1)\nOrder Dishes (2)\nExit (0)\nEnter your option: "))
        if option==0:
            return
        elif option==1:
            print("The Schema for entries (food_code,food_name,price_per_plate,plates,lat,long)")
            show_table("foods")
            continue
        
        elif option==2:
            order_dish(2,10)
            continue
        else:
            print("Please enter valid option")
            continue
    
    
    
    
    pass #delete when done
    
def main():
    cursor.execute(showtables)
    out=cursor.fetchall()
    empty_db=True if out==[] else False
    print("empty db %s",empty_db)

    if(empty_db):
        cursor.execute(make_accounts)
        cursor.execute(make_foods)
        conn.commit()
    else:
        pass

    # cursor.execute(showtables)
    # out=cursor.fetchall()
    # print("current tables: ")
    # print(out)
    # show_table(out[0][0])
    # print(out[1][0])
    # print("done")
    # show_table(out[1][0])
    # add_dish()
    # add_dish()
    # add_dish()
    # add_dish()
    # add_dish()
    # add_dish()
    # add_dish()
    # print(out[1][0])
    # print("done")
    # show_table(out[1][0])
    # view_foods(1.0)
    #order_dish("indi1","iname1")
    while(True):
        option=-1
        print("Welcome to WTF Co.")
        option=(int)(input("Options\n-------------------------\nLogin (1)\nSignup (2)\nLeave (0)\nEnter your Option:"))
        if option==0:
            break
        elif option==1:
            logged_in=login()
            print(logged_in)
            while (True):
                acc_type=(int)(logged_in[3])
                print(acc_type)
                if acc_type==1:
                    rest_options()
                elif acc_type==2:
                    indi_options()
                elif acc_type==3:
                    ngo_options()
                else:
                    ("lol this isn't supposed to be possible, yer here we are, lets just logout")
                    break
                
                    
                leave=(int)(input("DO you want to logout?(1 for yes/0 for no): "))
                if leave!=0:
                    break
            continue
        elif option==2:
            signup()
            continue
        elif option==84:
            show_table("accounts")
            continue
        
        
        else:
            print("Please enter a valid option or leave")
            continue
    
    
if __name__=="__main__":
    main()
    