import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        def getNeighbors(given_node):
            #Get list of neighbors of node in format NESW (clockwise)
            neighbors = [None]*4
            #There is neighbor North
            if given_node[1][0] > 0:
                neighbors[0] = (grid[given_node[1][0]-1][given_node[1][1]] ,(given_node[1][0]-1, given_node[1][1]))
            #There is neighbor east
            if given_node[1][1] < len(grid[0])-1:
                neighbors[1] = (grid[given_node[1][0]][given_node[1][1]+1], (given_node[1][0],given_node[1][1]+1))
            #There is neighbor south
            if given_node[1][0] < len(grid)-1:
                neighbors[2] = (grid[given_node[1][0]+1][given_node[1][1]],(given_node[1][0]+1,given_node[1][1]))
            if given_node[1][1] > 0:
                neighbors[3] = (grid[given_node[1][0]][given_node[1][1]-1],(given_node[1][0],given_node[1][1]-1))
            return neighbors
        
        
        def BFS(given_node):
            #Perform BFS from specific  node
            my_queue = queue.Queue()
            visited = set()
            
            my_queue.put(given_node)
            
            while my_queue.qsize() != 0:
                size = my_queue.qsize()
                for x in range(size):
                    current = my_queue.get()
                    
                    if current[0] == '1':
                        grid[current[1][0]][current[1][1]] = '0'
                    
                    for neighbor in getNeighbors(current):
                        #print("Neighbor is: (" + str(neighbor[0]) + ", (" + str(neighbor[1][0]) + "," + str(neighbor[1][1])+"))")
                        print(neighbor)
                        if (neighbor != None) and (neighbor not in visited) and (neighbor[0] == '1'):
                            print("HIT THIs")
                            grid[neighbor[1][0]][neighbor[1][1]] = '0'
                            #my_queue.put(neighbor)
                            #land.remove(neighbor)
                    
        
        
        
        
        
        island_count = 0
        land = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    
                    BFS((grid[row][col], (row,col)))
        return island_count
        