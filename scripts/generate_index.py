from bs4 import BeautifulSoup
import os

POSTS_DIR = "posts"  # ← 変更：相対パスをルートからに
OUTPUT_FILE = "index.html"

def get_post_info(filepath):
    with open(filepath, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        meta_date = soup.find("meta", attrs={"name": "date"})
        date = meta_date["content"] if meta_date else "Unknown"
        return {
            "filename": os.path.basename(filepath),
            "title": title,
            "date": date
        }

def main():
    files = sorted(os.listdir(POSTS_DIR))
    posts = []
    for f in files:
        if f.endswith(".html"):
            info = get_post_info(os.path.join(POSTS_DIR, f))
            posts.append(info)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("<!DOCTYPE html>\n<html lang='ja'>\n<head>\n")
        out.write("<meta charset='UTF-8'>\n<title>My Blog</title>\n")
        out.write("<link rel='stylesheet' href='assets/style.css'>\n</head>\n<body>\n")
        out.write("<h1>記事一覧</h1>\n<ul>\n")
        for post in sorted(posts, key=lambda x: x["date"], reverse=True):
            out.write(f"<li>{post['date']} - <a href='posts/{post['filename']}'>{post['title']}</a></li>\n")
        out.write("</ul>\n</body>\n</html>")

if __name__ == "__main__":
    main()
 