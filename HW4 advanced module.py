"""USING NESTED FUNCTIONS"""

def func1():                               #outer function to return
  list = []
  def func2(matrix,target):                 #inner function for iterating over given matrix

    for i in matrix:
      row=matrix.index(i)
      row_len=len(i)
      for column in range(row_len):        #iterating over columns based on row length
          val=matrix[row][column]
          if val==target:                  #Comparing with given target
              list.append(row)
              list.append(column)
              print(list)
              return True                 #inner function returns "true" if target is present

  c=func2([                               #calling inner function and collecting its result
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
], 1005)



  if c!=True:                           #if target is not available appending empty list with [-1,-1]
    list.append(-1)
    list.append(-1)
    print(list)
func1()



