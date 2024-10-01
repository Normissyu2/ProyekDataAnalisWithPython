# E-Commerce Data Analysis Dashboard

This project aims to analyze an e-commerce dataset and create an interactive dashboard using **Streamlit**. The dashboard provides insights into two main areas of analysis:

1. **Correlation between Return Rates and Total Orders**: This analysis examines how the return rate relates to the total number of orders and whether there is a significant correlation between these two factors.
2. **Top Product Categories by Sales and Revenue**: This analysis identifies the product categories with the highest sales and revenue.


## Project Structure

The project directory is organized as follows:

- `dashboard/`
  - `data1.csv`: The dataset containing return rates and total orders.
  - `data2.csv`: The dataset for order items and total sales per product category.
  - `dashboard.py`: The Python script that runs the Streamlit dashboard.
- `notebook.ipynb`: The Jupyter/Colab notebook for data analysis.
- `requirements.txt`: A file listing all the Python libraries required to run the project.
- `README.md`: This file, providing an overview of the project.
- `url.txt`: A file to store the link to the deployed dashboard (if applicable).

## Analysis Overview

### 1. Correlation between Return Rates and Total Orders

This part of the analysis uses a scatter plot to visualize the relationship between:
- **X-axis**: The sum of orders(`total_orders`).
- **Y-axis**: The value for return rate (`return_rate`).

### 2. Top Product Categories by Sales and Revenue
This part of the analysis uses a scatter plot to visualize the relationship between:
- **X-axis**: The sum of sales volume(`sales_voleme`).
- **Y-axis**: The name of city (`city`).

## Project Structure

The project directory is organized as follows:

- `dashboard/`
  - `data1_project.csv`: The dataset containing product photo quantities and review scores.
  - `data2_project.csv`: The dataset for sales and revenue analysis per product category.
  - `dashboard.py`: The Python script that runs the Streamlit dashboard.
- `notebook.ipynb`: The Jupyter/Colab notebook for data analysis.
- `requirements.txt`: A file listing all the Python libraries required to run the project.
- `README.md`: This file, providing an overview of the project.
- `url.txt`: A file to store the link to the deployed dashboard (if applicable).

## Analysis Overview
### 1. Correlation between Return Rates and Total Orders
This part of the analysis uses a scatter plot to visualize the relationship between:

- **X-axis**: Total orders (total_orders).
- **Y-axis**: Return rate (return_rate).
This visualization examines how the return rate relates to the total number of orders and whether there is a significant correlation between these two factors.

### 2. Sales Volume by City
This part of the analysis uses a bar chart to display:

- **X-axis**: Unique City Names
- **Y-axis**: Sales Volume
The chart visualizes the sales volume across different cities, highlighting which cities contribute most to total sales.


## How to Run the Dashboard

To run the dashboard locally, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/username/repository-name.git
    ```

2. Navigate into the project folder:
    ```bash
    cd repository-name
    ```

3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit dashboard:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

5. The dashboard will automatically open in your default web browser. If not, navigate to `http://localhost:8501/` manually.

## Libraries Used

This project utilizes the following libraries:

- `pandas`: For data manipulation and analysis.
- `streamlit`: For creating the interactive dashboard.
- `matplotlib`: For plotting graphs.
- `seaborn`: For statistical data visualization.
- `numpy`: For numerical operations.

## Example of Dashboard Visuals

- **Scatter Plot**: Relationship between total orders and returm rate
- **Bar & Line Plot**: Displaying the top 5 cities with the highest sales volume.

## Requirements

The required libraries are listed in the `requirements.txt` file. You can install them using:
```bash
pip install -r requirements.txt
