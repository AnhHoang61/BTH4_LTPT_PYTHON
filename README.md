
Chạy chương trình
Bước 1: Khởi động Name Server
Trước khi chạy server, bạn cần khởi động Name Server của Pyro4, có thể chạy lệnh sau trong dòng lệnh:

python -m Pyro4.naming

Bước 2: Khởi động Server
Trong một cửa sổ dòng lệnh khác, chạy server:

python server.py

Server sẽ in ra URI của đối tượng từ xa. Ví dụ: Ready. Object uri = PYRO:object_abcdef123456@localhost:12345


Bước 3: Khởi động Client
Trong một cửa sổ dòng lệnh khác, chạy client:

python client.py

Nhập URI của đối tượng từ xa được in ra từ server (ví dụ: PYRO:object_abcdef123456@localhost:12345).

Client sẽ hiển thị thông báo:
Response: Hello, World!