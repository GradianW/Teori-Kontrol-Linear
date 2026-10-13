import json

notebook_path = 'coret.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

md_cell = {
    'cell_type': 'markdown',
    'metadata': {},
    'source': [
        '---\n',
        '# Visualisasi & Pembuktian Aljabar Reduksi Diagram Blok (Soal 9)\n',
        '\n',
        '### Mengapa Lup Dalam Mereduksi Menjadi $G_{in}(s) = \\frac{G_1(s)}{1 + G_1(s)H_1(s)}$?\n',
        '\n',
        'Diagram blok pada Soal 9 terdiri dari dua lup umpan balik bersarang (*nested feedback loops*):\n',
        '1. **Sinyal-Sinyal Sistem:**\n',
        '   - $R(s)$: Sinyal masukan referensi.\n',
        '   - $E_1(s) = R(s) - H_2(s)Y(s)$: Sinyal keluaran simpul penjumlahan pertama (lup luar).\n',
        '   - $E_2(s)$: Sinyal masukan untuk subsistem lup dalam.\n',
        '   - $V(s)$: Sinyal perantara antara blok $G_1(s)$ dan $G_2(s)$.\n',
        '   - $Y(s) = G_2(s)V(s)$: Sinyal keluaran akhir sistem.\n',
        '\n',
        '2. **Dekomposisi Tahap 1: Isolasi Lup Bagian Dalam**\n',
        '   $$\\text{Masukan: } E_2(s) \\longrightarrow \\bigoplus_2 \\xrightarrow{E_2 - H_1 V} [G_1(s)] \\longrightarrow V(s)$$\n',
        '   $$\\text{Umpan Balik: } V(s) \\longrightarrow [H_1(s)] \\longrightarrow (-)\\bigoplus_2$$\n',
        '   \n',
        '   Persamaan aljabar sinyalnya:\n',
        '   $$V(s) = G_1(s)[E_2(s) - H_1(s)V(s)]$$\n',
        '   $$V(s) + G_1(s)H_1(s)V(s) = G_1(s)E_2(s)$$\n',
        '   $$V(s)[1 + G_1(s)H_1(s)] = G_1(s)E_2(s)$$\n',
        '   $$\\frac{V(s)}{E_2(s)} = G_{in}(s) = \\frac{G_1(s)}{1 + G_1(s)H_1(s)}$$\n',
        '\n',
        '3. **Dekomposisi Tahap 2 & 3: Hubungan Seri (Kaskade) dengan $G_2(s)$**\n',
        '   Karena keluaran $V(s)$ dari blok $G_{in}(s)$ langsung masuk ke blok $G_2(s)$ tanpa percabangan lain:\n',
        '   $$G_{fwd}(s) = G_{in}(s) \\cdot G_2(s) = \\frac{G_1(s)G_2(s)}{1 + G_1(s)H_1(s)}$$\n',
        '\n',
        '4. **Dekomposisi Tahap 4: Reduksi Lup Luar**\n',
        '   $$T(s) = \\frac{Y(s)}{R(s)} = \\frac{G_{fwd}(s)}{1 + G_{fwd}(s)H_2(s)} = \\frac{\\frac{G_1 G_2}{1 + G_1 H_1}}{1 + \\frac{G_1 G_2}{1 + G_1 H_1} H_2} = \\frac{G_1(s)G_2(s)}{1 + G_1(s)H_1(s) + G_1(s)G_2(s)H_2(s)}$$'
    ]
}

code_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [
        '# Verifikasi Simbolik Reduksi Diagram Blok (Soal 9)\n',
        'import sympy as sp\n',
        '\n',
        '# Definisikan simbol-simbol fungsi transfer dan sinyal\n',
        's = sp.Symbol("s")\n',
        'G1, G2, H1, H2 = sp.symbols("G_1 G_2 H_1 H_2")\n',
        'R, Y, V, E2 = sp.symbols("R Y V E_2")\n',
        '\n',
        '# Metode 1: Reduksi Langkah Demi Langkah Aljabar Diagram Blok\n',
        '# Tahap 1: Fungsi transfer ekuivalen lup dalam (inner loop)\n',
        'G_in = G1 / (1 + G1 * H1)\n',
        'print("G_in(s) =")\n',
        'display(G_in)\n',
        '\n',
        '# Tahap 2: Hubungan seri / kaskade dengan G2\n',
        'G_fwd = sp.simplify(G_in * G2)\n',
        'print("G_fwd(s) =")\n',
        'display(G_fwd)\n',
        '\n',
        '# Tahap 3: Fungsi transfer lup tertutup total (outer loop)\n',
        'T_step = sp.simplify(G_fwd / (1 + G_fwd * H2))\n',
        'print("T(s) dari reduksi bertahap =")\n',
        'display(T_step)\n',
        '\n',
        '# Metode 2: Solusi Simultan Persamaan Sinyal Sistem Utuh\n',
        '# Persamaan 1: Titik penjumlahan pertama E2 = R - H2 * Y\n',
        '# Persamaan 2: Titik penjumlahan kedua & blok G1: V = G1 * (E2 - H1 * V)\n',
        '# Persamaan 3: Blok G2: Y = G2 * V\n',
        'eq1 = sp.Eq(E2, R - H2 * Y)\n',
        'eq2 = sp.Eq(V, G1 * (E2 - H1 * V))\n',
        'eq3 = sp.Eq(Y, G2 * V)\n',
        '\n',
        'sol = sp.solve((eq1, eq2, eq3), (Y, V, E2))\n',
        'Y_sol = sol[Y]\n',
        'T_simultan = sp.simplify(Y_sol / R)\n',
        'print("T(s) dari solusi simultan sistem =")\n',
        'display(T_simultan)\n',
        '\n',
        '# Verifikasi kesetaraan kedua metode\n',
        'assert sp.simplify(T_step - T_simultan) == 0\n',
        'print("\\n=> PEMBUKTIAN VALID: Kedua metode terbukti menghasilkan fungsi transfer yang identik!")\n'
    ]
}

nb['cells'].append(md_cell)
nb['cells'].append(code_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Berhasil menambahkan cells ke coret.ipynb')
