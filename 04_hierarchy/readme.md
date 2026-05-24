# Combinatorial Equivalence Enumeration Service

An advanced enumerative combinatorics engine that computes unique, non-equivalent matrix states under strict row and column permutation group actions.

## 📌 Project Overview
This project addresses a severe scaling challenge where an exponential search space (up to $20^{144}$ raw states) must be evaluated for structural uniqueness. Because the system cannot distinguish between grids that have been rotated, flipped, or shifted, standard brute-force permutation checks cause immediate runtime freezing. The solution introduces a compressed representation framework to compute exact structural configurations instantly.

### Technical Specifications
* **Input Constraints:** Matrix dimensions bounded between 1 and 12; switch states bounded between 1 and 20.
* **Algorithmic Core:** Implements a partition-based application of Burnside's Lemma over the product group $S_w \times S_h$.
* **Architecture:** Utilizes closure-based encapsulation and argument-injected memoization tables.

---

## ⚙️ Core Logic Flow
The enumerator resolves spatial redundancy by mapping the underlying symmetry groups:

1. **Conjugacy Class Compression:** Maps the massive raw permutation space into neat, mathematical families using integer partition generators, avoiding billions of wasteful exploration loops.
2. **Decoupled Symmetry Modeling:** Explicitly isolates the canonical symmetric group weighting from a compressed GCD-based orbit interaction kernel, ensuring structural transparency and modularity.
3. **Encapsulation & Memory Invariant:** Employs precomputed factorial lookup tables passed securely via function parameters, bypassing the performance degradation of repeated math calls and ensuring strict $O(1)$ lookup speeds.
