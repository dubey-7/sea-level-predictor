# 🌊 Sea Level Predictor

## 📌 Overview

The **Sea Level Predictor** is a Python-based data analysis project that examines historical global average sea level data from 1880 onward and predicts future sea level rise up to the year 2050.

The goal of this project is to analyze long-term trends and compare them with recent patterns using statistical modeling and visualization techniques.

---

## 📂 Dataset

The dataset includes:

- **Year**
- **CSIRO Adjusted Sea Level**

The data represents global average sea level changes over time and helps identify climate-related trends.

---

## 📊 Project Objectives

This project performs the following steps:

1. Import sea level data using Pandas.
2. Create a scatter plot of Year vs Sea Level.
3. Compute a regression line using all available data.
4. Extend the prediction to the year 2050.
5. Compute a second regression line using data from 2000 onward.
6. Compare long-term and recent sea level rise trends.

---

## 📈 Visualization Output

The final graph includes:

- Historical sea level scatter plot  
- Long-term regression prediction (1880–2050)  
- Recent trend prediction (2000–2050)  

This comparison highlights the acceleration in sea level rise in recent years.

---

## 🛠 Technologies Used

- Python  
- Pandas  
- Matplotlib  
- SciPy (linregress)  

---

## 🗂 Project Structure

```
sea-level-predictor/
│
├── README.md                # Project documentation
├── epa-sea-level.csv        # Dataset file
├── main.py                  # Script to execute the project
├── sea_level_predictor.py   # Contains analysis and plotting functions
└── test_module.py           # Unit tests for validation
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/sea-level-predictor.git
   cd sea-level-predictor
   ```

2. Install required libraries:
   ```bash
   pip install pandas matplotlib scipy
   ```

3. Run the project:
   ```bash
   python main.py
   ```

---

## 🎯 Key Learning Outcomes

- Time series data analysis  
- Linear regression modeling  
- Future trend forecasting  
- Data visualization techniques  

This project demonstrates how statistical modeling can be used to analyze historical climate data and make meaningful future predictions.
