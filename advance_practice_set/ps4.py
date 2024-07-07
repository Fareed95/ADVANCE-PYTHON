list = [1,2,3,4,5,6,7,8,9,10]
try :
    user = int(input("Enter the mnumber whose multiplicatiion tablw you want to see :"))
    mu_table = [user*i for i in list]
    print(mu_table)
    with open("file.txt","a") as f :
        f.write(f"The table of {user} : {mu_table}\n")
except Exception as e :
    print(e)