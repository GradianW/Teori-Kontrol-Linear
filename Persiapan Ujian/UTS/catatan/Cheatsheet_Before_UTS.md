# 📑 Cheatsheet Lengkap Before UTS: Teori Kontrol Linear (MA4171)

**Mata Kuliah:** MA4171 Teori Kontrol Linear  
**Dosen Pengampu:** Dr. Dewi Handayani, S.Si., M.Si. (FMIPA ITB)  
**Cakupan Materi:** Pertemuan 1 s.d. 7 (Review Matematika, Diagram Blok, SFG / Aturan Mason, Ruang Keadaan, 4 Bentuk Kanonik, Keterkontrolan & Keterobservasian, Transformasi Z).

---

## 1. Transformasi Laplace & Solusi PDB Linear

### Definisi Dasar
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t) e^{-st} \, dt$$

### Sifat-Sifat Krusial untuk Ujian
- **Turunan Pertama**: $\mathcal{L}\{\dot{x}(t)\} = s X(s) - x(0)$
- **Turunan Kedua**: $\mathcal{L}\{\ddot{x}(t)\} = s^2 X(s) - s x(0) - \dot{x}(0)$
- **Turunan Ketiga**: $\mathcal{L}\{\dddot{x}(t)\} = s^3 X(s) - s^2 x(0) - s \dot{x}(0) - \ddot{x}(0)$
- **Turunan ke-$n$**: $\mathcal{L}\{x^{(n)}(t)\} = s^n X(s) - \sum_{k=1}^n s^{n-k} x^{(k-1)}(0)$
- **Integral**: $\mathcal{L}\left\{\int_0^t x(\tau) d\tau\right\} = \frac{1}{s} X(s)$
- **Pergeseran Waktu**: $\mathcal{L}\{f(t-a)u(t-a)\} = e^{-as} F(s)$
- **Pergeseran Frekuensi**: $\mathcal{L}\{e^{at} f(t)\} = F(s-a)$
- **Perkalian dengan $t$**: $\mathcal{L}\{t f(t)\} = -\frac{d}{ds} F(s)$

### Tabel Pasangan Transformasi Laplace Esensial
| Domain Waktu $f(t)$ | Domain Frekuensi $F(s)$ | Domain Waktu $f(t)$ | Domain Frekuensi $F(s)$ |
| :---: | :---: | :---: | :---: |
| $\delta(t)$ (Impuls) | $1$ | $u(t)$ (Step satuan) | $\frac{1}{s}$ |
| $t$ (Ramp) | $\frac{1}{s^2}$ | $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $e^{-at}$ | $\frac{1}{s+a}$ | $t e^{-at}$ | $\frac{1}{(s+a)^2}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2+\omega^2}$ | $\cos(\omega t)$ | $\frac{s}{s^2+\omega^2}$ |
| $e^{-at}\sin(\omega t)$ | $\frac{\omega}{(s+a)^2+\omega^2}$ | $e^{-at}\cos(\omega t)$ | $\frac{s+a}{(s+a)^2+\omega^2}$ |

### Prosedur Dekomposisi Pecahan Parsial
1. **Akar Berbeda (Kutub Sederhana)**:
   $$\frac{P(s)}{(s-p_1)(s-p_2)} = \frac{A}{s-p_1} + \frac{B}{s-p_2}, \quad A = \lim_{s \to p_1} (s-p_1) F(s)$$
2. **Akar Berulang (Kutub Ganda Orde $m$)**:
   $$\frac{P(s)}{(s-p)^m} = \sum_{k=1}^m \frac{A_k}{(s-p)^k}, \quad A_k = \frac{1}{(m-k)!} \lim_{s \to p} \frac{d^{m-k}}{ds^{m-k}} \left[ (s-p)^m F(s) \right]$$

---

## 2. Aljabar Diagram Blok & Fungsi Transfer

### Definisi Fungsi Transfer
$$G(s) = \frac{Y(s)}{U(s)} \quad \text{dengan seluruh kondisi awal nol } (x(0) = 0)$$

### Tiga Hubungan Blok Dasar
1. **Kaskade (Seri)**:
   $$G_{eq}(s) = G_1(s) G_2(s)$$
2. **Paralel**:
   $$G_{eq}(s) = G_1(s) \pm G_2(s)$$
3. **Umpan Balik (*Feedback Loop*)**:
   $$G_{eq}(s) = \frac{C(s)}{R(s)} = \frac{G(s)}{1 \pm G(s)H(s)}$$
   - Umpan balik **negatif** (tanda $-$ pada pembanding) $\implies$ penyebut bertanda **$+$**: $\frac{G}{1 + GH}$
   - Umpan balik **positif** (tanda $+$ pada pembanding) $\implies$ penyebut bertanda **$-$**: $\frac{G}{1 - GH}$

### Aturan Ekuivalensi Pemindahan
- Pindah titik cabang **melewati blok $G$ ke depan** (searah sinyal): kalikan cabang dengan $\frac{1}{G(s)}$.
- Pindah titik cabang **melewati blok $G$ ke belakang** (melawan sinyal): kalikan cabang dengan $G(s)$.
- Pindah titik penjumlahan **melewati blok $G$ ke depan**: kalikan masukan baru dengan $G(s)$.
- Pindah titik penjumlahan **melewati blok $G$ ke belakang**: kalikan masukan baru dengan $\frac{1}{G(s)}$.

---

## 3. Signal Flow Graph (SFG) & Aturan Penguatan Mason

### Rumus Penguatan Mason (*Mason's Gain Formula*)
$$P = \frac{Y_{out}}{U_{in}} = \frac{1}{\Delta} \sum_{k=1}^N P_k \Delta_k$$

### Komponen Rumus
1. **$P_k$**: Penguatan lintasan maju (*forward path gain*) ke-$k$ dari node input ke node output tanpa menyentuh satu simpul pun lebih dari satu kali.
2. **$\Delta$**: Determinan graf keseluruhan:
   $$\Delta = 1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \dots$$
   - $\sum L_i$: jumlah penguatan seluruh loop tunggal.
   - $\sum L_i L_j$: jumlah hasil kali penguatan pasangan dua loop yang **tidak saling bersentuhan** (*non-touching loops*).
   - $\sum L_i L_j L_k$: jumlah hasil kali penguatan tiga loop yang saling tidak bersentuhan.
3. **$\Delta_k$**: Kofaktor lintasan ke-$k$, diperoleh dari $\Delta$ dengan **menghapus semua loop yang bersentuhan dengan lintasan maju $P_k$** (jika $P_k$ menyentuh seluruh loop, maka $\Delta_k = 1$).

### Algoritma 5 Langkah Pengerjaan Soal Mason di Ujian
1. Tentukan seluruh lintasan maju $P_1, P_2, \dots$ beserta nilai penguatannya.
2. Identifikasi seluruh loop tunggal $L_1, L_2, \dots$ (pastikan tanda minus dari umpan balik negatif tercakup).
3. Cari apakah ada pasangan loop yang tidak bersentuhan (*non-touching*).
4. Hitung $\Delta$, kemudian hitung kofaktor $\Delta_k$ untuk masing-masing lintasan $P_k$.
5. Substitusikan ke rumus $P = \frac{\sum P_k \Delta_k}{\Delta}$.

---

## 4. Representasi Ruang Keadaan & Respon Waktu

### Bentuk Standar Sistem LTI Kontinu
$$\dot{x}(t) = A x(t) + B u(t) \quad \text{(Persamaan Keadaan)}$$
$$y(t) = C x(t) + D u(t) \quad \text{(Persamaan Keluaran)}$$
dengan dimensi: $x(t) \in \mathbb{R}^n$, $u(t) \in \mathbb{R}^m$, $y(t) \in \mathbb{R}^p$.

### Konversi Ruang Keadaan ke Fungsi Transfer
$$G(s) = C(sI - A)^{-1} B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$
Kutub-kutub (*poles*) sistem adalah akar dari persamaan karakteristik $\det(sI - A) = 0$.

### Matriks Fundamental / Transisi Keadaan $\Phi(t) = e^{At}$
$$e^{At} = \mathcal{L}^{-1}\left\{ (sI - A)^{-1} \right\}$$
Untuk matriks orde $2 \times 2$:
$$(sI - A)^{-1} = \frac{1}{\det(sI - A)} \begin{bmatrix} s - a_{22} & a_{12} \\ a_{21} & s - a_{11} \end{bmatrix}$$

### Solusi Respon Waktu Lengkap
$$x(t) = \underbrace{e^{At} x(0)}_{\text{Respon Masukan-Nol (ZIR)}} + \underbrace{\int_0^t e^{A(t-\tau)} B u(\tau) \, d\tau}_{\text{Respon Keadaan-Nol (ZSR)}}$$
Dalam domain frekuensi Laplace:
$$X(s) = (sI - A)^{-1} x(0) + (sI - A)^{-1} B U(s)$$
$$Y(s) = C(sI - A)^{-1} x(0) + \left[ C(sI - A)^{-1} B + D \right] U(s)$$

---

## 5. Empat Bentuk Kanonik Ruang Keadaan

Diberikan fungsi transfer SISO berorde $n$:
$$G(s) = \frac{b_0 s^n + b_1 s^{n-1} + \dots + b_{n-1}s + b_n}{s^n + a_1 s^{n-1} + \dots + a_{n-1}s + a_n}$$
Jika derajat pembilang lebih kecil dari penyebut ($b_0 = 0$), maka $D = 0$.

### 1. Bentuk Kanonik Keterkontrolan (CCF)
Variabel perantara: $Z(s) = \frac{U(s)}{s^n + a_1 s^{n-1} + \dots + a_n}$.  
Keadaan internal: $x_1 = z, x_2 = \dot{z}, \dots, x_n = z^{(n-1)}$.
$$A = \begin{bmatrix} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_n & -a_{n-1} & -a_{n-2} & \dots & -a_1 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$
$$C = \begin{bmatrix} b_n - a_n b_0 & b_{n-1} - a_{n-1} b_0 & \dots & b_1 - a_1 b_0 \end{bmatrix}, \quad D = b_0$$

### 2. Bentuk Kanonik Keterobservasian (OCF)
Bentuk dual dari CCF ($A_{ocf} = A_{ccf}^T, B_{ocf} = C_{ccf}^T, C_{ocf} = B_{ccf}^T$):
$$A = \begin{bmatrix} 0 & 0 & \dots & 0 & -a_n \\ 1 & 0 & \dots & 0 & -a_{n-1} \\ 0 & 1 & \dots & 0 & -a_{n-2} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & -a_1 \end{bmatrix}, \quad B = \begin{bmatrix} b_n - a_n b_0 \\ b_{n-1} - a_{n-1} b_0 \\ \vdots \\ b_1 - a_1 b_0 \end{bmatrix}$$
$$C = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix}, \quad D = b_0$$

### 3. Bentuk Kanonik Diagonal (DCF)
Syarat: Nilai eigen $\lambda_1, \dots, \lambda_n$ bernilai riil dan berbeda (distingtif).  
Ekspansi pecahan parsial: $G(s) = \sum_{i=1}^n \frac{c_i}{s - \lambda_i} + D$.
$$A = \begin{bmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix}$$

### 4. Bentuk Kanonik Jordan (JCF)
Bila terdapat nilai eigen berulang, misal $\lambda_1$ kelipatan 3:
$$J_1 = \begin{bmatrix} \lambda_1 & 1 & 0 \\ 0 & \lambda_1 & 1 \\ 0 & 0 & \lambda_1 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

---

## 6. Sistem Multivariabel (SIMO, MISO, MIMO)

- **SIMO (1 masukan, $p$ keluaran)**:
  $$G(s) = \frac{1}{d(s)} \begin{bmatrix} n_1(s) \\ \vdots \\ n_p(s) \end{bmatrix}$$
  Gunakan **CCF bersama**: matriks $A$ dan $B$ identik dengan sistem SISO, matriks $C \in \mathbb{R}^{p \times n}$ memuat koefisien pembilang masing-masing baris.
- **MISO ($m$ masukan, 1 keluaran)**:
  $$G(s) = \frac{1}{d(s)} \begin{bmatrix} n_1(s) & \dots & n_m(s) \end{bmatrix}$$
  Gunakan **OCF bersama**: matriks $A$ dan $C$ identik dengan sistem SISO, matriks $B \in \mathbb{R}^{n \times m}$ memuat koefisien pembilang masing-masing kolom.
- **MIMO ($m$ masukan, $p$ keluaran)**:
  Matriks transfer $\mathbf{G}(s) \in \mathbb{R}^{p \times m}$. Dibentuk melalui kombinasi blok kanonik atau bentuk Diagonal/Jordan via residu parsial.

---

## 7. Keterkontrolan & Keterobservasian Sistem (Topik 04)

### 1. Kriteria Keterkontrolan Kalman
$$M_c = \begin{bmatrix} B & AB & A^2B & \dots & A^{n-1}B \end{bmatrix} \in \mathbb{R}^{n \times n}$$
- Sistem terkontrol keadaan lengkap jika dan hanya jika $\operatorname{rank}(M_c) = n$ (atau $\det(M_c) \ne 0$).

### 2. Kriteria Keterobservasian Kalman
$$M_o = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix} \in \mathbb{R}^{n \times n}$$
- Sistem terobservasi keadaan lengkap jika dan hanya jika $\operatorname{rank}(M_o) = n$ (atau $\det(M_o) \ne 0$).

### 3. Transformasi ke Bentuk Kanonik Keterkontrolan ($T = M_c W$)
Jika polinomial karakteristik adalah $|sI - A| = s^n + a_1 s^{n-1} + \dots + a_n = 0$:
$$W = \begin{bmatrix} a_{n-1} & a_{n-2} & \dots & a_1 & 1 \\ a_{n-2} & a_{n-3} & \dots & 1 & 0 \\ \vdots & \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ 1 & 0 & \dots & 0 & 0 \end{bmatrix}$$
Matriks transformasi keserupaan $T = M_c W$ mentransformasikan keadaan $x = Tz$ sehingga:
$$A_{ccf} = T^{-1} A T, \quad B_{ccf} = T^{-1} B$$

### 4. Uji Gilbert (Bentuk Diagonal & Jordan)
- **Bentuk Diagonal** ($A = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$):
  - **Terkontrol**: Tidak ada baris pada matriks $\tilde{B} = P^{-1} B$ yang seluruh elemennya bernilai nol.
  - **Terobservasi**: Tidak ada kolom pada matriks $\tilde{C} = C P$ yang seluruh elemennya bernilai nol.
- **Bentuk Jordan** (Blok $J_i$ dengan nilai eigen berulang):
  - **Terkontrol**: Elemen pada **baris terakhir** setiap blok Jordan pada matriks $\tilde{B}$ bernilai bukan nol ($b_{terakhir} \ne 0$).
  - **Terobservasi**: Elemen pada **kolom pertama** setiap blok Jordan pada matriks $\tilde{C}$ bernilai bukan nol ($c_{pertama} \ne 0$).

### 5. Prinsip Dualitas Kalman
$$(A, B) \text{ terkontrol lengkap} \iff (A^T, B^T) \text{ terobservasi lengkap}$$
$$M_c(A, B) = M_o^T(A^T, B^T)$$

---

## 8. Transformasi Z & Sistem Waktu Diskrit

### Definisi Dasar
$$X(z) = \mathcal{Z}\{x(k)\} = \sum_{k=0}^\infty x(k) z^{-k}$$

### Tabel Transformasi Z Esensial
| Barisan Waktu $x(k)$ | Transformasi Z $X(z)$ | Barisan Waktu $x(k)$ | Transformasi Z $X(z)$ |
| :---: | :---: | :---: | :---: |
| $\delta(k)$ | $1$ | $1$ atau $u(k)$ (Step) | $\frac{z}{z-1}$ |
| $a^k$ | $\frac{z}{z-a}$ | $k$ (Ramp) | $\frac{z}{(z-1)^2}$ |
| $k a^k$ | $\frac{a z}{(z-a)^2}$ | $a^{k-1} u(k-1)$ | $\frac{1}{z-a}$ |

### Sifat Pergeseran Waktu Maju
$$\mathcal{Z}\{x(k+1)\} = z X(z) - z x(0)$$
$$\mathcal{Z}\{x(k+2)\} = z^2 X(z) - z^2 x(0) - z x(1)$$

### Trik Inversi Pecahan Parsial Domain Z
Selalu faktorkan dalam bentuk pecahan $\frac{X(z)}{z}$:
$$\frac{X(z)}{z} = \frac{A}{z - p_1} + \frac{B}{z - p_2} \implies X(z) = \frac{A z}{z - p_1} + \frac{B z}{z - p_2} \implies x(k) = A p_1^k + B p_2^k$$

### Ruang Keadaan Diskrit
$$x(k+1) = G x(k) + H u(k), \quad y(k) = C x(k) + D u(k)$$
Fungsi transfer diskrit: $G(z) = C(zI - G)^{-1} H + D$.

---

## 💡 Checklist & Tips Ujian UTS MA4171

- [ ] **Kondisi Awal Nol**: Pada saat mencari fungsi transfer dari diagram blok/SFG atau ruang keadaan, sebutkan selalu asumsi kondisi awal nol ($x(0) = 0$).
- [ ] **Tanda Umpan Balik**: Jangan terbalik! Umpan balik negatif memiliki tanda **$+$** di penyebut: $\frac{G}{1 + GH}$.
- [ ] **Non-Touching Loop Mason**: Teliti simpul (*nodes*) setiap loop. Pasangan loop hanya dikatakan *non-touching* jika **tidak berbagi simpul sama sekali**.
- [ ] **Matriks $e^{At}$**: Saat menghitung invers Laplace dari $(sI - A)^{-1}$, lakukan inversi untuk setiap elemen matriks secara terpisah.
- [ ] **Pemeriksaan Rank Matriks**:
  - Jika $\det(M_c) \ne 0$, rank langsung $n$ (penuh).
  - Jika $\det(M_c) = 0$, rank $< n$. Periksa minor $2 \times 2$ tak-nol untuk membuktikan rank $= 2$.
