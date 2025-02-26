# streamlit_uv_project
Sir Zia Khan Assignment

# Data Sweeper

## 📌 Overview
**Data Sweeper** is a web-based application built using **Streamlit** that enables users to:
- Upload CSV or Excel files.
- View their contents in a tabular format.
- Perform basic data cleaning operations.
- Download the cleaned data in CSV or Excel format.

## 🚀 Features
- **File Upload**: Supports multiple file uploads (CSV & XLSX formats).
- **File Preview**: Displays a preview of the uploaded data.
- **Data Cleaning Options**:
  - Remove duplicate rows.
  - Fill missing values with column means.
  - Select specific columns to keep.
- **Data Visualization**: Generate simple line charts for numeric columns.
- **File Download**: Convert cleaned data into CSV or Excel format and download it.

## 🛠 Installation
To run the **Data Sweeper** locally, follow these steps:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/data-sweeper.git
cd data-sweeper
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages using UV:
```sh
uv pip install -r requirements.txt
```

### 3️⃣ Run the App
```sh
uv streamlit run app.py
```

## 📂 Project Structure
```
Data-Sweeper/
│── app.py               # Main Streamlit application
│── requirements.txt     # List of dependencies
│── README.md            # Project documentation
```

## 📦 Dependencies
This project uses the following Python libraries:
- `streamlit`
- `pandas`
- `openpyxl` (for handling Excel files)

Install them using UV:
```sh
uv pip install streamlit pandas openpyxl
```

## 🎯 Usage
1. Run the Streamlit app.
2. Upload a CSV or Excel file.
3. Preview and clean the data as needed.
4. Download the processed file.

## 🏆 Contributing
Feel free to fork this repository, create a new branch, and submit a pull request!

## 📜 License
This project is licensed under the MIT License.

## 👩‍💻 Author
Hira Khalid

---
🎉 **Enjoy using Data Sweeper!**










