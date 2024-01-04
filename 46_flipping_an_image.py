def flip_and_invert_image(image):
    for row in image:
        l, r = 0, len(row)-1
        while l <= r:
            row[l], row[r] = row[r], row[l]
            row[l] = 1 - row[l]
            if l != r:
                row[r] = 1 - row[r]
            l += 1
            r -= 1

        
    return image


print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))