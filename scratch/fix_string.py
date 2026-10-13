import json

notebook_path = 'coret.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update the last cell's source line
last_cell = nb['cells'][-1]
last_cell['source'] = [
    line.replace(
        'print("=> Karena det(Cal_C) = 1 (konstan bukan nol untuk SEMUA parameter a_i), sistem PASTI terkontrol penuh!")',
        'print(f"=> Karena |det(Cal_C)| = {abs(det_C)} != 0 (selalu konstan bukan nol untuk parameter a_i apapun), sistem PASTI terkontrol penuh!")'
    ) for line in last_cell['source']
]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Selesai update string.')
