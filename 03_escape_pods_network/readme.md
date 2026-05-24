# Network Flow & Bottleneck Router (Escape Pods)

## Project Overview
A network routing solution modeled on the Ford-Fulkerson algorithm to compute the absolute maximum flow of data or entities through a constrained transit matrix.

## Core Architectural Solutions
* **Single-Checkpoint Simplification:** Unifies complex multi-source (ingress) and multi-drain (egress) matrix environments into a single stream by implementing a virtual "Super-Source" (Basement) and "Super-Sink" (Roof).
* **Compilation Stability:** Replaces volatile floating-point boundaries (`float('inf')`) with a secure integer infinity barrier (`INF = 2000000000`) to guarantee execution stability across different runtimes.
* **Deterministic Flow Mapping:** Tracks state saturation iteratively across forward paths using Breadth-First Search (BFS) while updating reverse paths to handle network traffic adjustments efficiently.
