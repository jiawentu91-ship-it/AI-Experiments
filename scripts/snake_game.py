
count=0
def change(ls,x,y):
    import copy
    ls=copy.deepcopy(ls)
    for i in range(3):
        ls[i].insert(0, 2)
        ls[i].append(2)
    ls.insert(0, [2, 2, 2, 2, 2])
    ls.append([2, 2, 2, 2, 2])
    x=x+1
    y=y+1
    return ls,x,y
    
def search(chls,chx,chy):
    global count
    if chls[chx][chy]==1:
        chls[chx][chy]=2
        count=count+1

        search(chls,chx-1,chy)
        search(chls,chx+1,chy)
        search(chls,chx,chy-1)
        search(chls,chx,chy+1)

    if chls[chx][chy]==0:
        chls[chx][chy]=2
        
        search(chls,chx-1,chy)
        search(chls,chx+1,chy)
        search(chls,chx,chy-1)
        search(chls,chx,chy+1)
    else:
        return 

grid=[[1, 2, 1],
      [2, 0, 2],
      [1, 2, 1]]
startx,starty=1,1
new_grid, new_x, new_y = change(grid,startx,starty)
search(new_grid,new_x,new_y)
print(count)

        