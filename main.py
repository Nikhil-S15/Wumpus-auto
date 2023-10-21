import random

n = 5  # Size of the grid


# Function to display the grid as a matrix
def grid_display(grid):
    for row in grid:
        for cell in row:
            print(cell, end="\t\t")
        print("\n")


# Function to generate an empty grid
def grid_gen(size):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    return grid


# Function to randomly place pits, wumpus, gold, and agent on the grid
def place_values(grid, n):
    agent_placed = False
    for val in ['p', 'w', 'g']:
        while True:
            x, y = random.randint(0, n - 1), random.randint(0, n - 1)
            if grid[x][y] == ' ':
                if val == 'p':
                    grid[x][y] = 'p'
                elif val == 'w':
                    grid[x][y] = 'w'
                elif val == 'g':
                    grid[x][y] = 'g'
                if not agent_placed:
                    grid[0][0] = 'A'
                    agent_placed = True
                break


# Function to place attributes like stench and breeze
def place_attributes(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'w':
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == ' ':
                        grid[ni][nj] = 'st'
            if grid[i][j] == 'p':
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == ' ':
                        grid[ni][nj] = 'Br'


# Function to find the current location of the agent
def find_agent_location(grid, n):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'A':
                return i, j


# Function to determine the available movements for the agent
def available_movements(grid, n):
    x, y = find_agent_location(grid, n)
    possible_movements = []
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = x + dx, y + dy
        if 0 <= ni < n and 0 <= nj < n:
            possible_movements.append([ni, nj])
    return possible_movements


# Function to update the agent's location
def update_agent_location(grid, x, y, new_x, new_y):
    grid[x][y] = ' '
    grid[new_x][new_y] = 'A'


# Main function for agent movement
def agent_move(grid, n):
    x, y = find_agent_location(grid, n)
    possible_movements = available_movements(grid, n)
    random.shuffle(possible_movements)

    for move in possible_movements:
        new_x, new_y = move
        if grid[new_x][new_y] == 'g':
            update_agent_location(grid, x, y, new_x, new_y)
            grid_display(grid)
            print("Gold found! Congratulations!")
            return
        elif grid[new_x][new_y] == ' ':
            update_agent_location(grid, x, y, new_x, new_y)
            x, y = new_x, new_y
        elif grid[new_x][new_y] == 'p':
            update_agent_location(grid, x, y, new_x, new_y)
            grid_display(grid)
            print("Agent fell into a pit! Game over!")
            return
        elif grid[new_x][new_y] == 'w':
            update_agent_location(grid, x, y, new_x, new_y)
            grid_display(grid)
            print("Agent was killed by the wumpus! Game over!")
            return
        grid_display(grid)
    print("No more possible moves for the agent. Game over!")


# Main code execution
if __name__ == "__main__":
    grid = grid_gen(n)
    place_values(grid, n)
    place_attributes(grid, n)
    grid_display(grid)
    agent_move(grid, n)
