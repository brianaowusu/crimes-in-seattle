<<<<<<< HEAD
# Seattle-Crimes-GIS
=======
# Seattle Crimes in 2025 
This project analyzes crime data from Seattle using Python to uncover trends, patterns, and geographic hotspots. The analysis focuses on 2025 crime data, with additional historical context spanning the past 10 years.

The project combines data cleaning, exploratory data analysis (EDA), and geospatial visualization (GIS) to better understand crime distribution across neighborhoods.



📊 Exploratory Data Analysis (EDA)
1. Crime Category Distribution

Visualized frequency of crime types using count plots

Identified most common offense subcategories

2. Crime by Neighborhood

Created stacked bar charts showing:

Crime types per neighborhood

Highlighted areas with higher crime concentration

3. Crime Trends Over Time

Analyzed monthly crime trends from 2015–2025

Used time series resampling to observe long-term patterns

🗺️ Geospatial Analysis (GIS)
Capitol Hill Crime Heatmap

Focused on Capitol Hill, identified as a high-crime neighborhood

Generated a heatmap using latitude and longitude data

Added markers to highlight specific incidents

Seattle-Wide Crime Heatmap

Visualized crime distribution across the entire city

Used Folium HeatMap to identify hotspots

Centered map on Seattle coordinates


🔍Key Insights

Certain neighborhoods consistently show higher crime density

Crime types vary significantly by location

Long-term trends reveal fluctuations in crime rates over time

Geospatial mapping highlights clear urban hotspots

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/brianaowusu/Seattle-Crimes-GIS
cd Seattle-Crimes-GIS

Install dependencies:

pip install pandas numpy seaborn matplotlib folium pandas-profiling

Update dataset path in the notebook:

pd.read_csv("/Users/bri/Downloads/seattle-crimes/Seattle-Crimes-GIS/SPD_Crime_Data__2008-Present_20260317.csv")

Run the Jupyter Notebook:

jupyter notebook

🔮 Future Improvements

Build a predictive model for crime forecasting

Deploy an interactive dashboard (Plotly Dash / Tableau)

Integrate real-time data pipelines (AWS, APIs)

Combine with demographic datasets for deeper insights

## License
<<<<<<< HEAD
This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
>>>>>>> cd25f7a (changes to readme.md)
=======
<!--
 Copyright 2026 brianaowusu
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     https://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
>>>>>>> b182b8e (other updates)
