import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data dari return_rate.csv
category_return_rates = pd.read_csv('dashboard/return_rate.csv')

# Streamlit dashboard
st.title('Top 10 Product Categories by Return Rate')
# Sort data by return rate in descending order and limit to top 10 for better readability
top10_category_return_rates = category_return_rates.sort_values(by='return_rate', ascending=False).head(10)

# Create a figure for the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Set background style using seaborn
sns.set(style="whitegrid")

# Plot the return rate as a bar chart
sns.barplot(y='product_category_name', x='return_rate', data=top10_category_return_rates, ax=ax, color='lightblue')

# Set labels and title
ax.set_xlabel('Return Rate', fontsize=12, color='black')
ax.set_ylabel('Product Category', fontsize=12, color='black')
plt.title('Top 10 Product Categories by Return Rate', fontsize=14, color='black')

# Customize label colors
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# Adjust layout to make space for labels
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

data1 = pd.read_csv('data1.csv')

# Assuming data1 has columns: product_category_name, total_orders
# Here, calculate return rates or ensure you have total_orders in data1
# For example:
category_return_rates = data1.groupby('product_category_name').agg({'order_id': 'count'}).reset_index()
category_return_rates.rename(columns={'order_id': 'total_orders'}, inplace=True)

# Sort data by total orders in descending order and limit to top 10
top10_category_return_rates = category_return_rates.sort_values(by='total_orders', ascending=False).head(10)

# Streamlit dashboard
st.title('Top 10 Product Categories: Total Orders')

# Create a figure
fig, ax1 = plt.subplots(figsize=(10, 6))

# Set background style using seaborn
sns.set(style="whitegrid")

# Plot the total orders as a bar chart
sns.barplot(y='product_category_name', x='total_orders', data=top10_category_return_rates, ax=ax1, color='skyblue')

# Set labels with black font color
ax1.set_ylabel('Product Category', fontsize=12, color='black')
ax1.set_xlabel('Total Orders', fontsize=12, color='black')

# Adjust layout to make space for labels
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

# Display data table
st.subheader('Data for Top 10 Product Categories')
st.write(top10_category_return_rates)

# Load return_rate.csv
return_rates_df = pd.read_csv('return_rate.csv')

# Load data1.csv
data1_df = pd.read_csv('data1.csv')


# Merge the two DataFrames on 'product_category_name'
merged_data = pd.merge(return_rates_df, data1_df, on='product_category_name', how='inner')


# Check if required columns exist in the merged data
if 'total_orders' in merged_data.columns and 'return_rate' in merged_data.columns:
    # Visualize correlation between return_rate and total_orders
    st.title('Correlation between Return Rate and Total Orders')

    # Create a scatter plot for return_rate vs total_orders
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set background style using seaborn
    sns.set(style="whitegrid")

    # Plot the scatter plot
    sns.scatterplot(data=merged_data, x='total_orders', y='return_rate', ax=ax, color='orange')

    # Set labels and title
    ax.set_xlabel('Total Orders', fontsize=12, color='black')
    ax.set_ylabel('Return Rate', fontsize=12, color='black')
    plt.title('Correlation between Return Rate and Total Orders', fontsize=14, color='black')

    # Adjust layout to make space for labels
    plt.tight_layout()

    # Display the scatter plot in Streamlit
    st.pyplot(fig)

    # Display correlation coefficient
    correlation = merged_data['return_rate'].corr(merged_data['total_orders'])
    st.subheader('Correlation Coefficient')
    st.write(f'The correlation coefficient between return rate and total orders is: {correlation:.2f}')
else:
    st.write("Required columns for correlation analysis are missing in the merged data.")

# Load the merged dataset
merged_sellers_df = pd.read_csv('data2.csv')

# Calculate sales volume per city
sales_volume_per_city = merged_sellers_df.groupby('seller_city').agg({'order_item_id': 'count'}).reset_index()
sales_volume_per_city.rename(columns={'order_item_id': 'sales_volume'}, inplace=True)

# Get the top 5 cities by sales volume
top_5_cities = sales_volume_per_city.sort_values(by='sales_volume', ascending=False).head(5)

# Streamlit dashboard
st.title('E-Commerce Sales Dashboard')

# Display top 5 cities
st.header('Top 5 Cities with Highest Sales Volume')
st.bar_chart(top_5_cities.set_index('seller_city')['sales_volume'])

# Display data table
st.subheader('Sales Volume Data for Top 5 Cities')
st.write(top_5_cities)
