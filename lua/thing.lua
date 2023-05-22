require "turtle"

local x,y = size() -- get the current screen size
updt(false) -- disable auto updates
zero(0, 0) -- change origin such that (0,0) is now in the left top corner
pnsz(3)
pncl(colr(255, 127, 00))
for x=0,250 do
  for y=0,250 do
    pixl(x,y)
    pncl(colr(x,y,x+y))
  end
end
wait()