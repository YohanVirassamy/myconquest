import random

list_length = int(input("Longueur de la liste: "))
my_list = [ random.randrange(1, 1001, 1) for _ in range(list_length) ]
print("My list : " + str(my_list))

my_ordered_list = []
first_element = 0
last_element = len(my_ordered_list) - 1

for i in range(len(my_list)):
    new_length = int(len(my_ordered_list) / 2)
    center_ordered_list = int(new_length)

#append the first element in the list
    if i == 0:
        my_ordered_list.append(my_list[0])

#the smallest number
    elif my_list[i] > my_ordered_list[last_element]:
        my_ordered_list.append( my_list[i] )

#the largest number
    elif my_list[i] <= my_ordered_list[first_element]:
        my_ordered_list.insert( 0, my_list[i])

    else:
        while my_list[i] <  my_ordered_list[center_ordered_list - 1] or my_list[i] > my_ordered_list[center_ordered_list]:
            if my_list[i] < my_ordered_list[center_ordered_list - 1]:
                new_length = int(new_length / 2)
                if new_length == 0:
                    new_length = 1
                center_ordered_list = center_ordered_list - new_length
            if my_list[i] > my_ordered_list[center_ordered_list]:
                new_length = int(new_length/ 2)
                if new_length == 0:
                    new_length = 1
                center_ordered_list = center_ordered_list + new_length

        my_ordered_list.insert(center_ordered_list, my_list[i])

print("My ordered list : " + str(my_ordered_list))
