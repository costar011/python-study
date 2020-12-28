# simple.py
languges = ['python', 'perl', 'c', 'java']

for lang in languges:
    if lang in ['python', 'perl']:
        print("%6s neeed interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
