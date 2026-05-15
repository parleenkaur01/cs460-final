"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Parleen Bagga
Student ID:  131159493

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
     return(
        "- A single shortest-path run from S is not enough because it only gives the cheapest "
        "cost from the entrance to each node; it does not decide which relic should be visited "
        "first, second, or last.\n"
        "- After all important travel costs are known, the remaining decision is the order of "
        "visiting the relic chambers before going to the exit.\n"
        "- This requires a search over orders because different relic orders can produce "
        "different total fuel costs, even when each point-to-point distance is already shortest."
         
     )
     


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    sources = []

    if spawn not in sources:
        sources.append(spawn)

    for relic in relics:
        if relic not in sources:
            sources.append(relic)

    return sources

def run_dijkstra(graph, source):
    dist = {}

    for node in graph:
        dist[node] = float('inf')
        for neighbor, cost in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = float('inf')

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, cost in graph.get(current_node, []):
            new_dist = current_dist + cost

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
   return """
Part 3a: Invariant Explanation
- For finalized nodes, the algorithm has already proven their shortest distance from the source, so those values will not change later.
- For non-finalized nodes, dist stores the best path found so far using only finalized nodes as internal steps.

Part 3b: Invariant Maintenance
- Initialization: Before the first loop, the source has distance 0 and every other node is infinity, so no incorrect shortest paths have been claimed.
- Maintenance: The node with the smallest tentative distance can be finalized because all edge weights are nonnegative, so no later path through another unfinished node can become cheaper.
- Termination: When the algorithm finishes, every reachable node has its true shortest-path distance, and unreachable nodes remain infinity.

Part 3c: Why Correctness Matters
- The route planner depends on these distances to compare relic orders, so incorrect shortest-path values could cause it to choose the wrong route.
     """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
   return """
Why Greedy Fails
- The failure mode: Greedy chooses the cheapest next relic immediately, but that local choice may make the remaining route more expensive.
- Counter-example setup: In the example, S to B costs 1, S to C costs 2, and S to D costs 2, but the costs between relics and to T change the best full route.
- What greedy picks: Greedy chooses B first because it is the cheapest relic to reach from S.
- What optimal picks: An optimal route is S -> B -> D -> C -> T with total cost 4.
- Why greedy loses: Greedy only considers the next step, while the total route depends on how that step affects all later relic visits and the exit.

What the Algorithm Must Explore
- The algorithm must explore the order of visiting relics because different relic sequences can produce different total fuel costs.
"""


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = 0
    best = [float('inf'), []]

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        cost_so_far,
        exit_node,
        best
    )
    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    
    # This pruning is safe because all edge weights are nonnegative, so any route
    # continuing from this state can only keep or increase cost_so_far.
    if cost_so_far >= best[0]:
        return
    if len(relics_remaining) == 0:
        exit_cost = dist_table.get(current_loc, {}).get(exit_node, float('inf'))
        if exit_cost == float('inf'):
            return
        
        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()
        return
    for relic in list(relics_remaining):
        travel_cost = dist_table.get(current_loc, {}).get(relic, float('inf'))
        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )
        relics_visited_order.pop()
        relics_remaining.add(relic)



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()


