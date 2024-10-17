import streamlit as st 
from frontend.kpi import ContentKPI
from frontend.graphs import ViewsTrend, VideoViewsTrend


# device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
video_views_graph = VideoViewsTrend()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i min youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    
    #La till en selectbox för att kunna se hur traffiken går per video
    video_views_graph.display_plot_selectbox()

if __name__ == "__main__":
    layout()