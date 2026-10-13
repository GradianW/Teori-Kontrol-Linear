# Lembar Latihan dan Pembahasan Lengkap
## Topik 02: Pemodelan Ruang Keadaan & Matriks Fundamental (Aspek Matematis Murni)
**Mata Kuliah:** MA4171 Teori Kontrol Linear --- FMIPA ITB

---

### **No. 1**

**Soal:**  
Diberikan persamaan diferensial linear invarian waktu (LTI) orde-3 dengan turunan pada fungsi masukan:
$$\dddot{y}(t) + 6\ddot{y}(t) + 11\dot{y}(t) + 6y(t) = 4\dot{u}(t) + 2u(t)$$
dengan seluruh kondisi awal diasumsikan bernilai nol pada $t = 0$.
(a) Tentukan fungsi transfer $G(s) = \frac{Y(s)}{U(s)}$ sistem tersebut.  
(b) Tentukan representasi ruang keadaan dalam Bentuk Kanonik Keterkontrolan (*Controllable Canonical Form*, CCF) menggunakan metode variabel perantara $Z(s)$.  
(c) Tentukan representasi ruang keadaan dalam Bentuk Kanonik Keterobservasian (*Observable Canonical Form*, OCF).

**Penyelesaian:**

**(a) Penentuan Fungsi Transfer**

Diberikan persamaan diferensial sistem:
$$\dddot{y}(t) + 6\ddot{y}(t) + 11\dot{y}(t) + 6y(t) = 4\dot{u}(t) + 2u(t)$$

Transformasi Laplace diterapkan secara linear pada kedua ruas persamaan diferensial:
$$\mathcal{L}\{\dddot{y}(t)\} + 6\mathcal{L}\{\ddot{y}(t)\} + 11\mathcal{L}\{\dot{y}(t)\} + 6\mathcal{L}\{y(t)\} = 4\mathcal{L}\{\dot{u}(t)\} + 2\mathcal{L}\{u(t)\}$$

Berdasarkan sifat transformasi Laplace untuk turunan waktu:
$$\mathcal{L}\{\dddot{y}(t)\} = s^3 Y(s) - s^2 y(0) - s \dot{y}(0) - \ddot{y}(0)$$
$$\mathcal{L}\{\ddot{y}(t)\} = s^2 Y(s) - s y(0) - \dot{y}(0)$$
$$\mathcal{L}\{\dot{y}(t)\} = s Y(s) - y(0)$$
$$\mathcal{L}\{y(t)\} = Y(s)$$
serta untuk fungsi masukan:
$$\mathcal{L}\{\dot{u}(t)\} = s U(s) - u(0)$$
$$\mathcal{L}\{u(t)\} = U(s)$$

Fungsi transfer sistem didefinisikan pada seluruh kondisi awal bernilai nol ($y(0) = 0$, $\dot{y}(0) = 0$, $\ddot{y}(0) = 0$, dan $u(0) = 0$), sehingga seluruh suku kondisi awal lenyap:
$$s^3 Y(s) + 6s^2 Y(s) + 11s Y(s) + 6Y(s) = 4s U(s) + 2U(s)$$

Variabel $Y(s)$ pada ruas kiri dan $U(s)$ pada ruas kanan difaktorkan ke luar:
$$(s^3 + 6s^2 + 11s + 6) Y(s) = (4s + 2) U(s)$$

Dengan membagi kedua ruas dengan polinomial karakteristik $(s^3 + 6s^2 + 11s + 6)$ dan membagi dengan $U(s)$, diperoleh fungsi transfer sistem:
$$G(s) = \frac{Y(s)}{U(s)} = \frac{4s + 2}{s^3 + 6s^2 + 11s + 6}$$

**(b) Konstruksi Bentuk Kanonik Keterkontrolan (CCF)**

Untuk memisahkan dinamika masukan dan keluaran secara sistematis tanpa melibatkan diferensiasi langsung dari sinyal kontrol $u(t)$, diperkenalkan suatu variabel perantara skalar $Z(s)$ sedemikian rupa sehingga:
$$Z(s) = \frac{U(s)}{s^3 + 6s^2 + 11s + 6} \implies (s^3 + 6s^2 + 11s + 6) Z(s) = U(s)$$
dan persamaan sinyal keluaran dinyatakan oleh pembilang fungsi transfer:
$$Y(s) = (4s + 2) Z(s) = 4s Z(s) + 2 Z(s)$$

Dalam domain waktu, persamaan diferensial untuk variabel perantara $z(t)$ berbentuk:
$$\dddot{z}(t) + 6\ddot{z}(t) + 11\dot{z}(t) + 6z(t) = u(t) \implies \dddot{z}(t) = -6z(t) - 11\dot{z}(t) - 6\ddot{z}(t) + u(t)$$

Variabel-variabel keadaan didefinisikan sebagai turunan berurutan dari variabel perantara:
$$x_1(t) = z(t), \quad x_2(t) = \dot{z}(t), \quad x_3(t) = \ddot{z}(t)$$

Diferensiasi terhadap waktu untuk masing-masing variabel keadaan menghasilkan persamaan ruang keadaan:
$$\dot{x}_1(t) = x_2(t)$$
$$\dot{x}_2(t) = x_3(t)$$
$$\dot{x}_3(t) = \dddot{z}(t) = -6x_1(t) - 11x_2(t) - 6x_3(t) + u(t)$$

Persamaan keluaran diperoleh melalui invers transformasi Laplace dari ekspresi $Y(s)$:
$$y(t) = 2z(t) + 4\dot{z}(t) = 2x_1(t) + 4x_2(t) + 0x_3(t)$$

Dalam notasi matriks standar $\dot{\mathbf{x}} = A\mathbf{x} + B u$ dan $y = C\mathbf{x} + D u$:
$$A_{ccf} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}, \quad B_{ccf} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
$$C_{ccf} = \begin{bmatrix} 2 & 4 & 0 \end{bmatrix}, \quad D_{ccf} = 0$$

**(c) Konstruksi Bentuk Kanonik Keterobservasian (OCF)**

Bentuk kanonik keterobservasian merupakan dual dari bentuk kanonik keterkontrolan. Koefisien-koefisien pembilang ditempatkan pada matriks masukan $B$, sedangkan koefisien penyebut ditempatkan pada kolom terakhir matriks sistem:
$$A_{ocf} = A_{ccf}^T = \begin{bmatrix} 0 & 0 & -6 \\ 1 & 0 & -11 \\ 0 & 1 & -6 \end{bmatrix}, \quad B_{ocf} = C_{ccf}^T = \begin{bmatrix} 2 \\ 4 \\ 0 \end{bmatrix}$$
$$C_{ocf} = B_{ccf}^T = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}, \quad D_{ocf} = 0$$

---

### **No. 2**

**Soal:**  
Diberikan fungsi transfer sistem kontinu berikut:
$$G(s) = \frac{3s + 7}{(s+1)(s+2)(s+3)}$$
(a) Uraikan fungsi transfer $G(s)$ ke dalam bentuk penjumlahan pecahan parsial.  
(b) Tentukan persamaan ruang keadaan dalam Bentuk Kanonik Diagonal (*Diagonal Canonical Form*, DCF).  
(c) Tuliskan persamaan diferensial untuk setiap variabel keadaan hasil dekomposisi tersebut dan jelaskan mengapa bentuk ini dinamakan ter-dekopel (*decoupled*).

**Penyelesaian:**

**(a) Dekomposisi Pecahan Parsial**

Penyebut fungsi transfer memiliki tiga kutub riil yang saling berbeda, yaitu $s = -1$, $s = -2$, dan $s = -3$. Fungsi transfer dapat diuraikan menjadi:
$$G(s) = \frac{R_1}{s+1} + \frac{R_2}{s+2} + \frac{R_3}{s+3}$$

Masing-masing residu dihitung menggunakan metode penutupan (*Heaviside cover-up method*):
Residu pertama pada kutub $s = -1$:
$$R_1 = \lim_{s \to -1} (s+1) G(s) = \left. \frac{3s + 7}{(s+2)(s+3)} \right|_{s=-1} = \frac{3(-1) + 7}{(-1+2)(-1+3)} = \frac{4}{(1)(2)} = 2$$

Residu kedua pada kutub $s = -2$:
$$R_2 = \lim_{s \to -2} (s+2) G(s) = \left. \frac{3s + 7}{(s+1)(s+3)} \right|_{s=-2} = \frac{3(-2) + 7}{(-2+1)(-2+3)} = \frac{1}{(-1)(1)} = -1$$

Residu ketiga pada kutub $s = -3$:
$$R_3 = \lim_{s \to -3} (s+3) G(s) = \left. \frac{3s + 7}{(s+1)(s+2)} \right|_{s=-3} = \frac{3(-3) + 7}{(-3+1)(-3+2)} = \frac{-2}{(-2)(-1)} = -1$$

Dengan demikian, bentuk pecahan parsial fungsi transfer adalah:
$$G(s) = \frac{2}{s+1} - \frac{1}{s+2} - \frac{1}{s+3}$$

**(b) Penyusunan Bentuk Kanonik Diagonal (DCF)**

Didefinisikan variabel keadaan dalam domain Laplace untuk masing-masing moda eigen sebagai:
$$X_1(s) = \frac{1}{s+1} U(s), \quad X_2(s) = \frac{1}{s+2} U(s), \quad X_3(s) = \frac{1}{s+3} U(s)$$

Sinyal keluaran $Y(s) = G(s) U(s)$ dinyatakan sebagai kombinasi linear dari variabel keadaan:
$$Y(s) = 2 X_1(s) - X_2(s) - X_3(s)$$

Transformasi balik ke domain waktu menghasilkan sistem matriks diagonal:
$$A_{diag} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}, \quad B_{diag} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$
$$C_{diag} = \begin{bmatrix} 2 & -1 & -1 \end{bmatrix}, \quad D_{diag} = 0$$

**(c) Karakteristik Ter-dekopel**

Persamaan diferensial untuk masing-masing variabel keadaan adalah:
$$\dot{x}_1(t) = -x_1(t) + u(t)$$
$$\dot{x}_2(t) = -2x_2(t) + u(t)$$
$$\dot{x}_3(t) = -3x_3(t) + u(t)$$

Sistem ini disebut ter-dekopel (*decoupled*) karena laju perubahan dari setiap variabel keadaan $\dot{x}_i(t)$ hanya bergantung secara eksklusif pada dirinya sendiri $x_i(t)$ dan masukan luar $u(t)$, tanpa adanya interaksi atau ketergantungan silang dengan variabel keadaan lainnya ($x_j(t)$ untuk $j \ne i$).

---

### **No. 3**

**Soal:**  
Diberikan fungsi transfer dengan kutub berulang (multiplisitas 3):
$$G(s) = \frac{2s^2 + 5s + 4}{(s+1)^3}$$
(a) Uraikan fungsi transfer $G(s)$ ke dalam basis pecahan parsial dengan penyebut perpangkatan $(s+1)$.  
(b) Susun representasi ruang keadaan sistem dalam Bentuk Kanonik Jordan (*Jordan Canonical Form*, JCF) di mana matriks sistem memuat satu blok Jordan tunggal.  
(c) Verifikasi kebenaran matriks ruang keadaan yang diperoleh dengan menghitung kembali fungsi transfer $G(s) = C(sI - A)^{-1} B$.

**Penyelesaian:**

**(a) Ekspansi Pecahan Parsial Basis $(s+1)$**

Polinomial pembilang dinyatakan dalam variabel pergeseran $p = s + 1 \implies s = p - 1$:
$$2s^2 + 5s + 4 = 2(p - 1)^2 + 5(p - 1) + 4 = 2(p^2 - 2p + 1) + 5p - 5 + 4 = 2p^2 + p + 1$$

Dengan mengembalikan substitusi $p = s + 1$, diperoleh bentuk pembilang:
$$2s^2 + 5s + 4 = 2(s+1)^2 + (s+1) + 1$$

Pembagian setiap suku dengan penyebut $(s+1)^3$ menghasilkan ekspansi pecahan parsial:
$$G(s) = \frac{2(s+1)^2}{(s+1)^3} + \frac{s+1}{(s+1)^3} + \frac{1}{(s+1)^3} = \frac{2}{s+1} + \frac{1}{(s+1)^2} + \frac{1}{(s+1)^3}$$

**(b) Penyusunan Bentuk Kanonik Jordan (JCF)**

Untuk membentuk satu blok Jordan berordo $3 \times 3$, rantai variabel keadaan didefinisikan secara bertingkat:
$$X_3(s) = \frac{1}{s+1} U(s) \implies (s+1) X_3(s) = U(s)$$
$$X_2(s) = \frac{1}{s+1} X_3(s) = \frac{1}{(s+1)^2} U(s) \implies (s+1) X_2(s) = X_3(s)$$
$$X_1(s) = \frac{1}{s+1} X_2(s) = \frac{1}{(s+1)^3} U(s) \implies (s+1) X_1(s) = X_2(s)$$

Dalam domain waktu, sistem diferensial bertingkat tersebut menjadi:
$$\dot{x}_1(t) = -x_1(t) + x_2(t)$$
$$\dot{x}_2(t) = -x_2(t) + x_3(t)$$
$$\dot{x}_3(t) = -x_3(t) + u(t)$$

Persamaan keluaran dinyatakan sesuai ekspansi pecahan parsial:
$$Y(s) = X_1(s) + X_2(s) + 2X_3(s) \implies y(t) = x_1(t) + x_2(t) + 2x_3(t)$$

Matriks ruang keadaan dalam bentuk blok Jordan adalah:
$$A_J = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{bmatrix}, \quad B_J = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
$$C_J = \begin{bmatrix} 1 & 1 & 2 \end{bmatrix}, \quad D_J = 0$$

**(c) Verifikasi Fungsi Transfer**

Matriks karakteristik $(sI - A_J)$ adalah matriks segitiga atas:
$$sI - A_J = \begin{bmatrix} s+1 & -1 & 0 \\ 0 & s+1 & -1 \\ 0 & 0 & s+1 \end{bmatrix}$$

Invers matriks segitiga atas dihitung secara langsung:
$$(sI - A_J)^{-1} = \begin{bmatrix} \frac{1}{s+1} & \frac{1}{(s+1)^2} & \frac{1}{(s+1)^3} \\ 0 & \frac{1}{s+1} & \frac{1}{(s+1)^2} \\ 0 & 0 & \frac{1}{s+1} \end{bmatrix}$$

Perkalian resolven dengan vektor masukan $B_J$ mengekstraksi kolom ketiga:
$$(sI - A_J)^{-1} B_J = \begin{bmatrix} \frac{1}{(s+1)^3} \\ \frac{1}{(s+1)^2} \\ \frac{1}{s+1} \end{bmatrix}$$

Perkalian dengan vektor baris keluaran $C_J$ menghasilkan:
$$G(s) = C_J (sI - A_J)^{-1} B_J = \begin{bmatrix} 1 & 1 & 2 \end{bmatrix} \begin{bmatrix} \frac{1}{(s+1)^3} \\ \frac{1}{(s+1)^2} \\ \frac{1}{s+1} \end{bmatrix} = \frac{1}{(s+1)^3} + \frac{1}{(s+1)^2} + \frac{2}{s+1} = \frac{2s^2 + 5s + 4}{(s+1)^3}$$
Hasil verifikasi tepat identik dengan fungsi transfer awal.

---

### **No. 4**

**Soal:**  
Suatu sistem dinamik linear didefinisikan oleh matriks ruang keadaan:
$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix}, \quad D = 0$$
(a) Hitung determinan $\det(sI - A)$ dan matriks adjoin $\operatorname{adj}(sI - A)$.  
(b) Tentukan fungsi transfer $G(s) = C(sI - A)^{-1} B + D$.  
(c) Identifikasi apakah terdapat pembatalan faktor persekutuan (*pole-zero cancellation*) pada fungsi transfer yang dihasilkan.

**Penyelesaian:**

**(a) Perhitungan Determinan dan Matriks Adjoin**

Dibentuk matriks $(sI - A)$:
$$sI - A = \begin{bmatrix} s & -1 & 0 \\ 0 & s & -1 \\ 6 & 11 & s+6 \end{bmatrix}$$

Determinan dihitung melalui ekspansi baris pertama:
$$\det(sI - A) = s [s^2 + 6s + 11] + [6] = s^3 + 6s^2 + 11s + 6 = (s+1)(s+2)(s+3)$$

Matriks adjoin dihitung melalui transpose matriks kofaktor:
$$\operatorname{adj}(sI - A) = \begin{bmatrix} s^2+6s+11 & s+6 & 1 \\ -6 & s(s+6) & s \\ -6s & -(11s+6) & s^2 \end{bmatrix}$$

**(b) Penentuan Fungsi Transfer**

Dihitung perkalian vektor baris $C$ dengan matriks adjoin:
$$C \operatorname{adj}(sI - A) = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} s^2+6s+11 & s+6 & 1 \\ -6 & s^2+6s & s \\ -6s & -(11s+6) & s^2 \end{bmatrix} = \begin{bmatrix} s^2+6s+5 & s^2+7s+6 & s+1 \end{bmatrix}$$

Setiap elemen memiliki faktor persekutuan $(s+1)$:
$$C \operatorname{adj}(sI - A) = (s+1) \begin{bmatrix} s+5 & s+6 & 1 \end{bmatrix}$$

Dikalikan dengan vektor kolom masukan $B$:
$$C \operatorname{adj}(sI - A) B = (s+1) [0(s+5) + 1(s+6) + 2(1)] = (s+1)(s + 8)$$

Fungsi transfer sistem adalah:
$$G(s) = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} = \frac{(s+1)(s+8)}{(s+1)(s+2)(s+3)}$$

**(c) Pembatalan Faktor Persekutuan (*Pole-Zero Cancellation*)**

Faktor $(s+1)$ muncul pada pembilang dan penyebut sehingga saling membatalkan:
$$G(s) = \frac{s + 8}{(s+2)(s+3)} = \frac{s + 8}{s^2 + 5s + 6}$$

---

### **No. 5**

**Soal:**  
Diberikan matriks dinamika sistem LTI kontinu orde-2:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$$
(a) Tentukan matriks resolven $(sI - A)^{-1}$ dalam domain frekuensi kompleks $s$.  
(b) Dengan menerapkan invers transformasi Laplace elemen demi elemen, tentukan matriks fundamental (matriks transisi keadaan) $\Phi(t) = e^{At}$.  
(c) Verifikasi sifat-sifat identitas matriks fundamental: $\Phi(0) = I$ dan $\left.\frac{d}{dt}\Phi(t)\right|_{t=0} = A$.

**Penyelesaian:**

**(a) Penentuan Matriks Resolven**

Matriks $(sI - A)$:
$$sI - A = \begin{bmatrix} s & -1 \\ 2 & s+3 \end{bmatrix} \implies \det(sI - A) = s^2 + 3s + 2 = (s+1)(s+2)$$

Matriks invers:
$$(sI - A)^{-1} = \frac{1}{(s+1)(s+2)} \begin{bmatrix} s+3 & 1 \\ -2 & s \end{bmatrix}$$

**(b) Invers Transformasi Laplace Elemen demi Elemen**

Uraian pecahan parsial masing-masing elemen:
- Baris 1, Kolom 1: $\frac{s+3}{(s+1)(s+2)} = \frac{2}{s+1} - \frac{1}{s+2} \implies 2e^{-t} - e^{-2t}$
- Baris 1, Kolom 2: $\frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2} \implies e^{-t} - e^{-2t}$
- Baris 2, Kolom 1: $\frac{-2}{(s+1)(s+2)} = \frac{-2}{s+1} + \frac{2}{s+2} \implies -2e^{-t} + 2e^{-2t}$
- Baris 2, Kolom 2: $\frac{s}{(s+1)(s+2)} = \frac{-1}{s+1} + \frac{2}{s+2} \implies -e^{-t} + 2e^{-2t}$

Diperoleh matriks fundamental untuk $t \ge 0$:
$$\Phi(t) = e^{At} = \begin{bmatrix} 2e^{-t} - e^{-2t} & e^{-t} - e^{-2t} \\ -2e^{-t} + 2e^{-2t} & -e^{-t} + 2e^{-2t} \end{bmatrix}$$

**(c) Verifikasi Sifat Identitas**

Evaluasi pada $t = 0$:
$$\Phi(0) = \begin{bmatrix} 2 - 1 & 1 - 1 \\ -2 + 2 & -1 + 2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$

Turunan pertama terhadap waktu dievaluasi pada $t = 0$:
$$\left.\frac{d}{dt}\Phi(t)\right|_{t=0} = \begin{bmatrix} -2 + 2 & -1 + 2 \\ 2 - 4 & 1 - 4 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} = A$$

---

### **No. 6**

**Soal:**  
Diberikan matriks sistem yang memiliki nilai eigen berulang dan membentuk blok Jordan:
$$A = \begin{bmatrix} -2 & 1 \\ 0 & -2 \end{bmatrix}$$
(a) Tentukan matriks fundamental $e^{At}$ menggunakan metode transformasi Laplace $\mathcal{L}^{-1}\{(sI - A)^{-1}\}$.  
(b) Hitung kembali matriks fundamental $e^{At}$ menggunakan dekomposisi matriks nilpoten $A = \lambda I + N$ dan ekspansi deret Taylor matriks eksponensial.  
(c) Bandingkan kedua hasil yang diperoleh.

**Penyelesaian:**

**(a) Metode Transformasi Laplace**

$$(sI - A)^{-1} = \begin{bmatrix} s+2 & -1 \\ 0 & s+2 \end{bmatrix}^{-1} = \begin{bmatrix} \frac{1}{s+2} & \frac{1}{(s+2)^2} \\ 0 & \frac{1}{s+2} \end{bmatrix}$$

Invers transformasi Laplace:
$$e^{At} = \begin{bmatrix} e^{-2t} & t e^{-2t} \\ 0 & e^{-2t} \end{bmatrix}$$

**(b) Metode Dekomposisi Matriks Nilpoten**

$$A = (-2I) + N, \quad N = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$$
Karena $N^2 = 0$, ekspansi deret Taylor terpotong:
$$e^{Nt} = I + N t = \begin{bmatrix} 1 & t \\ 0 & 1 \end{bmatrix}$$
Sehingga:
$$e^{At} = e^{-2I t} e^{Nt} = e^{-2t} \begin{bmatrix} 1 & t \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} e^{-2t} & t e^{-2t} \\ 0 & e^{-2t} \end{bmatrix}$$

**(c) Perbandingan Hasil**

Kedua metode menghasilkan matriks eksponensial yang identik, membuktikan bahwa kemunculan faktor linear $t$ merupakan akibat langsung dari superdiagonal blok Jordan.

---

### **No. 7**

**Soal:**  
Diberikan sistem LTI kontinu orde-2:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}(t)$$
dengan kondisi awal $\mathbf{x}(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ dan sinyal masukan berupa fungsi tangga satuan $u(t) = 1$ untuk seluruh $t \ge 0$.
(a) Tentukan respon masukan-nol (*Zero-Input Response*, ZIR) keadaan $\mathbf{x}_{ZIR}(t)$.  
(b) Tentukan respon keadaan-nol (*Zero-State Response*, ZSR) keadaan $\mathbf{x}_{ZSR}(t)$ melalui integral konvolusi transisi keadaan.  
(c) Tentukan solusi respon keadaan total $\mathbf{x}(t) = \mathbf{x}_{ZIR}(t) + \mathbf{x}_{ZSR}(t)$ dan tentukan respon keluaran sistem $y(t)$.

**Penyelesaian:**

**(a) Respon Masukan-Nol (ZIR)**

$$\mathbf{x}_{ZIR}(t) = e^{At} \mathbf{x}(0) = \begin{bmatrix} 2e^{-t} - e^{-2t} & e^{-t} - e^{-2t} \\ -2e^{-t} + 2e^{-2t} & -e^{-t} + 2e^{-2t} \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2e^{-t} - e^{-2t} \\ -2e^{-t} + 2e^{-2t} \end{bmatrix}$$

**(b) Respon Keadaan-Nol (ZSR)**

$$\mathbf{x}_{ZSR}(t) = \int_0^t e^{A(t-\tau)} B (1) \, d\tau = \int_0^t \begin{bmatrix} e^{-(t-\tau)} - e^{-2(t-\tau)} \\ -e^{-(t-\tau)} + 2e^{-2(t-\tau)} \end{bmatrix} d\tau = \begin{bmatrix} \frac{1}{2} - e^{-t} + \frac{1}{2}e^{-2t} \\ e^{-t} - e^{-2t} \end{bmatrix}$$

**(c) Respon Keadaan Total dan Respon Keluaran**

$$\mathbf{x}(t) = \mathbf{x}_{ZIR}(t) + \mathbf{x}_{ZSR}(t) = \begin{bmatrix} \frac{1}{2} + e^{-t} - \frac{1}{2}e^{-2t} \\ -e^{-t} + e^{-2t} \end{bmatrix}$$
$$y(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}(t) = x_1(t) = \frac{1}{2} + e^{-t} - \frac{1}{2}e^{-2t}$$
Nilai tunak saat $t \to \infty$ adalah $y(\infty) = \frac{1}{2}$.

---

### **No. 8**

**Soal:**  
Diberikan matriks sistem berorde $3 \times 3$:
$$A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix}$$
(a) Tentukan nilai-nilai eigen dari matriks $A$.  
(b) Dengan menggunakan Teorema Cayley-Hamilton, nyatakan matriks fundamental dalam bentuk kombinasi kuadratik $e^{At} = \alpha_0(t) I + \alpha_1(t) A + \alpha_2(t) A^2$.  
(c) Tentukan fungsi koefisien skalar $\alpha_0(t), \alpha_1(t), \alpha_2(t)$ dan tuliskan matriks fundamental $e^{At}$ secara eksplisit.

**Penyelesaian:**

**(a) Nilai-Nilai Eigen**

Karena matriks $A$ merupakan segitiga blok bawah, nilai eigen adalah entri diagonal utamanya:
$$\lambda_1 = 1, \quad \lambda_2 = -1, \quad \lambda_3 = -2$$

**(b) Formulasi Teorema Cayley-Hamilton**

$$e^{\lambda t} = \alpha_0(t) + \alpha_1(t)\lambda + \alpha_2(t)\lambda^2$$
- Untuk $\lambda_1 = 1$: $e^t = \alpha_0 + \alpha_1 + \alpha_2$
- Untuk $\lambda_2 = -1$: $e^{-t} = \alpha_0 - \alpha_1 + \alpha_2$
- Untuk $\lambda_3 = -2$: $e^{-2t} = \alpha_0 - 2\alpha_1 + 4\alpha_2$

**(c) Penentuan Koefisien dan Matriks Fundamental**

Penyelesaian sistem persamaan linier tersebut memberikan:
$$\alpha_1(t) = \frac{e^t - e^{-t}}{2} = \sinh(t)$$
$$\alpha_2(t) = \frac{e^t - 3e^{-t} + 2e^{-2t}}{6}$$
$$\alpha_0(t) = \frac{e^t + 9e^{-t} - 4e^{-2t}}{6}$$

Substitusi ke dalam $e^{At} = \alpha_0 I + \alpha_1 A + \alpha_2 A^2$ menghasilkan:
$$e^{At} = \begin{bmatrix} e^t & 0 & 0 \\ e^t - e^{-t} & e^{-t} & e^{-t} - e^{-2t} \\ 0 & 0 & e^{-2t} \end{bmatrix}$$

---

### **No. 9**

**Soal:**  
Diberikan sistem kendali lup tertutup dengan dua lup umpan balik bersarang:
(a) Reduksi lup umpan balik bagian dalam yang melibatkan blok $G_1(s)$ dan $H_1(s)$.  
(b) Tentukan fungsi transfer lingkar tertutup total $T(s) = \frac{Y(s)}{R(s)}$ menggunakan aljabar diagram blok.

**Penyelesaian:**

**(a) Reduksi Lup Umpan Balik Bagian Dalam**

Lup dalam dengan umpan balik negatif memiliki fungsi transfer ekuivalen:
$$G_{in}(s) = \frac{G_1(s)}{1 + G_1(s) H_1(s)}$$
Hubungan kaskade dengan $G_2(s)$:
$$G_{fwd}(s) = G_{in}(s) \cdot G_2(s) = \frac{G_1(s) G_2(s)}{1 + G_1(s) H_1(s)}$$

**(b) Reduksi Lup Umpan Balik Luar dan Fungsi Transfer Total**

Lup luar dengan umpan balik negatif $H_2(s)$:
$$T(s) = \frac{G_{fwd}(s)}{1 + G_{fwd}(s) H_2(s)} = \frac{\frac{G_1(s) G_2(s)}{1 + G_1(s) H_1(s)}}{1 + \left( \frac{G_1(s) G_2(s)}{1 + G_1(s) H_1(s)} \right) H_2(s)}$$
Dikalikan $(1 + G_1(s) H_1(s))$ pada pembilang dan penyebut:
$$T(s) = \frac{Y(s)}{R(s)} = \frac{G_1(s) G_2(s)}{1 + G_1(s) H_1(s) + G_1(s) G_2(s) H_2(s)}$$

---

### **No. 10**

**Soal:**  
Diberikan diagram aliran sinyal (*Signal Flow Graph*, SFG) dengan:
- Lintasan maju $P_1 = G_1 G_2$ dan lintasan pintas $P_2 = G_3$.
- Loop $L_1 = -H_1$, $L_2 = -H_2$, $L_3 = -G_2 H_3$.
- Loop $L_1$ dan $L_2$ tidak bersentuhan; loop $L_1$ dan $L_3$ tidak bersentuhan.
(a) Tentukan seluruh lintasan maju dan penguatannya.  
(b) Tentukan seluruh loop tunggal dan pasangan loop non-touching.  
(c) Hitung determinan graf $\Delta$ dan kofaktor lintasan $\Delta_k$.  
(d) Tentukan fungsi transfer total $\frac{Y(s)}{R(s)}$ menggunakan Aturan Penguatan Mason.

**Penyelesaian:**

**(a) Lintasan Maju**
$$P_1 = G_1 G_2, \quad P_2 = G_3$$

**(b) Loop Tunggal dan Pasangan Non-Touching**
$$L_1 = -H_1, \quad L_2 = -H_2, \quad L_3 = -G_2 H_3$$
Pasangan non-touching:
$$L_1 L_2 = H_1 H_2, \quad L_1 L_3 = G_2 H_1 H_3$$

**(c) Determinan Graf dan Kofaktor**
$$\Delta = 1 - (L_1 + L_2 + L_3) + (L_1 L_2 + L_1 L_3) = 1 + H_1 + H_2 + G_2 H_3 + H_1 H_2 + G_2 H_1 H_3$$
- $\Delta_1 = 1$ (lintasan $P_1$ menyentuh semua loop).
- $\Delta_2 = 1 - L_2 = 1 + H_2$ (lintasan $P_2$ tidak menyentuh loop $L_2$).

**(d) Fungsi Transfer Total via Aturan Mason**
$$\frac{Y(s)}{R(s)} = \frac{P_1 \Delta_1 + P_2 \Delta_2}{\Delta} = \frac{G_1 G_2 + G_3 (1 + H_2)}{1 + H_1 + H_2 + G_2 H_3 + H_1 H_2 + G_2 H_1 H_3}$$

---

### **No. 11**

**Soal:**  
Diberikan sistem multivariabel matematis:
(a) Sistem SIMO: $\mathbf{G}_{SIMO}(s) = \frac{1}{s^2 + 5s + 6} \begin{bmatrix} 2s + 1 \\ 3s + 4 \end{bmatrix}$. Tentukan representasi ruang keadaan CCF bersama.  
(b) Sistem MISO: $\mathbf{G}_{MISO}(s) = \frac{1}{s^2 + 4s + 3} \begin{bmatrix} s + 2 & 5 \end{bmatrix}$. Tentukan representasi ruang keadaan OCF bersama.

**Penyelesaian:**

**(a) CCF Bersama (SIMO)**

$$A = \begin{bmatrix} 0 & 1 \\ -6 & -5 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}, \quad D = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

**(b) OCF Bersama (MISO)**

$$A = \begin{bmatrix} 0 & -3 \\ 1 & -4 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 5 \\ 1 & 0 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 1 \end{bmatrix}, \quad D = \begin{bmatrix} 0 & 0 \end{bmatrix}$$

---

### **No. 12**

**Soal:**  
Diberikan sistem ruang keadaan kontinu:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 \\ 1 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 2 & 1 \end{bmatrix} \mathbf{x}(t)$$
(a) Tentukan nilai eigen dan matriks modal $P$ yang mendiagonalkan matriks $A$.  
(b) Lakukan transformasi keserupaan dengan $\mathbf{z}(t) = P^{-1}\mathbf{x}(t)$ untuk memperoleh $(\tilde{A}, \tilde{B}, \tilde{C}, \tilde{D})$.  
(c) Buktikan bahwa fungsi transfer sistem bernilai invarian di bawah transformasi tersebut.

**Penyelesaian:**

**(a) Nilai Eigen dan Matriks Modal**

$$\lambda_1 = 1 \implies \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \lambda_2 = 3 \implies \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
$$P = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \quad P^{-1} = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}$$

**(b) Transformasi Keserupaan**

$$\tilde{A} = P^{-1} A P = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix}$$
$$\tilde{B} = P^{-1} B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$
$$\tilde{C} = C P = \begin{bmatrix} 2 & 3 \end{bmatrix}, \quad \tilde{D} = 0$$

**(c) Pembuktian Invariansi Fungsi Transfer**

- Sistem Asli:
  $$G(s) = C(sI - A)^{-1} B = \begin{bmatrix} 2 & 1 \end{bmatrix} \begin{bmatrix} \frac{1}{s-3} \\ \frac{1}{s-3} \end{bmatrix} = \frac{3}{s-3}$$
- Sistem Transformasi:
  $$\tilde{G}(s) = \tilde{C}(sI - \tilde{A})^{-1} \tilde{B} = \begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0 \\ \frac{1}{s-3} \end{bmatrix} = \frac{3}{s-3}$$

Terbukti $\tilde{G}(s) \equiv G(s) = \frac{3}{s-3}$.
