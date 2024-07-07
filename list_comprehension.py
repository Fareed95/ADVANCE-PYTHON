List = [1,2,3,4,5,6,20]
list = []
for index in List :
    list.append(index*index)
print(list)

# any other method to replace it ??? yes ofcoarse 

cube_list = [i*i*i for i in List]
print(cube_list)