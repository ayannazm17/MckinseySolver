import streamlit as st
import pandas as pd
from mckinseysolvegame import Solver

st.set_page_config(page_title="McKinsey Solve: Sea Wolf Game", layout="centered")

st.title("🌊 McKinsey Solve: Ecosystem Builder")
st.write("Provide your species dataset to generate a sustainable food chain of 8 species.")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["📁 Upload CSV", "✍️ Manual Entry"])

df = None # This will hold our final data

with tab1:
    uploaded_file = st.file_uploader("Upload species.csv", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

with tab2:
    st.write("Type your species data below. Click the `+` at the bottom to add more rows.")
    
    # Define the required blank columns
    empty_template = pd.DataFrame(columns=[
        "name", "calories_provided", "calories_needed", 
        "depth_range", "temperature_range", "food_sources"
    ])
    
    # Create the interactive table
    edited_df = st.data_editor(empty_template, num_rows="dynamic", use_container_width=True)
    
    # If the user has typed at least one name, use this data
    if not edited_df.empty and edited_df['name'].notna().any():
        df = edited_df

# Only show the solve button if we have data from either tab
if df is not None and not df.empty:
    st.divider()
    
    if st.button("Solve Ecosystem", type="primary"):
        with st.spinner("Finding optimal food chain..."):
            try:
                solver = Solver()
                result = solver.solve_from_dataframe(df)
                
                if result:
                    st.success("Sustainable Food Chain Found!")
                    st.write(result)
                else:
                    st.warning("Could not find a sustainable food chain with the provided species.")
            except Exception as e:
                st.error(f"An error occurred. Check your formatting: {e}")
