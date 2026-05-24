# Combinatorial Equivalence Enumeration Service

An advanced enumerative combinatorics engine that collapses exponential state-spaces to compute unique, non-equivalent matrix configurations under strict row and column permutation group actions.

## 📌 System Overview
The system confronts a severe complexity scaling bottleneck where an exponential search space ($20^{144}$ raw states) fractures standard brute-force processing. Because naive architectures fail to isolate structurally identical grids under spatial transformation (rotation, reflection, or translation), redundant evaluation paths induce immediate runtime freezing. 

To resolve this execution pressure, the engine introduces a compressed representation framework. The architecture bypasses raw state exploration by mapping the search space directly to its underlying structural invariants, reducing runtime to negligible practical scales for typical inputs.

### Technical Parameters
* **Input Constraints:** Matrix dimensions bounded sequentially at $1 \le w, h \le 12$; discrete token states bounded at $1 \le s \le 20$.
* **Algorithmic Core:** Computes the exact orbit count via a partition-based application of Burnside's Lemma over the product group $S_w \times S_h$.
* **State Management:** Enforces closure-based encapsulation combined with parameter-injected memoization tables.

---

## ⚙️ Core Logic Flow
The engine systematically compresses spatial redundancy by executing a cascading reduction across three functional layers:

1. **Conjugacy Class Compression (Interface Register):**
   The pipeline collapses the massive raw permutation space into distinct, non-overlapping mathematical families. By leveraging integer partition generators, the system isolates invariant structures and entirely truncates redundant exploration loops before evaluation begins.
   > **Substrate Anchor:** Generates the precise conjugacy classes of the symmetric groups $S_w$ and $S_h$ via restricted integer partitions, bounding the iteration space to the partition functions $P(w) \times P(h)$.

2. **Decoupled Symmetry Modeling (Interface Register):**
   The architecture explicitly separates the structural weight of the canonical symmetric groups from the central orbit calculation kernel. This tracking mechanism mirrors the interaction of intersecting symmetries without blending their execution paths.
   > **Substrate Anchor:** Computes the joint orbit fixed-points by evaluating the Greatest Common Divisor (GCD) interaction matrix across the cycles of the chosen partitions (via Cauchy's formula for conjugacy class sizes).

3. **Memory Invariant Injection (Interface Register):**
   The system locks down its execution trajectory by feeding precomputed structural metrics directly through the function pipeline. This design choice prevents runtime drift, bypassing the latency overhead of repetitive inline math execution.
   > **Substrate Anchor:** Establishes a constant-time execution per step under scaling ($O(1)$ lookup complexity) by injecting static factorial arrays and memoization caches across the functional scope boundary.
