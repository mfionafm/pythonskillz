# pythonskillz
Python Proof of Concept
# Braille Translation Microservice

A lightweight, robust Python utility designed to translate standard plaintext ASCII strings into a specific 6-bit binary stream representation of Braille.

## 📌 Project Overview
This project solves a data-transformation challenge involving non-intuitive reading orders, case-modification protocols, and numerical state shifts. The solution bypasses over-engineered algorithmic generation in favor of a highly readable, performant lookup dictionary to map character data safely.

### Technical Specifications
* **Input Constraints:** Single string containing alphanumeric characters and spaces (1–50 characters).
* **Matrix Mapping:** 3x2 grid encoded as a continuous 6-bit binary stream.
* **Architecture:** Implements conditional state-tracking for uppercase modifiers and numeric indicators.

---

## ⚙️ Core Logic Flow
The translator processes strings linearly using a deterministic ruleset:

1. **Capitalisation Protocol:** Detects uppercase characters, prefixes the output stream with the capitalization indicator (`000001`), and maps the lowercase variant.
2. **Numerical Protocol:** Intercepts numeric digits, injects the number system indicator (`001111`), and routes the digit to its corresponding alphabetical Braille matrix (\(1 \rightarrow a, 2 \rightarrow b\), etc.).
3. **Robust Handling:** Sanitizes input streams by dynamically ignoring unknown punctuation or special characters, preventing system runtime crashes.
