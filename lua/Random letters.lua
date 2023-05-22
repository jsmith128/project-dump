local common = require('common')

letters=common.stringExplode("a b c d e f g h i j k l m n o p q r s t u v w x y z", " ")
a={}
b=""
n=10



function rand()
  b=" "

  for i=1,n do
    c=math.random(26)
    b=b..letters[c]
  end
  print(b)
end

for i=1,table.maxn(letters) do
    print(i..". "..letters[i])
end

for i=1,100 do
  rand()
end