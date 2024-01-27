import re

complement = 15
ALPHABET = {'a':10, 'b':11,'c':12,'d':13,'e':14,'f':15}

def hex_switch_space(n):
    """
    Function to change hex alphabet codes to 
    normal numbers with spaces separating each number.
    This is used for the below processes for calculating
    the complement of the number.
    """
    r_list = []  # return list
    for char in n:
        if char.lower in ALPHABET.keys():
            r_list += " " + str(ALPHABET[char])



with open('input.txt', 'r') as f:
    r = f.read()
    new_list = []
    for line in r.split('.'):
        if complement < 15:  # only works for things that don't have letters
            new_list.append(re.sub("[^0-9]", "", line))
        else:
            line_list = []  # list of things to replace line
            for char in line:

            new_list.append()

    new_list_ = []
    for line in new_list:
        if line:
            new_list_.append(line)
    new_list = new_list_
    del new_list_

    return_list = []
    for number in new_list:
        add_num = ""
        begin_count = False
        for char in list(number):
            if complement == 9 or complement == 10:
                add_num += ' '+str((9)-int(char))
            if complement == 8 or complement == 7:
                if begin_count or int(char) > 0:
                    if 7 - int(char) >= 0:
                        begin_count = True
                        add_num += ' '+str((7)-int(char))
                    else:
                        add_num += " 0"
                else:
                    add_num += " 0"
            print(add_num)
        if complement == 10:
            add_num = add_num[:-1] + str(1+int(add_num[-1]))
        if complement == 8:
            add_num = add_num[:-1] + str(1+int(add_num[-1]))

        return_list.append(add_num)

    if complement == 10 or complement == 8:
        # --- Remove numbers greater than 10 ---
        num_index = 0
        for cool_thing in return_list:
            #for i in range(len(cool_thing.strip().split(' '))):
            thing_index = 0
            cool_thing = cool_thing.strip()
            for thing in cool_thing.strip().split(' '):
                thing = thing.replace(' ', '')
                if thing:
                    if int(thing.strip()) > complement-1:
                        return_list[num_index] =' '+"".join(cool_thing.split(' ')[:thing_index-1])+ str(int(cool_thing.split(' ')[thing_index-1])+1)  + '0'
                thing_index += 1
            num_index += 1
            
    if complement == 9 or complement == 10:
        for thing in return_list:
            print("{:,}".format(int(thing.replace(' ', ''))))
    if complement == 8 or complement == 7:
        for thing in return_list:
            a= thing.replace(' ', '')
            a = [a[i:i+3] for i in range(0, len(a), 3)]
            if a[0] == "000":
                a = a[1:]
            print(' '.join(a))
            # https://stackoverflow.com/questions/15254195/python-how-to-add-space-on-each-3-characters
    print(return_list)
