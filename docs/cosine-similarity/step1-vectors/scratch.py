import math
import pdb

def dot_product(a, b):
    # pdb.set_trace()  
    return sum(x * y for x, y in zip(a, b))

def magnitude(a):
    # pdb.set_trace()  
    return math.sqrt(sum(x ** 2 for x in a))

def cosine_similarity(a, b):
    # pdb.set_trace()  
    dp = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    result = dp / (mag_a * mag_b)
    return result

vec_a = [1, 2, 3]
vec_b = [1, 2, 3]
vec_c = [3, 2, 1]

print(cosine_similarity(vec_a, vec_b))
print(cosine_similarity(vec_a, vec_c))