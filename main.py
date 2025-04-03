"""
Chương trình chính thực hiện thuật toán trao đổi khóa Diffie-Hellman
"""
import os
import random
from diffie_hellman import DiffieHellman
from prime_utils import is_prime, find_primitive_roots, generate_large_prime
from logger import Logger

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """In tiêu đề chương trình"""
    print("=" * 60)
    print("  CHƯƠNG TRÌNH MÔ PHỎNG TRAO ĐỔI KHÓA DIFFIE-HELLMAN  ")
    print("=" * 60)

def get_prime_number():
    """
    Lấy số nguyên tố từ người dùng hoặc tạo tự động
    """
    while True:
        print("\nChọn phương thức xác định số nguyên tố q:")
        print("1. Nhập số nguyên tố q từ bàn phím")
        print("2. Tạo số nguyên tố q ngẫu nhiên")
        choice = input("Lựa chọn của bạn (1/2): ")
        
        if choice == '1':
            q = input("\nNhập số nguyên tố q: ")
            try:
                q = int(q)
                if q < 5:
                    print("Số nguyên tố phải lớn hơn hoặc bằng 5 để có căn nguyên thủy.")
                    continue
                if not is_prime(q):
                    print(f"{q} không phải là số nguyên tố. Vui lòng nhập lại.")
                    continue
                return q
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")
        elif choice == '2':
            print("\nĐang tạo số nguyên tố ngẫu nhiên...")
            q = generate_large_prime(bits=8)  # Tạo số nguyên tố khoảng 8-bit để dễ hiểu quá trình
            print(f"Đã tạo số nguyên tố q = {q}")
            return q
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

def get_primitive_root(q):
    """
    Lấy căn nguyên thủy của q từ người dùng hoặc tìm tự động
    """
    # Tìm tất cả các căn nguyên thủy
    print("\nĐang tìm các căn nguyên thủy của", q, "...")
    primitive_roots = find_primitive_roots(q)
    
    if not primitive_roots:
        print(f"Không tìm thấy căn nguyên thủy cho {q}.")
        return None
    
    # Hiển thị danh sách các căn nguyên thủy
    print(f"\nDanh sách các căn nguyên thủy của {q}:")
    
    # Hiển thị theo hàng nếu có nhiều căn nguyên thủy
    if len(primitive_roots) > 10:
        for i in range(0, len(primitive_roots), 10):
            print(" ".join(str(root) for root in primitive_roots[i:i+10]))
    else:
        print(" ".join(str(root) for root in primitive_roots))
    
    while True:
        print("\nChọn phương thức xác định căn nguyên thủy α:")
        print("1. Nhập căn nguyên thủy α từ bàn phím")
        print("2. Chọn căn nguyên thủy α tự động")
        choice = input("Lựa chọn của bạn (1/2): ")
        
        if choice == '1':
            alpha = input("\nNhập căn nguyên thủy α từ danh sách trên: ")
            try:
                alpha = int(alpha)
                if alpha in primitive_roots:
                    print(f"Đã chọn căn nguyên thủy α = {alpha}")
                    return alpha
                else:
                    print(f"{alpha} không phải là căn nguyên thủy của {q}.")
                    print("Vui lòng chọn một giá trị từ danh sách trên.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")
        elif choice == '2':
            alpha = random.choice(primitive_roots)
            print(f"Đã chọn căn nguyên thủy α = {alpha}")
            return alpha
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

def get_private_key(q, user=""):
    """
    Lấy khóa riêng từ người dùng hoặc tạo tự động
    """
    while True:
        print(f"\nChọn phương thức xác định khóa riêng cho {user}:")
        print("1. Nhập khóa riêng từ bàn phím")
        print("2. Tạo khóa riêng ngẫu nhiên")
        choice = input("Lựa chọn của bạn (1/2): ")
        
        if choice == '1':
            x = input(f"\nNhập khóa riêng cho {user} (1 < X < {q}): ")
            try:
                x = int(x)
                if 1 < x < q:
                    return x
                else:
                    print(f"Khóa riêng phải nằm trong khoảng (1, {q}).")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")
        elif choice == '2':
            x = random.randint(2, q-2)
            print(f"Đã tạo khóa riêng cho {user}: {x}")
            return x
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

def display_full_process(q, alpha, xa, xb, ya, yb, k):
    """
    Hiển thị toàn bộ quá trình trao đổi khóa Diffie-Hellman
    """
    print("\n" + "=" * 60)
    print("  TÓM TẮT QUÁ TRÌNH TRAO ĐỔI KHÓA DIFFIE-HELLMAN  ")
    print("=" * 60)
    
    print("\nBước 1: Xác định các tham số công khai")
    print(f"  - Số nguyên tố q: {q}")
    print(f"  - Căn nguyên thủy α: {alpha}")
    
    print("\nBước 2: Tạo khóa riêng và tính khóa công khai")
    print(f"  - Alice chọn khóa riêng XA = {xa}")
    print(f"  - Alice tính khóa công khai YA = α^XA mod q = {alpha}^{xa} mod {q} = {ya}")
    print(f"  - Bob chọn khóa riêng XB = {xb}")
    print(f"  - Bob tính khóa công khai YB = α^XB mod q = {alpha}^{xb} mod {q} = {yb}")
    
    print("\nBước 3: Trao đổi khóa công khai")
    print("  - Alice gửi YA cho Bob")
    print("  - Bob gửi YB cho Alice")
    
    print("\nBước 4: Tính khóa chung")
    print(f"  - Alice tính K = YB^XA mod q = {yb}^{xa} mod {q} = {k}")
    print(f"  - Bob tính K = YA^XB mod q = {ya}^{xb} mod {q} = {k}")
    
    print(f"\nKhóa chung cuối cùng: {k}")
    print("=" * 60)

def main():
    """Hàm chính điều khiển luồng chương trình"""
    clear_screen()
    print_header()
    
    # Khởi tạo logger
    logger = Logger()
    
    print("\nBước 1: Xác định các tham số công khai")
    # Lấy số nguyên tố q
    q = get_prime_number()
    
    # Lấy căn nguyên thủy alpha
    alpha = get_primitive_root(q)
    
    # Ghi log tham số
    logger.log_parameters(q, alpha)
    
    print(f"\nTham số công khai: q = {q}, α = {alpha}")
    
    print("\nBước 2: Tạo khóa riêng và tính khóa công khai")
    # Khởi tạo đối tượng Diffie-Hellman cho Alice và Bob
    alice = DiffieHellman(q, alpha, logger)
    bob = DiffieHellman(q, alpha, logger)
    
    # Lấy khóa riêng cho Alice
    print("\n--- Alice ---")
    xa = get_private_key(q, "Alice")
    alice.set_private_key(xa)
    
    # Lấy khóa riêng cho Bob
    print("\n--- Bob ---")
    xb = get_private_key(q, "Bob")
    bob.set_private_key(xb)
    
    # Ghi log khóa riêng
    logger.log_private_keys(xa, xb)
    
    # Tính khóa công khai
    print("\nTính khóa công khai:")
    print(f"Alice tính YA = α^XA mod q = {alpha}^{xa} mod {q}")
    ya = alice.generate_public_key()
    print(f"YA = {ya}")
    
    print(f"\nBob tính YB = α^XB mod q = {alpha}^{xb} mod {q}")
    yb = bob.generate_public_key()
    print(f"YB = {yb}")
    
    # Ghi log khóa công khai
    logger.log_public_keys(ya, yb)
    
    print("\nBước 3: Trao đổi khóa công khai")
    print("Alice gửi YA cho Bob")
    print("Bob gửi YB cho Alice")
    
    print("\nBước 4: Tính khóa chung")
    print(f"Alice tính K = YB^XA mod q = {yb}^{xa} mod {q}")
    ka = alice.compute_shared_secret(yb)
    print(f"K = {ka}")
    
    print(f"\nBob tính K = YA^XB mod q = {ya}^{xb} mod {q}")
    kb = bob.compute_shared_secret(ya)
    print(f"K = {kb}")
    
    # Ghi log khóa chung
    logger.log_shared_secrets(ka, kb)
    
    # Kiểm tra khóa chung
    if ka == kb:
        print("\n✓ Hai khóa chung bằng nhau, quá trình trao đổi khóa thành công!")
    else:
        print("\n✗ Hai khóa chung không bằng nhau, quá trình trao đổi khóa thất bại!")
    
    # Ghi tóm tắt
    logger.log_summary(q, alpha, xa, xb, ya, yb, ka)
    
    # Hiển thị toàn bộ quá trình
    display_full_process(q, alpha, xa, xb, ya, yb, ka)
    
    print(f"\nKết quả chi tiết đã được lưu vào file: output/output.txt")
    
    input("\nNhấn Enter để kết thúc...")

if __name__ == "__main__":
    main()
