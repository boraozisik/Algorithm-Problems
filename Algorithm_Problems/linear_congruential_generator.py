"""
A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modular arithmetic by storage-bit truncation.

The generator is defined by the recurrence relation:

{\displaystyle X_{n+1}=\left(aX_{n}+c\right){\bmod {m}}}{\displaystyle X_{n+1}=\left(aX_{n}+c\right){\bmod {m}}}
where {\displaystyle X}X is the sequence of pseudorandom values, and

{\displaystyle m,\,0<m}m,\,0<m — the "modulus"
{\displaystyle a,\,0<a<m}a,\,0<a<m — the "multiplier"
{\displaystyle c,\,0\leq c<m}c,\,0\leq c<m — the "increment"
{\displaystyle X_{0},\,0\leq X_{0}<m}X_{0},\,0\leq X_{0}<m — the "seed" or "start value"
are integer constants that specify the generator. If c = 0, the generator is often called a multiplicative congruential generator (MCG), or Lehmer RNG. If c ≠ 0, the method is called a mixed congruential generator.[1]: 4- 

When c ≠ 0, a mathematician would call the recurrence an affine transformation, not a linear one, but the misnomer is well-established in computer science.
"""


print("The formula is: X(k+1) = a * Xk + c mod m")
seed_number = int(input("Enter seed number: "))
multiplier = int(input("Enter the multiplier(a): "))
increment = int(input("Enter the increment(c): "))
mod = int(input("Enter the modulus (m): "))
random_numbers = int(input("How many random numbers would you like to generate?\nInput: "))


def linearCongruentialGenerator():
    num_base = seed_number
    for i in range(random_numbers, 0, -1):
        rd = (multiplier * num_base + increment) % mod
        print(rd)
        num_base = rd

linearCongruentialGenerator()