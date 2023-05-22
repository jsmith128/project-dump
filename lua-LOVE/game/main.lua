function love.load()
  pl={}
  pl.x=10
  pl.y=10
  pl.w=15
  pl.h=15
  pl.speed=150
  pl.shots={}
end

function love.keyreleased(key)
  -- in v0.9.2 and earlier space is represented by the actual space character ' ', so check for both
  if (key == " " or key == "space") then
    shoot()
  end
end

function love.update(dt)
  if love.keyboard.isDown("left") then
    pl.x = pl.x - pl.speed*dt
  elseif love.keyboard.isDown("right") then
    pl.x = pl.x + pl.speed*dt
  end
  
   love.graphics.setColor(255,255,0,255)
  love.graphics.rectangle("fill", pl.x, pl.y, pl.w, pl.h)
  
end