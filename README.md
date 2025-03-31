# Hướng dẫn chạy
Sử dụng terminal và chạy 2 lệnh dưới dây

'pip install -r requirements.txt' (download các tài nguyên cần thiết)

'python manage.py runserver' (chạy ứng dụng)

# Cấu trúc cơ bản của web
ChessWeb/chessWeb là file quản lí và deploy web với cấu trúc cơ bản gồm

Folder 'static' chứa các file tĩnh như ảnh hoặc css, javascript files, trong đó chess.js là quan trọng nhất chứa hầu hết logic của bàn cờ và sử dụng ajax để truyền và nhận dữ liệu từ giao diện web qua thuật toán thông qua users/views.py
Foleder 'stockfish' chứa thuật toán stockfish
users có những file quan trọng cần lưu ý gồm : 
- users/templates chứa file html tạo các đối tượng cho web và chỉnh sửa 
- users/views.py : dùng để giao tiếp (truyền và nhận dữ liệu) giữa phần giao diện và thuật toán python
- users/urls.py : Import các hàm từ views.py vào để thực thi
- users/algorithms.py : Chứa thuật toán Alpha Beta