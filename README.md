# 💳 Lloyds Bank Customer Segmentation Dashboard

A comprehensive data science project that analyzes customer data to identify distinct customer segments and presents insights through an interactive Streamlit dashboard.

## 🎯 Project Overview

This project performs customer segmentation analysis for Lloyds Bank using machine learning clustering techniques. The analysis identifies four key customer segments:

- **High Value** - Premium customers with high engagement
- **Budget Conscious** - Cost-aware customers seeking value
- **Family Focused** - Customers with family-oriented financial needs
- **Growth Potential** - Emerging customers with expansion opportunities

## 🚀 Features

- Interactive Streamlit dashboard for data visualization
- Customer segmentation using clustering algorithms
- Exploratory Data Analysis (EDA) notebooks
- Machine learning model training and evaluation
- Comprehensive data preprocessing and cleaning

## 📁 Project Structure

```
streamlit-lloyds-segments/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── create_datascience_env.sh      # Environment setup script
├── README.md                      # Project documentation
├── data/                          # Data files
│   ├── customer_segments.csv      # Processed customer segments
│   ├── Customer_Churn_Data_Large.csv  # Raw customer data
│   ├── final_dataframe.csv        # Final processed dataset
│   └── ...                        # Additional data files
├── notebooks/                     # Jupyter notebooks
│   ├── lloyds_EDA.ipynb          # Exploratory Data Analysis
│   └── lloyds_modelling.ipynb    # Machine Learning models
└── datascience_env/               # Virtual environment
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Option 1: Automated Setup (Recommended)

1. **Clone the repository:**
```bash
git clone https://github.com/21407alfredmunga/streamlit-lloyds-segments.git
cd streamlit-lloyds-segments
```

2. **Run the environment setup script:**
```bash
chmod +x create_datascience_env.sh
./create_datascience_env.sh
```

3. **Activate the environment:**
```bash
source datascience_env/bin/activate
```

### Option 2: Manual Setup

1. **Clone the repository:**
```bash
git clone https://github.com/21407alfredmunga/streamlit-lloyds-segments.git
cd streamlit-lloyds-segments
```

2. **Create and activate virtual environment:**
```bash
python3 -m venv datascience_env
source datascience_env/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Running the Dashboard

1. **Ensure the virtual environment is activated:**
```bash
source datascience_env/bin/activate
```

2. **Launch the Streamlit application:**
```bash
streamlit run app.py
```

3. **Access the dashboard:**
   - Open your web browser and go to `http://localhost:8501`
   - The dashboard will display customer segmentation insights and visualizations

### Exploring the Notebooks

1. **Start Jupyter Lab/Notebook:**
```bash
jupyter lab notebooks/
```

2. **Available notebooks:**
   - `lloyds_EDA.ipynb` - Comprehensive exploratory data analysis
   - `lloyds_modelling.ipynb` - Machine learning model development

## 📊 Data Description

The project uses customer data with the following key features:
- **Demographics**: Age, Gender, Marital Status
- **Financial**: Income Level, Account Balance, Transaction History
- **Behavioral**: Product Usage, Channel Preferences, Engagement Metrics

## 🔧 Key Technologies

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn
- **Development**: Jupyter Notebooks, Python 3.8+

## 📈 Customer Segments

The analysis identifies four distinct customer segments:

1. **High Value Customers**
   - Premium service users
   - High account balances
   - Multiple product holdings

2. **Budget Conscious Customers**
   - Value-seeking behavior
   - Lower transaction volumes
   - Cost-sensitive product preferences

3. **Family Focused Customers**
   - Family-oriented financial products
   - Regular savings patterns
   - Education and mortgage products

4. **Growth Potential Customers**
   - Emerging customer base
   - Increasing engagement trends
   - Expansion opportunities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Alfred Munga**
- GitHub: [@21407alfredmunga](https://github.com/21407alfredmunga)

## 🙏 Acknowledgments

- Lloyds Bank for the inspiration and data context
- Streamlit community for excellent documentation
- Open source contributors to the libraries used

## 📞 Support

If you encounter any issues or have questions:
1. Check the existing [Issues](https://github.com/21407alfredmunga/streamlit-lloyds-segments/issues)
2. Create a new issue with detailed description
3. Contact the maintainer directly

---

**Happy Analyzing! 📊✨**