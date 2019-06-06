def process_text_map(map_str):
    """Processes the text representation of a graph into a workable data
        structure"""
    goal_node = (None, None)
    #walls = []
    empty_space = []
    solar_agents = []
    fuel_agents = [[], []] #Locations, fuel
    obstacles = []
    fuel_stations = []
    
    map_list = []
    map_str.strip()
    map_list_temp = map_str.splitlines()
    
    for row, line in enumerate(map_list_temp):
        newLine = []
        for col, char in enumerate(line):
            newLine.append(char)
            if char == "G":
                goal_node = (row, col)
            elif char in ["+", "-", "|", "X"]: #Since all are unable to be moved through
                obstacles.append((row, col))
            elif char == " ":
                empty_space.append((row, col))
            elif char == "S":
                solar_agents.append((row, col))
            elif char.isdigit():
                fuel_agents[0].append((row, col))
                fuel_agents[1].append(int(char))                
            #elif char == "X":
            #    obstacles.append((row, col))
            elif char == "F":
                fuel_stations.append((row, col))
        map_list.append(newLine)    
    
    """for line in map_list_temp:
        newLine = []
        for char in line:
            newLine.append(char)
        map_list.append(newLine)"""
    
    
    print("Goal node: ")
    print(goal_node)
    #print("\nWalls: ")
    #print(walls)
    print("\nEmpty space: ")
    print(empty_space)
    print("\nSolar Agents: ")
    print(solar_agents)
    print("\nFuel Agents: ")
    print(fuel_agents)
    print("\nObstacles: ")
    print(obstacles)
    print("\nFuel Stations: ")
    print(fuel_stations)
    
    #for i in map_list:
     #   print(i)
        
    print_map(map_list, goal_node, empty_space, solar_agents, fuel_agents, obstacles, fuel_stations)
    #print(map_list)
    
def print_map(map_list, goal_node, space, solar_agents, fuel_agents, obstacles, fuel_stations):
    """Prints a visual representation of a map"""
    done = []
    for row in range(len(map_list)):
        for col in range(len(map_list[row])):
            to_add = ""
            if (row, col) == goal_node:
                to_add += "G"
            elif (row, col) in space:
                to_add += " "
            elif (row, col) in fuel_agents[0]:
                index = fuel_agents[0].index((row, col))
                to_add += str(fuel_agents[1][index])
            elif (row, col) in solar_agents:
                to_add += "S"
            elif (row, col) in obstacles:
                to_add += "X"
            elif (row, col) in fuel_stations:
                to_add += "F"
            if (row, col) in done:
                map_list[row][col] += to_add
            else:
                map_list[row][col] = to_add
                
    for line in map_list:
        lineToPrint = ""
        for char in line:
            lineToPrint += char
        print(lineToPrint)
