x=0
y=0
a=""




function adir()
  a=io.read()
  
  if a=="u" then y=y-1
  elseif a=="d" then y=y+1
  elseif a=="l" then x=x-1
  elseif a=="r" then x=x+1
  end
  print(x.." "..y)
  print( )
  adir()
end

adir()