def contains(sequence,num):
    for element in sequence:
        if(element==num):
            return True
    return False
print(contains((1,2,3,5,3,9,8,78,8,6,6,6,9),7))
print(contains((1,2,3,5,3,9,8,78,8,6,6,6,9),78))
