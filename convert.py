import re
import argparse


def main():
    parser = argparse.ArgumentParser(description='add two integers')
    parser.add_argument('-i', '--input', type=str, help='input file')
    parser.add_argument('-o', '--output', type=str, help='output file')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        input = f.readlines()

    cache = ''
    for index, line in enumerate(input):
        # print(f'{index} {line}')
        prev_line = input[index - 1] if index != 0 else None
        next_line = input[index + 1] if index != len(input) - 1 else None

        if line.startswith('#'):
            cache += line
        elif line.isspace():
            cache += line
        elif line.startswith('title:'):
            cache += line
        elif line.startswith('description:'):
            cache += line
        elif line.startswith('---'):
            cache += line
        elif line.lstrip().startswith('['):  # リンク
            cache += line
        elif line.lstrip().startswith('|'):  # 表
            cache += line
        elif line.lstrip().startswith('>'):  # 引用
            cache += line
        elif line.lstrip().startswith('<'):  # HTMLタグ
            cache += line
        elif next_line is not None and next_line.startswith('---'):
            cache += line
        elif next_line is not None and next_line.lstrip().startswith('- '):
            cache += line
        elif next_line is not None and next_line.isspace():
            cache += line
        elif next_line is not None:
            line = line.replace('\n', ' ')  # 改行を削除
            cache += line
        else:
            cache += line

    output = ''
    for index, line in enumerate(cache.splitlines()):
        line = line.replace('  ', ' ')
        line = line.replace('  ', ' ')
        line = line.replace('  ', ' ')
        line = line.replace('  ', ' ')

        line = line.replace('- ', '-   ')  # インデントのルール
        line = line.replace(' - ', '    - ')  # インデントのルール
        output += line + '\n'

    with open(args.output, 'w') as f:
        f.write(output)


if __name__ == "__main__":
    main()
