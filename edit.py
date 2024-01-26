global s
with open('main.txt', 'r') as f:
    s = f.read()
    s.rstrip()
    print(f.read())
with open('main.txt', 'w') as w:

    w.write(s)