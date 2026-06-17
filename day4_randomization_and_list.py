import random
#we basically use macrenne twister for generating random number form a deterministic algorithm

print(random.randint(1,99)); #give a random num between 1 and 99 both 1 and 99 are included and this is for integer
print(random.random())  #this give a result btw  0 to 1
print(random.uniform(0,9)) #this give random float number btwn this two num
lst = [1,2,3,45,6,7,8,9,7,5,5,3,6,7,5,4,6,4,7,9,6,4,3]

random.choice(lst)      # 1 random item
random.choices(lst,k=3) # 3 random items, duplicates allowed
random.sample(lst,3)    # 3 unique random items
random.randint(1,10)    # int from 1 to 10
random.randrange(1,10)  # int from 1 to 9
random.uniform(1,10)    # float from 1 to 10
random.random()         # float from 0.0 to 1.0
random.shuffle(lst)     # shuffle original list


#List 
li = ["apple","ball","cat","dog"]
#to add a item at the end of list we use append
print(li)
li.append("samrat")
print(li)
#to add multiple value or elems in list we use extend
li.extend(["extend1","extend2"])
#extend helps to add other list at the end of of the current list in which we want to add
print(li)



# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
if "apple" in li:
    print("apple is in the list")
print(li[:3]) #from begining  stop before index 3
print(li[::-1]) #this help in reverse


#list[start : stop : step]
# print(li[::2])


# start = beginning
# stop = end
# step = 2
print(li[1::2]) #start from index 1 jump by 2
li = [0,1,2,3,4,5,6,7,8,9]
print(f'''
      {li[:3]}     # first 3 elements
        {li[2:]}     # from index 2 to end
          {li[1:4]}    # index 1 to 3
            {li[::2]}    # every second element
              {li[::-1]}   # reverse list
                {li[::-2]}   # reverse, skipping one each time
      
      
      
      ''')