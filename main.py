import re

complement = 10

with open('input.txt', 'r') as f:
    r = f.read()
    new_list = []
    for line in r.split('.'):
        new_list.append(re.sub("[^0-9]", "", line))

    new_list_ = []
    for line in new_list:
        if line:
            new_list_.append(line)
    new_list = new_list_
    del new_list_

    return_list = []
    for number in new_list:
        add_num = ""
        for char in list(number):
            if complement == 9 or complement == 10:
                add_num += ' '+str((9)-int(char))

        add_num = add_num[:-1] + str(1+int(add_num[-1]))

        return_list.append(add_num)

    # --- Remove numbers greater than 10 ---
    num_index = 0
    for cool_thing in return_list:
        #for i in range(len(cool_thing.strip().split(' '))):
        thing_index = 0
        cool_thing = cool_thing.strip()
        for thing in cool_thing.strip().split(' '):
            thing = thing.replace(' ', '')
            if thing:
                if int(thing.strip()) > 9:
                    print(cool_thing)
                    return_list[num_index] =' '+"".join(cool_thing.split(' ')[:thing_index-1])+ str(int(cool_thing.split(' ')[thing_index-1])+1)  + '0'
                    print(return_list[num_index])
            thing_index += 1
        num_index += 1
    for thing in return_list:
        print("{:,}".format(int(thing.replace(' ', ''))))
    print(return_list)
