def can_place_flowers(flowerbed: 'list[int]', n: int) -> bool:
    if n == 0:
        return True
    
    if len(flowerbed) == 1:
        return True if flowerbed[0] == 0 else False
    
    for i in range(0, len(flowerbed)):
        if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
        
        if i < len(flowerbed)-1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            n -= 1
    return n <= 0

print(can_place_flowers([0,0,1,0,0], 1))