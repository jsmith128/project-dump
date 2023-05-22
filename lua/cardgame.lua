pca,pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8,pc9,pc10,pcj,pcq,pck=0
eca,ec1,ec2,ec3,ec4,ec5,ec6,ec7,ec8,ec9,ec10,ecj,ecq,eck=0
pa=0
ea=0
etake=0 --0=nothing 1=yes
ptake=0 --0=nothing 1=yes
math.randomseed(os.time())
cards={}
for i=1,4 do
  table.insert(cards,"A")
  table.insert(cards,"2")
  table.insert(cards,"3")
  table.insert(cards,"4")
  table.insert(cards,"5")
  table.insert(cards,"6")
  table.insert(cards,"7")
  table.insert(cards,"8")
  table.insert(cards,"9")
  table.insert(cards,"10")
  table.insert(cards,"J")
  table.insert(cards,"Q")
  table.insert(cards,"K")
end

pcards={}
ecards={}

function addcards(n)
  for i=table.getn(pcards), n do
    pcards[i]=cards[math.random(table.getn(cards))]
    table.remove(cards,i)
  end
end

function addecards(n)
  for i=table.getn(ecards), n do
    ecards[i]=cards[math.random(table.getn(cards))]
    table.remove(cards,i)
  end
end

function printcards()
  for i=1, table.getn(pcards) do
    print(i..". "..pcards[i])
  end
end

addcards(7)
addecards(7)

function find3pcards()
  pca,pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8,pc9,pc10,pcj,pcq,pck=0
  for k,v in pairs(pcards) do
    if v=="A" then pca=pca+1 end
    if v=="1" then pc1=pc1+1 end
    if v=="2" then pc2=pc2+1 end
    if v=="3" then pc3=pc3+1 end
    if v=="4" then pc4=pc4+1 end
    if v=="5" then pc5=pc5+1 end
    if v=="6" then pc6=pc6+1 end
    if v=="7" then pc7=pc7+1 end
    if v=="8" then pc8=pc8+1 end
    if v=="9" then pc9=pc9+1 end
    if v=="10" then pc10=pc10+1 end
    if v=="J" then pcj=pcj+1 end
    if v=="Q" then pcq=pcq+1 end
    if v=="K" then pck=pck+1 end
  end
end

function pturn()
  etake=0
  print("Your turn...")
  printcards()
  print("What card do you choose?")
  pa=io.read()
  
  for i=1, table.getn(ecards) do
    if ecards[i]==pcards[a] then
      ptake=1
      print("You took computer's "..pcards[i])
      table.insert(pcards, ecards[i])
      table.remove(ecards, i)
    end
  end
  if ptake==0 then print("You didin't take anything") end
  eturn()
  find3pcards()
end

function eturn()
  etake=0
  print("Computers turn...")
  local ca=math.random(table.getn(ecards))
  
  for i=1, table.getn(pcards) do
    if pcards[i]==ecards[ca] then
      etake=1
      print("Computer took your "..pcards[i])
      table.insert(ecards, pcards[i])
      table.remove(pcards, i)
    end
  end
  if etake==0 then print("Computer didin't take anything") end
  pturn()
  find3pcards()
end

pturn()
