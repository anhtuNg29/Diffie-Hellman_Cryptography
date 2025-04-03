"""
Module chức năng chính của thuật toán Diffie-Hellman
"""
import random
from prime_utils import power_mod

class DiffieHellman:
    def __init__(self, q, alpha, logger=None):
        """
        Khởi tạo đối tượng Diffie-Hellman với các tham số công khai
        
        :param q: Số nguyên tố
        :param alpha: Căn nguyên thủy của q
        :param logger: Đối tượng logger để ghi log
        """
        self.q = q
        self.alpha = alpha
        self.private_key = None
        self.public_key = None
        self.shared_secret = None
        self.logger = logger
        
    def generate_private_key(self):
        """
        Tạo khóa riêng ngẫu nhiên nhỏ hơn q
        """
        self.private_key = random.randint(2, self.q - 2)
        return self.private_key
    
    def set_private_key(self, private_key):
        """
        Thiết lập khóa riêng
        
        :param private_key: Khóa riêng
        """
        if 1 < private_key < self.q:
            self.private_key = private_key
            return True
        return False
    
    def generate_public_key(self):
        """
        Tính khóa công khai từ khóa riêng: Y = alpha^X mod q
        """
        if self.private_key is None:
            raise ValueError("Cần thiết lập khóa riêng trước")
        
        self.public_key = power_mod(self.alpha, self.private_key, self.q)
        
        # Ghi log chi tiết tính toán
        if self.logger:
            self.logger.log_public_key_calculation(
                self.alpha, self.private_key, self.q, self.public_key
            )
            
        return self.public_key
    
    def compute_shared_secret(self, other_public_key):
        """
        Tính khóa chung từ khóa công khai của đối tác: K = Y^X mod q
        
        :param other_public_key: Khóa công khai của đối tác
        """
        if self.private_key is None:
            raise ValueError("Cần thiết lập khóa riêng trước")
        
        self.shared_secret = power_mod(other_public_key, self.private_key, self.q)
        
        # Ghi log chi tiết tính toán
        if self.logger:
            self.logger.log_shared_secret_calculation(
                other_public_key, self.private_key, self.q, self.shared_secret
            )
            
        return self.shared_secret
