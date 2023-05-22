local common = require('common')

a={}
b=""


for i=1,10000 do
c=math.random(100)
table.insert(a,i,c)

end

for i=1,table.maxn(a) do
 if i ~= table.maxn(a) then
  b=b..a[i]..", "
 else
  b=b..a[i]
 end
end
print(b)