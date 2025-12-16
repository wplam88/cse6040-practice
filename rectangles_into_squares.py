def sq_in_rect(lng, wdth):
    squares = []
    if lng != wdth:
        while lng > 0 and wdth > 0:
            if lng > wdth:
                squares.append(wdth)
                lng = lng - wdth
            else:
                squares.append(lng)
                wdth = wdth - lng
        return squares
    else:
        return None