# Catatan Kuliah MA4171 Teori Kontrol Linear
## Topik 02: Model Matematika pada Sistem Dinamik (Minggu 2 – 4)
**Referensi**: Katsuhiko Ogata, *Modern Control Engineering*, Bab 2 & Bab 9.2

---

## 📑 Daftar Isi
1. [Pendahuluan & Karakteristik Sistem LTI](#1-pendahuluan--karakteristik-sistem-lti)
2. [Fungsi Transfer (Transfer Function)](#2-fungsi-transfer-transfer-function)
3. [Aljabar & Reduksi Diagram Blok](#3-aljabar--reduksi-diagram-blok)
4. [Representasi Ruang Keadaan (State-Space Representation)](#4-representasi-ruang-keadaan-state-space-representation)
5. [Hubungan Ruang Keadaan dan Fungsi Transfer](#5-hubungan-ruang-keadaan-dan-fungsi-transfer)
6. [Bentuk-Bentuk Kanonik Ruang Keadaan](#6-bentuk-bentuk-kanonik-ruang-keadaan)
7. [Transformasi Keserupaan (Similarity Transformation)](#7-transformasi-keserupaan-similarity-transformation)
8. [Solusi Domain Waktu & Matriks Transisi Keadaan](#8-solusi-domain-waktu--matriks-transisi-keadaan)
9. [Contoh Soal & Pembahasan Komprehensif](#9-contoh-soal--pembahasan-komprehensif)

---

## 1. Pendahuluan & Karakteristik Sistem LTI

Pemodelan matematika adalah langkah mendasar untuk menganalisis perilaku sistem dinamik dan merancang pengontrol yang stabil dan optimal.

### Sistem Linear Time-Invariant (LTI)
Fokus kajian adalah sistem LTI kontinu:
- **Linearitas**: Memenuhi prinsip **superposisi** dan **homogenitas**.
- **Time-Invariance**: Parameter sistem konstan terhadap pergeseran waktu $t$.

### Dua Paradigma Representasi Sistem
| Karakteristik | Domain Frekuensi (*S-Domain*) | Domain Waktu (*State-Space*) |
| :--- | :--- | :--- |
| **Model Utama** | Fungsi Transfer $G(s)$, Diagram Blok | Persamaan Diferensial Vektor Orde 1 |
| **Tipe Sistem** | Sangat ideal untuk SISO (*Single-Input Single-Output*) | Sangat fleksibel untuk MIMO (*Multi-Input Multi-Output*) |
| **Kondisi Awal** | Diasumsikan bernilai nol ($x(0) = 0$) | Mengakomodasi kondisi awal riil ($x(0) \ne 0$) |
| **Dinamika Internal**| Model *Black-Box* (hanya relasi input-output) | Model *White-Box* (mencakup semua state internal) |

---

## 2. Fungsi Transfer (Transfer Function)

> **Definisi**: Perbandingan antara Transformasi Laplace dari sinyal keluaran $Y(s)$ terhadap Transformasi Laplace dari sinyal masukan $U(s)$ dengan **semua syarat awal nol**.

$$G(s) = \frac{Y(s)}{U(s)} = \frac{\mathcal{L}\{y(t)\}}{\mathcal{L}\{u(t)\}}\Bigg|_{\text{syarat awal } = 0}$$

Jika sistem dinyatakan dalam persamaan diferensial linear berorde $n$:
$$a_0 \frac{d^n y}{dt^n} + a_1 \frac{d^{n-1} y}{dt^{n-1}} + \dots + a_n y(t) = b_0 \frac{d^m u}{dt^m} + b_1 \frac{d^{m-1} u}{dt^{m-1}} + \dots + b_m u(t)$$

Dengan menerapkan Transformasi Laplace dan syarat awal nol:
$$G(s) = \frac{b_0 s^m + b_1 s^{m-1} + \dots + b_m}{a_0 s^n + a_1 s^{n-1} + \dots + a_n} = \frac{N(s)}{D(s)}$$

### Elemen Penting:
- **Persamaan Karakteristik**: $D(s) = a_0 s^n + a_1 s^{n-1} + \dots + a_n = 0$.
- **Kutub (*Poles*)**: Akar-akar dari penyebut $D(s) = 0$. Menentukan kestabilan sistem.
- **Pembuat Nol (*Zeros*)**: Akar-akar dari pembilang $N(s) = 0$.
- **Tanggapan Impuls (*Impulse Response*)**: Respon terhadap input impuls $\delta(t)$ di mana $U(s) = 1$, sehingga $y(t) = g(t) = \mathcal{L}^{-1}\{G(s)\}$.

---

## 3. Aljabar & Reduksi Diagram Blok

Diagram blok memvisualisasikan aliran sinyal dan pemrosesan fungsional dalam sistem kontrol.

### Aturan Ekuivalensi Reduksi

| Konfigurasi | Diagram Asli | Bentuk Ekuivalen / Rumus |
| :--- | :--- | :--- |
| **Kaskade (Seri)** | $\xrightarrow{U} [G_1] \xrightarrow{} [G_2] \xrightarrow{Y}$ | $G_{eq}(s) = G_1(s) G_2(s)$ |
| **Paralel** | $\xrightarrow{U} [G_1] \xrightarrow{+} \Sigma \xrightarrow{Y}$, $\xrightarrow{U} [G_2] \xrightarrow{+}$ | $G_{eq}(s) = G_1(s) \pm G_2(s)$ |
| **Loop Umpan Balik Negatif** | Forward $G(s)$, Feedback $H(s)$ (-) | $T(s) = \dfrac{Y(s)}{R(s)} = \dfrac{G(s)}{1 + G(s)H(s)}$ |
| **Loop Umpan Balik Positif** | Forward $G(s)$, Feedback $H(s)$ (+) | $T(s) = \dfrac{Y(s)}{R(s)} = \dfrac{G(s)}{1 - G(s)H(s)}$ |
| **Geser Titik Cabang Melewati Blok ke Kanan** | Ambil cabang sebelum $G(s)$ | Tambahkan blok $\dfrac{1}{G(s)}$ pada jalur cabang |
| **Geser Titik Jumlah Melewati Blok ke Kanan** | Jumlahkan sebelum $G(s)$ | Kalikan masukan cabang dengan $G(s)$ |

---

## 4. Representasi Ruang Keadaan (State-Space Representation)

Representasi ruang keadaan mendeskripsikan sistem orde-$n$ sebagai sistem $n$ persamaan diferensial linear orde satu yang saling berkait.

### Bentuk Standar Sistem LTI Kontinu
$$\begin{aligned}
\dot{x}(t) &= A x(t) + B u(t) \quad &&\text{\textbf{(Persamaan Keadaan / State Equation)}} \\
y(t) &= C x(t) + D u(t) \quad &&\text{\textbf{(Persamaan Keluaran / Output Equation)}}
\end{aligned}$$

Di mana:
- $x(t) \in \mathbb{R}^n$: Vektor keadaan (*state vector*)
- $u(t) \in \mathbb{R}^m$: Vektor masukan (*input vector*)
- $y(t) \in \mathbb{R}^p$: Vektor keluaran (*output vector*)
- $A \in \mathbb{R}^{n \times n}$: Matriks dinamika sistem (*system matrix*)
- $B \in \mathbb{R}^{n \times m}$: Matriks masukan (*input matrix*)
- $C \in \mathbb{R}^{p \times n}$: Matriks keluaran (*output matrix*)
- $D \in \mathbb{R}^{p \times m}$: Matriks transmisi langsung (*feedforward matrix*, umumnya bernilai 0)

---

## 5. Hubungan Ruang Keadaan dan Fungsi Transfer

Dengan menerapkan Transformasi Laplace pada persamaan keadaan dengan syarat awal $x(0) = 0$:
$$sX(s) = A X(s) + B U(s) \implies (sI - A) X(s) = B U(s)$$
$$X(s) = (sI - A)^{-1} B U(s)$$

Substitusi ke persamaan keluaran $Y(s) = C X(s) + D U(s)$:

$$G(s) = \frac{Y(s)}{U(s)} = C (sI - A)^{-1} B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$

> **Catatan Penting**:
> - Polinomial karakteristik sistem adalah $\det(sI - A) = 0$.
> - Nilai eigen dari matriks $A$ ($\lambda_i$) berkorespondensi langsung dengan kutub-kutub (*poles*) fungsi transfer sistem.

---

## 6. Bentuk-Bentuk Kanonik Ruang Keadaan

Diberikan fungsi transfer *strictly proper*:
$$G(s) = \frac{b_1 s^{n-1} + b_2 s^{n-2} + \dots + b_n}{s^n + a_1 s^{n-1} + a_2 s^{n-2} + \dots + a_n}$$

### 1. Bentuk Kanonik Terkontrol (*Controllable Canonical Form*)
Berguna untuk sintesis pengontrol umpan balik keadaan (*state feedback / pole placement*):
$$A = \begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
-a_n & -a_{n-1} & -a_{n-2} & \dots & -a_1
\end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$
$$C = \begin{bmatrix} b_n & b_{n-1} & \dots & b_1 \end{bmatrix}, \quad D = [0]$$

### 2. Bentuk Kanonik Terobservasi (*Observable Canonical Form*)
Bentuk dual dari bentuk terkontrol, sangat bermanfaat untuk perancangan *state observer*:
$$A = \begin{bmatrix}
0 & 0 & \dots & 0 & -a_n \\
1 & 0 & \dots & 0 & -a_{n-1} \\
0 & 1 & \dots & 0 & -a_{n-2} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & \dots & 1 & -a_1
\end{bmatrix}, \quad
B = \begin{bmatrix} b_n \\ b_{n-1} \\ \vdots \\ b_1 \end{bmatrix}$$
$$C = \begin{bmatrix} 0 & 0 & \dots & 0 & 1 \end{bmatrix}, \quad D = [0]$$

### 3. Bentuk Kanonik Diagonal / Jordan (*Diagonal / Jordan Form*)
Jika akar penyebut memiliki $n$ nilai unik $p_1, p_2, \dots, p_n$:
$$G(s) = \sum_{i=1}^n \frac{c_i}{s - p_i} \implies
A = \operatorname{diag}(p_1, p_2, \dots, p_n), \quad
B = \begin{bmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{bmatrix}, \quad
C = \begin{bmatrix} c_1 & c_2 & \dots & c_n \end{bmatrix}$$

---

## 7. Transformasi Keserupaan (Similarity Transformation)

Representasi ruang keadaan **tidak unik**. Melalui perubahan basis koordinat keadaan $x(t) = P z(t)$ dengan matriks non-singular $P$:

$$\tilde{A} = P^{-1} A P, \quad \tilde{B} = P^{-1} B, \quad \tilde{C} = C P, \quad \tilde{D} = D$$

### Sifat Invarian:
1. Polinomial karakteristik tidak berubah: $\det(sI - \tilde{A}) = \det(sI - A)$.
2. Nilai-nilai eigen matriks $A$ tetap sama.
3. Fungsi transfer $\tilde{G}(s) = G(s)$ tidak berubah.

---

## 8. Solusi Domain Waktu & Matriks Transisi Keadaan

Untuk sistem $\dot{x}(t) = A x(t) + B u(t)$ dengan syarat awal $x(0) = x_0$:

$$x(t) = e^{At} x(0) + \int_{0}^{t} e^{A(t - \tau)} B u(\tau) \, d\tau$$
$$y(t) = C e^{At} x(0) + C \int_{0}^{t} e^{A(t - \tau)} B u(\tau) \, d\tau + D u(t)$$

Di mana **Matriks Transisi Keadaan** didefinisikan sebagai:
$$\Phi(t) = e^{At} = \mathcal{L}^{-1}\{(sI - A)^{-1}\}$$

### Sifat-sifat Utama $e^{At}$:
- $e^{A \cdot 0} = I$
- $(e^{At})^{-1} = e^{-At}$
- $e^{A(t_1 + t_2)} = e^{At_1} e^{At_2}$
- $\frac{d}{dt} e^{At} = A e^{At} = e^{At} A$

---

## 9. Contoh Soal & Pembahasan Komprehensif

### Contoh 1: Konversi State-Space ke Transfer Function
Diberikan matriks sistem:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad D = 0$$

**Langkah Penyelesaian:**
1. Hitung $(sI - A)$:
   $$(sI - A) = \begin{bmatrix} s & -1 \\ 2 & s+3 \end{bmatrix}$$
2. Hitung determinan dan invers:
   $$\det(sI - A) = s^2 + 3s + 2 = (s+1)(s+2)$$
   $$(sI - A)^{-1} = \frac{1}{(s+1)(s+2)} \begin{bmatrix} s+3 & 1 \\ -2 & s \end{bmatrix}$$
3. Hitung $G(s) = C (sI - A)^{-1} B$:
   $$G(s) = \begin{bmatrix} 1 & 0 \end{bmatrix} \left( \frac{1}{(s+1)(s+2)} \begin{bmatrix} s+3 & 1 \\ -2 & s \end{bmatrix} \right) \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{s^2 + 3s + 2}$$

### Contoh 2: Menghitung Matriks Transisi Keadaan $e^{At}$
Dari matriks $(sI - A)^{-1}$ pada contoh 1, lakukan dekomposisi pecahan parsial:
$$\begin{aligned}
\mathcal{L}^{-1}\left\{ \frac{s+3}{(s+1)(s+2)} \right\} &= 2e^{-t} - e^{-2t} \\
\mathcal{L}^{-1}\left\{ \frac{1}{(s+1)(s+2)} \right\} &= e^{-t} - e^{-2t} \\
\mathcal{L}^{-1}\left\{ \frac{-2}{(s+1)(s+2)} \right\} &= -2e^{-t} + 2e^{-2t} \\
\mathcal{L}^{-1}\left\{ \frac{s}{(s+1)(s+2)} \right\} &= -e^{-t} + 2e^{-2t}
\end{aligned}$$

Maka:
$$e^{At} = \begin{bmatrix} 2e^{-t} - e^{-2t} & e^{-t} - e^{-2t} \\ -2e^{-t} + 2e^{-2t} & -e^{-t} + 2e^{-2t} \end{bmatrix}$$
