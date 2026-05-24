# Product Group Action Evaluator
An enumerative combinatorics system that collapses combinatorially explosive matrix spaces into unique orbit representatives under the direct product group action \(S_w \times S_h\).

## 📌 Project Overview
This system resolves an exponential scaling bottleneck in grid configuration domains where naive state enumeration collapses due to severe structural redundancy. While the unreduced state space scales up to \(20^{144}\) raw configurations under maximal grid bounds, the underlying topology fractures into symmetric equivalence classes under row and column permutations.

The evaluator bypasses linear-time traversal constraints by factoring the global configuration space into disjoint conjugacy classes. By explicitly evaluating the cycle-index structures of the underlying symmetries via Burnside-class enumeration, the engine computes exact unique orbit representatives without raw state iteration.

## Technical Specifications
* **Input Constraints:** Grid dimensions \(w, h \in [1, 12]\); state configurations \(s \in [1, 20]\).
* **Theoretical Framework:** Formal implementation of Burnside's Lemma over the direct product of symmetric groups via conjugacy-class decomposition.
* **Performance Profile:** Executes in \(\mathcal{O}(\text{partitions})\) time, compressing a factorial-scale search domain into a compact symmetry-class evaluation over orbit representatives to reduce execution runtime to negligible practical scales.

## ⚙️ Core Logic Flow
The evaluator enforces structural mathematical closure across the matrix mapping architecture:

### 1. Conjugacy Class Compression
The system collapses permutation redundancy by mapping the symmetric group \(S_n\) directly onto integer partitions indexed by cycle signatures. Rather than evaluating individual permutations as isolated states, the logic groups permutations into partition-indexed equivalence classes, eliminating redundant traversal across symmetric coordinates. This induces a complete re-expression of the configuration lattice into distinct orbits.

### 2. Orbit Weighting via Cycle Structure
Each conjugacy class contributes a mathematically weighted term defined by \(\frac{|S_n|}{z_\lambda}\), where the scaling denominator \(z_\lambda\) encodes structural stabilizer mass using partition multiplicities. The engine evaluates class mass directly in arithmetic partition space, bypassing factorial permutation loops. A precomputed lookup architecture ensures constant-time execution per step under fixed partition depth.

### 3. Product Group Interaction Kernel
The system resolves coupled row-and-column symmetry interactions under the direct product \(S_w \times S_h\) using cycle-index composition. Orbit splitting behavior is determined via a greatest common divisor (\(\text{gcd}\)) coupling of intersecting cycle lengths. This computes the precise alignment of row and column symmetry entanglement without explicit enumeration, inducing a compressed interaction geometry over the global lattice.
