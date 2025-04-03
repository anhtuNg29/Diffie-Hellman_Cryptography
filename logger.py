"""
Module xử lý ghi log cho chương trình Diffie-Hellman
"""
import os
import datetime

class Logger:
    def __init__(self):
        """Khởi tạo logger và tạo thư mục output nếu chưa tồn tại"""
        # Tạo thư mục output nếu chưa tồn tại
        if not os.path.exists('output'):
            os.makedirs('output')
        
        self.output_file = 'output/output.txt'
        
        # Xóa nội dung cũ và tạo file mới
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(f"DIFFIE-HELLMAN KEY EXCHANGE - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 70 + "\n\n")
    
    def log(self, message):
        """Ghi thông điệp vào file log"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")
    
    def log_parameters(self, q, alpha):
        """Ghi thông tin về các tham số công khai"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write("\nCÁC THAM SỐ CÔNG KHAI\n")
            f.write("-" * 70 + "\n")
            f.write(f"Số nguyên tố q: {q}\n")
            f.write(f"Căn nguyên thủy α: {alpha}\n")
            f.write("-" * 70 + "\n\n")
    
    def log_private_keys(self, xa, xb):
        """Ghi thông tin về các khóa riêng"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write("\nCÁC KHÓA RIÊNG\n")
            f.write("-" * 70 + "\n")
            f.write(f"Khóa riêng của A (XA): {xa}\n")
            f.write(f"Khóa riêng của B (XB): {xb}\n")
            f.write("-" * 70 + "\n\n")
    
    def log_public_key_calculation(self, alpha, x, q, y):
        """Ghi chi tiết tính toán khóa công khai"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(f"Tính khóa công khai Y = α^X mod q:\n")
            f.write(f"  Y = {alpha}^{x} mod {q}\n")
            f.write(f"  Y = {y}\n\n")
    
    def log_public_keys(self, ya, yb):
        """Ghi thông tin về các khóa công khai"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write("\nCÁC KHÓA CÔNG KHAI\n")
            f.write("-" * 70 + "\n")
            f.write(f"Khóa công khai của A (YA): {ya}\n")
            f.write(f"Khóa công khai của B (YB): {yb}\n")
            f.write("-" * 70 + "\n\n")
    
    def log_shared_secret_calculation(self, y, x, q, k):
        """Ghi chi tiết tính toán khóa chung"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(f"Tính khóa chung K = Y^X mod q:\n")
            f.write(f"  K = {y}^{x} mod {q}\n")
            f.write(f"  K = {k}\n\n")
    
    def log_shared_secrets(self, ka, kb):
        """Ghi thông tin về khóa chung"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write("\nKHÓA CHUNG\n")
            f.write("-" * 70 + "\n")
            f.write(f"Khóa chung tính bởi A: {ka}\n")
            f.write(f"Khóa chung tính bởi B: {kb}\n")
            
            if ka == kb:
                f.write("\n✓ Hai khóa chung bằng nhau, quá trình trao đổi khóa thành công!\n")
            else:
                f.write("\n✗ Hai khóa chung không bằng nhau, quá trình trao đổi khóa thất bại!\n")
            
            f.write("-" * 70 + "\n\n")
    
    def log_summary(self, q, alpha, xa, xb, ya, yb, k):
        """Ghi tóm tắt toàn bộ quá trình"""
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write("\nTÓM TẮT QUÁ TRÌNH TRAO ĐỔI KHÓA DIFFIE-HELLMAN\n")
            f.write("=" * 70 + "\n")
            f.write("Bước 1: Xác định các tham số công khai\n")
            f.write(f"  - Số nguyên tố q: {q}\n")
            f.write(f"  - Căn nguyên thủy α: {alpha}\n\n")
            
            f.write("Bước 2: Tạo khóa riêng và tính khóa công khai\n")
            f.write(f"  - A chọn khóa riêng XA = {xa}\n")
            f.write(f"  - A tính khóa công khai YA = α^XA mod q = {alpha}^{xa} mod {q} = {ya}\n")
            f.write(f"  - B chọn khóa riêng XB = {xb}\n")
            f.write(f"  - B tính khóa công khai YB = α^XB mod q = {alpha}^{xb} mod {q} = {yb}\n\n")
            
            f.write("Bước 3: Trao đổi khóa công khai\n")
            f.write("  - A gửi YA cho B\n")
            f.write("  - B gửi YB cho A\n\n")
            
            f.write("Bước 4: Tính khóa chung\n")
            f.write(f"  - A tính K = YB^XA mod q = {yb}^{xa} mod {q} = {k}\n")
            f.write(f"  - B tính K = YA^XB mod q = {ya}^{xb} mod {q} = {k}\n\n")
            
            f.write(f"Khóa chung cuối cùng: {k}\n")
            f.write("=" * 70 + "\n")
