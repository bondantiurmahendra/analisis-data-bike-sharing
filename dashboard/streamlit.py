import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("hour.csv")
df.loc[:, 'dteday'] = pd.to_datetime(df['dteday'])

# Streamlit app
st.title("Bike Sharing Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
selected_display = st.sidebar.selectbox("Display", ['total rentals per hour', 'bike rentals distribution', 'bike rentals per season', 'scatter plot temperature'])

# Display the selected plot
if selected_display == 'total rentals per hour':
    st.subheader("Total Bike Rentals per Hour")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hr', y='cnt', data=df, ax=ax)
    plt.title('Total Bike Rentals per Hour')
    plt.xlabel('Hour')
    plt.ylabel('Total Rentals')
    st.pyplot(fig)
    st.markdown("## Kesimpulan")
    st.write("Berdasarkan lineplot diatas, dapat disimpulkan bahwa rata-rata penyewaan sepeda paling banyak terjadi pada jam 17 dan 18 atau jam 5 PM dan 6 PM. Paling sedikit jam 4 AM")
elif selected_display == 'bike rentals distribution':
    st.subheader("Distribution of Bike Rentals by Weather Condition")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=df, ax=ax)
    plt.title('Distribution of Bike Rentals by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Rentals')
    plt.xticks([0, 1, 2, 3], ['Sunny/Slightly Cloudy', 'Cloudy/Foggy', 'Snowfall/Storm', 'Extreme Weather'])
    st.pyplot(fig)
    st.markdown("## Kesimpulan")
    st.write("Berdasarkan barplot diatas, dapat disimpulkan bahwa rata-rata penyewaan sepeda paling banyak terjadi pada kondisi cerah/berawan dengan jumlah penyewa lebih dari 200.")
elif selected_display == 'bike rentals per season':
    st.subheader("Bike Rentals per Season")   
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season', y='cnt', data=df, ax=ax)
    plt.title('Bike Rentals per Season')
    plt.xlabel('Season')
    plt.ylabel('Total Rentals')
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Autumn', 'Winter'])
    st.pyplot(fig)
    st.markdown("## Kesimpulan")
    st.write("Berdasarkan barplot diatas, dapat disimpulkan bahwa periode antara pertengahan musim semi hingga pertengahan musim gugur umumnya mengalami peningkatan jumlah penyewaan sekitar 175%, sementara musim dingin mencatat penurunan yang signifikan sekitar 28%.")
elif selected_display == 'scatter plot temperature':
    st.subheader("Bike Rentals vs Temperature by Season")
    fig = px.scatter(df, x='temp', y='cnt', color='season', title='Bike Rentals vs Temperature by Season',
                     labels={"temp": "Temperature", "cnt": "Total Rentals"})
    st.plotly_chart(fig)
    st.markdown("## Kesimpulan")
    st.write("Berdasarkan scatterplot diatas, terdapat lonjakan signifikan dalam jumlah penyewaan sepeda pada musim gugur, meskipun suhu udara mulai menurun. Hal ini mengindikasikan bahwa faktor-faktor lain selain suhu, seperti perubahan warna dedaunan, cuaca yang lebih sejuk namun cerah, atau adanya festival musim gugur, menjadi daya tarik utama bagi masyarakat untuk menyewa sepeda.")