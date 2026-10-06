# Catatan Kuliah MA4171 Teori Kontrol Linear
## Topik 03: Transformasi Z dan Sistem Diskrit (Minggu 5)
**Referensi Utama**: Katsuhiko Ogata, *Modern Control Engineering* & *Discrete-Time Control Systems*

---

## 📑 Daftar Isi
1. [Pendahuluan Sistem Waktu Diskrit & Pencuplikan](#1-pendahuluan-sistem-waktu-diskrit--pencuplikan)
2. [Definisi Transformasi Z](#2-definisi-transformasi-z)
3. [Sifat-Sifat dan Teorema Transformasi Z](#3-sifat-sifat-dan-teorema-transformasi-z)
4. [Invers Transformasi Z](#4-invers-transformasi-z)
5. [Fungsi Pulsa Transfer (Pulse Transfer Function)](#5-fungsi-pulsa-transfer-pulse-transfer-function)
6. [Representasi Ruang Keadaan Sistem Diskrit](#6-representasi-ruang-keadaan-sistem-diskrit)
7. [Solusi Ruang Keadaan Diskrit & Matriks Transisi Keadaan](#7-solusi-ruang-keadaan-diskrit--matriks-transisi-keadaan)
8. [Kestabilan Sistem Waktu Diskrit](#8-kestabilan-sistem-waktu-diskrit)
9. [Contoh Soal & Pembahasan Komprehensif](#9-contoh-soal--pembahasan-komprehensif)

---

## 1. Pendahuluan Sistem Waktu Diskrit & Pencuplikan

Dalam implementasi sistem kendali modern, algoritma kontrol umumnya dieksekusi menggunakan komputer digital, mikrokontroler, atau DSP (*Digital Signal Processor*).

### Klasifikasi Sinyal
- **Sinyal Kontinu (Analog)**: Terdefinisi untuk setiap waktu riil $t \in \mathbb{R}$, dinotasikan $x(t)$.
- **Sinyal Diskrit (Discrete-Time)**: Terdefinisi hanya pada saat-saat diskrit $t = kT$ ($k \in \mathbb{Z}$), dinotasikan $x(k)$ atau $x(kT)$, dengan $T$ adalah periode pencuplikan (*sampling period*).
- **Sinyal Digital**: Sinyal diskrit yang amplitudonya telah dikuantisasi dalam taraf biner terbatas.

### Proses Pencuplikan & Teorema Sampling Nyquist-Shannon
Sinyal kontinu $x(t)$ yang dicuplik secara ideal dimodelkan sebagai modulasi impuls Dirac:
$$x^*(t) = \sum_{k=0}^{\infty} x(kT) \delta(t - kT)$$

> **Teorema Sampling Nyquist-Shannon**:  
> Agar sinyal kontinu $x(t)$ dengan frekuensi tertinggi $\omega_{\max}$ dapat direkonstruksi secara sempurna dari sinyal sampel $x(kT)$, frekuensi sampling $\omega_s = \frac{2\pi}{T}$ harus memenuhi:
> $$\omega_s \ge 2\omega_{\max} \quad \left( f_s \ge 2 f_{\max} \right)$$
> Pelanggaran terhadap syarat ini menyebabkan fenomena tumpang-tindih spektrum frekuensi yang disebut **aliasing**.

### Penahan Orde Nol (*Zero-Order Hold* / ZOH)
Rangkaian ZOH memegang nilai cuplikan $u(kT)$ secara konstan selama interval satu periode sampling:
$$u(t) = u(kT), \quad kT \le t < (k+1)T$$

Fungsi transfer ZOH dalam domain Laplace:
$$G_h(s) = \frac{1 - e^{-Ts}}{s}$$

---

## 2. Definisi Transformasi Z

Transformasi Z merupakan padanan domain diskrit dari Transformasi Laplace pada sistem kontinu.

> **Definisi (Unilateral Z-Transform)**:  
> Untuk deret waktu diskrit kausal $x(k) = x(kT)$ ($k \ge 0$):
> $$\mathcal{Z}\{x(k)\} = X(z) = \sum_{k=0}^{\infty} x(k) z^{-k}$$
> Dengan relasi antara variabel Laplace $s$ dan variabel kompleks $z$:
> $$z = e^{sT}$$

### Daerah Konvergensi (*Region of Convergence* / ROC)
Himpunan nilai $z \in \mathbb{C}$ yang membuat deret $\sum_{k=0}^\infty |x(k) z^{-k}| < \infty$. Untuk sinyal kausal, ROC berbentuk $|z| > R$.

### Tabel Transformasi Z Sinyal Dasar

| Nama Sinyal | Domain Kontinu $x(t)$ | Domain Diskrit $x(k)$ | Transformasi Z $X(z)$ |
| :--- | :--- | :--- | :--- |
| **Impuls Satuan** | $\delta(t)$ | $\delta(k) = \begin{cases} 1, & k=0 \\ 0, & k \ne 0 \end{cases}$ | $1$ |
| **Tangga Satuan (Step)** | $1(t)$ | $1(k) = 1$ | $\dfrac{z}{z-1} = \dfrac{1}{1-z^{-1}}$ |
| **Ramp Satuan** | $t$ | $kT$ | $\dfrac{T z}{(z-1)^2}$ |
| **Polinomial $k$** | - | $k$ | $\dfrac{z}{(z-1)^2}$ |
| **Eksponensial** | $e^{-at}$ | $e^{-akT} = (e^{-aT})^k$ | $\dfrac{z}{z - e^{-aT}}$ |
| **Pangkat Basis $a$** | - | $a^k$ | $\dfrac{z}{z-a}$ |
| **Sinusoidal** | $\sin(\omega t)$ | $\sin(\omega k T)$ | $\dfrac{z \sin(\omega T)}{z^2 - 2z \cos(\omega T) + 1}$ |
| **Cosinusoidal** | $\cos(\omega t)$ | $\cos(\omega k T)$ | $\dfrac{z (z - \cos(\omega T))}{z^2 - 2z \cos(\omega T) + 1}$ |

---

## 3. Sifat-Sifat dan Teorema Transformasi Z

1. **Linearitas**:
   $$\mathcal{Z}\{\alpha x_1(k) + \beta x_2(k)\} = \alpha X_1(z) + \beta X_2(z)$$

2. **Pergeseran Waktu (*Time Shifting*)**:
   - *Delay* (Mundur): $\mathcal{Z}\{x(k-m)\} = z^{-m} X(z)$ (untuk sinyal kausal $x(k) = 0, k < 0$).
   - *Advance* (Maju):
     $$\begin{aligned}
     \mathcal{Z}\{x(k+1)\} &= z X(z) - z x(0) \\
     \mathcal{Z}\{x(k+2)\} &= z^2 X(z) - z^2 x(0) - z x(1) \\
     \mathcal{Z}\{x(k+m)\} &= z^m X(z) - \sum_{j=0}^{m-1} z^{m-j} x(j)
     \end{aligned}$$

3. **Penskalaan Kompleks**:
   $$\mathcal{Z}\{a^{-k} x(k)\} = X(az), \quad \mathcal{Z}\{e^{-akT} x(k)\} = X(z e^{aT})$$

4. **Diferensiasi Kompleks**:
   $$\mathcal{Z}\{k \, x(k)\} = -z \frac{d}{dz} X(z)$$

5. **Teorema Nilai Awal (*Initial Value Theorem*)**:
   $$x(0) = \lim_{z \to \infty} X(z)$$

6. **Teorema Nilai Akhir (*Final Value Theorem*)**:
   $$\lim_{k \to \infty} x(k) = \lim_{z \to 1} (1 - z^{-1}) X(z) = \lim_{z \to 1} (z-1) X(z)$$
   *(Syarat: Semua kutub dari $(z-1)X(z)$ berada di dalam lingkaran satuan $|z| < 1$)*.

7. **Konvolusi Diskrit**:
   $$\mathcal{Z}\left\{ \sum_{j=0}^k x_1(j) x_2(k-j) \right\} = X_1(z) \cdot X_2(z)$$

---

## 4. Invers Transformasi Z

Metode untuk memperoleh $x(k) = \mathcal{Z}^{-1}\{X(z)\}$:

### 1. Metode Ekspansi Pecahan Parsial
Ekspansikan $\dfrac{X(z)}{z}$:
$$\frac{X(z)}{z} = \sum_{i=1}^n \frac{c_i}{z - p_i} \implies X(z) = \sum_{i=1}^n c_i \frac{z}{z - p_i}$$
Sehingga inversnya:
$$x(k) = \sum_{i=1}^n c_i (p_i)^k, \quad k \ge 0$$

### 2. Metode Pembagian Langsung (*Power Series*)
Membagi pembilang dengan penyebut dalam pangkat menurun $z^{-1}$:
$$X(z) = x(0) + x(1) z^{-1} + x(2) z^{-2} + \dots$$

### 3. Metode Integral Inversi (Residu)
$$x(k) = \sum_{i} \operatorname{Res}\left[ X(z) z^{k-1}, z = p_i \right] = \sum_i \lim_{z \to p_i} (z - p_i) X(z) z^{k-1}$$

---

## 5. Fungsi Pulsa Transfer (Pulse Transfer Function)

### Persamaan Beda LTI Diskrit
$$y(k) + a_1 y(k-1) + \dots + a_n y(k-n) = b_0 u(k) + b_1 u(k-1) + \dots + b_m u(k-m)$$

Fungsi transfer pulsa:
$$G(z) = \frac{Y(z)}{U(z)} = \frac{b_0 + b_1 z^{-1} + \dots + b_m z^{-m}}{1 + a_1 z^{-1} + \dots + a_n z^{-n}} = \frac{b_0 z^n + b_1 z^{n-1} + \dots + b_m z^{n-m}}{z^n + a_1 z^{n-1} + \dots + a_n}$$

### Diskritisasi Plant Kontinu dengan ZOH
Jika plant kontinu $G_p(s)$ didahului oleh penahan ZOH:
$$G(z) = \mathcal{Z}\{ G_h(s) G_p(s) \} = (1 - z^{-1}) \mathcal{Z}\left\{ \frac{G_p(s)}{s} \right\}$$

---

## 6. Representasi Ruang Keadaan Sistem Diskrit

### Bentuk Standar Sistem Diskrit LTI
$$\begin{aligned}
x(k+1) &= G x(k) + H u(k) \quad &&\text{\textbf{(Persamaan Keadaan Diskrit)}} \\
y(k) &= C x(k) + D u(k) \quad &&\text{\textbf{(Persamaan Keluaran Diskrit)}}
\end{aligned}$$

Di mana:
- $x(k) \in \mathbb{R}^n$: Vektor keadaan diskrit
- $u(k) \in \mathbb{R}^m$: Vektor masukan kontrol
- $y(k) \in \mathbb{R}^p$: Vektor keluaran
- $G \in \mathbb{R}^{n \times n}$: Matriks sistem diskrit ($A_d$ atau $\Phi$)
- $H \in \mathbb{R}^{n \times m}$: Matriks masukan diskrit ($B_d$ atau $\Gamma$)

### Diskritisasi dari Sistem Kontinu $(\dot{x} = Ax + Bu)$
$$G = e^{AT}, \quad H = \left( \int_{0}^T e^{A\tau} \, d\tau \right) B = A^{-1}(e^{AT} - I) B$$

### Konversi Ruang Keadaan Diskrit ke Fungsi Transfer
$$G(z) = \frac{Y(z)}{U(z)} = C (zI - G)^{-1} H + D = \frac{C \operatorname{adj}(zI - G) H}{\det(zI - G)} + D$$
Persamaan karakteristik sistem: $\det(zI - G) = 0$.

---

## 7. Solusi Ruang Keadaan Diskrit & Matriks Transisi Keadaan

### Solusi Waktu Rekursif
$$x(k) = G^k x(0) + \sum_{j=0}^{k-1} G^{k-1-j} H u(j)$$
$$y(k) = C G^k x(0) + C \sum_{j=0}^{k-1} G^{k-1-j} H u(j) + D u(k)$$

### Matriks Transisi Keadaan Diskrit $\Psi(k) = G^k$
$$\Psi(k) = G^k = \mathcal{Z}^{-1}\left\{ (zI - G)^{-1} z \right\}$$

---

## 8. Kestabilan Sistem Waktu Diskrit

### Pemetaan Bidang $s$ ke Bidang $z$ ($z = e^{sT}$)
- **Setengah Bidang Kiri Kontinu ($\operatorname{Re}(s) < 0$)** $\iff$ **Bagian Dalam Lingkaran Satuan ($|z| < 1$)** $\to$ **Stabil Asimtotik**
- **Sumbu Imajiner Kontinu ($\operatorname{Re}(s) = 0$)** $\iff$ **Garis Lingkaran Satuan ($|z| = 1$)** $\to$ **Stabil Marjinal**
- **Setengah Bidang Kanan Kontinu ($\operatorname{Re}(s) > 0$)** $\iff$ **Bagian Luar Lingkaran Satuan ($|z| > 1$)** $\to$ **Tak Stabil**

> **Kriteria Kestabilan Diskrit**:  
> Sistem stabil asimtotik jika dan hanya jika seluruh kutub dari $G(z)$ atau seluruh nilai eigen matriks $G$ berada di dalam lingkaran satuan:
> $$|\lambda_i| < 1 \quad (\forall i = 1, 2, \dots, n)$$

### Uji Kestabilan Jury (*Jury Test*) Orde-2 ($P(z) = a_0 z^2 + a_1 z + a_2 = 0, a_0 > 0$)
1. $|a_2| < a_0$
2. $P(1) = a_0 + a_1 + a_2 > 0$
3. $P(-1) = a_0 - a_1 + a_2 > 0$

---

## 9. Contoh Soal & Pembahasan Komprehensif

### Contoh 1: Invers Transformasi Z Pecahan Parsial
Diberikan:
$$X(z) = \frac{z(2z + 1)}{(z - 1)(z - 0.5)}$$

**Penyelesaian**:
$$\frac{X(z)}{z} = \frac{2z + 1}{(z - 1)(z - 0.5)} = \frac{6}{z - 1} - \frac{4}{z - 0.5}$$
$$X(z) = 6 \frac{z}{z - 1} - 4 \frac{z}{z - 0.5}$$
Invers Transformasi Z:
$$x(k) = 6(1)^k - 4(0.5)^k = 6 - 4(0.5)^k, \quad k \ge 0$$

---

### Contoh 2: Diskritisasi Plant Kontinu dengan ZOH
Diberikan plant kontinu $G_p(s) = \dfrac{2}{s + 2}$ dengan periode pencuplikan $T = 0.1$ detik.

**Penyelesaian**:
$$G(z) = (1 - z^{-1}) \mathcal{Z}\left\{ \frac{2}{s(s+2)} \right\} = \frac{z - 1}{z} \mathcal{Z}\left\{ \frac{1}{s} - \frac{1}{s+2} \right\}$$
$$\mathcal{L}^{-1}\left\{ \frac{1}{s} - \frac{1}{s+2} \right\} = 1 - e^{-2t} \xrightarrow{t=kT} 1 - (e^{-2T})^k$$
$$\mathcal{Z}\left\{ 1 - (e^{-2T})^k \right\} = \frac{z(1 - e^{-2T})}{(z - 1)(z - e^{-2T})}$$
$$G(z) = \frac{z - 1}{z} \cdot \frac{z(1 - e^{-2T})}{(z - 1)(z - e^{-2T})} = \frac{1 - e^{-2T}}{z - e^{-2T}}$$
Untuk $T = 0.1 \implies e^{-0.2} \approx 0.8187$:
$$G(z) = \frac{0.1813}{z - 0.8187}$$

---

### Contoh 3: Ruang Keadaan Diskrit & Matriks Transisi $G^k$
Diberikan:
$$x(k+1) = \begin{bmatrix} 0 & 1 \\ -0.16 & 1 \end{bmatrix} x(k) + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u(k), \quad y(k) = \begin{bmatrix} 1 & 0 \end{bmatrix} x(k)$$

**Penyelesaian**:
1. Hitung $(zI - G)^{-1}$:
   $$\det(zI - G) = z(z - 1) + 0.16 = (z - 0.8)(z - 0.2)$$
   $$(zI - G)^{-1} = \frac{1}{(z - 0.8)(z - 0.2)} \begin{bmatrix} z - 1 & 1 \\ -0.16 & z \end{bmatrix}$$

2. Fungsi transfer $G(z) = C(zI - G)^{-1} H$:
   $$G(z) = \begin{bmatrix} 1 & 0 \end{bmatrix} \left( \frac{1}{(z - 0.8)(z - 0.2)} \begin{bmatrix} z - 1 & 1 \\ -0.16 & z \end{bmatrix} \right) \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \frac{1}{z^2 - z + 0.16}$$

3. Matriks transisi $G^k = \mathcal{Z}^{-1}\{(zI - G)^{-1} z\}$:
   $$G^k = \begin{bmatrix}
   -\frac{1}{3}(0.8)^k - \frac{4}{3}(0.2)^k & \frac{5}{3}(0.8)^k - \frac{5}{3}(0.2)^k \\[6pt]
   -\frac{4}{15}(0.8)^k + \frac{4}{15}(0.2)^k & \frac{4}{3}(0.8)^k - \frac{1}{3}(0.2)^k
   \end{bmatrix}, \quad k \ge 0$$
