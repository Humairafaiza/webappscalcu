import streamlit as st

def main():
    st.title("Umayy :cherry_blossom: menemukan inovasi baru dengan menemukan Kalkulator Sederhana")
    st.write("Kalkulator ajaib untuk menghitung :sushi:.")
    st.write("Umay pacar Adit :cupid:")
    st.write("Umay sayang Adit Selamanyaa :dizzy:")
    st.write("Umayy suka makan nasipadang pomad :arrow_double_up::arrow_double_up::arrow_double_up:")
     
    # Input angka pertama
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

    # Input angka kedua
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)
    
    # Pilihan operasi
    operation = st.selectbox(
        "Pilih operasi matematika:",
        ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
    )
    
    # Tombol untuk menghitung
    if st.button("Hitung"):
        if operation == "Penjumlahan":
            result = num1 + num2
            st.success(f"Hasil Penjumlahan: {result}")
        elif operation == "Pengurangan":
            result = num1 - num2
            st.success(f"Hasil Pengurangan: {result}")
        elif operation == "Perkalian":
            result = num1 * num2
            st.success(f"Hasil Perkalian: {result}")
        elif operation == "Pembagian":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Hasil Pembagian: {result}")
            else:
                st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
    
if __name__ == "__main__":
    main()
