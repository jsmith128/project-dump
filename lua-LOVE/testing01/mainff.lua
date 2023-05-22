function love.load()
	world = love.physics.newWorld(0, 200, true)
	box = {}
	box.image = love.graphics.newImage("ship.png")
	box.body = love.physics.newBody(world, 200, 200, "dynamic")
	box.shape = love.physics.newRectangleShape(box.image:getWidth(), box.image:getHeight())
	box.fixture = love.physics.newFixture(box.body, box.shape)
  
	ball = {}
	ball.body = love.physics.newBody(world, 180, 300, "static")
	ball.shape = love.physics.newCircleShape(40)
	ball.fixture = love.physics.newFixture(ball.body, ball.shape)
  ball2 = {}
	ball2.body = love.physics.newBody(world, 300, 400, "static")
	ball2.shape = love.physics.newCircleShape(40)
	ball2.fixture = love.physics.newFixture(ball2.body, ball2.shape)
end


function love.update(dt)
	world:update(dt)
end

function love.draw()
	love.graphics.draw(box.image, box.body:getX(), box.body:getY(), box.body:getAngle(),  1, 1, box.image:getWidth()/2, box.image:getHeight()/2)
	love.graphics.circle("fill", ball.body:getX(), ball.body:getY(), 40)
  love.graphics.circle("fill", ball2.body:getX(), ball2.body:getY(), 40)
end
