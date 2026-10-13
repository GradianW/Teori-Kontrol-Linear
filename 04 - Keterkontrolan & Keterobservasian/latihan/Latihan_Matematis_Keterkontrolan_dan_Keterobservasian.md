# Lembar Latihan dan Pembahasan Lengkap
## Topik 04: Keterkontrolan & Keterobservasian Sistem Dinamik Kontinu
**Mata Kuliah:** MA4171 Teori Kontrol Linear --- FMIPA ITB

---

### **No. 1**

**Soal:**  
Diberikan sistem LTI kontinu orde-3 dengan representasi ruang keadaan:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & -5 & -4 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} u(t)$$
(a) Hitung vektor-vektor kolom $AB$ dan $A^2 B$.  
(b) Susun matriks keterkontrolan Kalman $\mathcal{C}$ dan hitung nilai determinannya.  
(c) Tentukan apakah sistem tersebut terkontrol penuh (*controllable*).  
(d) Berdasarkan Teorema Cayley-Hamilton, jelaskan mengapa uji rank matriks keterkontrolan cukup dievaluasi hingga perpangkatan matriks $A^{n-1} B$.

**Penyelesaian:**

**(a) Perhitungan Vektor Kolom $AB$ dan $A^2 B$**

Perkalian matriks dinamika $A$ dengan vektor masukan $B$:
$$AB = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & -5 & -4 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ -9 \end{bmatrix}$$

Perkalian berikutnya untuk memperoleh $A^2 B$:
$$A^2 B = A(AB) = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & -5 & -4 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -9 \end{bmatrix} = \begin{bmatrix} 1 \\ -9 \\ 29 \end{bmatrix}$$

**(b) Konstruksi Matriks Keterkontrolan dan Perhitungan Determinan**

Matriks keterkontrolan Kalman untuk sistem orde $n = 3$ disusun dari kolom-kolom $[B \;\; AB \;\; A^2 B]$:
$$\mathcal{C} = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 1 & -9 \\ 1 & -9 & 29 \end{bmatrix}$$

Determinan matriks $\mathcal{C}$ dievaluasi melalui ekspansi kofaktor sepanjang baris pertama:
$$\det(\mathcal{C}) = -1(29 - (-9)) + 1(-9 - 1) = -38 - 10 = -48$$

**(c) Kesimpulan Keterkontrolan Sistem**

Karena $\det(\mathcal{C}) = -48 \ne 0$, matriks $\mathcal{C}$ berderajat penuh:
$$\text{rank}(\mathcal{C}) = 3 = n$$
Berdasarkan Kriteria Rank Kalman, sistem terbukti **terkontrol penuh (*controllable*)**.

**(d) Justifikasi Berdasarkan Teorema Cayley-Hamilton**

Polinomial karakteristik matriks $A$ berderajat 3 dinyatakan oleh:
$$p(\lambda) = \det(\lambda I - A) = \lambda^3 + 4\lambda^2 + 5\lambda + 2$$
Berdasarkan Teorema Cayley-Hamilton, setiap matriks bujursangkar memenuhi persamaan karakteristiknya sendiri:
$$A^3 + 4A^2 + 5A + 2I = 0 \implies A^3 = -4A^2 - 5A - 2I$$
Jika kedua ruas dikalikan dengan vektor $B$:
$$A^3 B = -4A^2 B - 5AB - 2B$$
Vektor kolom $A^3 B$ merupakan kombinasi linear dari kolom-kolom $B, AB,$ dan $A^2 B$. Secara induksi matematis, untuk setiap $k \ge n$, suku $A^k B$ selalu berada di dalam ruang rentang linear (*column space*) yang dibentuk oleh $\{B, AB, \dots, A^{n-1}B\}$, sehingga kolom-kolom dengan pangkat yang lebih tinggi tidak akan pernah menambah rank dari matriks keterkontrolan.

---

### **No. 2**

**Soal:**  
Diberikan sistem LTI kontinu orde-3 dengan matriks dinamika $A$ dan matriks keluaran $C$ sebagai berikut:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix} \mathbf{x}(t), \quad y(t) = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix} \mathbf{x}(t)$$
(a) Hitung vektor-vektor baris $CA$ dan $CA^2$.  
(b) Susun matriks keterobservasian Kalman $\mathcal{O}$ dan hitung determinannya.  
(c) Tentukan apakah sistem tersebut terobservasi penuh (*observable*).  
(d) Tentukan ruang nol (*unobservable subspace*) dari matriks $\mathcal{O}$ dan jelaskan interpretasi fisisnya.

**Penyelesaian:**

**(a) Perhitungan Vektor Baris $CA$ dan $CA^2$**

Perkalian matriks keluaran $C$ dengan matriks sistem $A$:
$$CA = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 2 & -2 \end{bmatrix}$$

Perkalian baris berikutnya untuk memperoleh $CA^2$:
$$CA^2 = (CA)A = \begin{bmatrix} 1 & 2 & -2 \end{bmatrix} \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 6 \end{bmatrix}$$

**(b) Konstruksi Matriks Keterobservasian dan Perhitungan Determinan**

Matriks keterobservasian Kalman $\mathcal{O}$ dibentuk dari tumpukan vektor baris:
$$\mathcal{O} = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 2 & -2 \\ 1 & 0 & 6 \end{bmatrix}$$

Determinannya dievaluasi sepanjang kolom kedua:
$$\det(\mathcal{O}) = 2(6 - 1) = 10$$

**(c) Kesimpulan Keterobservasian Sistem**

Karena $\det(\mathcal{O}) = 10 \ne 0$, matriks memiliki rank penuh:
$$\text{rank}(\mathcal{O}) = 3 = n$$
Berdasarkan Kriteria Rank Kalman, sistem terbukti **terobservasi penuh (*observable*)**.

**(d) Ruang Nol (*Unobservable Subspace*)**

Ruang nol dari matriks keterobservasian didefinisikan sebagai himpunan seluruh vektor keadaan $\mathbf{x}$ yang menghasilkan keluaran nol identik ketika masukan nol:
$$\text{Ker}(\mathcal{O}) = \{ \mathbf{x} \in \mathbb{R}^3 \mid \mathcal{O}\mathbf{x} = \mathbf{0} \} = \{ \mathbf{0} \}$$
Secara fisis, dimensi subruang tak-terobservasi adalah 0, yang menegaskan bahwa tidak ada lintasan keadaan tak-nol dalam sistem yang tersembunyi dari pengamatan sinyal keluaran $y(t)$. Setiap perubahan pada seluruh variabel keadaan dapat dideteksi dan direkonstruksi dari sinyal keluaran.

---

### **No. 3**

**Soal:**  
Diberikan sistem LTI kontinu orde-2 yang memuat parameter skalar $\alpha$ dan $\beta$:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & \alpha \\ 0 & 2 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 \\ \beta \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 1 \end{bmatrix} \mathbf{x}(t)$$
(a) Tentukan matriks keterkontrolan $\mathcal{C}(\alpha, \beta)$ dan hitung determinannya sebagai fungsi dari $\alpha$ dan $\beta$.  
(b) Tentukan syarat perlu dan cukup pada nilai parameter $\alpha$ dan $\beta$ agar sistem terkontrol penuh.  
(c) Tentukan matriks keterobservasian $\mathcal{O}(\alpha)$ dan tentukan nilai parameter $\alpha$ yang menyebabkan sistem kehilangan sifat keterobservasiannya.  
(d) Berikan interpretasi geometris dari hilangnya keterkontrolan saat $\beta = 0$.

**Penyelesaian:**

**(a) Matriks Keterkontrolan dan Determinan**

$$AB = \begin{bmatrix} 1 & \alpha \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ \beta \end{bmatrix} = \begin{bmatrix} 1 + \alpha \beta \\ 2\beta \end{bmatrix}$$
$$\mathcal{C}(\alpha, \beta) = \begin{bmatrix} 1 & 1 + \alpha\beta \\ \beta & 2\beta \end{bmatrix}$$
$$\det(\mathcal{C}) = 2\beta - \beta(1 + \alpha\beta) = \beta(1 - \alpha\beta)$$

**(b) Syarat Keterkontrolan Penuh**

Sistem berorde $n = 2$ terkontrol penuh jika dan hanya jika $\det(\mathcal{C}) \ne 0$:
$$\det(\mathcal{C}) \ne 0 \iff \beta \ne 0 \quad \text{dan} \quad \alpha\beta \ne 1$$
Sistem kehilangan keterkontrolan jika $\beta = 0$ atau $\beta = \frac{1}{\alpha}$ (untuk $\alpha \ne 0$).

**(c) Matriks Keterobservasian dan Nilai Singular $\alpha$**

$$CA = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & \alpha \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 1 & \alpha + 2 \end{bmatrix}$$
$$\mathcal{O}(\alpha) = \begin{bmatrix} 1 & 1 \\ 1 & \alpha + 2 \end{bmatrix} \implies \det(\mathcal{O}) = (\alpha + 2) - 1 = \alpha + 1$$
Sistem kehilangan sifat keterobservasian jika:
$$\det(\mathcal{O}) = 0 \iff \alpha = -1$$
Untuk seluruh $\alpha \ne -1$, sistem bersifat terobservasi penuh.

**(d) Interpretasi Geometris Kasus $\beta = 0$**

Saat $\beta = 0$, persamaan diferensial untuk variabel keadaan kedua berbentuk $\dot{x}_2(t) = 2x_2(t)$. Sinyal masukan $u(t)$ sama sekali tidak memiliki jalur pengaruh ke dalam variabel keadaan $x_2(t)$. Ruang keadaan yang dapat dicapai (*reachable subspace*) tereduksi menjadi garis horizontal sumbu-$x_1$, yaitu $\text{span}\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right\}$. Karena dimensinya hanya 1 (kurang dari dimensi ruang keadaan total $n = 2$), keadaan $x_2$ tidak dapat dikendalikan dari luar, sehingga sistem tak-terkontrol.

---

### **No. 4**

**Soal:**  
Diberikan sistem LTI kontinu yang matriks dinamikanya telah berada dalam bentuk diagonal terdekopel dengan nilai eigen riil distingtif:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 3 & 0 \end{bmatrix} \mathbf{x}(t)$$
(a) Ujilah keterkontrolan setiap mode eigen menggunakan Kriteria Gilbert untuk matriks diagonal.  
(b) Ujilah keterobservasian setiap mode eigen menggunakan Kriteria Gilbert untuk matriks diagonal.  
(c) Tentukan klasifikasi keempat subruang keadaan Kalman untuk masing-masing mode eigen $\lambda_1 = -1, \lambda_2 = -2,$ dan $\lambda_3 = -3$.  
(d) Tentukan fungsi transfer sistem $G(s) = \frac{Y(s)}{U(s)}$ dan tunjukkan mode mana saja yang muncul pada fungsi transfer tersebut.

**Penyelesaian:**

**(a) Uji Keterkontrolan Gilbert**

Untuk matriks diagonal dengan nilai eigen berbeda, sistem terkontrol jika dan hanya jika seluruh elemen vektor masukan $B$ bernilai tidak nol:
$$B = \begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}$$
- Mode $\lambda_1 = -1$: elemen $b_1 = 2 \ne 0 \implies$ **Terkontrol**.
- Mode $\lambda_2 = -2$: elemen $b_2 = 0 \implies$ **Tak-terkontrol**.
- Mode $\lambda_3 = -3$: elemen $b_3 = 1 \ne 0 \implies$ **Terkontrol**.

Secara keseluruhan, sistem bersifat tak-terkontrol karena mode $\lambda_2 = -2$ tidak terhubung dengan masukan.

**(b) Uji Keterobservasian Gilbert**

Sistem terobservasi jika dan hanya jika seluruh elemen vektor keluaran $C$ bernilai tidak nol:
$$C = \begin{bmatrix} 1 & 3 & 0 \end{bmatrix}$$
- Mode $\lambda_1 = -1$: elemen $c_1 = 1 \ne 0 \implies$ **Terobservasi**.
- Mode $\lambda_2 = -2$: elemen $c_2 = 3 \ne 0 \implies$ **Terobservasi**.
- Mode $\lambda_3 = -3$: elemen $c_3 = 0 \implies$ **Tak-terobservasi**.

Secara keseluruhan, sistem bersifat tak-terobservasi karena mode $\lambda_3 = -3$ tidak terhubung dengan keluaran.

**(c) Klasifikasi Subruang Kalman Setiap Mode**

- Mode $\lambda_1 = -1$: Terkontrol dan Terobservasi (*controllable and observable*).
- Mode $\lambda_2 = -2$: Tak-terkontrol tetapi Terobservasi (*uncontrollable and observable*).
- Mode $\lambda_3 = -3$: Terkontrol tetapi Tak-terobservasi (*controllable and unobservable*).

**(d) Penentuan Fungsi Transfer Sistem**

$$G(s) = \frac{c_1 b_1}{s - \lambda_1} + \frac{c_2 b_2}{s - \lambda_2} + \frac{c_3 b_3}{s - \lambda_3} = \frac{1(2)}{s+1} + \frac{3(0)}{s+2} + \frac{0(1)}{s+3} = \frac{2}{s+1}$$
Hanya mode $\lambda_1 = -1$ (yang terkontrol sekaligus terobservasi) yang muncul pada fungsi transfer. Mode $\lambda_2$ dan $\lambda_3$ lenyap dari hubungan masukan-keluaran.

---

### **No. 5**

**Soal:**  
Diberikan sistem LTI dengan matriks dinamika berupa satu blok Jordan berukuran $3 \times 3$ yang berasosiasi dengan nilai eigen berulang $\lambda = -2$:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 0 & 3 \end{bmatrix} \mathbf{x}(t)$$
(a) Ujilah keterkontrolan sistem menggunakan Kriteria Gilbert untuk bentuk kanonik Jordan.  
(b) Ujilah keterobservasian sistem menggunakan Kriteria Gilbert untuk bentuk kanonik Jordan.  
(c) Verifikasi hasil keterkontrolan menggunakan matriks keterkontrolan Kalman $\mathcal{C}$.  
(d) Verifikasi hasil keterobservasian menggunakan matriks keterobservasian Kalman $\mathcal{O}$.

**Penyelesaian:**

**(a) Uji Keterkontrolan Gilbert untuk Blok Jordan**

Kriteria Gilbert menyatakan bahwa suatu blok Jordan $J_i$ terkontrol penuh jika dan hanya jika elemen pada **baris terakhir** dari sub-vektor masukan bernilai tidak nol:
$$b_3 = 0$$
Karena elemen baris terakhir bernilai nol, sistem terbukti **tak-terkontrol (*uncontrollable*)**.

**(b) Uji Keterobservasian Gilbert untuk Blok Jordan**

Suatu blok Jordan $J_i$ terobservasi penuh jika dan hanya jika elemen pada **kolom pertama** dari sub-vektor keluaran bernilai tidak nol:
$$c_1 = 1 \ne 0$$
Karena elemen kolom pertama bernilai tidak nol, sistem terbukti **terobservasi penuh (*observable*)**.

**(c) Verifikasi Keterkontrolan via Matriks Kalman**

$$\mathcal{C} = \begin{bmatrix} B & AB & A^2 B \end{bmatrix} = \begin{bmatrix} 1 & 0 & -4 \\ 2 & -4 & 8 \\ 0 & 0 & 0 \end{bmatrix}$$
Baris ketiga seluruhnya bernilai nol, sehingga $\text{rank}(\mathcal{C}) = 2 < 3 = n$ (tak-terkontrol).

**(d) Verifikasi Keterobservasian via Matriks Kalman**

$$\mathcal{O} = \begin{bmatrix} C \\ CA \\ CA^2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 3 \\ -2 & 1 & -6 \\ 4 & -4 & 13 \end{bmatrix} \implies \det(\mathcal{O}) = 1 \ne 0$$
Maka $\text{rank}(\mathcal{O}) = 3 = n$ (terobservasi penuh).

---

### **No. 6**

**Soal:**  
Diberikan sistem LTI kontinu dengan representasi ruang keadaan awal $(A, B, C)$. Dilakukan transformasi koordinat ruang keadaan linier nonsingular:
$$\mathbf{z}(t) = P \mathbf{x}(t)$$
dengan $P \in \mathbb{R}^{n \times n}$ merupakan matriks yang memiliki invers $P^{-1}$.  
(a) Tentukan representasi ruang keadaan sistem yang baru $(\bar{A}, \bar{B}, \bar{C})$ dalam koordinat $\mathbf{z}(t)$.  
(b) Buktikan secara analitis hubungan antara matriks keterkontrolan sistem baru $\bar{\mathcal{C}}$ dan sistem awal $\mathcal{C}$, serta buktikan bahwa $\text{rank}(\bar{\mathcal{C}}) = \text{rank}(\mathcal{C})$.  
(c) Buktikan secara analitis hubungan antara matriks keterobservasian sistem baru $\bar{\mathcal{O}}$ dan sistem awal $\mathcal{O}$, serta buktikan bahwa $\text{rank}(\bar{\mathcal{O}}) = \text{rank}(\mathcal{O})$.  
(d) Jelaskan konsekuensi matematis dari hasil ini terhadap sifat keterkontrolan dan keterobservasian sistem.

**Penyelesaian:**

**(a) Transformasi Koordinat Ruang Keadaan**

$$\bar{A} = P A P^{-1}, \quad \bar{B} = P B, \quad \bar{C} = C P^{-1}$$

**(b) Invariansi Keterkontrolan**

Karena $\bar{A}^k \bar{B} = (P A P^{-1})^k (P B) = P A^k B$, maka:
$$\bar{\mathcal{C}} = \begin{bmatrix} P B & P A B & \dots & P A^{n-1} B \end{bmatrix} = P \mathcal{C}$$
Karena $P$ nonsingular:
$$\text{rank}(\bar{\mathcal{C}}) = \text{rank}(P \mathcal{C}) = \text{rank}(\mathcal{C})$$

**(c) Invariansi Keterobservasian**

Karena $\bar{C} \bar{A}^k = (C P^{-1}) (P A P^{-1})^k = C A^k P^{-1}$, maka:
$$\bar{\mathcal{O}} = \mathcal{O} P^{-1}$$
Karena $P^{-1}$ nonsingular:
$$\text{rank}(\bar{\mathcal{O}}) = \text{rank}(\mathcal{O} P^{-1}) = \text{rank}(\mathcal{O})$$

**(d) Konsekuensi Matematis**

Keterkontrolan dan keterobservasian merupakan **sifat intrinsik struktural sistem**, bukan sifat yang bergantung pada pemilihan sistem koordinat atau basis ruang keadaan.

---

### **No. 7**

**Soal:**  
Diberikan sistem LTI kontinu orde-2 yang terkontrol:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u(t)$$
(a) Hitung polinomial karakteristik matriks $A$ dan tentukan matriks target dalam Bentuk Kanonik Keterkontrolan $(\bar{A}_{ccf}, \bar{B}_{ccf})$.  
(b) Susun matriks keterkontrolan sistem awal $\mathcal{C}$ dan matriks keterkontrolan sistem target $\bar{\mathcal{C}}$.  
(c) Tentukan matriks transformasi similaritas $P$ sedemikian rupa sehingga $\mathbf{x} = P \mathbf{z}$ mentransformasikan sistem ke CCF ($P^{-1} A P = \bar{A}_{ccf}$ dan $P^{-1} B = \bar{B}_{ccf}$).  
(d) Lakukan verifikasi eksplisit perkalian matriks untuk membuktikan kebenaran transformasi tersebut.

**Penyelesaian:**

**(a) Polinomial Karakteristik dan Bentuk Target CCF**

$$\det(sI - A) = (s - 1)(s - 3) = s^2 - 4s + 3 \implies a_1 = -4, a_2 = 3$$
$$\bar{A}_{ccf} = \begin{bmatrix} 0 & 1 \\ -3 & 4 \end{bmatrix}, \quad \bar{B}_{ccf} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

**(b) Matriks Keterkontrolan $\mathcal{C}$ dan $\bar{\mathcal{C}}$**

$$\mathcal{C} = \begin{bmatrix} B & AB \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 3 \end{bmatrix}, \quad \bar{\mathcal{C}} = \begin{bmatrix} \bar{B} & \bar{A}\bar{B} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 4 \end{bmatrix}$$

**(c) Penentuan Matriks Transformasi Similaritas $P$**

$$P = \mathcal{C} \bar{\mathcal{C}}^{-1} = \begin{bmatrix} 0 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} -4 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}$$
$$P^{-1} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$$

**(d) Verifikasi Eksplisit**

$$P^{-1} B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \bar{B}_{ccf}$$
$$P^{-1} A P = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ -3 & 3 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -3 & 4 \end{bmatrix} = \bar{A}_{ccf}$$

---

### **No. 8**

**Soal:**  
Diberikan sistem LTI kontinu orde-2 yang terobservasi:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix} \mathbf{x}(t), \quad y(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}(t)$$
(a) Hitung polinomial karakteristik sistem dan tentukan bentuk target Kanonik Keterobservasian $(\bar{A}_{ocf}, \bar{C}_{ocf})$.  
(b) Tentukan matriks keterobservasian sistem awal $\mathcal{O}$ dan sistem target $\bar{\mathcal{O}}$.  
(c) Tentukan matriks transformasi koordinat $T$ sedemikian rupa sehingga $\mathbf{z} = T \mathbf{x}$ mentransformasikan sistem ke OCF ($T A T^{-1} = \bar{A}_{ocf}$ dan $\bar{C}_{ocf} = C T^{-1}$).  
(d) Lakukan verifikasi eksplisit hasil transformasi tersebut.

**Penyelesaian:**

**(a) Polinomial Karakteristik dan Target OCF**

$$\det(sI - A) = s(s + 3) + 2 = s^2 + 3s + 2 \implies a_1 = 3, a_2 = 2$$
$$\bar{A}_{ocf} = \begin{bmatrix} 0 & -2 \\ 1 & -3 \end{bmatrix}, \quad \bar{C}_{ocf} = \begin{bmatrix} 0 & 1 \end{bmatrix}$$

**(b) Matriks Keterobservasian $\mathcal{O}$ dan $\bar{\mathcal{O}}$**

$$\mathcal{O} = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}, \quad \bar{\mathcal{O}} = \begin{bmatrix} \bar{C} \\ \bar{C}\bar{A} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & -3 \end{bmatrix}$$

**(c) Penentuan Matriks Transformasi $T$**

$$T = \bar{\mathcal{O}}^{-1} \mathcal{O} = \begin{bmatrix} 3 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 3 & 2 \\ 1 & 0 \end{bmatrix}$$
$$T^{-1} = \begin{bmatrix} 0 & 1 \\ 1/2 & -3/2 \end{bmatrix}$$

**(d) Verifikasi Eksplisit**

$$C T^{-1} = \begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1/2 & -3/2 \end{bmatrix} = \begin{bmatrix} 0 & 1 \end{bmatrix} = \bar{C}_{ocf}$$
$$T A T^{-1} = \begin{bmatrix} -2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 0 & 1 \\ 1/2 & -3/2 \end{bmatrix} = \begin{bmatrix} 0 & -2 \\ 1 & -3 \end{bmatrix} = \bar{A}_{ocf}$$

---

### **No. 9**

**Soal:**  
Diberikan sistem LTI kontinu orde-3 yang tidak terkontrol penuh:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & -1 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} u(t)$$
(a) Hitung matriks keterkontrolan $\mathcal{C}$ dan tentukan dimensi subruang terkontrol $\mathcal{X}_c = \text{Im}(\mathcal{C})$.  
(b) Tentukan basis untuk subruang terkontrol dan perluas basis tersebut menjadi basis ruang keadaan $\mathbb{R}^3$ untuk membentuk matriks transformasi $M$.  
(c) Lakukan Dekomposisi Kanonik Keterkontrolan Kalman $(\bar{A} = M^{-1} A M, \bar{B} = M^{-1} B)$.  
(d) Pisahkan matriks hasil transformasi ke dalam struktur blok subsistem terkontrol dan subsistem tak-terkontrol.

**Penyelesaian:**

**(a) Matriks Keterkontrolan dan Dimensi $\mathcal{X}_c$**

$$\mathcal{C} = \begin{bmatrix} 1 & 2 & 4 \\ 1 & 2 & 4 \\ 0 & 0 & 0 \end{bmatrix} \implies \text{rank}(\mathcal{C}) = 1$$
Dimensi subruang terkontrol adalah $\dim(\mathcal{X}_c) = 1$.

**(b) Konstruksi Basis dan Matriks $M$**

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{v}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \implies M = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad M^{-1} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**(c) Transformasi Dekomposisi Kalman**

$$\bar{B} = M^{-1} B = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$$
$$\bar{A} = M^{-1} A M = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{bmatrix}$$

**(d) Pemisahan Blok**

$$\bar{A} = \begin{bmatrix} A_c & A_{12} \\ 0 & A_{\bar{c}} \end{bmatrix} = \begin{bmatrix} 2 & \vline & 0 & 0 \\ \hline 0 & \vline & 1 & 0 \\ 0 & \vline & 0 & -1 \end{bmatrix}, \quad \bar{B} = \begin{bmatrix} B_c \\ \hline 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ \hline 0 \\ 0 \end{bmatrix}$$
- **Subsistem Terkontrol ($c$):** $A_c = [2]$ dan $B_c = [1]$ (nilai eigen $\lambda = 2$).
- **Subsistem Tak-Terkontrol ($\bar{c}$):** $A_{\bar{c}} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ (nilai eigen $\lambda = 1, -1$).

---

### **No. 10**

**Soal:**  
Diberikan sistem LTI kontinu orde-3 dengan matriks dinamika dan matriks keluaran:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 1 & 3 \end{bmatrix} \mathbf{x}(t), \quad y(t) = \begin{bmatrix} 0 & 1 & 0 \end{bmatrix} \mathbf{x}(t)$$
(a) Hitung matriks keterobservasian $\mathcal{O}$ dan tentukan rank-nya.  
(b) Tentukan subruang tak-terobservasi $\mathcal{X}_{\bar{o}} = \text{Ker}(\mathcal{O})$ dan tentukan basisnya.  
(c) Lakukan Dekomposisi Kanonik Keterobservasian Kalman untuk memisahkan keadaan terobservasi dan keadaan tak-terobservasi.

**Penyelesaian:**

**(a) Matriks Keterobservasian dan Rank**

$$\mathcal{O} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 2 & 0 \\ 3 & 4 & 0 \end{bmatrix} \implies \text{rank}(\mathcal{O}) = 2 < 3 = n$$

**(b) Subruang Tak-Terobservasi $\text{Ker}(\mathcal{O})$**

$$\mathcal{O}\mathbf{x} = \mathbf{0} \implies x_1 = 0, \quad x_2 = 0, \quad x_3 \in \mathbb{R} \implies \mathbf{w}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$
Dimensi subruang tak-terobservasi adalah $\dim(\mathcal{X}_{\bar{o}}) = 1$.

**(c) Dekomposisi Kanonik Keterobservasian**

Dengan basis $\mathbf{w}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \mathbf{w}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \mathbf{w}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$ ($T = I_3$):
$$A = \begin{bmatrix} A_o & 0 \\ A_{21} & A_{\bar{o}} \end{bmatrix} = \begin{bmatrix} 1 & 0 & \vline & 0 \\ 1 & 2 & \vline & 0 \\ \hline 1 & 1 & \vline & 3 \end{bmatrix}, \quad C = \begin{bmatrix} C_o & \vline & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & \vline & 0 \end{bmatrix}$$
- **Subsistem Terobservasi ($o$):** berdimensi 2 dengan nilai eigen $\lambda_1 = 1, \lambda_2 = 2$.
- **Subsistem Tak-Terobservasi ($\bar{o}$):** berdimensi 1 dengan nilai eigen $\lambda_3 = 3$.

---

### **No. 11**

**Soal:**  
Diberikan sistem LTI kontinu orde-2:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 \\ -1 \end{bmatrix} u(t), \quad y(t) = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}(t)$$
(a) Tentukan nilai-nilai eigen dari matriks dinamika $A$.  
(b) Ujilah keterkontrolan sistem dan tentukan mode mana yang tidak dapat dikontrol.  
(c) Ujilah keterobservasian sistem menggunakan kriteria Kalman.  
(d) Hitung fungsi transfer sistem $G(s) = C(sI - A)^{-1} B$. Tunjukkan bahwa terjadi pembatalan kutub-nol (*pole-zero cancellation*) dan jelaskan keterkaitannya dengan hasil uji keterkontrolan.

**Penyelesaian:**

**(a) Nilai-Nilai Eigen Matriks $A$**

$$\det(sI - A) = s^2 + 3s + 2 = (s + 1)(s + 2) = 0 \implies \lambda_1 = -1, \quad \lambda_2 = -2$$

**(b) Uji Keterkontrolan Kalman**

$$AB = \begin{bmatrix} -1 \\ 1 \end{bmatrix} = -B \implies \mathcal{C} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \implies \det(\mathcal{C}) = 0$$
Karena $\text{rank}(\mathcal{C}) = 1 < 2$, sistem **tak-terkontrol**. Vektor masukan $B$ adalah vektor eigen yang berasosiasi dengan $\lambda_1 = -1$, sehingga masukan hanya menggerakkan mode $\lambda_1 = -1$. Mode $\lambda_2 = -2$ sama sekali tidak terhubung dan menjadi mode tak-terkontrol.

**(c) Uji Keterobservasian Kalman**

$$\mathcal{O} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2 \implies \det(\mathcal{O}) = 1 \ne 0 \implies \text{rank}(\mathcal{O}) = 2$$
Sistem bersifat **terobservasi penuh**.

**(d) Fungsi Transfer dan Pembatalan Kutub-Nol**

$$G(s) = C(sI - A)^{-1} B = \frac{s + 2}{(s+1)(s+2)} = \frac{1}{s + 1}$$
Kutub pada $s = -2$ dibatalkan oleh pembuat nol pada $s = -2$. Mode yang tereliminasi akibat pembatalan aljabar tersebut berkorespondensi tepat dengan mode $\lambda_2 = -2$ yang tak-terkontrol.

---

### **No. 12**

**Soal:**  
Diberikan sistem multivariabel 2-masukan 2-keluaran (MIMO) kontinu berorde-2:
$$\dot{\mathbf{x}}(t) = \begin{bmatrix} -1 & 0 \\ 0 & -3 \end{bmatrix} \mathbf{x}(t) + \begin{bmatrix} 1 & 1 \\ 0 & 2 \end{bmatrix} \mathbf{u}(t), \quad \mathbf{y}(t) = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \mathbf{x}(t)$$
(a) Susun matriks keterkontrolan Kalman multivariabel $\mathcal{C}$ dan tentukan rank-nya.  
(b) Susun matriks keterobservasian Kalman multivariabel $\mathcal{O}$ dan tentukan rank-nya.  
(c) Tentukan apakah sistem MIMO tersebut terkontrol penuh dan terobservasi penuh.

**Penyelesaian:**

**(a) Matriks Keterkontrolan Multivariabel**

$$AB = \begin{bmatrix} -1 & -1 \\ 0 & -6 \end{bmatrix} \implies \mathcal{C} = \begin{bmatrix} B & AB \end{bmatrix} = \begin{bmatrix} 1 & 1 & -1 & -1 \\ 0 & 2 & 0 & -6 \end{bmatrix}$$
Dua kolom pertama memuat matriks $B$ dengan $\det(B) = 2 \ne 0 \implies \text{rank}(\mathcal{C}) = 2 = n$.

**(b) Matriks Keterobservasian Multivariabel**

$$CA = \begin{bmatrix} -1 & 0 \\ -1 & -3 \end{bmatrix} \implies \mathcal{O} = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ -1 & 0 \\ -1 & -3 \end{bmatrix}$$
Dua baris pertama memuat matriks $C$ dengan $\det(C) = 1 \ne 0 \implies \text{rank}(\mathcal{O}) = 2 = n$.

**(c) Kesimpulan**

Karena $\text{rank}(\mathcal{C}) = 2 = n$ dan $\text{rank}(\mathcal{O}) = 2 = n$, sistem MIMO tersebut terbukti **terkontrol penuh (*controllable*)** dan **terobservasi penuh (*observable*)**.
