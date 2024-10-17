import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend, VideoViewsTrend, AgeDemographicsTrend
from frontend.barcharts import CountryViews


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
video_views_graph = VideoViewsTrend()
age_demographic_graph = AgeDemographicsTrend()
top_countries_bars = CountryViews()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    
    #La till en selectbox för att kunna se hur traffiken går per video
    video_views_graph.display_plot_selectbox()
    age_demographic_graph.display_demographics_info()
    top_countries_bars.display_top_countries()


if __name__ == "__main__":
    layout()