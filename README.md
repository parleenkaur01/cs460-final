# The Torchbearer

**Student Name:** Parleen Bagga
**Student ID:** 131159493
**Course:** CS 460 – Algorithms | Spring 2026

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run only gives the minimum cost from the entrance to each node, but it does not determine the order in which the relics should be visited.

- **What decision remains after all inter-location costs are known:**
  The remaining decision is choosing the best order to visit all relic chambers before finally reaching the exit.

- **Why this requires a search over orders (one sentence):**
  This requires a search over orders because different sequences of visiting relics can result in different total fuel costs.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance / spawn node| The route always begins here, so shortest costs from the entrance to relics are needed. |
| Relic chamber nodes| After collecting one relic, the planner must know the cheapest cost from that relic to every other relic and to the exit. |

### Part 2b: Distance Storage


| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary `dist_table`  |
| What the keys represent | Outer key = source node; inner key = destination node |
| What the values represent | Shortest-path fuel cost from the source node to the destination node |
| Lookup time complexity | O(1) average case|
| Why O(1) lookup is possible | Python dictionaries use hash-table lookup  |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** `k + 1`
- **Cost per run:** `O(m log n)`
- **Total complexity:** `O((k + 1)m log n)`
- **Justification (one line):** Dijkstra runs once from the entrance and once from each of the `k` relic chambers.


---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  Their shortest distance from the source has already been confirmed, so those distance values will not need to change later.

- **For nodes not yet finalized (not in S):**
  Their current distance is the best route discovered so far using finalized nodes as the completed middle portion of the path.

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  At the beginning, the source has distance `0` and all other nodes have distance `infinity`, so no incorrect shortest-path claim has been made.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The node with the smallest tentative distance is safe to finalize because all edge weights are nonnegative. Any later route through another unfinished node cannot become cheaper than the smallest current tentative distance.


- **Termination : what the invariant guarantees when the algorithm ends:**
  When the priority queue is empty, every reachable node has its true shortest-path distance from the source, and unreachable nodes remain at `infinity`.

### Part 3c: Why This Matters for the Route Planner

Correct shortest-path distances are necessary because the route planner compares relic visit orders using these costs, so incorrect distances could make it choose the wrong route.

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** Greedy chooses the cheapest immediate next relic, but that local decision may lead to a more expensive complete route.
- **Counter-example setup:** Suppose `S -> B = 1`, `S -> C = 2`, `B -> D = 100`, `C -> D = 1`, `D -> T = 1`, and `B -> T = 50`.
- **What greedy picks:** Greedy chooses `B` first because `S -> B = 1` is cheaper than `S -> C = 2`.
- **What optimal picks:** The better route is `S -> C -> D -> B -> T` because the paths after `C` are much cheaper overall
- **Why greedy loses:** Starting with `B` saves only `1` unit initially, but later forces the algorithm to use the very expensive edge `B -> D = 100`. Starting with `C` costs slightly more at first but avoids that expensive path, giving a lower total route cost.

### What the Algorithm Must Explore

The algorithm must explore the order of visiting relics because the total fuel cost depends on the sequence in which relic chambers are visited.

---

## Part 5: State and Search Space

### Part 5a: State Representation


| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location |`current_loc` | node| The node where the search is currently located. |
| Relics already collected |`relics_visited_order` |list |Stores the relics collected so far in the order they were visited. |
| Fuel cost so far |`cost_so_far`  | float/int| The total fuel cost accumulated along the current partial route.|

### Part 5b: Data Structure for Visited Relics


| Property | Your answer |
|---|---|
| Data structure chosen |Set (`relics_remaining`) |
| Operation: check if relic already collected | Time complexity:O(1) average case |
| Operation: mark a relic as collected | Time complexity:O(1) average case using `remove()` |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) average case using `add()`|
| Why this structure fits | A set allows fast insertion, removal, and membership checks during recursive backtracking. |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** `k!`
- **Why:** In the worst case, the algorithm may need to examine every possible ordering of the `k` relic chambers.
---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** The minimum complete route cost found so far and the relic order that produced it.
- **When it is used:** It is checked before recursively exploring deeper branches of the search tree.
- **What it allows the algorithm to skip:** It skips any branch whose current partial cost is already greater than or equal to the best complete solution found.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** The current location, remaining relics, current fuel cost, exit node, and precomputed shortest-path distances.
- **What the lower bound accounts for:** The lower bound uses `cost_so_far` as the minimum guaranteed cost already spent on the route.

- **Why it never overestimates:** Since all edge weights are nonnegative, completing the route can only increase the total cost beyond `cost_so_far`.


### Part 6c: Pruning Correctness


- A branch is pruned only if its lower bound is already at least the best complete route found so far.
- Because the lower bound never overestimates the remaining route cost, pruning cannot remove the true optimal solution.


## References

Lecture Notes Only
