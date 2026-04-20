print("hekko")

def chai(n):
    print(n)

chai("hello ")

num_list= "5145464431"
print(num_list[3:])
print(num_list[:7])

chai= "lemon , ginger, masala, chai"
print(chai.split(","))

# print(chai.replace("lemon", "ginger"))
##########################################

chai_type= "masala"
quantity = 2

order = "i ordered {} cup of {} tea "

print(order.format(quantity, chai_type))

############################################

chai_variety= ['lemon', 'masala', 'ginger']
print(", ".join(chai_variety))

######################################
l = [1, 2, 3]

l.append(4)        # Add at end → [1,2,3,4]
l.insert(1, 10)    # Insert at index → [1,10,2,3,4]
l.remove(2)        # Remove value → [1,10,3,4]
l.pop()            # Remove last → [1,10,3]
l.sort()           # Sort list
l.reverse()        # Reverse list