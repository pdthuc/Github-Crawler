# Crawler Tìm Liên Kết GitHub của Bài Báo

## Giới thiệu

Đây là một chương trình Python dùng để tìm liên kết GitHub của bài báo dựa vào tên bài báo được cung cấp. Chương trình sử dụng Selenium để tự động tìm kiếm thông tin trên Google và kiểm tra xem bài báo có liên kết GitHub hay không. Nếu có, chương trình sẽ trả về liên kết, ngược lại sẽ thông báo không tìm thấy liên kết GitHub.

## Yêu cầu

- Python 3.8
- `selenium`
- `requests`
- Trình duyệt Chrome (hoặc trình duyệt khác và tương ứng với ChromeDriver)

## Cài đặt

1. Clone repository này về máy của bạn:

```bash
git https://github.com/pdthuc/Github-Crawler.git
cd Github-Crawler
```

2. Cài đặt các gói cần thiết bằng pip:

```bash
pip install -r requirements.txt
```

3. Đảm bảo bạn đã cài đặt trình duyệt Chrome (hoặc trình duyệt khác) và ChromeDriver phù hợp.

## Sử dụng

Chạy chương trình với cú pháp:
```bash
python find_github.py --name "<Tên bài báo>"
```

Thay `"Tên bài báo"` bằng tiêu đề của bài báo bạn muốn tìm liên kết GitHub.

## Ví dụ
```bash
python find_github.py --name "Improving Pixel-based MIM by Reducing Wasted Modeling Capability"
```

Kết quả:
```bash
Found paper: 
{
    "Acticle_title": "Improving Pixel-based MIM by Reducing Wasted Modeling Capability",
    "status": "OK",
    "Github": [
        "https://github.com/open-mmlab/mmpretrain"
    ]
}
```
Hoặc nếu không tìm thấy liên kết GitHub cho bài báo (Paper no code):
```bash
Found paper: 
{
    "Acticle_title": "Emotion and Sentiment Guided Paraphrasing",
    "status": "OK",
    "Github": "No code"
}
```

Hoặc nếu không tìm thấy bài báo:
```bash
{
    "Acticle_title": "Truong dai hoc Khoa hoc Tu nhien",
    "status": "Paper not found"
}
```

## Lưu ý

- Chương trình này sử dụng trình duyệt Chrome để tìm kiếm thông tin trên Google, vì vậy hãy đảm bảo rằng bạn đã cài đặt ChromeDriver phù hợp và có đường dẫn tới nó trong biến môi trường PATH hoặc chỉ định đúng đường dẫn tới ChromeDriver trong code.

## Đóng góp

Nếu bạn tìm thấy lỗi hoặc có cách cải thiện chương trình, vui lòng tạo một pull request hoặc báo cáo vấn đề mới.

## Tác giả

- Họ tên: PHAM DINH THUC
- Email: 22C11045@student.hcmus.edu.vn

## Giấy phép

Chương trình này được phân phối dưới giấy phép MIT. Xem `LICENSE` để biết thêm thông tin.
