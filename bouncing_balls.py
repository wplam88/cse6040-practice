def bouncing_ball(h, bounce, window):
    position = h
    views = 0
    
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while position > window:
            views += 1
            position = position * bounce
            if position > window:
                views += 1
        return views
    else:
        return -1