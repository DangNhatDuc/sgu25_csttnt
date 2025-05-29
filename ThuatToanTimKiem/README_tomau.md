
# Thuật toán tô màu đồ thị - Welsh-Powell

Đây là chương trình Python cài đặt thuật toán **Welsh-Powell** để tô màu các đỉnh của một đồ thị sao cho không có hai đỉnh kề nhau nào có cùng màu, sử dụng ít màu nhất có thể.

## 📁 Cấu trúc tệp

- `tomau.py`: Tệp chính chứa mã nguồn cài đặt thuật toán Welsh-Powell.
- `color.txt`: Tệp đầu vào chứa ma trận kề của đồ thị.
- `output.txt`: Tệp đầu ra lưu kết quả tô màu.

## 🚀 Cách chạy chương trình

```bash
python tomau.py
```

Đảm bảo rằng tệp `color.txt` nằm cùng thư mục với `tomau.py`.

## 📄 Định dạng tệp đầu vào (`color.txt`)

Tệp đầu vào là một ma trận kề của đồ thị, với định dạng:

```
<n>
<dòng 1 gồm n số>
<dòng 2 gồm n số>
...
<dòng n gồm n số>
```

- `n`: số lượng đỉnh của đồ thị.
- Các dòng tiếp theo là ma trận kề kích thước `n x n`, mỗi phần tử là 0 hoặc 1:
  - `1` nếu hai đỉnh kề nhau.
  - `0` nếu không kề nhau.

### Ví dụ:

```
4
0 1 1 0
1 0 1 1
1 1 0 1
0 1 1 0
```

Đây là đồ thị có 4 đỉnh, với các cạnh giữa các đỉnh có giá trị là `1`.

## ✅ Kết quả đầu ra

Chương trình in ra màn hình và ghi vào `output.txt`:

- Số màu sử dụng để tô đồ thị.
- Màu tương ứng của từng đỉnh.

Ví dụ trong `output.txt`:

```
So mau su dung: 3
Cac dinh va mau tuong ung:
Dinh 0 : Mau 1
Dinh 1 : Mau 2
Dinh 2 : Mau 3
Dinh 3 : Mau 1
```

## 🧠 Mô tả thuật toán Welsh-Powell

1. Tính bậc (số đỉnh kề) của mỗi đỉnh.
2. Sắp xếp các đỉnh theo thứ tự giảm dần bậc.
3. Duyệt từng đỉnh, tô màu một cách **tham lam (greedy)**:
   - Duyệt qua các đỉnh chưa tô màu.
   - Nếu một đỉnh không kề với đỉnh nào đã tô màu hiện tại, gán cho nó màu đó.

## 📌 Ghi chú

- Các đỉnh được đánh số từ `0`.
- Đảm bảo rằng dữ liệu trong `color.txt` đúng định dạng.

