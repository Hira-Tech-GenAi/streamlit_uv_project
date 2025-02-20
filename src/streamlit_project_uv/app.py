# type: ignore
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the Streamlit page configuration
st.set_page_config(page_title="💽 Data Sweeper", page_icon=":tada:", layout="wide")

# Title and description
st.title("💽 Data Sweeper")
st.write("""
Welcome to Data Sweeper! This app allows you to:
- Select and upload CSV or Excel files.
- View their contents in a tabular format.
- Perform basic data cleaning.
- Download cleaned data in CSV or Excel format.
""")

# File upload section
uploaded_files = st.file_uploader("Upload your files 📂 (CSV or XLSX):", type=["csv", "xlsx"], accept_multiple_files=True)

# Process each uploaded file
if uploaded_files:
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Invalid file format. Please upload a CSV or XLSX file. (Uploaded: {file_extension})")
            continue

        # Display file information
        st.write(f"### 📄 File Name: {file.name}")
        st.write(f"📏 File Size: {file.size / 1024:.2f} KB")

        # Preview the dataframe
        st.write("### 🔍 Preview of the Data")
        st.dataframe(df.head())

        # Data cleaning options
        st.write("### 🛠 Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed successfully!")
            
            with col2:
                if st.button(f"Fill Missing Values in {file.name}"):
                    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
                    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
                    st.success("Missing values filled with column means.")

            # Select specific columns to keep
            st.subheader("🎯 Select Columns to Keep")
            selected_columns = st.multiselect(f"Select columns for {file.name}:", df.columns, default=df.columns.tolist())
            df = df[selected_columns]

            # Visualization
            st.subheader("📊 Data Visualizations")
            if st.checkbox(f"Show Visualizations for {file.name}"):
                numeric_df = df.select_dtypes(include=['float64', 'int64'])
                if not numeric_df.empty:
                    st.line_chart(numeric_df)
                else:
                    st.warning("No numeric columns available for visualization.")

            # Conversion to CSV or Excel
            st.subheader("📝 Convert & Download Data")
            conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                file_name = os.path.splitext(file.name)[0]
                mime_type = ""

                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    mime_type = "text/csv"
                    file_ext = "csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    file_ext = "xlsx"
                
                buffer.seek(0)
                st.download_button(
                    label=f"⬇ Download {file_name}.{file_ext}",
                    data=buffer.getvalue(),
                    file_name=f"{file_name}.{file_ext}",
                    mime=mime_type
                )

st.success("🎉 Thanks for using Data Sweeper! All files processed.")
