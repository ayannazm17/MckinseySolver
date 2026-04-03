# MckinseySolver

# 🌊 McKinsey Solve: Ecosystem Builder

A Streamlit-based web interface to solve the McKinsey Solve Sea Wolf (Ecosystem) Game. This application allows users to upload a dataset of species and automatically calculates a valid, sustainable food chain of 8 species following the game's strict resource constraints.

The underlying calculation engine utilizes the `mckinseysolvegame` package by [Sebastien Eveno](https://github.com/SebastienEveno/mckinseysolvegame).

## ✨ Features
* **Interactive Web UI:** Built with Streamlit for quick, code-free interaction.
* **Automated Algorithm:** Sorts, targets, and calculates consumption metrics to ensure zero starvation and zero extinction.
* **CSV Support:** Easily upload your species parameters and instantly view the generated food chain.

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/ayannazm17/MckinseySolver.git](https://github.com/ayannazm17/MckinseySolver.git)
   cd MckinseySolver
2. Install dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

Launch the application
```bash
python -m streamlit run app.py
```

📊 Data Formatting
To use the solver, upload a .csv file containing your species data. The CSV must include the following column headers exactly as written:

name
calories_provided
calories_needed
depth_range
temperature_range
food_sources (Note: Separate multiple food sources with a semicolon, e.g., Sea Lettuce;Red Moss)
