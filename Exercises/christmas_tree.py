picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture: 
  for pexel in row: 
      if pexel:
        print('*', end='')
      else: 
        print(' ', end='')
  print(' ') #for a new line after every row