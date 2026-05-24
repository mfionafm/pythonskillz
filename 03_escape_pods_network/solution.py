from collections import deque

def find_open_path(matrix, basement, roof, parent_map):
    visited = [False] * len(matrix)
    queue = deque([basement])
    visited[basement] = True
    
    while queue:
        current_room = queue.popleft()
        for next_room, pipe_width in enumerate(matrix[current_room]):
            if not visited[next_room] and pipe_width > 0:
                queue.append(next_room)
                visited[next_room] = True
                parent_map[next_room] = current_room
                if next_room == roof:
                    return True
    return False

def solution(starts, exits, path):
    num_real_rooms = len(path)
    total_rooms = num_real_rooms + 2
    basement = num_real_rooms
    roof = num_real_rooms + 1
    
    # Secure integer infinity barrier for compiling stability
    INF = 2000000000
    
    master_matrix = [[0] * total_rooms for _ in range(total_rooms)]
    
    for i in range(num_real_rooms):
        for j in range(num_real_rooms):
            master_matrix[i][j] = path[i][j]
            
    for start in starts:
        master_matrix[basement][start] = INF
        
    for exit_room in exits:
        master_matrix[exit_room][roof] = INF
        
    total_escaped_bunnies = 0
    parent_map = [-1] * total_rooms
    
    while find_open_path(master_matrix, basement, roof, parent_map):
        bottleneck = INF
        current = roof
        while current != basement:
            prev = parent_map[current]
            bottleneck = min(bottleneck, master_matrix[prev][current])
            current = prev
            
        total_escaped_bunnies += bottleneck
        
        current = roof
        while current != basement:
            prev = parent_map[current]
            master_matrix[prev][current] -= bottleneck
            master_matrix[current][prev] += bottleneck
            current = prev
            
    return total_escaped_bunnies
