# Dự án mô phỏng trao đổi khóa Diffie-Hellman

Dự án này mô phỏng quá trình trao đổi khóa sử dụng thuật toán Diffie-Hellman. Chương trình cho phép người dùng thực hiện từng bước của quá trình và hiển thị chi tiết các bước tính toán.

## Cấu trúc dự án

- `main.py`: Chương trình chính điều khiển luồng chương trình
- `prime_utils.py`: Các tiện ích liên quan đến số nguyên tố
- `diffie_hellman.py`: Module chính thực hiện thuật toán Diffie-Hellman
- `user_interface.py`: Các chức năng giao diện người dùng

## Cách sử dụng

1. Chạy chương trình:
```
python main.py
```

2. Theo dõi các bước trong quá trình:
   - Xác định số nguyên tố q (nhập từ bàn phím hoặc tạo ngẫu nhiên)
   - Xác định căn nguyên thủy α (chọn từ danh sách, nhập từ bàn phím hoặc chọn ngẫu nhiên) 
   - Tạo khóa riêng cho bên A và B (nhập từ bàn phím hoặc tạo ngẫu nhiên)
   - Tính toán và hiển thị khóa công khai
   - Tính toán và hiển thị khóa bí mật
   - Hiển thị chi tiết từng bước của quá trình

## Thuật toán Diffie-Hellman

### Bước thiết lập ban đầu
1. Chọn số nguyên tố q
2. Chọn căn nguyên thủy α của q (α < q)

### Bước thực hiện cho bên A
1. Chọn khóa riêng X_A (X_A < q)
2. Tính khóa công khai Y_A = α^X_A mod q
3. Gửi Y_A cho B

### Bước thực hiện cho bên B
1. Chọn khóa riêng X_B (X_B < q)
2. Tính khóa công khai Y_B = α^X_B mod q
3. Gửi Y_B cho A

### Tính toán khóa bí mật chung
- A tính: K = (Y_B)^X_A mod q
- B tính: K = (Y_A)^X_B mod q

Lý thuyết toán học đảm bảo rằng cả hai khóa bí mật đều giống nhau.

## Chú ý

- Chương trình mô phỏng vẫn sử dụng các số nhỏ hơn nhiều so với ứng dụng thực tế để dễ hiểu
- Trong các ứng dụng thực tế, q thường là số nguyên tố có 2048 bit hoặc lớn hơn
- Việc tìm căn nguyên thủy có thể tốn nhiều thời gian với số nguyên tố lớn