"""
Tiện ích xử lý số nguyên tố cho thuật toán Diffie-Hellman
"""
import random
import math

def is_prime(n):
    """
    Kiểm tra xem một số có phải là số nguyên tố không
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Kiểm tra các ước số từ 5 đến căn bậc hai của n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def generate_large_prime(bits=10):
    """
    Tạo một số nguyên tố lớn ngẫu nhiên với số bit xác định
    """
    while True:
        # Tạo một số ngẫu nhiên với số bit cho trước
        n = random.getrandbits(bits)
        # Đảm bảo số lớn nhất là 1
        n |= (1 << bits - 1)
        # Đảm bảo số là lẻ
        n |= 1
        
        if is_prime(n):
            return n

def power_mod(base, exponent, modulus):
    """
    Tính (base^exponent) % modulus một cách hiệu quả
    Sử dụng thuật toán Square and Multiply
    """
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # Nếu exponent lẻ, nhân result với base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # exponent chia đôi
        exponent = exponent >> 1
        # base bình phương
        base = (base * base) % modulus
    
    return result

def gcd(a, b):
    """
    Tìm ước số chung lớn nhất của a và b
    """
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(g, p):
    """
    Kiểm tra xem g có phải là căn nguyên thủy của p hay không
    """
    # Tính phi(p) - số Euler của p
    phi = p - 1
    
    # Phân tích phi(p) thành các thừa số nguyên tố
    prime_factors = []
    n = phi
    
    # Tìm thừa số 2
    while n % 2 == 0:
        if 2 not in prime_factors:
            prime_factors.append(2)
        n //= 2
    
    # Tìm các thừa số lẻ
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in prime_factors:
                prime_factors.append(i)
            n //= i
    
    # Nếu n > 1 thì n là số nguyên tố
    if n > 1:
        prime_factors.append(n)
    
    # Kiểm tra điều kiện căn nguyên thủy
    for factor in prime_factors:
        if power_mod(g, phi // factor, p) == 1:
            return False
    
    return True

def find_primitive_roots(p, limit=10):
    """
    Tìm các căn nguyên thủy của p, giới hạn số lượng tìm được
    """
    roots = []
    count = 0
    
    for g in range(2, p):
        if is_primitive_root(g, p):
            roots.append(g)
            count += 1
            if count >= limit:
                break
    
    return roots