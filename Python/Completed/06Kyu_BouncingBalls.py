def bouncingBall(h, bounce, window):
    count = 0
    if h <= 0 or bounce <=0 or bounce >= 1 or window > h:
        return -1
    else:
        while h > window:
            h = h * bounce
            count += 2
        return count -1