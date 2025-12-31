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

# --- Multi-Trit Circuits & Spatial Primitives ---
def half_adder(a: Trit, b: Trit):
    """Ternary half-adder: returns (sum, carry)"""
    sum_trit = tri_and(tri_not(a), b) if a.value == b.value == -1 else \
               tri_or(a, b) if a.value != b.value else \
               Trit(0)
    carry = tri_and(a, b) if a.value == b.value == 1 else Trit(0)
    return sum_trit, carry

def spatial_balance(voxels):
    """Spatial primitive: balance a region using ternary consensus"""
    # Simple 3-voxel balance (center influenced by neighbors)
    center = voxels[0]
    neighbors = voxels[1:]
    consensus = center
    for n in neighbors:
        consensus = tri_consensus(consensus, n)
    return consensus

if __name__ == "__main__":
    print("\n=== Day 3: Multi-Trit Circuits & Spatial Balance ===")
    
    p, n, z = Trit(1), Trit(-1), Trit(0)
    
    sum_trit, carry = half_adder(p, p)
    print(f"Half-adder P + P = sum: {sum_trit}, carry: {carry}")
    
    # Spatial balance: center P with two N neighbors → pulls to neutral
    balanced = spatial_balance([p, n, n])
    print(f"Spatial balance [P, N, N] → {balanced}")
    
    print("\nDay 3 complete.")
    print("Ternary computing layer ready for LeoOS shell.")
    print("Next: Volumetric workspace with real-time interference.")

# --- Ternary ALU (Arithmetic Logic Unit) ---
class TernaryALU:
    """Simple ternary ALU – combines arithmetic and logic"""
    def __init__(self):
        self.result = Trit(0)

    def execute(self, op: str, a: Trit, b: Trit = None) -> Trit:
        if op == "ADD":
            return sn_add(a, b)
        elif op == "SUB":
            return sn_add(a, Trit(-b.value))
        elif op == "NOT":
            return tri_not(a)
        elif op == "AND":
            return tri_and(a, b)
        elif op == "OR":
            return tri_or(a, b)
        elif op == "CONSENSUS":
            return tri_consensus(a, b)
        elif op == "ANY":
            return tri_any(a, b)
        else:
            raise ValueError("Unknown operation")

if __name__ == "__main__":
    print("\n=== Day 3: Ternary ALU ===")
    
    alu = TernaryALU()
    
    # Arithmetic tests
    print("ADD P + N =", alu.execute("ADD", Trit(1), Trit(-1)))  # 0
    print("SUB PP - P =", alu.execute("SUB", TernaryInt([Trit(1), Trit(1)]), TernaryInt([Trit(1)])))  # P0 = 3
    
    # Logic tests
    print("NOT P =", alu.execute("NOT", Trit(1)))  # N
    print("P AND N =", alu.execute("AND", Trit(1), Trit(-1)))  # N
    print("P OR N =", alu.execute("OR", Trit(1), Trit(-1)))  # P
    print("CONSENSUS P N =", alu.execute("CONSENSUS", Trit(1), Trit(-1)))  # 0
    
    print("\nTernary ALU operational.")
    print("Next: Spatial primitives (3D vector operations).")
