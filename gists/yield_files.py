# from https://stackoverflow.com/questions/7883962/where-to-use-yield-in-python-best
def get_lines(files):
    for f in files:
        for line in f:
            #preprocess line
            yield line


for line in get_lines(files):
    #process line

