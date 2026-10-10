# Catatan Kuliah MA4171 Teori Kontrol Linear
## Topik 02: Model Matematika pada Sistem Dinamik (Minggu 2 – 4)
**Referensi Utama**: Katsuhiko Ogata, *Modern Control Engineering*, Bab 2 & Bab 9.2; Slide Kuliah MA4171 ITB

---

## 📑 Daftar Isi
1. [Pendahuluan & Karakteristik Sistem LTI](#1-pendahuluan--karakteristik-sistem-lti)
2. [Fungsi Transfer (Transfer Function)](#2-fungsi-transfer-transfer-function)
3. [Aljabar & Reduksi Diagram Blok](#3-aljabar--reduksi-diagram-blok)
4. [Signal-Flow Graph (SFG) & Aturan Penguatan Mason](#4-signal-flow-graph-sfg--aturan-penguatan-mason)
5. [Representasi Ruang Keadaan (State-Space Representation)](#5-representasi-ruang-keadaan-state-space-representation)
6. [Hubungan Ruang Keadaan dan Fungsi Transfer](#6-hubungan-ruang-keadaan-dan-fungsi-transfer)
7. [Bentuk-Bentuk Kanonik Ruang Keadaan](#7-bentuk-bentuk-kanonik-ruang-keadaan)
8. [Representasi SFG untuk Persamaan Ruang Keadaan](#8-representasi-sfg-untuk-persamaan-ruang-keadaan)
9. [Pemodelan Sistem Multivariabel (SIMO, MISO, MIMO)](#9-pemodelan-sistem-multivariabel-simo-miso-mimo)
10. [Transformasi Keserupaan (Similarity Transformation)](#10-transformasi-keserupaan-similarity-transformation)
11. [Solusi Domain Waktu & Matriks Transisi Keadaan](#11-solusi-domain-waktu--matriks-transisi-keadaan)
12. [Contoh Soal & Pembahasan Komprehensif](#12-contoh-soal--pembahasan-komprehensif)

---

## 1. Pendahuluan & Karakteristik Sistem LTI

Pemodelan matematika merupakan langkah fundamental untuk menganalisis karakteristik alami sistem fisik dan merancang pengontrol yang stabil, cepat, dan tangguh (*robust*).

### Sistem Linear Time-Invariant (LTI)
Kajian berfokus pada sistem kontinu LTI:
- **Linearitas**: Memenuhi prinsip **superposisi** dan **homogenitas**. Jika input $u_1(t) \to y_1(t)$ dan $u_2(t) \to y_2(t)$, maka untuk sembarang skalar $\alpha, \beta \in \mathbb{R}$:
  $$\alpha u_1(t) + \beta u_2(t) \implies \alpha y_1(t) + \beta y_2(t)$$
- **Time-Invariance (Invarian Waktu)**: Parameter sistem konstan terhadap waktu, sehingga pergeseran waktu pada masukan menghasilkan pergeseran waktu yang sama pada keluaran:
  $$u(t - \tau) \implies y(t - \tau), \quad \forall \tau \ge 0$$

### Dua Pendekatan Utama Representasi Sistem
| Karakteristik | Domain Frekuensi (*S-Domain* / Kontrol Klasik) | Domain Waktu (*State-Space* / Kontrol Modern) |
| :--- | :--- | :--- |
| **Model Utama** | Fungsi Transfer $G(s)$, Diagram Blok, Signal Flow Graph | Persamaan Diferensial Vektor Orde 1 ($\dot{x} = Ax + Bu$) |
| **Tipe Sistem** | Sangat ideal untuk SISO (*Single-Input Single-Output*) | Fleksibel untuk SISO, SIMO, MISO, hingga MIMO |
| **Kondisi Awal** | Diasumsikan bernilai nol ($x(0) = 0$) | Mengakomodasi kondisi awal riil ($x(0) \ne 0$) |
| **Dinamika Internal**| *Black-Box* (hanya relasi masukan-keluaran) | *White-Box* (mencakup seluruh variabel internal) |

---

## 2. Fungsi Transfer (Transfer Function)

> **Definisi**: Perbandingan antara Transformasi Laplace dari sinyal keluaran $Y(s)$ terhadap Transformasi Laplace dari sinyal masukan $U(s)$ dengan **semua syarat awal nol**:
> $$G(s) = \frac{Y(s)}{U(s)} = \frac{\mathcal{L}\{y(t)\}}{\mathcal{L}\{u(t)\}}\Bigg|_{\text{syarat awal } = 0}$$

Jika sistem dinyatakan dalam persamaan diferensial linear berorde $n$:
$$a_0 \frac{d^n y}{dt^n} + a_1 \frac{d^{n-1} y}{dt^{n-1}} + \dots + a_n y(t) = b_0 \frac{d^m u}{dt^m} + b_1 \frac{d^{m-1} u}{dt^{m-1}} + \dots + b_m u(t) \quad (n \ge m)$$

Dengan menerapkan Transformasi Laplace dan syarat awal nol:
$$G(s) = \frac{b_0 s^m + b_1 s^{m-1} + \dots + b_m}{a_0 s^n + a_1 s^{n-1} + \dots + a_n} = \frac{N(s)}{D(s)}$$

### Elemen Penting:
- **Persamaan Karakteristik**: $D(s) = a_0 s^n + a_1 s^{n-1} + \dots + a_n = 0$.
- **Kutub (*Poles*)**: Akar-akar dari penyebut $D(s) = 0$. Menentukan kestabilan dan respon transient sistem.
- **Pembuat Nol (*Zeros*)**: Akar-akar dari pembilang $N(s) = 0$.
- **Tanggapan Impuls (*Impulse Response*)**: Respon terhadap input impuls Dirac $\delta(t)$ di mana $U(s) = 1$, sehingga $y(t) = g(t) = \mathcal{L}^{-1}\{G(s)\}$.

---

## 3. Aljabar & Reduksi Diagram Blok

Diagram blok memvisualisasikan aliran sinyal dan pemrosesan fungsional antar subsistem.

### Aturan Ekuivalensi Reduksi
| Konfigurasi | Deskripsi | Fungsi Transfer Ekuivalen |
| :--- | :--- | :--- |
| **Kaskade (Seri)** | Blok tersusun berurutan | $G_{eq}(s) = G_1(s) G_2(s)$ |
| **Paralel** | Input yang sama dijumlahkan | $G_{eq}(s) = G_1(s) \pm G_2(s)$ |
| **Loop Umpan Balik Negatif** | Maju $G(s)$, Umpan Balik $H(s)$ (-) | $T(s) = \dfrac{Y(s)}{R(s)} = \dfrac{G(s)}{1 + G(s)H(s)}$ |
| **Loop Umpan Balik Positif** | Maju $G(s)$, Umpan Balik $H(s)$ (+) | $T(s) = \dfrac{Y(s)}{R(s)} = \dfrac{G(s)}{1 - G(s)H(s)}$ |
| **Pindah Titik Cabang Melewati Blok ke Kanan** | Ambil cabang sebelum $G(s)$ | Tambahkan blok $\dfrac{1}{G(s)}$ pada cabang |
| **Pindah Titik Jumlah Melewati Blok ke Kanan** | Titik jumlah sebelum $G(s)$ | Kalikan masukan cabang dengan $G(s)$ |

Untuk sistem dengan gangguan (*disturbance*) $D(s)$ dan masukan acuan $R(s)$, keluaran dihitung menggunakan prinsip superposisi:
$$C(s) = T_R(s) R(s) + T_D(s) D(s)$$

---

## 4. Signal-Flow Graph (SFG) & Aturan Penguatan Mason

**Signal-Flow Graph (SFG)** adalah diagram graf berarah yang terdiri atas simpul (*nodes*) yang dihubungkan oleh cabang berarah (*branches*).

### Terminologi Graf Aliran Sinyal
- **Simpul Masukan (*Source Node*)**: Simpul yang hanya memiliki cabang keluar (misal: $R(s)$ atau $U(s)$).
- **Simpul Keluaran (*Sink Node*)**: Simpul yang hanya memiliki cabang masuk (misal: $C(s)$ atau $Y(s)$).
- **Simpul Campuran (*Mixed Node*)**: Simpul yang memiliki cabang masuk dan keluar.
- **Transmitansi (*Branch Gain*)**: Faktor pengali sinyal sepanjang cabang.
- **Jalur Maju (*Forward Path*, $F_k$ atau $P_k$)**: Lintasan dari simpul input ke simpul output yang searah dengan panah tanpa melintasi simpul yang sama lebih dari sekali. Penguatan jalur maju adalah perkalian seluruh gain cabang pada jalur tersebut.
- **Lup (*Loop*, $L_i$)**: Lintasan tertutup yang dimulai dan berakhir pada simpul yang sama serta tidak melewati simpul lain lebih dari satu kali. Penguatan lup adalah perkalian gain cabang pada lintasan tersebut.
- **Lup Tak Bersentuhan (*Non-touching Loops*)**: Lup-lup yang tidak memiliki simpul bersama (*tidak menyentuh satu sama lain*).

### Rumus Penguatan Mason (*Mason's Gain Formula*)
Fungsi transfer keseluruhan dari input $R(s)$ ke output $C(s)$ dihitung melalui:

$$G(s) = \frac{C(s)}{R(s)} = \frac{\sum_{k=1}^N F_k \Delta_k}{\Delta}$$

Di mana:
- $N$ = Jumlah total jalur maju (*forward paths*).
- $F_k$ = Penguatan (*gain*) dari jalur maju ke-$k$.
- $\Delta$ = **Determinan graf sistem**:
  $$\Delta = 1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \dots$$
  - $\sum L_i$ = Jumlah penguatan dari seluruh individual loop.
  - $\sum L_i L_j$ = Jumlah hasil kali penguatan dari semua pasangan 2 loop yang tidak bersentuhan (*non-touching*).
  - $\sum L_i L_j L_k$ = Jumlah hasil kali penguatan dari semua kombinasi 3 loop yang tidak bersentuhan.
- $\Delta_k$ = **Kofaktor dari jalur maju ke-$k$**:
  Nilai $\Delta$ yang dievaluasi untuk bagian graf yang **tidak menyentuh** jalur maju ke-$k$:
  $$\Delta_k = 1 - \sum L_{i, \text{non-touching to path } k} + \sum L_{i} L_{j, \text{non-touching to path } k} - \dots$$
  *(Jika jalur maju ke-$k$ menyentuh semua lup yang ada pada sistem, maka $\Delta_k = 1$)*.

---

## 5. Representasi Ruang Keadaan (State-Space Representation)

Representasi ruang keadaan mendeskripsikan sistem orde-$n$ sebagai sistem $n$ persamaan diferensial linear orde satu yang simultan.

### Bentuk Standar Sistem LTI Kontinu
$$\begin{aligned}
\dot{x}(t) &= A x(t) + B u(t) \quad &&\text{\textbf{(Persamaan Keadaan / State Equation)}} \\
y(t) &= C x(t) + D u(t) \quad &&\text{\textbf{(Persamaan Keluaran / Output Equation)}}
\end{aligned}$$

Di mana:
- $x(t) \in \mathbb{R}^n$: Vektor keadaan (*state vector*)
- $u(t) \in \mathbb{R}^m$: Vektor masukan (*input vector*)
- $y(t) \in \mathbb{R}^p$: Vektor keluaran (*output vector*)
- $A \in \mathbb{R}^{n \times n}$: Matriks sistem (*system matrix*)
- $B \in \mathbb{R}^{n \times m}$: Matriks masukan (*input matrix*)
- $C \in \mathbb{R}^{p \times n}$: Matriks keluaran (*output matrix*)
- $D \in \mathbb{R}^{p \times m}$: Matriks transmisi langsung (*feedforward matrix*)

---

## 6. Hubungan Ruang Keadaan dan Fungsi Transfer

Dengan menerapkan Transformasi Laplace pada persamaan keadaan dengan syarat awal $x(0) = 0$:
$$sX(s) = A X(s) + B U(s) \implies (sI - A) X(s) = B U(s) \implies X(s) = (sI - A)^{-1} B U(s)$$

Substitusi ke persamaan keluaran $Y(s) = C X(s) + D U(s)$:
$$G(s) = \frac{Y(s)}{U(s)} = C (sI - A)^{-1} B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$

> **Catatan Penting**:
> - Polinomial karakteristik sistem adalah $\det(sI - A) = 0$.
> - Nilai eigen dari matriks $A$ ($\lambda_i$) berkorespondensi langsung dengan kutub-kutub (*poles*) fungsi transfer sistem.

---

## 7. Bentuk-Bentuk Kanonik Ruang Keadaan

Diberikan fungsi transfer SISO *strictly proper*:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{b_1 s^{n-1} + b_2 s^{n-2} + \dots + b_n}{s^n + a_1 s^{n-1} + a_2 s^{n-2} + \dots + a_n}$$

### 1. Bentuk Kanonik Keterkontrolan (*Controllable Canonical Form*)
Bentuk ini mengalokasikan masukan kontrol langsung pada integrator keadaan terakhir (atau pertama):
- **Konvensi Standar (Bottom Companion)**:
  $$A = \begin{bmatrix}
  0 & 1 & 0 & \dots & 0 \\
  0 & 0 & 1 & \dots & 0 \\
  \vdots & \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & 0 & \dots & 1 \\
  -a_n & -a_{n-1} & -a_{n-2} & \dots & -a_1
  \end{bmatrix}, \quad
  B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$
  $$C = \begin{bmatrix} b_n & b_{n-1} & \dots & b_1 \end{bmatrix}, \quad D = [0]$$

- **Konvensi Top Companion (Sering digunakan pada slide kuliah)**:
  $$A = \begin{bmatrix}
  -a_1 & -a_2 & \dots & -a_{n-1} & -a_n \\
  1 & 0 & \dots & 0 & 0 \\
  0 & 1 & \dots & 0 & 0 \\
  \vdots & \vdots & \ddots & \vdots & \vdots \\
  0 & 0 & \dots & 1 & 0
  \end{bmatrix}, \quad
  B = \begin{bmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad
  C = \begin{bmatrix} b_1 & b_2 & \dots & b_n \end{bmatrix}$$

### 2. Bentuk Kanonik Keterobservasian (*Observable Canonical Form*)
Bentuk dual dari bentuk keterkontrolan, di mana keluaran hanya membaca keadaan pertama:
$$A = \begin{bmatrix}
-a_1 & 1 & 0 & \dots & 0 \\
-a_2 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
-a_{n-1} & 0 & 0 & \dots & 1 \\
-a_n & 0 & 0 & \dots & 0
\end{bmatrix} \quad \text{atau} \quad
A = \begin{bmatrix}
0 & 0 & \dots & 0 & -a_n \\
1 & 0 & \dots & 0 & -a_{n-1} \\
0 & 1 & \dots & 0 & -a_{n-2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & -a_1
\end{bmatrix}$$
$$B = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix} \quad \text{atau} \quad B = \begin{bmatrix} b_n \\ b_{n-1} \\ \vdots \\ b_1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & \dots & 0 \end{bmatrix} \text{ atau } \begin{bmatrix} 0 & \dots & 0 & 1 \end{bmatrix}$$

### 3. Bentuk Kanonik Diagonal / Jordan
Jika akar penyebut memiliki $n$ nilai unik $p_1, p_2, \dots, p_n$:
$$G(s) = \sum_{i=1}^n \frac{c_i}{s - p_i} \implies A = \operatorname{diag}(p_1, p_2, \dots, p_n), \quad B = \begin{bmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix}$$

Untuk pole berulang dengan kelipatan 3 pada $s = \lambda$:
$$A = \begin{bmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{bmatrix}, \quad B = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}, \quad C = \begin{bmatrix} c_1 & c_2 & c_3 \end{bmatrix}$$

---

## 8. Representasi SFG untuk Persamaan Ruang Keadaan

Hubungan antara bentuk kanonik ruang keadaan dan graf aliran sinyal diwujudkan melalui blok-blok integrator $\frac{1}{s}$:

### 1. SFG Bentuk Kanonik Keterkontrolan
- Rangkaian kaskade integrator $\frac{1}{s}$ disusun dari kiri ke kanan.
- Lup umpan balik internal $-a_1, -a_2, \dots, -a_n$ ditarik dari setiap simpul keadaan kembali ke simpul masukan sebelum integrator pertama.
- Jalur umpan maju $b_1, b_2, \dots, b_n$ menghubungkan setiap simpul keadaan menuju simpul keluaran $Y(s)$.

### 2. SFG Bentuk Kanonik Keterobservasian
- Masukan $U(s)$ didistribusikan ke input setiap integrator dengan bobot $b_1, b_2, \dots, b_n$.
- Sinyal keluaran $Y(s) = X_1(s)$ diumpanbalikkan kembali ke simpul masukan tiap integrator dengan bobot $-a_1, -a_2, \dots, -a_n$.

---

## 9. Pemodelan Sistem Multivariabel (SIMO, MISO, MIMO)

### 1. Sistem SIMO (*Single-Input Multiple-Output*)
Fungsi transfer dinyatakan sebagai vektor kolom:
$$\mathbf{G}(s) = \begin{bmatrix} g_1(s) \\ g_2(s) \\ \vdots \\ g_p(s) \end{bmatrix} = \frac{\boldsymbol{\beta}_1 s^{n-1} + \boldsymbol{\beta}_2 s^{n-2} + \dots + \boldsymbol{\beta}_n}{s^n + a_1 s^{n-1} + \dots + a_n} + \mathbf{d}, \quad \boldsymbol{\beta}_i \in \mathbb{R}^p$$

Realisasi ruang keadaan dalam **Bentuk Kanonik Keterkontrolan**:
$$A = \begin{bmatrix} -a_1 & -a_2 & \dots & -a_n \\ 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad C = \begin{bmatrix} \boldsymbol{\beta}_1 & \boldsymbol{\beta}_2 & \dots & \boldsymbol{\beta}_n \end{bmatrix} \in \mathbb{R}^{p \times n}, \quad D = \mathbf{d}$$

### 2. Sistem MISO (*Multiple-Input Single-Output*)
Fungsi transfer dinyatakan sebagai vektor baris:
$$\mathbf{G}(s) = \begin{bmatrix} g_1(s) & g_2(s) & \dots & g_m(s) \end{bmatrix} = \frac{\boldsymbol{\eta}_1 s^{n-1} + \boldsymbol{\eta}_2 s^{n-2} + \dots + \boldsymbol{\eta}_n}{s^n + a_1 s^{n-1} + \dots + a_n} + \mathbf{d}, \quad \boldsymbol{\eta}_i \in \mathbb{R}^{1 \times m}$$

Realisasi ruang keadaan dalam **Bentuk Kanonik Keterobservasian**:
$$A = \begin{bmatrix} -a_1 & 1 & 0 & \dots & 0 \\ -a_2 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_n & 0 & 0 & \dots & 0 \end{bmatrix}, \quad B = \begin{bmatrix} \boldsymbol{\eta}_1 \\ \boldsymbol{\eta}_2 \\ \vdots \\ \boldsymbol{\eta}_n \end{bmatrix} \in \mathbb{R}^{n \times m}, \quad C = \begin{bmatrix} 1 & 0 & \dots & 0 \end{bmatrix}, \quad D = \mathbf{d}$$

### 3. Sistem MIMO (*Multi-Input Multi-Output*)
Diberikan matriks fungsi transfer $G(s) \in \mathbb{R}^{p \times m}$. Melalui dekomposisi pecahan parsial:
$$G(s) = D + \sum_{i=1}^r \frac{W_i}{s - \lambda_i}$$

- **Metode Realisasi Minimal Gilbert**:
  Misalkan $\operatorname{rank}(W_i) = k_i$. Faktorisasi matriks residu menjadi:
  $$W_i = C_i B_i, \quad \text{dengan } C_i \in \mathbb{R}^{p \times k_i}, \; B_i \in \mathbb{R}^{k_i \times m}$$
  Realisasi minimal berorde $n = \sum_{i=1}^r k_i$ diperoleh melalui:
  $$A = \operatorname{diag}(\lambda_1 I_{k_1}, \lambda_2 I_{k_2}, \dots, \lambda_r I_{k_r}), \quad B = \begin{bmatrix} B_1 \\ B_2 \\ \vdots \\ B_r \end{bmatrix}, \quad C = \begin{bmatrix} C_1 & C_2 & \dots & C_r \end{bmatrix}$$

---

## 10. Transformasi Keserupaan (Similarity Transformation)

Representasi ruang keadaan **tidak unik**. Melalui perubahan basis koordinat $x(t) = P z(t)$ dengan matriks non-singular $P$:
$$\tilde{A} = P^{-1} A P, \quad \tilde{B} = P^{-1} B, \quad \tilde{C} = C P, \quad \tilde{D} = D$$

### Sifat Invarian:
1. Polinomial karakteristik tidak berubah: $\det(sI - \tilde{A}) = \det(sI - A)$.
2. Nilai-nilai eigen matriks $A$ tetap sama.
3. Fungsi transfer $\tilde{G}(s) = G(s)$ tidak berubah.

---

## 11. Solusi Domain Waktu & Matriks Transisi Keadaan

Untuk sistem $\dot{x}(t) = A x(t) + B u(t)$ dengan kondisi awal $x(0) = x_0$:
$$x(t) = e^{At} x(0) + \int_{0}^{t} e^{A(t - \tau)} B u(\tau) \, d\tau$$
$$y(t) = C e^{At} x(0) + C \int_{0}^{t} e^{A(t - \tau)} B u(\tau) \, d\tau + D u(t)$$

Di mana **Matriks Transisi Keadaan** adalah:
$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\}$$

### Sifat-sifat Utama $e^{At}$:
- $e^{A \cdot 0} = I$
- $(e^{At})^{-1} = e^{-At}$
- $e^{A(t_1 + t_2)} = e^{At_1} e^{At_2}$
- $\frac{d}{dt} e^{At} = A e^{At} = e^{At} A$

---

## 12. Contoh Soal & Pembahasan Komprehensif

### Contoh 1: Formula Penguatan Mason pada SFG
Diberikan SFG dengan lintasan:
- Jalur maju: $F_1 = G_1 G_2 G_3 G_4 G_5$, $F_2 = G_6$
- Lup individual: $L_1 = -G_2 H_1$, $L_2 = -G_4 H_2$, $L_3 = -G_1 G_2 G_3 G_4 G_5 H_3$
- Pasangan lup non-touching: $L_1$ dan $L_2$ tidak bersentuhan $\implies L_1 L_2 = G_2 G_4 H_1 H_2$.

**Penyelesaian**:
Determinan sistem:
$$\Delta = 1 - (L_1 + L_2 + L_3) + L_1 L_2 = 1 + G_2 H_1 + G_4 H_2 + G_1 G_2 G_3 G_4 G_5 H_3 + G_2 G_4 H_1 H_2$$
Kofaktor jalur maju:
- Jalur $F_1$ menyentuh semua lup $\implies \Delta_1 = 1$.
- Jalur $F_2$ tidak menyentuh lup $L_1$ dan $L_2$ $\implies \Delta_2 = 1 - (L_1 + L_2) + L_1 L_2 = (1 + G_2 H_1)(1 + G_4 H_2)$.

Fungsi transfer total:
$$G(s) = \frac{F_1 \Delta_1 + F_2 \Delta_2}{\Delta} = \frac{G_1 G_2 G_3 G_4 G_5 + G_6(1 + G_2 H_1 + G_4 H_2 + G_2 G_4 H_1 H_2)}{1 + G_2 H_1 + G_4 H_2 + G_1 G_2 G_3 G_4 G_5 H_3 + G_2 G_4 H_1 H_2}$$

---

### Contoh 2: Realisasi Sistem SIMO ke Ruang Keadaan
Diberikan fungsi transfer SIMO:
$$T(s) = \frac{1}{s^2 + 7s + 12} \begin{bmatrix} 3s + 13 \\ 3s + 11 \end{bmatrix}$$

**Penyelesaian**:
Polinomial penyebut: $s^2 + 7s + 12 \implies a_1 = 7, a_2 = 12$.
Pembilang:
$$\begin{bmatrix} 3s + 13 \\ 3s + 11 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} s + \begin{bmatrix} 13 \\ 11 \end{bmatrix} \implies \boldsymbol{\beta}_1 = \begin{bmatrix} 3 \\ 3 \end{bmatrix}, \; \boldsymbol{\beta}_2 = \begin{bmatrix} 13 \\ 11 \end{bmatrix}$$

Realisasi bentuk kanonik keterkontrolan:
$$\begin{aligned}
\begin{bmatrix} \dot{x}_1 \\ \dot{x}_2 \end{bmatrix} &= \begin{bmatrix} 0 & 1 \\ -12 & -7 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u \\
\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} &= \begin{bmatrix} 13 & 3 \\ 11 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
\end{aligned}$$
