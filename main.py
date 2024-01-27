import re

complement = 16
base = 16
ALPHABET = {'a':10, 'b':11,'c':12,'d':13,'e':14,'f':15}

def hex_switch_space(n):
    """
    Function to change hex alphabet codes to 
    normal numbers in a list.
    This is used for the below processes for calculating
    the complement of the number.
    """
    r_list = []  # return list
    for char in n:
        if char.lower() in ALPHABET.keys():
            r_list.append(str(ALPHABET[char]))
        elif char.replace(' ', ''):
            r_list.append(str(char))
    return r_list

def back_to_hex(n):
    """
    Take a string of hex_switch_space but each
    number in the number is separated by a space instead
    of being in a list.
    """
    r_list = []
    for char in n.split(' '):
        char = char.strip()
        if char.replace(" ", ''):
            if int(char) in list(ALPHABET.values()):
                r_list.append(str(list(ALPHABET.keys())[list(ALPHABET.values()).index(int(char))]))
                #  https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
            else:
                r_list.append(char)
    return r_list


with open('input.txt', 'r') as f:
    r = f.read()
    new_list = []
    for line in r.split('.'):
        if complement < 15:  # only works for things that don't have letters
            new_list.append(re.sub("[^0-9]", "", line))
        else:
            line = line[-11:]
            new_list.append(hex_switch_space(line))

    # --- Remove empty strings/lists from list ---
    new_list_ = []
    for line in new_list:
        if line:
            new_list_.append(line)
    new_list = new_list_
    del new_list_

    return_list = []

    # --- Base calculations ---
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
            if complement == 15 or complement == 16:
                if int(char) != 0 and 15 - int(char) > 0:
                    begin_count = True
                    

                if begin_count:
                    if 15 - int(char) > 0:
                        begin_count = True
                        add_num += ' '+str((15)-int(char))
                    else:
                        add_num += ' ' + '0'
                    
        if complement == 16:
            print(add_num,'l',len(add_num.split(' ')))
            if len(add_num.split(' ')) % 3 > 0:
                add_num = "0 "+add_num

        if complement == 10 or complement == 8:
            add_num = add_num[:-1] + str(1+int(add_num[-1]))
        if complement == 16:
            add_num = " ".join(add_num.split(" ")[:-1])+" "+str(int(add_num.split(' ')[-1]) + 1)
        return_list.append(add_num)

    if complement == 10 or complement == 8 or complement == 16:
        # --- Remove numbers greater than complement base ---
        for redos in range(len(return_list[0])):
            num_index = 0

            for cool_thing in return_list:
                #for i in range(len(cool_thing.strip().split(' '))):
                thing_index = 0
                cool_thing = cool_thing.strip()
                for thing in cool_thing.strip().split(' '):
                    thing = thing.replace(' ', '')
                    if thing:
                        if int(thing.strip()) > base-1:
                            if not complement == 16:
                                return_list[num_index] =' '+"".join(cool_thing.split(' ')[:thing_index-1])+ str(int(cool_thing.split(' ')[thing_index-1])+1)  + ' 0'
                            else:
                                return_list[num_index] =' '+" ".join(cool_thing.split(' ')[:thing_index-2])+ " "+ str(int(cool_thing.split(' ')[thing_index-2])+1)  + ' 0'
                    thing_index += 1
                num_index += 1
                
            
    # --- Print it out ---
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
    if complement == 15 or complement == 16:
        for thing in return_list:
            a = "".join(back_to_hex(thing))
            if len(a)%2 > 0:
                a =  a+"0"
            new_a = ""
            i=0
            for char in a:
                if i == 2:
                    i=0
                    new_a+=" "
                new_a += char
                i+=1
            print(new_a)
    
    print(return_list)
