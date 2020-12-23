

def filter_tn(groups):
    #print(len(groups))
    tn = []
    count = []
    for name, group in groups:
        if (len(group) > 1):
            tn.append(name)
            count.append(len(group))
    return tn, count