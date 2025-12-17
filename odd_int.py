def find_it(seq):
    counts = {}
    
    for n in seq:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
        
    for n, count in counts.items():
        if count % 2 == 1:
            return n