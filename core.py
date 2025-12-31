# ternary_core/core.py
# LeoOS TernaryCore v0.1 – Day 1 (December 31, 2025)
# Balanced ternary: -1 (N), 0, +1 (P)

class Trit:
    """Balanced ternary digit"""
    def __init__(self, value: int):
        if value not in [-1, 0, 1]:
            raise ValueError("Trit must be -1, 0, or 1")
        self.value = value

    def __repr__(self):
        return "P" if self.value == 1 else ("0" if self.value == 0 else "N")

class TernaryInt:
    """Multi-trit integer (LSB first)"""
    def __init__(self, trits=None):
        self.trits = trits[:] if trits else [Trit(0)]

    def __repr__(self):
        if all(t.value == 0 for t in self.trits):
            return "0"
        return "".join(str(t) for t in reversed(self.trits))

def add(a: TernaryInt, b: TernaryInt) -> TernaryInt:
    result = []
    carry = 0
    max_len = max(len(a.trits), len(b.trits))
    
    for i in range(max_len):
        av = a.trits[i].value if i < len(a.trits) else 0
        bv = b.trits[i].value if i < len(b.trits) else 0
        total = av + bv + carry
        
        if total == 3:
            result.append(Trit(0))
            carry = 1
        elif total == 2:
            result.append(Trit(-1))
            carry = 1
        elif total == 1:
            result.append(Trit(1))
            carry = 0
        elif total == 0:
            result.append(Trit(0))
            carry = 0
        elif total == -1:
            result.append(Trit(-1))
            carry = 0
        elif total == -2:
            result.append(Trit(1))
            carry = -1
        elif total == -3:
            result.append(Trit(0))
            carry = -1
    
    if carry:
        result.append(Trit(carry))
    
    return TernaryInt(result)

# Day 1 Test
if __name__ == "__main__":
    print("LeoOS TernaryCore v0.1 – Day 1")
    print("P + N =", add(TernaryInt([Trit(1)]), TernaryInt([Trit(-1)])))  # 0
    print("PP + PN =", add(TernaryInt([Trit(1), Trit(1)]), TernaryInt([Trit(-1), Trit(1)])))  # P0P = 6
    print("Foundation active. Ternary revolution begins.")

# --- Ternary Logic Gates ---

def tri_not(a: Trit) -> Trit:
    """Ternary NOT: invert the state"""
    return Trit(-a.value)  # +1 → -1, -1 → +1, 0 → 0

def tri_and(a: Trit, b: Trit) -> Trit:
    """Ternary AND: minimum of the two values (common in balanced ternary)"""
    return Trit(min(a.value, b.value))

def tri_or(a: Trit, b: Trit) -> Trit:
    """Ternary OR: maximum of the two values"""
    return Trit(max(a.value, b.value))

def tri_consensus(a: Trit, b: Trit) -> Trit:
    """Consensus: agree if same, neutral if different"""
    if a.value == b.value:
        return Trit(a.value)
    return Trit(0)

def tri_any(a: Trit, b: Trit) -> Trit:
    """Any non-neutral"""
    if a.value != 0 or b.value != 0:
        return Trit(1 if (a.value + b.value) > 0 else -1)
    return Trit(0)

# Day 2 Test
if __name__ == "__main__":
    print("\n=== Day 2: Ternary Logic Gates ===")
    
    p = Trit(1)
    n = Trit(-1)
    z = Trit(0)
    
    print("NOT P =", tri_not(p))
    print("P AND P =", tri_and(p, p))
    print("P AND N =", tri_and(p, n))
    print("P OR N =", tri_or(p, n))
    print("Consensus P N =", tri_consensus(p, n))
    
    print("\nLogic foundation complete.")
    print("Next: Multi-trit logic circuits and spatial primitives.")
