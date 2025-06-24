import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        before_map = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
        after_map = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
        m.split_map(
            left_layer=before_map, right_layer=after_map, left_label="Before", right_label="After"
        )
        # m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)
