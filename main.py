# ENTER VECTORS HERE -- [a_n, b_n] where v_n = a_n + b_n * i
vec1 = [[5, -9], [1, 9], [8, 10], [1, -1]]
vec2 = [[-7, 7], [-1, -8], [9, -4], [-9, 4]]
# ENTER VECTORS HERE ---------------------------------------

def complex_mult(a, b, c, d):
    return[(a*c - b*d), (b*c + a*d)]

for vec in vec2:
    vec[1] *= -1

Re = 0
Im = 0

for i in range(len(vec1)):
    product = complex_mult(vec1[i][0], vec1[i][1], vec2[i][0], vec2[i][1])
    Re += product[0]
    Im += product[1]
    
print("Standard inner product = %d + %di" % (Re, Im))