nos = [1, 2, 2, 3, 3, 3, 4, 4, 6, 10]



looped_nos = list()



for no in nos:

  if not nos.count(no) > 1:

     looped_nos.append(no)





print(looped_nos)
