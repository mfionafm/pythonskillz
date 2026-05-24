# Product Group Action Evaluator

An elite enumerative combinatorics system that computes exact unique, non-equivalent matrix configurations under strict symmetric product group actions ($S_w \times S_h$).

## 📌 Project Overview
This project delivers a mathematically rigorous, hyper-optimized solution to an exponential search space challenge (up to $20^{144}$ raw states). Standard traversal methods collapse due to spatial redundancy caused by row and column permutations. This service resolves the scaling bottleneck by factoring the global problem space into disjoint conjugacy classes and explicitly evaluating the cycle-index structures of the underlying symmetries.

### Technical Specifications
* **Input Constraints:** Grid dimensions $w$ and $h$ (1–12); switch states $s$ (1–20).
* **Theoretical Framework:** Formal implementation of Burnside's Lemma over the direct product of symmetric groups.
* **Performance Profile:** Executes in $O(\text{partitions})$ time, dropping computational load from trillions of iterations down to a fraction of a second.

---

## ⚙️ Core Logic Flow
The evaluator enforces absolute mathematical closure across the matrix mapping system:

1. **Conjugacy Class Normalization:** Utilizes non-decreasing integer partitions to map the symmetric group $S_n$ directly onto its conjugacy classes, bypassing redundant permutation states entirely.
2. **Explicit Weighting Protocol:** Applies standard group theory formulas ($|S_n| / z_\lambda$) to calculate the precise size of each conjugacy class, using a precomputed lookup table to maintain strict $O(1)$ factorial retrieval speeds.
3. **Induced Orbit Interaction Kernel:** Evaluates the cycle-index interaction of the product group using a mathematically derived Greatest Common Divisor ($\text{gcd}$) exponent, matching the exact orbit splitting behaviors of overlapping row and column cycles.
