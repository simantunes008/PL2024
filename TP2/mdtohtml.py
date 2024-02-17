import re
import sys

def markdown_to_html(markdown):
    # Cabeçalhos
    markdown = re.sub(r'#{3}\s+(.*)', r'<h3>\1</h3>', markdown)
    markdown = re.sub(r'#{2}\s+(.*)', r'<h2>\1</h2>', markdown)
    markdown = re.sub(r'#{1}\s+(.*)', r'<h1>\1</h1>', markdown)
    
    # Negritos
    markdown = re.sub(r'\*{2}(.*?)\*{2}', r'<b>\1</b>', markdown)
    
    # Itálicos
    markdown = re.sub(r'\*{1}(.*?)\*{1}', r'<i>\1</i>', markdown)
    
    # Listas numeradas
    markdown = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', markdown)
    markdown = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>', markdown)
    
    # Imagens
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)
    
    # Links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    
    return markdown

def main():
    markdown_text = sys.stdin.read()
    html_text = markdown_to_html(markdown_text)
    with open('output.html', 'w') as file:
        file.write(html_text)

if __name__ == '__main__':
    main()
