
# Thuật toán A* tìm đường ngắn nhất

Đây là chương trình Python cài đặt thuật toán **A*** (A-star) để tìm đường đi ngắn nhất giữa hai đỉnh trên đồ thị có trọng số và có giá trị heuristic (ước lượng chi phí còn lại đến đích).

## 📁 Cấu trúc tệp

- `astar.py`: Tệp chính chứa mã nguồn thuật toán A*.
- `graph.txt`: Tệp đầu vào chứa thông tin đồ thị và heuristic (người dùng cần tạo tệp này).

## 🚀 Cách chạy chương trình

```bash
python astar.py
```

Đảm bảo rằng tệp `graph.txt` nằm cùng thư mục với `astar.py`.

## 📄 Định dạng tệp đầu vào (`graph.txt`)

Tệp `graph.txt` cần có định dạng như sau:

```
<số đỉnh> <số cạnh>
<đỉnh bắt đầu> <đỉnh kết thúc>
<u1> <v1> <w1>
<u2> <v2> <w2>
...
<heuristic1> <heuristic2> ... <heuristicN>
```

- Các đỉnh được đánh số từ 1.
- Các cạnh là **vô hướng** và có trọng số `w`.
- Dòng cuối cùng là các giá trị **heuristic** ứng với từng đỉnh, từ 1 đến N.

### Ví dụ tệp `graph.txt`:

```
5 6
1 5
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
7 6 2 1 0
```

Trong đó:
- Đồ thị có 5 đỉnh, 6 cạnh.
- Tìm đường từ đỉnh 1 đến đỉnh 5.
- Giá trị heuristic của các đỉnh lần lượt là: h(1)=7, h(2)=6, h(3)=2, h(4)=1, h(5)=0

## ✅ Kết quả đầu ra

Chương trình sẽ in ra:

- `Chi Phi la`: Tổng chi phí đường đi từ đỉnh bắt đầu đến đỉnh kết thúc.
- `Duong di`: Danh sách các đỉnh theo thứ tự từ đỉnh bắt đầu đến đỉnh kết thúc.

### Ví dụ đầu ra:

```
Chi Phi la : 7
Duong di: [1, 2, 3, 5]
```

## 🧠 Mô tả thuật toán A*

Thuật toán A* là một thuật toán tìm kiếm có trọng số sử dụng công thức:

```
f(n) = g(n) + h(n)
```

- `g(n)`: Chi phí từ đỉnh bắt đầu đến đỉnh `n` (đã biết).
- `h(n)`: Heuristic – ước lượng chi phí từ `n` đến đích (do người dùng cung cấp).
- `f(n)`: Tổng chi phí ước lượng để đi từ đỉnh bắt đầu qua `n` đến đích.

Thuật toán sử dụng hai danh sách:
- **open list**: các đỉnh đang chờ được xét.
- **closed list**: các đỉnh đã xét.

Tại mỗi bước, thuật toán chọn đỉnh có giá trị `f(n)` nhỏ nhất từ open list và mở rộng nó, cập nhật chi phí và đường đi nếu tìm được đường tốt hơn.

## 📌 Ghi chú

- Thuật toán áp dụng cho đồ thị vô hướng.
- Heuristic cần **không vượt quá chi phí thực tế còn lại** (tính chất admissible) để đảm bảo tìm được đường đi tối ưu.

## 📜 Giấy phép

Chương trình được cung cấp miễn phí cho mục đích học tập và nghiên cứu.
