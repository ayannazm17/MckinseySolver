import streamlit as st
import pandas as pd
from mckinseysolvegame import Solver

st.set_page_config(page_title="McKinsey Solve: Sea Wolf Game", layout="centered")

st.title("🌊 McKinsey Solve: Ecosystem Builder")
st.write("Upload your species dataset to generate a sustainable food chain of 8 species.")

# Provide formatting instructions
with st.expander("How to format your CSV"):
    st.markdown("""
    Your CSV must include the following columns:
    * `name`
    * `calories_provided`
    * `calories_needed`
    * `depth_range`
    * `temperature_range`
    * `food_sources` (separated by semicolons, e.g., `Sea Lettuce;Red Moss`)
    """)

uploaded_file = st.file_uploader("Upload species.csv", type=["csv"])

if uploaded_file is not None:
    # Read the CSV into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    # Run the solver
    if st.button("Solve Ecosystem"):
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
                st.error(f"An error occurred: {e}")