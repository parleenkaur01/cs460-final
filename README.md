# The Torchbearer

**Student Name:** ___________________________
**Student ID:** ___________________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run only gives the minimum cost from the entrance to each node, but it does not determine the order in which the relics should be visited.

- **What decision remains after all inter-location costs are known:**
  The remaining decision is choosing the best order to visit all relic chambers before finally reaching the exit.

- **Why this requires a search over orders (one sentence):**
  This requires a search over orders because different sequences of visiting relics can result in different total fuel costs.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Entrance / spawn node| The route always begins here, so shortest costs from the entrance to relics are needed. |
| Relic chamber nodes| After collecting one relic, the planner must know the cheapest cost from that relic to every other relic and to the exit. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary `dist_table`  |
| What the keys represent | Outer key = source node; inner key = destination node |
| What the values represent | Shortest-path fuel cost from the source node to the destination node |
| Lookup time complexity | O(1) average case|
| Why O(1) lookup is possible | Python dictionaries use hash-table lookup  |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** `k + 1`
- **Cost per run:** `O(m log n)`
- **Total complexity:** `O((k + 1)m log n)`
- **Justification (one line):** Dijkstra runs once from the entrance and once from each of the `k` relic chambers.


---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  Their shortest distance from the source has already been confirmed, so those distance values will not need to change later.

- **For nodes not yet finalized (not in S):**
  Their current distance is the best route discovered so far using finalized nodes as the completed middle portion of the path.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  At the beginning, the source has distance `0` and all other nodes have distance `infinity`, so no incorrect shortest-path claim has been made.

- **Maintenance : why finalizing the min-dist node is always correct:**
  The node with the smallest tentative distance is safe to finalize because all edge weights are nonnegative. Any later route through another unfinished node cannot become cheaper than the smallest current tentative distance.


- **Termination : what the invariant guarantees when the algorithm ends:**
  When the priority queue is empty, every reachable node has its true shortest-path distance from the source, and unreachable nodes remain at `infinity`.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

Correct shortest-path distances are necessary because the route planner compares relic visit orders using these costs, so incorrect distances could make it choose the wrong route.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** Greedy chooses the cheapest next relic immediately, but that local choice may make the remaining route more expensive.
- **Counter-example setup:** In the example, `S -> B` costs `1`, `S -> C` costs `2`, and `S -> D` costs `2`, but the costs between relics and to `T` change the best full route.
- **What greedy picks:** Greedy chooses `B` first because it is the cheapest relic to reach from `S`.
- **What optimal picks:** An optimal route is `S -> B -> D -> C -> T` with total cost `4`.
- **Why greedy loses:** Greedy only considers the next step, while the total route depends on how that step affects all later relic visits and the exit.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore the order of visiting relics because different relic sequences can produce different total fuel costs.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
