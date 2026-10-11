# Lembar Latihan dan Pembahasan Lengkap
## Topik 04: Keterkontrolan dan Keterobservasian Sistem
**Mata Kuliah:** MA4171 Teori Kontrol Linear

---

### **No. 1**

**Soal:**  
Suatu sistem dinamik linear invarian waktu (LTI) kontinu orde-3 memiliki representasi ruang keadaan dengan matriks dinamika dan matriks masukan sebagai berikut:
$$A = \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$
(a) Hitung matriks keterkontrolan Kalman $M_c$.  
(b) Tentukan nilai determinan dan rank dari matriks $M_c$.  
(c) Tarik kesimpulan apakah sistem tersebut terkontrol keadaan lengkap (*completely state controllable*).

**Penyelesaian:**

**(a) Perhitungan Matriks Keterkontrolan Kalman**

Matriks keterkontrolan Kalman untuk sistem berorde $n = 3$ didefinisikan sebagai:
$$M_c = \begin{bmatrix} B & AB & A^2B \end{bmatrix}$$

Kolom pertama adalah vektor masukan $B$:
$$B = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$$

Kolom kedua dihitung melalui perkalian $A$ dengan $B$:
$$AB = \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix}$$

Kolom ketiga diperoleh dengan mengalikan $A$ dengan vektor $AB$:
$$A^2B = \begin{bmatrix} 1 & 2 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -2 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -2 \end{bmatrix} = \begin{bmatrix} 3 \\ -3 \\ 4 \end{bmatrix}$$

Dengan menyusun ketiga vektor kolom tersebut secara berdampingan:
$$M_c = \begin{bmatrix} 1 & 1 & 3 \\ 0 & 1 & -3 \\ 1 & -2 & 4 \end{bmatrix}$$

**(b) Penentuan Determinan dan Rank**

$$\det(M_c) = 1(4 - 6) - 1(0 + 3) + 3(0 - 1) = -2 - 3 - 3 = -8$$

Karena $\det(M_c) = -8 \ne 0$, rank matriks $M_c$ adalah:
$$\operatorname{rank}(M_c) = 3$$

**(c) Kesimpulan Keterkontrolan**

Karena $\operatorname{rank}(M_c) = n = 3$, sistem dinyatakan **terkontrol keadaan lengkap** (*completely state controllable*).

---

### **No. 2**

**Soal:**  
Diberikan sistem LTI orde-3 dengan matriks dinamika $A$ dan matriks keluaran $C$ sebagai berikut:
$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6 \end{bmatrix}, \quad C = \begin{bmatrix} 2 & 1 & 0 \end{bmatrix}$$
(a) Hitung matriks keterobservasian Kalman $M_o$.  
(b) Evaluasi apakah sistem terobservasi keadaan lengkap (*completely state observable*).  
(c) Jika tidak terobservasi lengkap, tentukan dimensi subruang tak-terobservasi (*unobservable subspace*).

**Penyelesaian:**

**(a) Perhitungan Matriks Keterobservasian Kalman**

$$M_o = \begin{bmatrix} C \\ CA \\ CA^2 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ -6 & -11 & -4 \end{bmatrix}$$

**(b) Evaluasi Keterobservasian Sistem**

$$\det(M_o) = 2(-8 + 11) - 1(0 + 6) = 6 - 6 = 0$$
$$\operatorname{rank}(M_o) = 2 < 3$$
Sistem **tidak terobservasi keadaan lengkap**.

**(c) Dimensi Subruang Tak-Terobservasi**

$$\dim(\ker(M_o)) = n - \operatorname{rank}(M_o) = 3 - 2 = 1$$

---

### **No. 3**

**Soal:**  
Suatu sistem fisik memiliki representasi ruang keadaan yang bergantung pada dua parameter skalar $\alpha$ dan $\beta$:
$$A = \begin{bmatrix} 1 & 1 \\ 0 & \alpha \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ \beta \end{bmatrix}, \quad C = \begin{bmatrix} 1 & -1 \end{bmatrix}$$
(a) Tentukan syarat nilai $\alpha$ dan $\beta$ agar sistem terkontrol keadaan lengkap.  
(b) Tentukan syarat nilai $\alpha$ agar sistem terobservasi keadaan lengkap.  
(c) Tentukan pasangan parameter $(\alpha, \beta)$ sedemikian sehingga sistem sekaligus terkontrol dan terobservasi.

**Penyelesaian:**

**(a) Syarat Keterkontrolan**
$$M_c = \begin{bmatrix} 1 & 1+\beta \\ \beta & \alpha\beta \end{bmatrix} \implies \det(M_c) = \beta(\alpha - 1 - \beta) \ne 0 \implies \beta \ne 0 \text{ dan } \alpha - \beta \ne 1$$

**(b) Syarat Keterobservasian**
$$M_o = \begin{bmatrix} 1 & -1 \\ 1 & 1-\alpha \end{bmatrix} \implies \det(M_o) = 2 - \alpha \ne 0 \implies \alpha \ne 2$$

**(c) Syarat Simultan**
$$\alpha \ne 2, \quad \beta \ne 0, \quad \text{dan} \quad \beta \ne \alpha - 1$$

---

### **No. 4**

**Soal:**  
Gunakan Uji Popov-Belevitch-Hautus (PBH Controllability Test) untuk memeriksa keterkontrolan sistem dengan matriks:
$$A = \begin{bmatrix} -2 & 1 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$$

**Penyelesaian:**

Nilai-nilai eigen: $\lambda_1 = \lambda_2 = -2$, $\lambda_3 = -3$.
- Pada $\lambda = -2$:
  $$\operatorname{rank} \begin{bmatrix} -2I - A & B \end{bmatrix} = \operatorname{rank} \begin{bmatrix} 0 & -1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix} = 3$$
- Pada $\lambda = -3$:
  $$\operatorname{rank} \begin{bmatrix} -3I - A & B \end{bmatrix} = \operatorname{rank} \begin{bmatrix} -1 & -1 & 0 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix} = 3$$

Karena rank bernilai 3 untuk seluruh nilai eigen, sistem **terkontrol keadaan lengkap**.

---

### **No. 5**

**Soal:**  
Gunakan Uji PBH Keterobservasian untuk menentukan apakah sistem berikut terobservasi:
$$A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 3 & 0 \\ 1 & 1 & 2 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & 1 \end{bmatrix}$$

**Penyelesaian:**

Nilai eigen: $\lambda_1 = 1, \lambda_2 = 2, \lambda_3 = 3$.
Untuk setiap $\lambda_i \in \{1, 2, 3\}$, matriks $\begin{bmatrix} \lambda_i I - A \\ C \end{bmatrix}$ diuji dan terbukti memiliki $\operatorname{rank} = 3$.
Sistem **terobservasi keadaan lengkap**.

---

### **No. 6**

**Soal:**  
Terapkan Uji Keterkontrolan dan Keterobservasian Gilbert untuk menganalisis kedua sistem berikut:
$$\dot{\mathbf{x}}_1 = \begin{bmatrix} -1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -4 \end{bmatrix} \mathbf{x}_1 + \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix} u, \quad y_1 = \begin{bmatrix} 1 & 4 & 2 \end{bmatrix} \mathbf{x}_1$$
$$\dot{\mathbf{x}}_2 = \begin{bmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{bmatrix} \mathbf{x}_2 + \begin{bmatrix} 0 \\ 0 \\ 5 \end{bmatrix} u, \quad y_2 = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \mathbf{x}_2$$

**Penyelesaian:**

- **Sistem 1 (Diagonal):** Baris ke-2 dari $B_1$ bernilai nol ($b_2 = 0$) $\implies$ **tidak terkontrol lengkap** (moda $\lambda = -2$ tak-terkontrol). Seluruh kolom $C_1$ bukan nol $\implies$ **terobservasi lengkap**.
- **Sistem 2 (Blok Jordan):** Baris terakhir blok Jordan pada $B_2$ adalah $5 \ne 0 \implies$ **terkontrol lengkap**. Kolom pertama blok Jordan pada $C_2$ adalah $1 \ne 0 \implies$ **terobservasi lengkap**.

---

### **No. 7**

**Soal:**  
Diberikan sistem LTI:
$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
Tentukan matriks transformasi $P$ sedemikian rupa sehingga sistem berada dalam Bentuk Kanonik Keterkontrolan.

**Penyelesaian:**

Polinomial karakteristik: $\det(sI - A) = s^2 - 5s - 2 \implies a_1 = -5, a_2 = -2$.
Matriks keterkontrolan: $M_c = \begin{bmatrix} 1 & 3 \\ 1 & 7 \end{bmatrix} \implies M_c^{-1} = \begin{bmatrix} 7/4 & -3/4 \\ -1/4 & 1/4 \end{bmatrix}$.
Baris terakhir $M_c^{-1}$ adalah $t_1^T = [-1/4, 1/4]$.
$$P^{-1} = \begin{bmatrix} t_1^T \\ t_1^T A \end{bmatrix} = \begin{bmatrix} -1/4 & 1/4 \\ 1/2 & 1/2 \end{bmatrix} \implies P = \begin{bmatrix} -2 & 1 \\ 2 & 1 \end{bmatrix}$$
$$\tilde{A} = P^{-1} A P = \begin{bmatrix} 0 & 1 \\ 2 & 5 \end{bmatrix}, \quad \tilde{B} = P^{-1} B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

---

### **No. 8**

**Soal:**  
Diberikan sistem terobservasi:
$$A = \begin{bmatrix} 0 & -2 \\ 1 & -3 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 1 \end{bmatrix}$$
Tentukan matriks transformasi koordinat $Q$ ke Bentuk Kanonik Keterobservasian.

**Penyelesaian:**

$$M_o = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & -3 \end{bmatrix} \implies M_o^{-1} = \begin{bmatrix} 3 & 1 \\ 1 & 0 \end{bmatrix}$$
Kolom terakhir $M_o^{-1}$ adalah $q_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
$$Q^{-1} = \begin{bmatrix} q_1 & A q_1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I \implies Q = I$$
Sistem yang diberikan sudah berada secara alami dalam bentuk kanonik keterobservasian.

---

### **No. 9**

**Soal:**  
Diberikan sistem LTI:
$$A = \begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 2 \end{bmatrix}, \quad D = [0]$$
(a) Uji keterkontrolan keadaan sistem.  
(b) Uji keterkontrolan keluaran (*output controllability*) sistem.  
(c) Jelaskan signifikansi fisisnya.

**Penyelesaian:**

- $\operatorname{rank}(M_c) = 1 < 2 \implies$ **tidak terkontrol keadaan**.
- $M_{co} = \begin{bmatrix} CB & CAB & D \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 \end{bmatrix} \implies \operatorname{rank}(M_{co}) = 1 = p \implies$ **terkontrol keluaran lengkap**.
- Penjelasan fisis: Keluaran $y = x_1 + 2x_2$ dapat diarahkan ke sembarang nilai karena variabel $x_1$ sepenuhnya terkontrol oleh masukan $u$.

---

### **No. 10**

**Soal:**  
Suatu sistem memiliki matriks:
$$A = \begin{bmatrix} -2 & 0 \\ 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}$$
Tentukan apakah sistem tersebut terstabilkan (*stabilizable*) dan terdeteksi (*detectable*).

**Penyelesaian:**

Nilai eigen: $\lambda_1 = -2$ (stabil), $\lambda_2 = 1$ (tidak stabil).
- Moda tak-terkontrol adalah $\lambda_2 = 1$. Karena $\operatorname{Re}(\lambda_2) > 0$, sistem **tidak terstabilkan** (*not stabilizable*).
- Moda tak-terobservasi adalah $\lambda_2 = 1$. Karena $\operatorname{Re}(\lambda_2) > 0$, sistem **tidak terdeteksi** (*not detectable*).

---

### **No. 11**

**Soal:**  
Diberikan sistem:
$$A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 1 & 0 \end{bmatrix}$$
Identifikasi 4 subruang Dekomposisi Kalman dan hitung fungsi transfernya.

**Penyelesaian:**

- $x_1$ ($\lambda = 1$): $b_1 \ne 0, c_1 \ne 0 \implies$ subruang **terkontrol dan terobservasi ($x_{co}$)**.
- $x_2$ ($\lambda = -2$): $b_2 = 0, c_2 \ne 0 \implies$ subruang **tak-terkontrol tetapi terobservasi ($x_{\bar{c}o}$)**.
- $x_3$ ($\lambda = -3$): $b_3 \ne 0, c_3 = 0 \implies$ subruang **terkontrol tetapi tak-terobservasi ($x_{c\bar{o}}$)**.
- Fungsi transfer: $G(s) = C(sI - A)^{-1} B = \frac{1}{s - 1}$. Fungsi transfer hanya merepresentasikan subruang $x_{co}$.

---

### **No. 12**

**Soal:**  
Diberikan sistem:
$$A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 \end{bmatrix}$$
Tunjukkan pembatalan kutub-nol dan dampaknya pada keterkontrolan dan keterobservasian.

**Penyelesaian:**

$$G(s) = \frac{s + 2}{(s + 1)(s + 2)} = \frac{1}{s + 1}$$
Terjadi pembatalan kutub-nol pada $s = -2$.
- $M_c = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} \implies \det(M_c) = 0 \implies$ **tidak terkontrol**.
- $M_o = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \implies \det(M_o) = 1 \implies$ **terobservasi lengkap**.
Pembatalan kutub-nol menghilangkan sifat keterkontrolan pada moda tersebut.

---

### **No. 13**

**Soal:**  
Hitung Gramian Keterkontrolan $W_c$ dari persamaan Lyapunov $A W_c + W_c A^T + B B^T = 0$ untuk:
$$A = \begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix}, \quad B = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

**Penyelesaian:**

$$B B^T = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$
$$\begin{bmatrix} -2w_{11} & -3w_{12} \\ -3w_{12} & -4w_{22} \end{bmatrix} = \begin{bmatrix} -1 & -2 \\ -2 & -4 \end{bmatrix} \implies W_c = \begin{bmatrix} 1/2 & 2/3 \\ 2/3 & 1 \end{bmatrix}$$
$\det(W_c) = 1/2 - 4/9 = 1/18 > 0$ dan $w_{11} > 0 \implies W_c > 0$ (definit positif) $\implies$ sistem terkontrol lengkap.

---

### **No. 14**

**Soal:**  
Uji keterkontrolan dan keterobservasian sistem MIMO:
$$A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & -3 & -4 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & -1 \end{bmatrix}, \quad C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \end{bmatrix}$$

**Penyelesaian:**

- $M_c = \begin{bmatrix} B & AB & A^2B \end{bmatrix} \in \mathbb{R}^{3 \times 6}$. Tiga kolom pertamanya memiliki determinan $2 \ne 0 \implies \operatorname{rank}(M_c) = 3 \implies$ **terkontrol lengkap**.
- $M_o = \begin{bmatrix} C \\ CA \\ CA^2 \end{bmatrix} \in \mathbb{R}^{6 \times 3}$. Tiga baris pertamanya memiliki determinan $-1 \ne 0 \implies \operatorname{rank}(M_o) = 3 \implies$ **terobservasi lengkap**.

---

### **No. 15**

**Soal:**  
Diberikan sistem diskrit:
$$\mathbf{x}(k+1) = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} \mathbf{x}(k) + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u(k), \quad y(k) = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}(k)$$
(a) Uji keterjangkauan dan keterkontrolan diskrit.  
(b) Tentukan respons *deadbeat* saat $u = 0$.

**Penyelesaian:**

- $M_c = \begin{bmatrix} H & GH \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \implies \det(M_c) = -1 \ne 0 \implies \operatorname{rank}(M_c) = 2 \implies$ **terjangkau dan terkontrol lengkap**.
- Matriks nilpoten: $G^2 = \mathbf{0}$. Dalam $k = 2$ langkah, untuk sembarang kondisi awal $\mathbf{x}(0)$, diperoleh $\mathbf{x}(2) = G^2 \mathbf{x}(0) = \mathbf{0}$ (*deadbeat response*).
