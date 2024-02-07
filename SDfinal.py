from itertools import permutations
import copy

agent_numbers = int(input('How many agents are there? '))
good_numbers = int(input('How many goods are there? '))
a_and_p = []
all_lists = []
for x in range(agent_numbers):
    name = input('What is agent name? ')
    preferences = []
    
    for y in range(good_numbers):
        preference = input(f'What is your {y + 1} preference? ')
        preferences.append(preference)

    all_lists.append([name, preferences])
    a_and_p.append([name, preferences])

permutations_list = permutations(all_lists)
permutations_list = list(permutations_list)
i = 1
lists=[]
for permutation in permutations_list:
    new_list_name = "list_" + str(i)
    new_list = list(permutation)
    i += 1
    lists.append(new_list)

copied_list = copy.deepcopy(lists)
def allocation_function (mylist):
    for x in range (int(len(mylist))):
        for sublist in mylist[x+1:]:
            value_to_remove=mylist[x][1][0]
            if value_to_remove in sublist[1]:
                sublist[1].remove(value_to_remove)

allocation_function(a_and_p)






def result_function (my_list):
    done='done'
    for i in range (int(len(my_list))):
        print ('%s gets %s' % (my_list[i][0], my_list[i][1][0]))
    return done

print ('Allocation result according to your order: ')
print (result_function (a_and_p))

print ('All possible allocations are as follows: ')
for list in copied_list:
    list_copy=copy.deepcopy(list)
    print('Results: ')
    allocation_function(list_copy)
    print (result_function (list_copy))
    print("----")
