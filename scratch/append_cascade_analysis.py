import json

notebook_path = 'coret.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

md_cell = {
    'cell_type': 'markdown',
    'metadata': {},
    'source': [
        '---\n',
        '# Analisis Soal No. 4: Apakah Bisa Dikerjakan dengan Menjabarkan $G(s)$ Lalu Mengaplikasikan Bentuk Kanonik?\n',
        '\n',
        '### 1. Kesimpulan Singkat\n',
        '- **Secara Fisik & Matematis:** **Bisa**, sistem yang dihasilkan merepresentasikan dinamika masukan-keluaran yang identik.\n',
        '- **Secara Ketepatan Ujian/Akademik:** **TIDAK BISA / SALAH**, jika soal secara eksplisit meminta **Bentuk Kanonik Kaskade (*Cascade/Series Form*)**.\n',
        '\n',
        '---\n',
        '\n',
        '### 2. Mengapa Menjabarkan $G(s)$ Menghasilkan Bentuk yang Berbeda?\n',
        'Diberikan:\n',
        '$$G(s) = \\frac{8}{(s+1)(s+2)(s+4)}$$\n',
        '\n',
        'Jika penyebutnya dijabarkan:\n',
        '$$(s+1)(s+2)(s+4) = s^3 + 7s^2 + 14s + 8 \\implies G(s) = \\frac{8}{s^3 + 7s^2 + 14s + 8}$$\n',
        'Lalu diaplikasikan metode kanonik standar (variabel perantara $Z(s)$), Anda akan memperoleh **Bentuk Kanonik Keterkontrolan (CCF)**:\n',
        '$$A_{ccf} = \\begin{bmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ -8 & -14 & -7 \\end{bmatrix}, \\quad B_{ccf} = \\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\end{bmatrix}, \\quad C_{ccf} = \\begin{bmatrix} 8 & 0 & 0 \\end{bmatrix}$$\n',
        '\n',
        'Matriks $A_{ccf}$ ini adalah **Matriks Pendamping Frobenius (*Companion Matrix*)**, BUKAN Bentuk Kaskade!\n',
        '\n',
        '---\n',
        '\n',
        '### 3. Perbandingan Mendalam: Bentuk Kaskade vs CCF\n',
        '\n',
        '| Aspek | Bentuk Kanonik Kaskade (*Cascade Form*) | Bentuk Kanonik Keterkontrolan (*CCF*) |\n',
        '| :--- | :--- | :--- |\n',
        '| **Operasi Matematika** | **Faktorisasi perkalian**: $G_1(s) \\cdot G_2(s) \\cdot G_3(s)$ | **Penjabaran polinomial**: $s^3 + a_1 s^2 + a_2 s + a_3$ |\n',
        '| **Struktur Matriks $A$** | **Matriks Segitiga (*Triangular Matrix*)**: <br> $A = \\begin{bmatrix} -1 & 8 & 0 \\\\ 0 & -2 & 1 \\\\ 0 & 0 & -4 \\end{bmatrix}$ | **Matriks Pendamping (*Companion Matrix*)**: <br> $A = \\begin{bmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ -8 & -14 & -7 \\end{bmatrix}$ |\n',
        '| **Diagonal Utama Matriks $A$** | Langsung memuat **kutub-kutub sistem** ($\\lambda_1 = -1, \\lambda_2 = -2, \\lambda_3 = -4$) | Berisi angka $0$ dan koefisien $-a_1$ di sudut kanan bawah |\n',
        '| **Arti Variabel Keadaan $x_i$** | Sinyal fisik terukur di antara modul blok yang tersambung seri | Rantai turunan fiktif dari variabel perantara $z(t)$ ($x_1=z, x_2=\\dot{z}, x_3=\\ddot{z}$) |\n',
        '| **Tujuan Praktis** | Tahan terhadap galat pembulatan koefisien pada sistem orde tinggi (filter analog/DSP bertingkat) | Memudahkan perancangan *state feedback pole placement* karena vektor $B = [0 \\; 0 \\; 1]^T$ |\n',
        '\n',
        '---\n',
        '\n',
        '### 4. Hubungan Keduanya (Transformasi Similaritas)\n',
        'Kedua representasi tersebut saling terhubung melalui matriks transformasi koordinat nonsingular $P$:\n',
        '$$\\mathbf{x}_{cas} = P \\mathbf{x}_{ccf} \\implies A_{cas} = P A_{ccf} P^{-1}, \\quad B_{cas} = P B_{ccf}, \\quad C_{cas} = C_{ccf} P^{-1}$$\n',
        'Sehingga kedua sistem menghasilkan fungsi transfer yang identik:\n',
        '$$C_{cas}(sI - A_{cas})^{-1} B_{cas} \\equiv C_{ccf}(sI - A_{ccf})^{-1} B_{ccf} \\equiv G(s)$$'
    ]
}

code_cell = {
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': [
        '# =========================================================================\n',
        '# Verifikasi Simbolik: Perbandingan Bentuk Kaskade vs CCF (Soal No. 4)\n',
        '# =========================================================================\n',
        'import sympy as sp\n',
        'try:\n',
        '    from IPython.display import display\n',
        'except ImportError:\n',
        '    display = print\n',
        '\n',
        's = sp.Symbol("s")\n',
        '\n',
        '# 1. Representasi Bentuk Kanonik Kaskade (Cascade Form)\n',
        'A_cas = sp.Matrix([\n',
        '    [-1,  8,  0],\n',
        '    [ 0, -2,  1],\n',
        '    [ 0,  0, -4]\n',
        '])\n',
        'B_cas = sp.Matrix([[0], [0], [1]])\n',
        'C_cas = sp.Matrix([[1, 0, 0]])\n',
        'D_cas = sp.Matrix([[0]])\n',
        '\n',
        'print("=== 1. Bentuk Kanonik Kaskade (Matriks A Berstruktur Segitiga) ===")\n',
        'print("Matriks A_cascade:")\n',
        'display(A_cas)\n',
        'print("Nilai eigen langsung terlihat pada diagonal:", A_cas.eigenvals())\n',
        '\n',
        '# 2. Representasi Bentuk Kanonik Keterkontrolan (CCF dari penjabaran polinomial)\n',
        '# Penyebut: (s+1)(s+2)(s+4) = s^3 + 7s^2 + 14s + 8\n',
        'A_ccf = sp.Matrix([\n',
        '    [ 0,   1,   0],\n',
        '    [ 0,   0,   1],\n',
        '    [-8, -14,  -7]\n',
        '])\n',
        'B_ccf = sp.Matrix([[0], [0], [1]])\n',
        'C_ccf = sp.Matrix([[8, 0, 0]])\n',
        'D_ccf = sp.Matrix([[0]])\n',
        '\n',
        'print("\\n=== 2. Bentuk Kanonik Keterkontrolan (CCF - Matriks Pendamping Frobenius) ===")\n',
        'print("Matriks A_ccf:")\n',
        'display(A_ccf)\n',
        '\n',
        '# 3. Bukti Bahwa Kedua Representasi Menghasilkan Fungsi Transfer yang Identik\n',
        'I3 = sp.eye(3)\n',
        'G_from_cas = sp.simplify(C_cas * (s * I3 - A_cas).inv() * B_cas + D_cas)[0, 0]\n',
        'G_from_ccf = sp.simplify(C_ccf * (s * I3 - A_ccf).inv() * B_ccf + D_ccf)[0, 0]\n',
        'G_original = 8 / ((s + 1) * (s + 2) * (s + 4))\n',
        '\n',
        'print("\\n=== 3. Rekonstruksi Fungsi Transfer ===")\n',
        'print("G(s) dari Bentuk Kaskade:")\n',
        'display(G_from_cas)\n',
        'print("G(s) dari Bentuk CCF:")\n',
        'display(G_from_ccf)\n',
        '\n',
        'assert sp.simplify(G_from_cas - sp.simplify(G_original)) == 0\n',
        'assert sp.simplify(G_from_ccf - sp.simplify(G_original)) == 0\n',
        'print("=> KESIMPULAN:")\n',
        'print("   1. Kedua representasi secara matematis menghasilkan transfer function yang PERSIS SAMA.")\n',
        'print("   2. Tetapi strukturnya BERBEDA: A_cascade berbentuk segitiga (triangular), sedangkan A_ccf adalah matriks pendamping (companion).")\n',
        'print("   3. Jika instruksi soal meminta \'Cascade Form\', wajib menggunakan matriks segitiga hasil pemfaktoran!")\n'
    ]
}

nb['cells'].append(md_cell)
nb['cells'].append(code_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Berhasil menambahkan analisis soal 4 ke coret.ipynb')
