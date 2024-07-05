import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

dataset = st.container()

with dataset:
  st.write("Google play store Dataset")
  df = pd.read_csv('/content/googleplaystore.csv')
  st.write(df.head())
  st.write("Google play store ratings")
  st.bar_chart(df.Rating.value_counts())
  st.write("Scatter Plot: Rating vs. Reviews")
  fig, ax = plt.subplots()
  sns.scatterplot(data=df, x='Reviews', y='Rating', ax=ax)
  ax.set_title('Scatter Plot: Rating vs. Reviews')
  st.pyplot(fig)
  st.write("Google play store Genres count ")
  st.bar_chart(df.Genres.value_counts())