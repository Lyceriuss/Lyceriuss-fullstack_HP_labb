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
        
        
class AgeDemographicsTrend:                #Vår age demographic mart
    def __init__(self) -> None:
        self.df = QueryDatabase("""
            SELECT *
            FROM marts.age_demographic_summary """).df
        print(self.df.columns)  

    def display_demographics_info(self):
        st.markdown("## Age Demographics Overview")

        # Displaying all metrics for each age group
        for index, row in self.df.iterrows():
            age_group = row['age_group']
            total_views = row['total_views_percentage']
            avg_percentage_watched = row['avg_percentage_watched']
            avg_minutes_watched = row['avg_minutes_watched']

            # Creating a column layout for each age group
            with st.container():
                st.markdown(f"### Age Group: {age_group}")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Views", f"{round(total_views, 2)}%")
                with col2:
                    st.metric("Percentage of video watched",
                              f"{round(avg_percentage_watched, 2)}%")
                with col3:
                    st.metric("Avg Minutes Watched",
                              round(avg_minutes_watched, 2))

            # Add a horizontal line separator for each age group
            st.markdown("---")
