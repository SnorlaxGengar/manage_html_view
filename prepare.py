import os
import re

paragraphs = {}
max_chapter_number = 0
for (dir_path, dir_names, filenames) in os.walk('.'):
    if dir_path == '.':
        continue
    chapter_number = re.findall(r'\d+', dir_path)
    if not chapter_number:
        continue
    chapter_number = int(chapter_number[0])
    max_chapter_number = max(max_chapter_number, chapter_number)
    dir_name = dir_path.split(os.path.sep)[-1]
    index_html = os.path.join(dir_path, 'index.html')
    with open(index_html, 'w') as file:
        file.write(f'<title>{dir_name}</title>\n')
        file.write(f'<body>\n')
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext not in ['.jpg', '.png']:
                continue
            file.write(f'<img src="{filename}" alt=""/>\n')
        file.write(f'</body>')
    paragraphs[chapter_number] = f'<a href="{index_html}">{dir_name}</a><br/>'

with open('demo.html', 'w', encoding='utf8') as demo:
    demo.write('''
<head>
    <meta charset="UTF-8">
</head>
''')
    demo.write(f'<body>\n')
    for i in range(max_chapter_number):
        demo.write(paragraphs[i+1] + '\n')
    demo.write(f'</body>\n')