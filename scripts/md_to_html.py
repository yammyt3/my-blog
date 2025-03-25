import markdown
import os
import sys

def convert(md_path):
    filename = os.path.basename(md_path)
    name, _ = os.path.splitext(filename)
    output_path = f"../posts/{name}.html"

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text)

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <title>{name}</title>
  <link rel="stylesheet" href="../assets/style.css">
  <meta name="date" content="{name}">
</head>
<body>
  <h1>{name}</h1>
  {html_body}
  <p><a href="../index.html">← トップに戻る</a></p>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ 変換完了: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python md_to_html.py ../drafts/2025-03-28.md")
    else:
        convert(sys.argv[1])
