local common = require('common')
require("turtle")

letters=common.stringExplode("a b c d e f g h i j k l m n o p q r s t u v w x y z", " ")
a={}
b=""
n=10



function rand()
  b=" "

  for i=1,n do
    c=math.random(28)
    if (c>26) then b=b.." " 
    else b=b..letters[c] end
    text(b,0,0,i*10)
  end
  print(b)
end



for i=1,10 do
  rand()
end

show()
wait()