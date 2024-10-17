from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)


    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)

    def display_plot_selectbox(self):
        # Use 'Datum' column for the selectbox since 'Videotitel' doesn't exist
        video_title = st.selectbox("Select Date:", self.df["Datum"].unique())
        # Filter the DataFrame based on the selected date
        filtered_df = self.df[self.df["Datum"] == video_title]

        fig = px.line(filtered_df, x="Datum", y="Visningar")
        st.plotly_chart(fig)
        
        

class VideoViewsTrend:              #Ny selecbox
    def __init__(self) -> None:
        self.df = QueryDatabase("""
            SELECT "Videotitel", "Datum", "Visningar"
            FROM innehall.diagramdata""").df
        print(self.df.columns)

    def display_plot_selectbox(self):
        video_title = st.selectbox(
            "Select Video Title:", self.df["Videotitel"].unique())
        filtered_df = self.df[self.df["Videotitel"] == video_title]
        fig = px.line(filtered_df, x="Datum", y="Visningar",
                      title=f"Views for {video_title}")
        st.plotly_chart(fig)

