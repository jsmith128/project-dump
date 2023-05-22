require("turtle")
t=5
show()

zero(0,100)
size(3000,300)
pnsz(5)
function go()
for i=1,50 do
  move(3)
  turn(t)
  t=t-0.2
end

for i=1,50 do
  move(3)
  turn(t)
  t=t+0.2
end
go()
end
go()
wait()
