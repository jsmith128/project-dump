function love.conf(t)
  t.window.title = "New Game"
end

function love.load()
  obj = love.physics.newWorld()
  ship = love.physics.newBody(obj, 750, 550, "dynamic")
  shipf = love.physics.newFixture( ship, shape, density )
end

function love.update()
  sx = ship:getX() 
  sy = ship:getY()
  print(ship:getX())
end

function love.update()
  if love.keyboard.isDown("right") then
    ship:applyForce(50, 0)
  end
  if love.keyboard.isDown("left") then
    ship:applyForce(-50, 0)
  end
end

function love.draw()
  love.graphics.print("#", sx, sy)
end

