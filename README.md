# BÁO CÁO THỰC HÀNH KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM

## 1. Thông tin bài thực hành

- **Chủ đề:** Tìm hiểu Selenium và xây dựng kiểm thử tự động cho website.
- **Website:** [SauceDemo](https://www.saucedemo.com/)
- **Công nghệ:** Python 3.10+, Selenium WebDriver, pytest, Google Chrome, GitHub Actions.
- **Họ tên / Mã sinh viên / Lớp:** *[Sinh viên bổ sung]*
- **Ngày thực hiện:** *[Sinh viên bổ sung]*

## 2. Mục tiêu

1. Tìm hiểu cách Selenium WebDriver điều khiển trình duyệt và các bộ định vị (locator).
2. Thiết kế và lập trình tối thiểu 05 test case kiểm thử tự động.
3. Sử dụng pytest để tổ chức test và assertion để đối chiếu kết quả.
4. Quản lý mã nguồn và trình bày báo cáo bằng README trên GitHub.

## 3. Tài liệu học tập

- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)
- [Selenium Getting Started](https://www.selenium.dev/documentation/webdriver/getting_started/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)

Các chủ đề cần tìm hiểu: Selenium WebDriver; Selenium Manager; `By.ID`, `By.CLASS_NAME`, `By.CSS_SELECTOR`; `WebDriverWait`; `pytest.fixture` và `assert`.

*Ghi rõ video hoặc tài liệu bạn đã thực sự học khi hoàn thiện báo cáo.*

## 4. Giới thiệu website kiểm thử

[https://www.saucedemo.com/](https://www.saucedemo.com/) là trang demo thương mại điện tử, hỗ trợ đăng nhập, xem sản phẩm, thêm/xóa giỏ hàng, sắp xếp và đăng xuất.

Tài khoản demo công khai:
- Username: `standard_user`
- Password: `secret_sauce`

## 5. Thiết kế test case

| ID | Chức năng | Các bước thực hiện | Kết quả mong đợi |
|---|---|---|---|
| TC01 | Đăng nhập đúng | Mở trang, nhập tài khoản demo, nhấn Login | Hiển thị danh sách Products |
| TC02 | Đăng nhập sai | Nhập username đúng, password sai | Thông báo lỗi, không đăng nhập |
| TC03 | Thêm giỏ hàng | Đăng nhập, Add to cart cho Backpack, mở giỏ | Có 1 sản phẩm Sauce Labs Backpack |
| TC04 | Xóa khỏi giỏ | Thêm Backpack, vào giỏ, nhấn Remove | Giỏ hàng rỗng |
| TC05 | Sắp xếp giá tăng dần | Đăng nhập, chọn Price (low to high) | Giá được sắp xếp tăng dần |
| TC06 | Đăng xuất | Đăng nhập, mở menu, nhấn Logout | Trở về trang đăng nhập |

**Tổng cộng: 06 test case (vượt yêu cầu 05 test case).**

## 6. Cấu trúc repository

```text
selenium-automation-testing/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   ├── conftest.py
│   └── test_saucedemo.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 7. Cài đặt và chạy

Máy cần có Python 3.10+, Google Chrome và kết nối mạng.

Trên Windows PowerShell:

```powershell
git clone https://github.com/AChingNoLu/selenium-automation-testing..git
cd selenium-automation-testing.
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
```

Chạy một test:

```powershell
python -m pytest -v tests/test_saucedemo.py::test_03_add_product_to_cart
```

Chạy không mở giao diện Chrome:

```powershell
$env:HEADLESS="1"
python -m pytest -v
```

Xem chạy kiểm thử trên CI ở tab **Actions** của repository.

## 8. Kết quả thực hiện

**Đã hoàn thiện:** Mã nguồn Python cho 06 test case Selenium, fixture pytest, danh sách thư viện cần cài, GitHub Actions và báo cáo này.

**Chưa xác minh:** Kết quả thực thi thực tế trên Chrome/GitHub Actions. Không mặc định đánh dấu PASS khi chưa có log.

| Thông tin | Kết quả |
|---|---|
| Ngày kiểm thử | Chưa cập nhật |
| Chrome / Python | Chưa cập nhật |
| Số test đã chạy | Chưa cập nhật |
| PASSED / FAILED | Chưa cập nhật |
| Link log hoặc hình ảnh minh chứng | Chưa cập nhật |

## 9. Nhận xét và hạn chế

- Các test mô phỏng hành vi người dùng thông qua trình duyệt thật, có kiểm tra kết quả bằng assertion.
- Sử dụng fixture để tránh lặp thao tác chuẩn bị; các ca kiểm thử tách riêng và dễ mở rộng.
- Selenium phụ thuộc phần tử HTML và trạng thái website, do đó locator có thể cần cập nhật nếu trang thay đổi.
- Chưa thử nhiều trình duyệt, chưa kiểm thử thanh toán và chưa bổ sung minh chứng thực chạy.

## 10. Kết luận

Bài thực hành triển khai 06 kịch bản kiểm thử tự động bằng Selenium cho SauceDemo, đáp ứng yêu cầu tối thiểu 05 test case. Sau khi chạy thử, sinh viên bổ sung kết quả thực tế và hình ảnh hoặc link Actions, điền thông tin cá nhân trước khi nộp.

**Link nộp:** https://github.com/AChingNoLu/selenium-automation-testing.
