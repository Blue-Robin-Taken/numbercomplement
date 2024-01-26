global s
with open('main.py', 'r') as f:
    lines = []
    s = f.read()
    for line in s.split('\n'):
        lines.append(line.rstrip() + "\n")
    s = "".join(lines)
with open('main.py', 'w') as w:
    w.write(s)