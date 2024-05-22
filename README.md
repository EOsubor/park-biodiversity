
# Biodiversity in National Parks: Conservation Status Analysis

## Description
This repository contains an analytical project and an interactive dashboard exploring biodiversity within national parks, focusing on conservation needs and patterns. The goal is to provide insights into species conservation statuses and their observations across different national parks.

### [Biodiversity Analysis Report](biodiversity_analysis.md)

## Project Structure
- `species_info.csv` & `observations.csv`: These data files contain detailed species classifications, conservation statuses, and observation records across various national parks.
- `biodiversity_analysis.ipynb`: A Jupyter notebook that performs a detailed analysis of the species data, including visualization and statistical testing.
- `biodiversity_dashboard.py`: A Python script using Streamlit to create an interactive web dashboard for exploring the biodiversity data visually.
- `README.md`: This file provides an overview of the project, setup instructions, and usage details.

## Installation
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/yourusername/biodiversity_project.git
cd biodiversity_project
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

## How to Run
### Jupyter Notebook
To explore the detailed data analysis, navigate to the project directory and run Jupyter Notebook:
```bash
jupyter notebook
```
Open `biodiversity_analysis.ipynb` in the Jupyter interface that appears in your browser.

### Streamlit Dashboard
To start the interactive dashboard, run the following command in your terminal from the project directory:
```bash
streamlit run biodiversity_dashboard.py
```
This will start a local web server and automatically open the dashboard in your default web browser. You can interact with the visualizations and explore the data through this user-friendly interface.

## Contributing
Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request with a clear description of your modifications.

## License
Distributed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments
- National Parks Service for providing access to the data.
- Biodiversity Heritage Library for additional resources.
- The Python community for supporting libraries like Pandas, Matplotlib, Seaborn, and Streamlit.

## Contact Information
For any additional questions or feedback, please contact [Your Name] at [your.email@example.com].
