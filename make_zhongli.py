"""由桃園版 index.html 產生中壢版 zhongli/index.html。

開課分校兩版都是桃園分校，只替換報名諮詢窗口（電話、LINE、QR Code）。
修改內容時請只改 index.html，再執行：python make_zhongli.py
"""
from pathlib import Path

ROOT = Path(__file__).parent

# (桃園版原文, 中壢版替換文字, 預期出現次數)
REPLACEMENTS = [
    ('<b>桃園分校 課程諮詢</b>', '<b>中壢分校 課程諮詢</b>', 1),
    ('<span>LINE ID：<span class="num">@gqf5629y</span></span>', '<span>掃描 QR Code 加 LINE</span>', 1),
    ('images/qr-line-taoyuan.png', 'images/qr-line-zhongli.png', 1),
    ('https://lin.ee/TgQkT03', 'https://lin.ee/y1D19NG', 2),
    ('tel:+88633471078', 'tel:+88634271238', 1),
    ('03-3471078', '03-4271238', 3),
    ('洽詢桃園分校', '洽詢中壢分校', 1),
    # 中壢版放在子資料夾，共用上一層的圖片
    ('src="images/', 'src="../images/', None),
]


def main():
    html = (ROOT / "index.html").read_text(encoding="utf8")
    for old, new, count in REPLACEMENTS:
        found = html.count(old)
        if count is not None and found != count:
            raise SystemExit(f"預期找到 {count} 處「{old}」，實際 {found} 處，請檢查 index.html")
        html = html.replace(old, new)
    out = ROOT / "zhongli" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf8", newline="")
    print(f"已產生 {out}")


if __name__ == "__main__":
    main()
