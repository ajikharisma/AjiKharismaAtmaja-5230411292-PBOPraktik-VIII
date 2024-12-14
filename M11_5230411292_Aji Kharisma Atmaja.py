import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# import matplotlib.pyplot as plt
# import seaborn as sns

#READ XLSX
missing_values = ["NaN","."]
df = pd.read_excel('air_quality.xlsx')




#MENGGANTI MISSING VALUE DATA DENGAN MEDIAN
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].median())
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].median())
df['PM2.5'] = df['PM2.5'].fillna(df['PM2.5'].median())
df['PM10'] = df['PM10'].fillna(df['PM10'].median())
df['NO2'] = df['NO2'].fillna(df['NO2'].median())
df['SO2'] = df['SO2'].fillna(df['SO2'].median())
df['CO'] = df['CO'].fillna(df['CO'].median())
df['Proximity_to_Industrial_Areas'] = df['Proximity_to_Industrial_Areas'].fillna(df['Proximity_to_Industrial_Areas'].median())
df['Population_Density'] = df['Population_Density'].fillna(df['Population_Density'].median())

# MERUBAH MISSING VALUE OBJECT DENGAN MODUS
df['Air Quality'] = df['Air Quality'].fillna(df['Air Quality'].mode()[0])


column =['Air Quality']
encoder = LabelEncoder()

for i in column:
    df[i] = encoder.fit_transform(df[i])


feature = df.drop('Air Quality', axis=1).values  # Semua kolom kecuali target
label = df['Air Quality'].values  # Kolom targets

scaler = MinMaxScaler()
feature = scaler.fit_transform(feature)



X_train, X_test, y_train, y_test = train_test_split(feature,label,random_state=42, test_size=0.2)


while True:
    print("\nMENU OLAH DATA PBO:")
    print("1. Tampilkan data")
    print("2. Gaussian Naive Bayes")
    print("3. KNN")
    print("4. Keluar")
    input_user = input("Masukkan pilihan Anda (1/2/3/4): ")
    
    if input_user == "1":
        # MENAMPILKAN DATASET PENUH
        print("\nData lengkap:")
        print(df)
    elif input_user == "2":
        # HITUNG AKURASI DENGAN GAUSSIAN NAIVE BAYES
        GNB = GaussianNB()
        GNB.fit(X_train, y_train)
        pred = GNB.predict(X_test)
        accuracy = accuracy_score(y_test, pred)
        print(f"Accuracy Gaussian Naive Bayes: {accuracy:.2f}")
    elif input_user == "3":
        # HITUNG AKURASI DENGAN KNN
        KNN = KNeighborsClassifier(n_neighbors=5)
        KNN.fit(X_train, y_train)
        pred = KNN.predict(X_test)
        accuracy = accuracy_score(y_test, pred)
        print(f"Akurasi model KNN: {accuracy:.2f}")
    elif input_user == "4":
        # KELUAR DARI PROGRAM
        print("Program selesai Terimakasih Yaaaa.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
        
