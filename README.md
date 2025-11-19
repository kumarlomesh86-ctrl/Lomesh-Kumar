🥛 Milk Volume Prediction using Machine Learning

Predicting daily and monthly shiftwise milk production using machine learning models to support dairy Company Savihaat OPC PVT LTD operations, optimize logistics, and reduce waste.

📌 Project Overview

This project aims to forecast milk volume based on historical data and relevant features such as FAT and SNF. Accurate predictions help streamline supply chain decisions and improve farm efficiency.

🚀 Features
- Data preprocessing and feature engineering
- Exploratory data analysis (EDA)
- Model training and evaluation (Linear Regression, Random Forest, XGBoost, etc.)
- Streamlit dashboard for interactive predictions
- Region wise sales dashboard for interactive predictions
- Power BI Dashboard for Summary, Farmer Insights, Forcasts visualization, Anomaly dection and business actions
- R code web app for milk rate Calculator.
  
🧠 Machine Learning Models Used
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

  
📊 Dataset
- Source: [real-time sensor data collected from the Dairy Company Savihaat OPC PVT LTD]
- Features include:
- Member Code
- FAT
- SNF
- Rate
- Milk Qty
- Milk Amount
  
🛠️ Tech Stack

| Tool                                | Purpose  
| Python, Jupyter Notebook,            | Core Programming language
| Pandas, Numpy                       | Data Manipulation
| scikit-learn                        | ML Modeling
|  Random Forest                      | Regression
|  Matplotlib, seaborn, plotly        | Data Visualization
| Streamlit                           | Web based dashboard
| Power BI                            | Web based dashboard
| R studio                            | Web based rate calulator


📈 Sample Results
- R² Score: 0.99 (Random Forest)
- MSE: 0.004
- Next Month Milk Quantity Predicted: 1347.874
- Visualizations: correlation matrix, outlier detection, feature importance, prediction vs actual plots, top ten  contributors milk volume with KPIs plot
  
📂 Project Structure

Lomesh-Kumar/
│
├── January 2022_data.csv                # Raw and processed datasets
├── Milk Collection Dashboard Code           # Streamlit dashboard code
├── Milk Volume Prediction_Machine Learning                 # Scripts for preprocessing, training, and evaluation
├── Milk Volume Prediction_Machine Learning.ipynb  # Scripts with plots for preprocessing, training, and evaluation
├── Milk_Collection_Dashboard.py   # Streamlit dashboard code
├── Sales_Data_Region.py # Streamlit dashboard code
├── README.md            # Project overview
└── requirements.txt     # Python/Jupyter notebook and Rstudio dependencies


🧪 How to Run
- Clone the repository:
git clone https://github.com/kumarlomesh86-ctrl/Lomesh-Kumar/blob/main/Milk%20Volume%20Prediction_Machine%20Learning.ipynb

-cd milk-volume-prediction

- Install dependencies:
pip install -r requirements.txt


- Run the Streamlit app:
streamlit run Milk_Collection_Dashboard.py
streamlit run Sales_Data_Region.py


📌 Future Improvements

- Hyperparameter tuning
- Model performance visualization
- Deploy model via API
  
🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

📜 License

No License yet.
