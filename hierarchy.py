def solution(h, q):
    # Step 1: Calculate the absolute top match of the whole tournament
    # (The closed loop size based on the height 'h')
    total_nodes = (2 ** h) - 1
    results = []
    
    # Step 2: Loop through each player/match ID they want us to look up
    for target in q:
        # Rule 1: If it's the Grand Finals match, it has no next round
        if target == total_nodes:
            results.append(-1)
            continue
            
        # Start tracking from the very top of the tournament
        current_top = total_nodes
        sub_tree_size = total_nodes
        
        # Rule 2: Keep splitting the brackets down the middle
        while True:
            # Split the remaining matches in half to find the twin bracket size
            sub_tree_size = sub_tree_size // 2
            
            # Find the local champion of the Left Bracket and Right Bracket
            left_child = current_top - sub_tree_size - 1
            right_child = current_top - 1
            
            # If our target is either the left or right child, 
            # then the current_top is its manager/next round!
            if target == left_child or target == right_child:
                results.append(current_top)
                break
                
            # If we haven't found it yet, shrink our focus to the correct side
            if target <= left_child:
                current_top = left_child  # Zoom into the Left Bracket
            else:
                current_top = right_child # Zoom into the Right Bracket
                
    return results
