import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load datasets
csv_file1 = "day_cleaned.csv"
csv_file2 = "hour_cleaned.csv"
day_df = pd.read_csv(csv_file1)
hour_df = pd.read_csv(csv_file2)

# Sidebar Menu
st.sidebar.title("Menu Visualisasi")
visualization = st.sidebar.radio(
    "Pilih Visualisasi:",
    ("Distribusi Penggunaan Sepeda Per Jam",
     "Penggunaan Sepeda pada Hari Kerja vs Bukan Hari Kerja",
     "Penggunaan Sepeda per Musim",
     "Penggunaan Sepeda per Hari dalam Seminggu")
)

st.title("Dashboard Penggunaan Sepeda")

# Visualisasi Distribusi Penggunaan Sepeda Per Jam
if visualization == "Distribusi Penggunaan Sepeda Per Jam":
    st.subheader("Distribusi Penggunaan Sepeda Per Jam")
    hourly_mean_usage = hour_df.groupby("hr")["cnt"].mean()
    hours = range(24)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(hours, hourly_mean_usage, marker="o", linestyle="-", color="b")
    ax.set_title("Distribusi Penggunaan Sepeda Per Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penggunaan Sepeda")
    ax.set_xticks(hours)
    ax.grid(True)
    st.pyplot(fig)

# Visualisasi Penggunaan Sepeda pada Hari Kerja vs Bukan Hari Kerja
elif visualization == "Penggunaan Sepeda pada Hari Kerja vs Bukan Hari Kerja":
    st.subheader("Rata-rata Penggunaan Sepeda pada Hari Kerja vs Bukan Hari Kerja")
    workingday_usage = hour_df.groupby("workingday")["cnt"].mean()
    labels = ["Bukan Hari Kerja", "Hari Kerja"]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, workingday_usage, color=["skyblue", "lightgreen"])
    ax.set_title("Rata-rata Penggunaan Sepeda pada Hari Kerja vs Bukan Hari Kerja")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Rata-rata Jumlah Penggunaan Sepeda")
    st.pyplot(fig)

# Visualisasi Penggunaan Sepeda per Musim
elif visualization == "Penggunaan Sepeda per Musim":
    st.subheader("Rata-rata Penggunaan Sepeda per Musim")
    season_usage = hour_df.groupby("season")["cnt"].mean()
    labels = ["Musim Gugur", "Musim Semi", "Musim Panas", "Musim Dingin"]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, season_usage, color=["lightgreen", "orange", "red", "lightblue"])
    ax.set_title("Rata-rata Penggunaan Sepeda per Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Jumlah Penggunaan Sepeda")
    st.pyplot(fig)

# Visualisasi Penggunaan Sepeda per Hari dalam Seminggu
elif visualization == "Penggunaan Sepeda per Hari dalam Seminggu":
    st.subheader("Rata-rata Penggunaan Sepeda per Hari dalam Seminggu")
    weekday_usage = day_df.groupby("weekday")["cnt"].mean()
    labels = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(labels, weekday_usage, color="lightcoral")
    ax.set_title("Rata-rata Penggunaan Sepeda per Hari dalam Seminggu")
    ax.set_xlabel("Hari")
    ax.set_ylabel("Rata-rata Jumlah Penggunaan Sepeda")
    st.pyplot(fig)
