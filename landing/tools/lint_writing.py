"""WRITING_RULES.md의 regex 규칙과 em dash를 검사한다.
사용법: python3 tools/lint_writing.py <파일...> [--rules WRITING_RULES.md]
HTML은 태그를 지운 뒤 줄 단위로 검사한다. 코드 블록(```)은 건너뛴다."""
import re, sys, os
args = sys.argv[1:]
rules_path = os.path.join(os.path.dirname(__file__), '..', 'WRITING_RULES.md')
if '--rules' in args:
    i = args.index('--rules'); rules_path = args[i + 1]; del args[i:i + 2]
rules = open(rules_path, encoding='utf-8').read()
pats = []
for m in re.finditer(r"regex:\s*'((?:[^']|'')*)'", rules):
    p = m.group(1).replace("''", "'")
    try: pats.append((p, re.compile(p)))
    except re.error as e: print('bad rule', p, e)
bad = 0
for f in args:
    text = open(f, encoding='utf-8').read()
    if f.endswith('.html'):
        text = re.sub(r'<(script|style)[\s\S]*?</\1>', '', text)
        text = re.sub(r'<[^>]+>', '\n', text)
    code = False
    for i, line in enumerate(text.splitlines(), 1):
        t = line.strip()
        if t.startswith('```'): code = not code; continue
        if code or not t: continue
        for p, c in pats:
            m = c.search(t)
            if m: bad += 1; print(f'{f}:{i}', 'RULE', p, '=>', m.group(0), '|', t[:70])
        if '—' in t: bad += 1; print(f'{f}:{i}', 'EMDASH |', t[:70])
print('errors', bad)
