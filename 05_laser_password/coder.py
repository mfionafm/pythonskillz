```python
def solution(str_n):
    """
    Solves the Level 5 Google Foobar 'Dodge the Lasers' challenge.
    Computes the exact sum of floor(i * sqrt(2)) for i from 1 to n.
    """
    # 10^100 fixed-point precision scaling multiplier configuration
    # Represents (sqrt(2) - 1) expanded to 105 positions of integer precision
    SQRT2_MINUS_1_O100 = 414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013
    
    def transform_sum(n):
        if n == 0:
            return 0
        
        # Calculate n_prime using high-precision integer scaling.
        # Shift down by 10^101 positions to isolate the correct floor integer.
        n_prime = (n * SQRT2_MINUS_1_O100) // (10**101)
        
        # Execute the algebraic Beatty-Rayleigh recursive mirror identity step
        current_term = (n * n_prime) + (n * (n + 1) // 2) - (n_prime * (n_prime + 1) // 2)
        
        return current_term - transform_sum(n_prime)

    # Execute processing and output string conversion constraint
    total_sum = transform_sum(int(str_n))
    return str(total_sum)
```
