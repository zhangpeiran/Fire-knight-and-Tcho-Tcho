girl_speed=5

def outrange(name,rrange,brange):
    if name.x < 0:
        name.x = 0
    if name.right > rrange:
        name.right = rrange
    if name.y < 0:
        name.y = 0
    if name.bottom > brange:
        name.bottom = brange