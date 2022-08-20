#bitwise operators
a=12
b=4
print(f"{a} & {b}={a & b}")
print(f"{a} | {b}={a | b}")
print(f"{a} ^ {b}={a ^ b}")
print(f"{a} = {~a}")
print(f"{'a<<b'} = {a<<b}")
print(f"{'a>>b'} = {a>>b}")
# 12   1 1 0 0
#  4   0 1 0 0
# and  0 1 0 0  ===> 4

#12  1  1  0 0
#4   0 1   0 0


#OR  1 1   0 0  ===> 12

#12   1 1 0 0
#4    0 1 0 0
#XOR  1 0 0 0 ===> 8

# n = 12  ~n = -(n+1) = -13

#LEFT SHIFT
#x<<n  = x * 2^n
#3 << 2 = 3 * 2^2  = 12

# x >> n  = x / 2^n