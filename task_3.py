def delete(list_, index=-1):
    if index < 0:   #если индекс отрицательный
        index = len(list_) + index; 
    return list_[:index] + list_[index + 1:]

print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
#print(delete([0, 1, 2, 3, 4, 4], index=50))  #Error!
