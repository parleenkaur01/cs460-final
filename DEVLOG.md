# Development Log – The Torchbearer

**Student Name:** PARLEEN BAGGA
**Student ID:** 131159493

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/11/2026]: Initial Plan


I plan to begin by understanding the problem structure and separating it into two main parts: computing shortest paths and searching over relic visit orders. I will first implement Dijkstra’s algorithm and use it to precompute distances between the spawn, all relics, and the exit. After that, I will implement a recursive backtracking approach to explore all possible orders of visiting relics, while using pruning to reduce unnecessary exploration. I expect the most difficult part will be designing correct pruning logic without eliminating the optimal solution. I will test my implementation using the provided test cases and by creating small custom graphs to verify correctness step by step.
---

## Entry 2 – [05/12/2026]: Implemented Dijkstra & PreComputation

While working on Dijkstra’s algorithm, I noticed that some nodes were getting processed more than once, which led to incorrect distances. After debugging, I realized I wasn’t properly tracking visited nodes. I fixed this by adding a visited set and making sure each node is only processed once after being popped from the priority queue. 

Once Dijkstra was working correctly, I moved on to Part 2 and implemented source selection and distance precomputation. I used the spawn and all relics as sources and ran Dijkstra from each one to build a distance table. This will help make the search part faster later on.

---

## Entry 3 – [5/1]: Correctness and Search Design
I completed the Dijkstra correctness explanation for Part 3 by understanding the invariant, why nonnegative edge weights matter, and how the algorithm guarantees correct shortest-path distances. I also worked on Part 4 and analyzed why a greedy approach fails for this problem. I realized that choosing the closest relic first does not always lead to the optimal total route, which confirmed the need to explore all possible orders. I then began planning the backtracking approach by identifying the current location, visited relics, and total cost as the key components of the search state.

---

## Entry 4 – 05/14 : Post-Implementation Reflection

After completing the project, I better understood how shortest-path algorithms and recursive search techniques can be combined to solve optimization problems. The most challenging part was designing pruning logic that improves efficiency without removing the optimal solution. If I had more time, I would improve the lower-bound estimation to make pruning more aggressive and reduce unnecessary recursive calls. I would also add more custom test cases for larger graphs and edge cases involving unreachable relics or exits.

## Final Entry – 05/14: Time Estimate


| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |1 |
| Part 2: Precomputation Design |2 |
| Part 3: Algorithm Correctness | 1.5|
| Part 4: Search Design | 1|
| Part 5: State and Search Space |2 |
| Part 6: Pruning |1.5 |
| Part 7: Implementation |4 |
| README and DEVLOG writing |1.5 |
| **Total** | 14.5|
