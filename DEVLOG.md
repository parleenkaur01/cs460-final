# Development Log – The Torchbearer

**Student Name:** PARLEEN BAGGA
**Student ID:** 131159493

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/11/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_Your entry here._
I plan to begin by understanding the problem structure and separating it into two main parts: computing shortest paths and searching over relic visit orders. I will first implement Dijkstra’s algorithm and use it to precompute distances between the spawn, all relics, and the exit. After that, I will implement a recursive backtracking approach to explore all possible orders of visiting relics, while using pruning to reduce unnecessary exploration. I expect the most difficult part will be designing correct pruning logic without eliminating the optimal solution. I will test my implementation using the provided test cases and by creating small custom graphs to verify correctness step by step.
---

## Entry 2 – [05/12/2026]: Implemented Dijkstra & PreComputation

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

While working on Dijkstra’s algorithm, I noticed that some nodes were getting processed more than once, which led to incorrect distances. After debugging, I realized I wasn’t properly tracking visited nodes. I fixed this by adding a visited set and making sure each node is only processed once after being popped from the priority queue. 

Once Dijkstra was working correctly, I moved on to Part 2 and implemented source selection and distance precomputation. I used the spawn and all relics as sources and ran Dijkstra from each one to build a distance table. This will help make the search part faster later on.

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
