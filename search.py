def SearchingChallenge(strArr):
  def search(strArr,row, col, visited):
    if (row < 0 or row >= len(strArr) or col < 0 or col >= len(strArr[0]) or (row, col) in visited or strArr[row][col] == 1):
      return 0
    
    visited.add((row,col))

    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    for r,c in dir:
     search(strArr, row + r, col + c, visited)
    # print(count)
    return 1

  visited = set()
  count = 0


  for row in range(len(strArr)):
    for col in range(len(strArr[0])):
      if strArr[row][col] == "0" and (row,col) not in visited:
        print(f'row => {row} col => {col}')
        count += search(strArr, row, col, visited)
        print(count)
  
  print(f'count => {count}')

  # for row in range(len(strArr)):
  #   for col in range(len(strArr[0])):
  #     print(strArr[row][col])


  # # code goes here
  # return strArr

# keep this function call here 
print(SearchingChallenge(["01111", "01101", "00011", "11110"]))