import re

new_l = []  # list of questions
with open('input.txt', 'r') as f:
    r = f.read().split('.')  # read file
    for i in r:  # make a list out of every question
        new_l.append(re.sub('[^0-9]','', i).strip())

# --- Remove blanks ---
print(new_l)
new_l_ = []
for i in new_l:
    if i:
        new_l_.append(i)

new_l = new_l_
print(new_l)
    
return_str = ""  # the string to return at the end
print(new_l)
for question in new_l:
    question_return = ""  # the return for each question
    start_number = False
    
    # --- Base calculation ---
    for character in question:
        if not start_number:
            if int(character) > 0:
                question_return += str(7-int(character))
            else:
                question_return += "0"
    print(question_return[-1])
    
    # --- Fixing values over 7 ---
    ind = 0
    temp_val_store = ""
    add_one = False
    for char in question_return:
        if add_one:
            temp_val_store += str(int(char)+1)
        else:
            temp_val_store += char

        if int(char[-1]) > 7:
            temp_val_store += "0"
            add_one = True
        else:
            add_one = False
        ind += 1
        
        
    temp_q_store = ""  # used for storing the temporary formatting
    ind=0  # index of formatting within the return string

    # --- Formatting ---
    for char_format in temp_val_store:
        if ind%3 == 0:
            temp_q_store += ' '
        temp_q_store += char_format
        ind += 1

    return_str += temp_q_store.strip() + '\n'
print("RETURNING \n\n", return_str)
