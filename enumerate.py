l = [1,2,3,4,5,6,7,7]
# long method ..
# index = 0 
# for item in l :
#     print(f"the item number art {index } is {item}")
#     index+= 1 

# but can we do in more simple way ???? yes of coarse

for index, item in enumerate(l):
     print(f"the item number art {index } is {item}")