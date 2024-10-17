from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st


class CountryViews:
    def __init__(self) -> None:
        self.df = QueryDatabase("""
            SELECT Geografi AS country, SUM(Visningar) AS total_views
            FROM geografi.diagramdata
            GROUP BY Geografi
            ORDER BY total_views DESC
            LIMIT 3""").df

    def display_top_countries(self):
        st.markdown("## Top 3 Countries by Viewership")

        for index, row in self.df.iterrows():
            country = row['country']
            total_views = int(row['total_views'])
            st.metric(f"Country: {country}", f"{total_views} views")
