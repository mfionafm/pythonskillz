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

---

## 🚀 The Code

```python
def translate_to_braille(text_input):
    # Core 6-bit Braille translation matrix
    braille_dict = {
        'a': '100000', 'b': '110000', 'c': '100100', 'd': '100110', 'e': '100010',
        'f': '110100', 'g': '110110', 'h': '110010', 'i': '010100', 'j': '010110',
        'k': '101000', 'l': '111000', 'm': '101100', 'n': '101110', 'o': '101010',
        'p': '111100', 'q': '111110', 'r': '111010', 's': '011100', 't': '011110',
        'u': '101001', 'v': '111001', 'w': '010111', 'x': '101101', 'y': '101111', 
        'z': '101011', ' ': '000000'
    }
    
    # Braille numerical system maps digits 1-9 and 0 to alphabet keys a-j
    num_dict = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'
    }
    
    final_output = ""
    
    for character in text_input:
        # Rule 1: Capital Modifier
        if character.isupper():
            final_output += "000001"
            final_output += braille_dict[character.lower()]
            
        # Rule 2: Number System Modifier
        elif character.isdigit():
            final_output += "001111"
            corresponding_letter = num_dict[character]
            final_output += braille_dict[corresponding_letter]
            
        # Rule 3: Standard Translation
        elif character in braille_dict:
            final_output += braille_dict[character]
            
        # Rule 4: Exception Shielding (Failsafe for unsupported punctuation)
        else:
            continue 
            
    return final_output
```

---

## 🧪 Verification & Test Cases


| Input String | Expected Continuous Output Stream | Note |
| :--- | :--- | :--- |
| `"a"` | `100000` | Baseline lowercase letter |
| `"A"` | `000001100000` | Triggers Capitalization prefix |
| `"1"` | `001111100000` | Triggers Numerical prefix + 'a' matrix |
| `"a A 1"` | `100000000000000001100000000000001111100000` | Composite chain verification |
| `"Hello, World!"`| Continuous valid bitstream | Safely skips commas and exclamation points |
