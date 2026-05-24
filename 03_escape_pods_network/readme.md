# Network Flow & Bottleneck Matrix Router

A network routing architecture modeled on the Ford-Fulkerson algorithm to compute maximum capacity metrics across constrained, directed graph transit networks.

## 📌 Project Overview
This project addresses structural transport bottlenecks within multi-ingress (starting points) and multi-egress (exit points) matrix layouts. In highly redundant networks, local pipe saturation easily causes systemic gridlock. The solution introduces virtual boundaries to simplify network tracking and leverages residual traffic mapping to ensure maximum data flow.

### Technical Specifications
* **Input Constraints:** Ingress node arrays, egress node arrays, and a 2D capacity adjacency matrix (up to 50x50).
* **Throughput Capacity:** Processes individual corridor widths scale-bounded between 0 and 2,000,000 units.
* **Architecture:** Employs a Breadth-First Search (BFS) shortest-path scout loop.

---

## ⚙️ Core Logic Flow
The router optimizes system throughput by funneling and balancing the flow matrix:

1. **Virtual Node Aggregation:** Normalizes complex multi-source networks by generating a virtual "Super-Source" (Basement) and "Super-Sink" (Roof) with infinite capacities, simplifying graph traversal into a single-checkpoint pipeline.
2. **Compilation Stability Invariant:** Explicitly enforces a secure integer infinity barrier (`INF = 2000000000`) instead of floating-point boundaries (`float('inf')`), ensuring numerical stability and cross-compiler consistency.
3. **Residual Capacitation Protocol:** Updates the network map dynamically by subtracting saturated volumes from forward paths while opening inverse return valves, allowing the routing engine to automatically recalculate around emerging bottlenecks.
