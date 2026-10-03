# flight-advisor-using-ml
Buy-now-or-wait advisor for flight tickets using Python, ML, and savings simulation.
# ✈️ Flight Price Timing Advisor

**Should you buy a flight ticket now, or wait?**

This project analyzes how flight prices change as departure approaches and builds a "buy now or wait" advisor. It recommends an action, estimates the expected saving, and tests the advice against simple baseline strategies using a simulation.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Table of Contents

1. [Business Question](#-business-question)
2. [Dataset](#-dataset)
3. [Important Limitation](#-important-limitation)
4. [Approach](#-approach)
5. [Results](#-results)
6. [Key Insights](#-key-insights)
7. [Streamlit App](#-streamlit-app)
8. [Project Structure](#-project-structure)
9. [How to Run](#-how-to-run)
10. [Tech Stack](#-tech-stack)
11. [Roadmap](#-roadmap)
12. [Author](#-author)

---

## 🎯 Business Question

> For a given route, airline, and travel class, is it better to buy a ticket **today** or **wait**, and how much money is at stake?

Most flight-price projects only predict the price. This project goes one step further and turns the prediction into a **decision**, then measures whether that decision actually saves money.

---

## 📊 Dataset

- **Source:** [Flight Price Prediction on Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)
- **Size:** about 300,000 flight booking options
- **Origin:** Ease My Trip website, covering travel between India's top 6 metro cities
- **Collection period:** early 2022 (prices are **not** current fares)
- **File used:** `Clean_Dataset.csv`

| Column | Description |
|---|---|
| `airline` | Airline name |
| `flight` | Flight code |
| `source_city` | City of departure |
| `departure_time` | Departure time bucket (e.g., Morning, Evening) |
| `stops` | Number of stops |
| `arrival_time` | Arrival time bucket |
| `destination_city` | City of arrival |
| `class` | Economy or Business |
| `duration` | Travel time in hours |
| `days_left` | Days between booking and departure |
| `price` | Ticket price in INR (target variable) |

> The dataset is not uploaded to this repo. Download it from Kaggle and place it in the `data/` folder.

---

## ⚠️ Important Limitation

The dataset is a **snapshot of listings with a `days_left` column**. It is **not** a tracked price history of the same flight over time, and it contains no departure date.

This means the project **cannot** claim "this exact flight dropped on day X." Instead, it models **average price behavior by route, airline, and class as departure approaches**. All conclusions should be read as patterns across groups of similar flights, not guarantees for a single ticket.

---

## 🧭 Approach

### 1. Data cleaning and exploration
- Check missing values, duplicates, and outliers
- Drop the unused index column
- Convert `stops` from text to numbers
- Analyze Economy and Business separately, since their pricing behavior differs

### 2. Price-vs-days-left analysis
- Plot average price against `days_left` for each class, route, and airline
- Identify where prices start to rise sharply before departure

### 3. Defining the "buy now" vs. "wait" label
For each listing, compare the current price with the lowest price available later (fewer days left) within the same group of similar flights (route, airline, class, stops, departure time).

```python
group = ["source_city", "destination_city", "airline", "class", "stops", "departure_time"]
# saving_pct = (current_price - future_min_price) / current_price
# label = "wait" if saving_pct > threshold else "buy_now"
```

The threshold (5% by default) is tested for sensitivity at 3%, 5%, and 10%.

### 4. Baseline strategies
The model must beat these to be useful:
- **Always buy now**
- **Fixed 21-day rule:** buy 21 days before departure
- **Route-average rule:** buy at the point where the route's average price curve is lowest

### 5. Modeling
- **Classification:** predict `buy_now` vs. `wait` (Random Forest, LightGBM)
- **Regression add-on:** predict the expected future price to estimate the saving in rupees
- **Group-based train/test split:** the same flight group never appears in both sets, which avoids data leakage

### 6. Savings simulation
Simulate thousands of virtual travelers and compare every strategy on:
- Average price paid
- Average saving versus buying immediately
- **Regret:** how often waiting cost the traveler more

### 7. Streamlit app
A simple interface where a user chooses a route, airline, class, and days left, and receives a recommendation with the expected saving.

---

## 📈 Results

> _To be completed. Replace the dashes with your actual numbers once the simulation is finished. Do not publish estimates._

### Strategy comparison

| Strategy | Avg price paid (₹) | Avg saving vs. buy-now | % of travelers who lose money |
|---|---|---|---|
| Always buy now | - | - | - |
| Fixed 21-day rule | - | - | - |
| Route-average rule | - | - | - |
| **Advisor model** | - | - | - |

### Model performance

| Model | Precision | Recall | F1 |
|---|---|---|---|
| Random Forest | - | - | - |
| LightGBM | - | - | - |

---

## 💡 Key Insights

> _To be completed after the analysis. Write only findings your data confirms._

Template:
- On `[route]` in Economy, the cheapest booking window is about `[X–Y]` days before departure.
- Business class prices rise `[X]%` more than Economy for last-minute bookings.
- `[Budget airlines]` show a smaller last-minute penalty than `[full-service airlines]` on `[routes]`.

---

## 🖥️ Streamlit App

**Live demo:** _link to be added after deployment_

Planned features:
- Select source, destination, airline, class, and days left
- Get a "Buy now" or "Wait" recommendation with the expected saving
- View the price-vs-days-left chart for the chosen route
- Risk slider (conservative vs. aggressive) that changes the decision threshold

_Add a screenshot here:_

```
![App screenshot](images/app_screenshot.png)
```

---

## 🗂️ Project Structure

```
flight-price-advisor/
├── data/                  # place Clean_Dataset.csv here (not tracked)
├── notebooks/
│   ├── 01_cleaning_and_eda.ipynb
│   ├── 02_price_curves.ipynb
│   ├── 03_label_and_baselines.ipynb
│   ├── 04_modeling.ipynb
│   └── 05_simulation.ipynb
├── src/                   # reusable functions
├── app/
│   └── app.py             # Streamlit app
├── models/                # saved model files
├── images/                # charts and screenshots
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How to Run

### Option 1: Google Colab
1. Open a notebook from the `notebooks/` folder in Colab
2. Upload `Clean_Dataset.csv` using the file icon in the sidebar
3. Run the cells in order

### Option 2: Run locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/flight-price-advisor.git
cd flight-price-advisor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download the dataset from Kaggle and place it in data/

# 4. Launch the app (after the model is trained)
streamlit run app/app.py
```

### Suggested `requirements.txt`

```
pandas
numpy
matplotlib
seaborn
scikit-learn
lightgbm
streamlit
plotly
joblib
```

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Data handling | pandas, NumPy |
| Visualization | matplotlib, seaborn, Plotly |
| Modeling | scikit-learn, LightGBM |
| App | Streamlit |
| Version control | Git, GitHub |

---

## 🗺️ Roadmap

- [x] Project setup and dataset download
- [ ] Data cleaning and exploration
- [ ] Price-vs-days-left analysis
- [ ] Buy/wait label and sensitivity check
- [ ] Baseline strategies
- [ ] Model training with group-based split
- [ ] Savings simulation
- [ ] Streamlit app and deployment
- [ ] Final write-up and LinkedIn post

**Future ideas**
- Add a price-alert simulation (how often a target price is reached)
- Validate findings on a second flight dataset
- Include holiday and festival effects if departure dates become available

---

## 🙏 Acknowledgements

- Dataset: [Shubham Bathwal on Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction), sourced from Ease My Trip

---

## 👤 Author

Parigi Anya Reddy

---

## 📄 License

This project is licensed under the MIT License. Check the dataset's own license on Kaggle before reusing the data.

