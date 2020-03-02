def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    if dolphin == True:
        sharkSpeed /= 2
    while pontoonDistance > 0:
        pontoonDistance -= youSpeed
        sharkDistance -= sharkSpeed
    if pontoonDistance <= 0 and sharkDistance >= 0:
        return "Alive!"
    else:
        return "Shark Bait!"