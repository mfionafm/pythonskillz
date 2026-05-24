# Combinatorial Equivalence Enumeration (Disorderly Escape)

## Project Overview
An advanced enumerative combinatorics system that computes unique, non-equivalent matrix states under strict row and column permutation groups. 

## Core Architectural Solutions
* **Conjugacy Class Grouping:** Reduces massive combinatorial search fields (up to $20^{144}$ raw states) into highly compressed families using integer partition mappings.
* **Decoupled Symmetry Modeling:** Explicitly separates standard symmetric group calculations from a compressed GCD-based orbit interaction kernel, ensuring structural transparency and modularity.
* **Encapsulation & Performance:** Employs argument-injected lookup tables to eliminate performance degradation from repeated factorial recomputation.
