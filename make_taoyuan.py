"""由中壢版 index.html 產生桃園版 taoyuan/index.html。

開課分校兩版都是桃園分校，只替換報名諮詢窗口（電話、LINE、QR Code）。
修改內容時請只改 index.html，再執行：python make_taoyuan.py
"""
from pathlib import Path

ROOT = Path(__file__).parent

# (中壢版原文, 桃園版替換文字, 預期出現次數)
REPLACEMENTS = [
    ('<b>中壢分校 課程諮詢</b>', '<b>桃園分校 課程諮詢</b>', 1),
    ('<span>掃描 QR Code 加 LINE</span>', '<span>LINE ID：<span class="num">@gqf5629y</span></span>', 1),
    ('images/qr-line-zhongli.png', 'images/qr-line-taoyuan.png', 1),
    ('https://lin.ee/y1D19NG', 'https://lin.ee/TgQkT03', 2),
    ('tel:+88634271238', 'tel:+88633471078', 1),
    ('03-4271238', '03-3471078', 3),
    ('洽詢中壢分校', '洽詢桃園分校', 1),
    # 桃園版放在子資料夾，共用上一層的圖片
    ('src="images/', 'src="../images/', None),
]


def main():
    html = (ROOT / "index.html").read_text(encoding="utf8")
    for old, new, count in REPLACEMENTS:
        found = html.count(old)
        if count is not None and found != count:
            raise SystemExit(f"預期找到 {count} 處「{old}」，實際 {found} 處，請檢查 index.html")
        html = html.replace(old, new)
    out = ROOT / "taoyuan" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf8", newline="")
    print("done:", out.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
