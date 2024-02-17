import re
import sys

def markdown_to_html(markdown):
    # Cabeçalhos
    markdown = re.sub(r'###\s+(.*)', r'<h3>\1</h3>', markdown)
    markdown = re.sub(r'##\s+(.*)', r'<h2>\1</h2>', markdown)
    markdown = re.sub(r'#\s+(.*)', r'<h1>\1</h1>', markdown)
    
    # Negrito
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    
    # Itálico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    
    # Linha horizontal
    markdown = re.sub(r'---', r'<hr/>', markdown)
    
    # Bloco de código
    markdown = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown)
    
    # Lista numerada
    markdown = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', markdown)
    markdown = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>\n', markdown)
    
    # Lista não numerada
    markdown = re.sub(r'(-\s+.*\n?)+', r'<ul>\g<0></ul>', markdown)
    markdown = re.sub(r'-\s+(.*)', r'<li>\1</li>\n', markdown)
    
    # Imagem
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)
    
    # Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    
    return markdown

def main():
    markdown_text = sys.stdin.read()
    html_text = markdown_to_html(markdown_text)
    with open('output.html', 'w') as file:
        file.write(html_text)

if __name__ == '__main__':
    main()
