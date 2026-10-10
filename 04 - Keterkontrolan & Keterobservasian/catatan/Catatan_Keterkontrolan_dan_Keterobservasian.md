# Catatan Kuliah MA4171 Teori Kontrol Linear
## Topik 04: Keterkontrolan dan Keterobservasian Sistem (Minggu 6 – 7)
**Referensi Utama**: Katsuhiko Ogata, *Modern Control Engineering* (Bab 9.2, 9.6, & 9.7); Slide Kuliah MA4171 ITB

---

## 📑 Daftar Isi
1. [Pendahuluan & Konsep Struktural Sistem](#1-pendahuluan--konsep-struktural-sistem)
2. [Keterkontrolan Keadaan (State Controllability)](#2-keterkontrolan-keadaan-state-controllability)
3. [Keterobservasian Keadaan (State Observability)](#3-keterobservasian-keadaan-state-observability)
4. [Prinsip Dualitas Kalman](#4-prinsip-dualitas-kalman)
5. [Matriks Transformasi ke Bentuk Kanonik (P dan Q)](#5-matriks-transformasi-ke-bentuk-kanonik-p-dan-q)
6. [Keterkontrolan Keluaran (Output Controllability)](#6-keterkontrolan-keluaran-output-controllability)
7. [Keterstabilan (Stabilizability) & Keterdeteksian (Detectability)](#7-keterstabilan-stabilizability--keterdeteksian-detectability)
8. [Dekomposisi Kanonik Kalman & Pembatalan Kutub-Nol](#8-dekomposisi-kanonik-kalman--pembatalan-kutub-nol)
9. [Keterkontrolan & Keterobservasian Sistem Diskrit](#9-keterkontrolan--keterobservasian-sistem-diskrit)
10. [Contoh Soal & Pembahasan Komprehensif](#10-contoh-soal--pembahasan-komprehensif)

---

## 1. Pendahuluan & Konsep Struktural Sistem

Konsep **Keterkontrolan (*Controllability*)** dan **Keterobservasian (*Observability*)** diperkenalkan oleh Rudolf E. Kalman pada awal 1960-an sebagai pilar fundamental teori kontrol modern berbasis ruang keadaan (*state-space*):

- **Keterkontrolan**: Apakah masukan kendali $u(t)$ mampu mengarahkan seluruh variabel keadaan internal $x(t)$ dari sembarang kondisi awal menuju titik tujuan dalam waktu berhingga?
- **Keterobservasian**: Apakah kondisi awal seluruh variabel keadaan internal $x(0)$ dapat direkonstruksi secara unik hanya melalui pengukuran riwayat keluaran $y(t)$ dan masukan $u(t)$?

> **Peran Krusial dalam Desain Kontrol**:
> - Keterkontrolan adalah prasyarat mutlak untuk perancangan **umpan balik keadaan (*state feedback / pole placement*)**.
> - Keterobservasian adalah prasyarat mutlak untuk perancangan **pengamat keadaan (*state observer / estimator*)**.

---

## 2. Keterkontrolan Keadaan (State Controllability)

Diberikan sistem LTI kontinu:
$$\dot{x}(t) = A x(t) + B u(t), \quad x(t) \in \mathbb{R}^n, \; u(t) \in \mathbb{R}^m$$

> **Definisi**:  
> Sistem $(A, B)$ dikatakan **terkontrol keadaan lengkap** (*completely state controllable*) jika untuk setiap keadaan awal $x(t_0) = x_0$ dan sembarang keadaan target $x_1$, terdapat sinyal kontrol tak-terkendala $u(t)$ yang dapat mentransfer sistem dari $x_0$ ke $x_1$ dalam interval waktu berhingga $t_0 \le t \le t_1$.

### Kriteria Matriks Keterkontrolan Kalman
Berbasis Teorema Cayley-Hamilton, matriks keterkontrolan Kalman didefinisikan sebagai:

$$M_c = \begin{bmatrix} B & AB & A^2 B & \dots & A^{n-1} B \end{bmatrix} \in \mathbb{R}^{n \times nm}$$

> **Teorema Kalman**:  
> Sistem $(A, B)$ terkontrol keadaan lengkap jika dan hanya jika:
> $$\operatorname{rank}(M_c) = n$$
> Untuk sistem SISO ($m=1$), $M_c \in \mathbb{R}^{n \times n} \implies \det(M_c) \ne 0$.

### Gramian Keterkontrolan (*Controllability Gramian*)
$$W_c(0, t_1) = \int_0^{t_1} e^{A(t_1 - \tau)} B B^T e^{A^T(t_1 - \tau)} \, d\tau \in \mathbb{R}^{n \times n}$$
Sistem $(A, B)$ terkontrol $\iff W_c(0, t_1) > 0$ (simetris definit positif) untuk setiap $t_1 > 0$.

Sinyal kendali dengan energi minimum $\int_0^{t_1} u^T(t) u(t) \, dt$:
$$u(t) = B^T e^{A^T(t_1 - t)} W_c^{-1}(0, t_1) \left[ x_1 - e^{At_1} x_0 \right]$$

### Uji Popov-Belevitch-Hautus (PBH Test) Keterkontrolan
> **Uji PBH**:  
> Sistem $(A, B)$ terkontrol lengkap jika dan hanya jika:
> $$\operatorname{rank} \begin{bmatrix} sI - A & B \end{bmatrix} = n, \quad \forall s \in \mathbb{C}$$
> *(Cukup diuji pada seluruh nilai eigen $s = \lambda_i$ dari matriks $A$)*.

### Uji Keterkontrolan Gilbert (Bentuk Diagonal)
Jika $\Lambda = P^{-1} A P = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ dengan nilai eigen berbeda:
$$\dot{z}(t) = \Lambda z(t) + \tilde{B} u(t), \quad \tilde{B} = P^{-1} B$$
Sistem terkontrol $\iff$ **tidak ada baris pada matriks $\tilde{B}$ yang seluruh elemennya bernilai nol**.

---

## 3. Keterobservasian Keadaan (State Observability)

Diberikan sistem LTI kontinu:
$$\dot{x}(t) = A x(t) + B u(t), \quad y(t) = C x(t) + D u(t)$$
dengan $x \in \mathbb{R}^n, u \in \mathbb{R}^m, y \in \mathbb{R}^p$.

> **Definisi**:  
> Sistem $(A, C)$ dikatakan **terobservasi keadaan lengkap** (*completely state observable*) jika setiap keadaan awal $x(t_0) = x_0$ dapat ditentukan secara unik dari pengukuran keluaran $y(t)$ dan masukan $u(t)$ pada interval waktu berhingga $t_0 \le t \le t_1$.

### Kriteria Matriks Keterobservasian Kalman
Matriks keterobservasian Kalman didefinisikan sebagai:

$$M_o = \begin{bmatrix} C \\ CA \\ CA^2 \\ \vdots \\ CA^{n-1} \end{bmatrix} \in \mathbb{R}^{np \times n}$$

> **Teorema Kalman**:  
> Sistem $(A, C)$ terobservasi keadaan lengkap jika dan hanya jika:
> $$\operatorname{rank}(M_o) = n$$
> Untuk sistem ber-output skalar ($p=1$), $M_o \in \mathbb{R}^{n \times n} \implies \det(M_o) \ne 0$.

### Gramian Keterobservasian (*Observability Gramian*)
$$W_o(0, t_1) = \int_0^{t_1} e^{A^T \tau} C^T C e^{A \tau} \, d\tau \in \mathbb{R}^{n \times n}$$
Sistem $(A, C)$ terobservasi $\iff W_o(0, t_1) > 0$ (simetris definit positif) untuk setiap $t_1 > 0$.

### Uji PBH Keterobservasian
> **Uji PBH**:  
> Sistem $(A, C)$ terobservasi lengkap jika dan hanya jika:
> $$\operatorname{rank} \begin{bmatrix} sI - A \\ C \end{bmatrix} = n, \quad \forall s \in \mathbb{C}$$
> *(Cukup diuji pada seluruh nilai eigen $s = \lambda_i$ dari matriks $A$)*.

### Uji Keterobservasian Gilbert (Bentuk Diagonal)
Jika $\Lambda = P^{-1} A P = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ dan $\tilde{C} = C P$:
Sistem terobservasi $\iff$ **tidak ada kolom pada matriks $\tilde{C}$ yang seluruh elemennya bernilai nol**.

---

## 4. Prinsip Dualitas Kalman

> **Teorema Dualitas Kalman**:  
> Pasangan $(A, B)$ bersifat **terkontrol lengkap** jika dan hanya jika pasangan dualnya $(A^T, B^T)$ bersifat **terobservasi lengkap**.

### Tabel Ekuivalensi Dualitas
| Properti | Sistem Primer $\mathcal{S}$ | Sistem Dual $\mathcal{S}^*$ |
| :--- | :--- | :--- |
| **Persamaan Sistem** | $\dot{x} = Ax + Bu, \; y = Cx$ | $\dot{z} = A^T z + C^T v, \; w = B^T z$ |
| **Matriks Sistem** | $A$ | $A^T$ |
| **Matriks Masukan / Keluaran** | Masukan: $B$, Keluaran: $C$ | Masukan: $C^T$, Keluaran: $B^T$ |
| **Matriks Keterkontrolan** | $M_c = \begin{bmatrix} B & AB & \dots & A^{n-1}B \end{bmatrix}$ | $M_c^* = M_o^T$ |
| **Matriks Keterobservasian**| $M_o = \begin{bmatrix} C \\ CA \\ \dots \\ CA^{n-1} \end{bmatrix}$ | $M_o^* = M_c^T$ |
| **Kondisi Rank** | $\operatorname{rank}(M_c) = n$ | $\operatorname{rank}(M_o^*) = \operatorname{rank}(M_c^T) = n$ |

---

## 5. Matriks Transformasi ke Bentuk Kanonik (P dan Q)

Jika sistem SISO $(A, B)$ bersifat terkontrol lengkap, sistem dapat ditransformasikan ke bentuk kanonik terkontrol melalui transformasi keadaan $x = T z$ atau $x = P z$.

Misalkan polinomial karakteristik matriks $A$ adalah:
$$\det(sI - A) = s^n + a_1 s^{n-1} + a_2 s^{n-2} + \dots + a_{n-1} s + a_n$$

Definisikan matriks segitiga Toeplitz atas $W$:
$$W = \begin{bmatrix}
a_{n-1} & a_{n-2} & \dots & a_1 & 1 \\
a_{n-2} & a_{n-3} & \dots & 1 & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_1 & 1 & \dots & 0 & 0 \\
1 & 0 & \dots & 0 & 0
\end{bmatrix}$$

### Matriks Transformasi Keterkontrolan:
$$T = M_c W = \begin{bmatrix} B & AB & \dots & A^{n-1} B \end{bmatrix} W$$
Maka:
$$T^{-1} A T = \begin{bmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
-a_n & -a_{n-1} & -a_{n-2} & \dots & -a_1
\end{bmatrix}, \quad
T^{-1} B = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$

---

## 6. Keterkontrolan Keluaran (Output Controllability)

> **Definisi**:  
> Kemampuan sinyal kontrol $u(t)$ mentransfer keluaran $y(t)$ dari sembarang nilai awal $y(t_0)$ ke sembarang nilai target $y(t_1)$ dalam waktu berhingga.

Matriks keterkontrolan keluaran:
$$M_{co} = \begin{bmatrix} CB & CAB & CA^2 B & \dots & CA^{n-1} B & D \end{bmatrix} \in \mathbb{R}^{p \times (nm + m)}$$

> **Syarat Rank**: Terkontrol keluaran lengkap $\iff \operatorname{rank}(M_{co}) = p$.

- Keterkontrolan keadaan $+$ rank penuh matriks keluaran ($\operatorname{rank}(C) = p$) $\implies$ **Terkontrol keluaran**.
- Keterkontrolan keluaran **tidak menjamin** keterkontrolan seluruh variabel keadaan internal.

---

## 7. Keterstabilan (Stabilizability) & Keterdeteksian (Detectability)

- **Keterstabilan (*Stabilizability*)**: Seluruh mode yang tidak terkontrol bersifat stabil asimtotik ($\operatorname{Re}(\lambda) < 0$).
- **Keterdeteksian (*Detectability*)**: Seluruh mode yang tidak terobservasi bersifat stabil asimtotik ($\operatorname{Re}(\lambda) < 0$).

> **Uji PBH**:
> $$\begin{aligned}
> (A, B) \text{ stabilizable} &\iff \operatorname{rank} \begin{bmatrix} sI - A & B \end{bmatrix} = n, \quad \forall s \in \mathbb{C} \text{ dengan } \operatorname{Re}(s) \ge 0 \\
> (A, C) \text{ detectable} &\iff \operatorname{rank} \begin{bmatrix} sI - A \\ C \end{bmatrix} = n, \quad \forall s \in \mathbb{C} \text{ dengan } \operatorname{Re}(s) \ge 0
> \end{aligned}$$

---

## 8. Dekomposisi Kanonik Kalman & Pembatalan Kutub-Nol

### Empat Sub-ruang Keadaan Kalman
Ruang keadaan dapat didekomposisi menjadi 4 sub-ruang ortogonal:
$$x = \begin{bmatrix} x_{co} \\ x_{c\bar{o}} \\ x_{\bar{c}o} \\ x_{\bar{c}\bar{o}} \end{bmatrix}
\begin{array}{l}
\leftarrow \text{Terkontrol dan Terobservasi} \\
\leftarrow \text{Terkontrol dan Tak Terobservasi} \\
\leftarrow \text{Tak Terkontrol dan Terobservasi} \\
\leftarrow \text{Tak Terkontrol dan Tak Terobservasi}
\end{array}$$

Fungsi transfer input-output $G(s)$ **hanya merepresentasikan sub-ruang $x_{co}$**:
$$G(s) = C_{co} (sI - A_{co})^{-1} B_{co} + D$$

> **Teorema Realisasi Minimal & Pole-Zero Cancellation**:
> 1. Representasi ruang keadaan adalah **realisasi minimal** dari $G(s)$ jika dan hanya jika sistem bersifat **terkontrol dan terobservasi lengkap**.
> 2. Adanya **pembatalan kutub-pembuat nol (*pole-zero cancellation*)** pada fungsi transfer menyebabkan representasi ruang keadaan kehilangan sifat keterkontrolan, keterobservasian, atau keduanya.

---

## 9. Keterkontrolan & Keterobservasian Sistem Diskrit

Untuk sistem diskrit $x(k+1) = G x(k) + H u(k), \; y(k) = C x(k) + D u(k)$:

$$M_c = \begin{bmatrix} H & GH & G^2 H & \dots & G^{n-1} H \end{bmatrix} \in \mathbb{R}^{n \times nm}, \quad \operatorname{rank}(M_c) = n$$
$$M_o = \begin{bmatrix} C \\ CG \\ CG^2 \\ \vdots \\ CG^{n-1} \end{bmatrix} \in \mathbb{R}^{np \times n}, \quad \operatorname{rank}(M_o) = n$$

---

## 10. Contoh Soal & Pembahasan Komprehensif

### Contoh 1: Uji Keterkontrolan Berparameter
Diberikan sistem:
$$\dot{x} = \begin{bmatrix} 1 & 2 \\ -4 & -3 \end{bmatrix} x + \begin{bmatrix} 1 \\ 2 \end{bmatrix} u, \quad y = \begin{bmatrix} a & 1 \end{bmatrix} x$$

**Penyelesaian**:
1. **Keterkontrolan**:
   $$AB = \begin{bmatrix} 1 & 2 \\ -4 & -3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ -10 \end{bmatrix}$$
   Matriks keterkontrolan:
   $$M_c = \begin{bmatrix} 1 & 5 \\ 2 & -10 \end{bmatrix} \implies \det(M_c) = -10 - 10 = -20 \ne 0$$
   Sehingga $\operatorname{rank}(M_c) = 2$ (**Sistem Terkontrol Lengkap**).

2. **Keterobservasian**:
   $$CA = \begin{bmatrix} a & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ -4 & -3 \end{bmatrix} = \begin{bmatrix} a - 4 & 2a - 3 \end{bmatrix}$$
   Matriks keterobservasian:
   $$M_o = \begin{bmatrix} a & 1 \\ a - 4 & 2a - 3 \end{bmatrix}$$
   Determinan:
   $$\det(M_o) = a(2a - 3) - 1(a - 4) = 2a^2 - 4a + 4 = 2(a^2 - 2a + 2) = 2[(a-1)^2 + 1]$$
   Karena $(a-1)^2 + 1 > 0$ untuk setiap $a \in \mathbb{R}$, maka $\det(M_o) \ne 0$ untuk seluruh $a \in \mathbb{R}$.  
   Jadi sistem terobservasi lengkap untuk semua $a \in \mathbb{R}$.
