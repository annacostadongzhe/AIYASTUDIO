import re
f1 = r'C:\Users\PC\Documents\AIYA 项目\aiya-紫荆文化合作提案-精简版.html'
h1 = open(f1, encoding='utf-8').read()
h1 = h1.replace('\u25cb\u5267\u672c Benchmark / Script benchmark', '\u2713\u5267\u672c Benchmark \u2014 AIYA Studio \u5b98\u7f51\u53ef\u67e5\u770b')
h1 = h1.replace('\u25cb\u6f14\u793a\u6837\u7247 / Demo reel', '\u2713\u6f14\u793a\u6837\u7247 \u2014 AIYA Studio \u5b98\u7f51\u53ef\u67e5\u770b')
open(f1, 'w', encoding='utf-8').write(h1)
print('Simplified: OK')
f2 = r'C:\Users\PC\Documents\AIYA 项目\aiya-紫荆文化合作提案-v2.html'
h2 = open(f2, encoding='utf-8').read()
h2 = h2.replace('>\u5f85\u8865\u5145</div></div><div class="model-card" style="background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12)"><div class="type" style="color:var(--white)">\u6f14\u793a\u6837\u7247', '>\u5df2\u5b8c\u6210 \u2713</div></div><div class="model-card" style="background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12)"><div class="type" style="color:var(--white)">\u6f14\u793a\u6837\u7247')
h2 = h2.replace('>\u5f85\u8865\u5145</div></div><div class="model-card" style="background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12)"><div class="type" style="color:var(--white)">\u5267\u672c Benchmark', '>\u5df2\u5b8c\u6210 \u2713</div></div><div class="model-card" style="background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12)"><div class="type" style="color:var(--white)">\u5267\u672c Benchmark')
open(f2, 'w', encoding='utf-8').write(h2)
print('Full version: OK')
