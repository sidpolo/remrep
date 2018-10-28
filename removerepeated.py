nos= [1,2,3,3,3,5,5,5,7,8,9,4,4,66,666,666]
looped_nos=[x for x in nos if nos.count(x)<2]
print(looped_nos)
