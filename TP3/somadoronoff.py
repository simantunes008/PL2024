import sys
import re

def somador_on_off(text):
    pattern_on_off = re.compile(r'on.*?off|=', re.IGNORECASE)
    pattern_inteiros = re.compile(r'[+-]?\d+|=')
    
    matches = pattern_on_off.findall(text)
    
    result = []
    
    for match in matches:
        result.extend(pattern_inteiros.findall(match))
    
    soma = 0
    for item in result:
        if item == '=':
            print(soma)
        else:
            soma += int(item)
    return soma

def main():
    input = sys.stdin.read()
    print(somador_on_off(input))

if __name__ == '__main__':
    main()
