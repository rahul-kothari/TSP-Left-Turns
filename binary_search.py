import math

def binary_search(optimal_distance, current_distance):
    """
    Finds the fraction to be multiplied to current_distance for current_distance == optimal_distance.
    """

    start = 0.1
    end = 0.9
    fraction = 0.5
    # Tolerate a difference of 1% between optimal distance and current_distance.
    abs_tol = 0.01 * optimal_distance
    
    while(True):
        
        current_distance = current_distance * fraction
        print("curr_dist=", current_distance, "\tfrac=", fraction)

        if (math.isclose(optimal_distance, current_distance, abs_tol=abs_tol) == True):
            break;
            
        elif  (optimal_distance > current_distance):
            # TODO: There is a bug here - you are setting fraction, but not "start" or "end" values. So it screws up. Try a test run with the values 44474.86 and 52982.41 to know what I mean.




            #Reduce fraction
            fraction = start + (fraction / 2)
        
        else:
            #Increase fraction
            fraction = end + (fraction / 2)
    
    return fraction

            
if __name__ == "__main__":

    binary_search(44474.86, 52982.41)
    """
    import osmnx as ox
    from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
    from tsp import get_full_tsp_path    

    # Step 1: Get graph and nodes.
    G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
    ox.bearing.add_edge_bearings(G)
    
    n1 = G.nodes[416913103]
    n2 = G.nodes[338834142]
    n3 = G.nodes[423810866]
    n4 = G.nodes[27207873]
    n5 = G.nodes[60179781]
    node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]

    # Step 2: Dijkstra on all pairs.
    dist_matrix, route_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids)
    
    # Step 3: TSP 
    _, _, dist_traversed_no_constraints = get_full_tsp_path(node_ids, dist_matrix, route_matrix)

    # Step 4: Graph with avoid right turns:
    avoid_right_turns = True
    # Don't create new graph with edge factor yet. That's what binary search looks for!

    # Step 5: Dijkstra on all pairs avoiding bad turns
    dist_matrix_avoid_bad_turn, route_matrix_avoid_bad_turn = dijkstra_on_all_pair_of_nodes(G, node_ids, avoid_right_turns)

    # Step 6: tsp.
    _, _, dist_traversed_avoid_bad_turn = get_full_tsp_path(node_ids, dist_matrix_avoid_bad_turn, route_matrix_avoid_bad_turn, avoid_right_turns)

    # Step 7: binary search on required edge factor for dist_traversed_no_constraints == dist_traversed_avoid_bad_turn 
    edge_factor = binary_search(dist_traversed_no_constraints, dist_traversed_avoid_bad_turn)
    print("Fraction: ", edge_factor)
    """