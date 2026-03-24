#!/usr/bin/env python3
"""Convert a markdown file to PDF with CJK font support."""

import sys
import markdown
from weasyprint import HTML

def convert(md_path: str, output_path: str):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=['tables', 'toc'])

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    font-family: 'Droid Sans Fallback', sans-serif;
    font-size: 13px;
    line-height: 1.7;
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 50px;
    color: #1a1a1a;
  }}
  h1 {{ font-size: 22px; border-bottom: 2px solid #333; padding-bottom: 8px; margin-bottom: 20px; }}
  h2 {{ font-size: 17px; border-left: 4px solid #4a90d9; padding-left: 10px; margin-top: 30px; color: #2c3e50; }}
  h3 {{ font-size: 14px; margin-top: 20px; color: #34495e; }}
  table {{ border-collapse: collapse; width: 100%; margin: 14px 0; font-size: 12px; }}
  th {{ background: #4a90d9; color: white; padding: 8px 10px; text-align: left; }}
  td {{ border: 1px solid #ddd; padding: 7px 10px; text-align: center; }}
  td:first-child {{ text-align: left; font-weight: bold; }}
  tr:nth-child(even) {{ background: #f7f9fc; }}
  blockquote {{
    background: #fff8e1;
    border-left: 4px solid #f5a623;
    margin: 14px 0;
    padding: 10px 16px;
    border-radius: 0 4px 4px 0;
  }}
  blockquote p {{ margin: 4px 0; }}
  code {{ background: #f0f0f0; padding: 1px 5px; border-radius: 3px; font-size: 11px; }}
  ul, ol {{ padding-left: 22px; }}
  li {{ margin: 4px 0; }}
  del {{ color: #999; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 24px 0; }}
  p {{ margin: 8px 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=html).write_pdf(output_path)
    print(f"PDF generated: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        convert(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        md = sys.argv[1]
        out = md.rsplit('.', 1)[0] + '.pdf'
        convert(md, out)
    else:
        print("Usage: python3 generate_pdf.py <input.md> [output.pdf]")
        sys.exit(1)
