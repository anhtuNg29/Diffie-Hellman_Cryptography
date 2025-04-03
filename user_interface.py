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
