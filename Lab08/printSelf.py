with open("printSelf.py", 'r') as fh:
    for i, line in enumerate(fh):
        print(f"{i+1}: {line}")
