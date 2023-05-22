function love.load()
  --world = love.physics.newWorld(0,0)
  --beginContact, endContact, preSolve, postSolve = world:getCallbacks( )
  destroy = {
    needtobullet=0,
    needtobunker=0,
    bullet = {},
    bunker = {}
    }
  bspeed=5 --lower = faster
  t=0
  bullets=0
  bulletx={}
  bullety={}
  bulleti = love.graphics.newImage("bullet.png")
  bulletphs = {
    body = {},
    shape = {},
    fixture = {}
    }
  
  ship = {
    s = 5,
    x = 400,
    y = 800,
    i = love.graphics.newImage("ship.png")
    }
  --explosion = love.graphics.newVideo("explosion.ogv")
  bunker = {
    baseh = 10,
    total = 4,
    --body = {},
    --shape = {},
    --fixture = {},
    x = {},
    y = 700,
    h = {},
    im = love.graphics.newImage("bunkerretro.png"),
    num = 0
    }
  for i=1, bunker.total do
    --table.insert(bunker.x, i*200+200)
    --table.insert(bunker.h, 10)
    --Make bunker x coordinates and health 
    --[[bunker.x[i] = i*150
    destroy.bunker[i] = 0]]
    
    bunker.num = bunker.num + 1
    table.insert(bunker.x, 1, i*800/bunker.total-100)
    table.insert(destroy.bunker, 1, 0)
    table.insert(bunker.h, 1, bunker.baseh)
      
    --[[bunker.body.i = love.physics.newBody(world, i*150, bunker.y, "dynamic")
    bunker.shape.i = love.physics.newRectangleShape(50,50)
    bunker.fixture.i = love.physics.newFixture(bunker.body.i,bunker.shape.i)]]
  end
  
end

function love.update(dt)
  --world:update(dt) 
  if destroy.needtobullet==1 then
    for i=1, bullets do
      if destroy.bullet[i]==1 then
        bullets = bullets-1 
        table.remove(bulletx, i) 
        table.remove(bullety, i)
        table.remove(destroy.bullet, i)
        --love.graphics.draw(explosion, bulletx[i], bullety[i], 180, 1, 1)
        --explosion:play()
      end
    end
    destroy.needtobullet=0
  end
 
  if destroy.needtobunker==1 then
    for i=1, bunker.num do
      if destroy.bunker[i]==1 then
        bunker.num = bunker.num - 1 
        table.remove(bunker.x, i)
        table.remove(destroy.bunker, i)
        --love.graphics.draw(explosion, bulletx[i], bullety[i], 0, 1, 1)
        --explosion:play()
      end
    end
    destroy.needtobunker=0
  end
  
  
  if love.keyboard.isDown("right") and ship.x<=775 or love.keyboard.isDown("d") and ship.x<=775 then
    ship.x = ship.x + ship.s
  end
  if love.keyboard.isDown("left") and ship.x>=25 or love.keyboard.isDown("a") and ship.x>=25 then
    ship.x = ship.x - ship.s
  end
  function love.keypressed(key)
    if key=="space" then
      
      bullets=bullets+1
      table.insert(bulletx, 1, ship.x)
      table.insert(bullety, 1, ship.y)
      table.insert(destroy.bullet, 1, 0)
      
      --[[bulletphs.body.i = love.physics.newBody(world, ship.x, ship.y, "dynamic")
      bulletphs.shape.i = love.physics.newRectangleShape(6,50)
      bulletphs.fixture.i = love.physics.newFixture(bulletphs.body.i,bulletphs.shape.i)]]
      
    end
  end
  t=t+200*dt
  if t>=bspeed then 
    t=0
    
    if bullets~=0 then
      for i=1, bullets do
        bullety[i] = bullety[i] - 5
        
        --"COLLISION"
        
        if bullety[i] - 25 <= 20 then 
          destroy.bullet[i] = 1
          destroy.needtobullet = 1
        end
        
          --hit bunker
        for b=1, bunker.num do
          if bulletx[i] <= bunker.x[b] + 50 and bulletx[i] >= bunker.x[b] and bullety[i]-20 <= bunker.y + 50 then --50 = width/height of bunker
            destroy.bullet[i] = 1
            destroy.needtobullet = 1
            bunker.h[b] = bunker.h[b] - 1
            if bunker.h[b] <= 0 then 
              destroy.bunker[b] = 1
              destroy.needtobunker = 1
            end
          end
        end
      end
    end
  end
end 

--[[function beginContact(a, b, coll)
  for i=1,bullets do
    if a==bulletphs.fixture.i then
      destroy.bullet[i]=1
      destroy.needtobullet=1
    end
    
    if b==bulletphs.fixture.i then
      destroy.bullet[i]=1
      destroy.needtobullet=1
    end
    
  end
end]]

function love.draw()
  love.graphics.rectangle("fill", 790,600,10,40)
  love.graphics.setColor(0.125, 1, 0.125)
  love.graphics.rectangle("fill", 0, 0, 800, 20)
  love.graphics.setColor(1, 1, 1)
  for i=1, bullets do
    love.graphics.draw(bulleti, bulletx[i], bullety[i], 0, 1, 1, bulleti:getWidth()/2, bulleti:getHeight()/2)
  end
  
  for i=1, bunker.num do
    local bimage = bunker.im
    love.graphics.draw(bimage, bunker.x[i], bunker.y)
  end
  love.graphics.draw(ship.i, ship.x, ship.y, 0, 1, 1, ship.i:getWidth()/2, ship.i:getHeight()/2)
  
end

