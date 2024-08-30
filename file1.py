# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Connect to the MySQL database
# db_conn = mysql.connector.connect(
#     host="localhost",   # Replace with your host, e.g., "127.0.0.1"
#     user="root",        # Replace with your MySQL username
#     password="2102901520070",# Replace with your MySQL password
#     database="ecommerce"
# )

# # Query to retrieve data from MySQL tables
# query_customers = "SELECT * FROM customer"
# query_products = "SELECT * FROM product"
# query_orders = "SELECT * FROM order_details"

# # Read data from MySQL tables into Pandas DataFrames
# customers_df = pd.read_sql(query_customers, db_conn)
# products_df = pd.read_sql(query_products, db_conn)
# orders_df = pd.read_sql(query_orders, db_conn)

# # Close the database connection
# db_conn.close()

# # Merge orders with customers and products to get full order details
# full_orders_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

# # Display the merged data
# print("\nFull Orders Data:")
# print(full_orders_df)

# # Plot the total sales by product
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Product')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the number of orders by city
# plt.figure(figsize=(10, 6))
# sns.countplot(x='city', data=full_orders_df)
# plt.title('Number of Orders by City')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the total sales by category
# plt.figure(figsize=(10, 6))
# sns.barplot(x='category', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Category')
# plt.xticks(rotation=45)
# plt.show()

# # Display order count and total sales by customer
# customer_sales = full_orders_df.groupby('name').agg({'order_id': 'count', 'total_price': 'sum'}).reset_index()
# customer_sales.columns = ['Customer Name', 'Order Count', 'Total Sales']
# print("\nCustomer Sales Summary:")
# print(customer_sales)

# # Plot the total sales by customer
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Customer Name', y='Total Sales', data=customer_sales)
# plt.title('Total Sales by Customer')
# plt.xticks(rotation=45)
# plt.show()

# # ============================================================================


# # ================================================================
# db_conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2102901520070",
#     database="ecommerce"
# )





























# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Connect to the MySQL database
# db_conn = mysql.connector.connect(
#     host="localhost",   
#     user="root",        
#     password="2102901520070",  
#     database="ecommerce"
# )

# # Query to retrieve data from MySQL tables
# query_customers = "SELECT * FROM customer"
# query_products = "SELECT * FROM product"
# query_orders = "SELECT * FROM order_details"

# # Read data from MySQL tables into Pandas DataFrames
# customers_df = pd.read_sql(query_customers, db_conn)
# products_df = pd.read_sql(query_products, db_conn)
# orders_df = pd.read_sql(query_orders, db_conn)

# # Close the database connection
# db_conn.close()

# # Merge orders with customers and products to get full order details
# full_orders_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

# # Display the merged data
# print("\nFull Orders Data:")
# print(full_orders_df)

# # Plot the total sales by product
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Product')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the number of orders by city
# plt.figure(figsize=(10, 6))
# sns.countplot(x='city', data=full_orders_df)
# plt.title('Number of Orders by City')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the total sales by category
# plt.figure(figsize=(10, 6))
# sns.barplot(x='category', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Category')
# plt.xticks(rotation=45)
# plt.show()

# # Display order count and total sales by customer
# customer_sales = full_orders_df.groupby('name').agg({'order_id': 'count', 'total_price': 'sum'}).reset_index()
# customer_sales.columns = ['Customer Name', 'Order Count', 'Total Sales']
# print("\nCustomer Sales Summary:")
# print(customer_sales)

# # Plot the total sales by customer
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Customer Name', y='Total Sales', data=customer_sales)
# plt.title('Total Sales by Customer')
# plt.xticks(rotation=45)
# plt.show()

# # ================= Additional Analysis ==================

# # 1. Create a bar chart for total number of customers city-wise
# customer_city_count = customers_df['city'].value_counts()
# plt.figure(figsize=(10, 6))
# customer_city_count.plot(kind='bar', color='skyblue')
# plt.title('Total Number of Customers City-Wise')
# plt.xlabel('City')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 2. Identify the most frequent customers based on their order history
# frequent_customers = full_orders_df['customer_id'].value_counts().reset_index()
# frequent_customers.columns = ['Customer ID', 'Order Count']
# print("\nMost frequent customers based on their order history:")
# print(frequent_customers.head())

# # Create a bar chart for the top 10 most frequent customers
# top_10_customers = frequent_customers.head(10)
# plt.figure(figsize=(10, 6))
# plt.bar(top_10_customers['Customer ID'], top_10_customers['Order Count'], color='salmon')
# plt.title('Top 10 Most Frequent Customers Based on Order History')
# plt.xlabel('Customer ID')
# plt.ylabel('Number of Orders')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Product Analysis

# # 3. Determine the total number of products available by category
# product_category_count = products_df['category'].value_counts()
# print("\nTotal number of products available by category:")
# print(product_category_count)

# # Create a bar chart for total number of products available by category
# plt.figure(figsize=(10, 6))
# product_category_count.plot(kind='bar', color='lightgreen')
# plt.title('Total Number of Products Available by Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 4. Analyze the distribution of products across sub-categories
# product_sub_category_distribution = products_df['sub_category'].value_counts()
# print("\nDistribution of products across sub-categories:")
# print(product_sub_category_distribution)

# # Create a bar chart for the distribution of products across sub-categories
# plt.figure(figsize=(10, 6))
# product_sub_category_distribution.plot(kind='bar', color='violet')
# plt.title('Distribution of Products Across Sub-Categories')
# plt.xlabel('Sub-Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# # ===================================================================================================================================

# customer_order_quantity = full_orders_df.groupby('name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
# max_order_customer = customer_order_quantity.iloc[0]
# min_order_customer = customer_order_quantity.iloc[-1]
# print(f"\nCustomer with the Highest Order Quantity: {max_order_customer['name']} ({max_order_customer['quantity']})")
# print(f"Customer with the Lowest Order Quantity: {min_order_customer['name']} ({min_order_customer['quantity']})")

# # Plot Customer Order Quantities
# plt.figure(figsize=(10, 6))
# sns.barplot(x='name', y='quantity', data=customer_order_quantity.head(10), palette='Set2')
# plt.title('Top 10 Customers with Highest Order Quantities')
# plt.xticks(rotation=45)
# plt.show()

# # 10. Month and year-wise total sale
# full_orders_df['order_date'] = pd.to_datetime(full_orders_df['order_date'])
# full_orders_df['year_month'] = full_orders_df['order_date'].dt.to_period('M')
# monthly_sales = full_orders_df.groupby('year_month')['total_price'].sum().reset_index()
# print("\nMonth and Year Wise Total Sale:")
# print(monthly_sales)

# # Plot Month and Year Wise Total Sale
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='year_month', y='total_price', data=monthly_sales, marker='o')
# plt.title('Month and Year Wise Total Sale')
# plt.xticks(rotation=45)
# plt.show()

# # 11. Identify peak order date
# peak_order_date = full_orders_df.groupby('order_date')['order_id'].count().reset_index().sort_values(by='order_id', ascending=False).iloc[0]
# print(f"\nPeak Order Date: {peak_order_date['order_date']} with {peak_order_date['order_id']} orders")

# # Plot Peak Order Date
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='order_date', y='order_id', data=full_orders_df.groupby('order_date')['order_id'].count().reset_index())
# plt.title('Orders Over Time')
# plt.xticks(rotation=45)
# plt.show()



# plt.figure(figsize=(8, 5))
# sns.barplot(x='Statistic', y='Price', data=price_stats, palette='Blues_r')
# plt.title('Price Statistics')
# plt.show()
# # ===========================================================================================================

# customer_city_count = customers_df['city'].value_counts()
# # ==================================================================
# frequent_customers = full_orders_df['customer_id'].value_counts().reset_index()
# # ================================================
# product_category_count = products_df['category'].value_counts()
# product_sub_category_distribution = products_df['sub_category'].value_counts()








































# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Connect to the MySQL database
# db_conn = mysql.connector.connect(
#     host="localhost",   
#     user="root",        
#     password="2102901520070",  
#     database="ecommerce"
# )

# # Query to retrieve data from MySQL tables
# query_customers = "SELECT * FROM customer"
# query_products = "SELECT * FROM product"
# query_orders = "SELECT * FROM order_details"

# # Read data from MySQL tables into Pandas DataFrames
# customers_df = pd.read_sql(query_customers, db_conn)
# products_df = pd.read_sql(query_products, db_conn)
# orders_df = pd.read_sql(query_orders, db_conn)

# # Close the database connection
# db_conn.close()

# # Merge orders with customers and products to get full order details
# full_orders_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

# # Display the merged data
# print("\nFull Orders Data:")
# print(full_orders_df.head())

# # Plot the total sales by product
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Product')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the number of orders by city
# plt.figure(figsize=(10, 6))
# sns.countplot(x='city', data=full_orders_df)
# plt.title('Number of Orders by City')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the total sales by category
# plt.figure(figsize=(10, 6))
# sns.barplot(x='category', y='total_price', data=full_orders_df, estimator=sum)
# plt.title('Total Sales by Category')
# plt.xticks(rotation=45)
# plt.show()

# # Display order count and total sales by customer
# customer_sales = full_orders_df.groupby('name').agg({'order_id': 'count', 'total_price': 'sum'}).reset_index()
# customer_sales.columns = ['Customer Name', 'Order Count', 'Total Sales']
# print("\nCustomer Sales Summary:")
# print(customer_sales.head())

# # Plot the total sales by customer
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Customer Name', y='Total Sales', data=customer_sales)
# plt.title('Total Sales by Customer')
# plt.xticks(rotation=45)
# plt.show()

# # ================= Additional Analysis ==================

# # 1. Create a bar chart for total number of customers city-wise
# customer_city_count = customers_df['city'].value_counts()
# plt.figure(figsize=(10, 6))
# customer_city_count.plot(kind='bar', color='skyblue')
# plt.title('Total Number of Customers City-Wise')
# plt.xlabel('City')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 2. Identify the most frequent customers based on their order history
# frequent_customers = full_orders_df['customer_id'].value_counts().reset_index()
# frequent_customers.columns = ['Customer ID', 'Order Count']
# print("\nMost frequent customers based on their order history:")
# print(frequent_customers.head())

# # Create a bar chart for the top 10 most frequent customers
# top_10_customers = frequent_customers.head(10)
# plt.figure(figsize=(10, 6))
# plt.bar(top_10_customers['Customer ID'], top_10_customers['Order Count'], color='salmon')
# plt.title('Top 10 Most Frequent Customers Based on Order History')
# plt.xlabel('Customer ID')
# plt.ylabel('Number of Orders')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Product Analysis

# # 3. Determine the total number of products available by category
# product_category_count = products_df['category'].value_counts()
# print("\nTotal number of products available by category:")
# print(product_category_count)

# # Create a bar chart for total number of products available by category
# plt.figure(figsize=(10, 6))
# product_category_count.plot(kind='bar', color='lightgreen')
# plt.title('Total Number of Products Available by Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 4. Analyze the distribution of products across sub-categories
# product_sub_category_distribution = products_df['sub_category'].value_counts()
# print("\nDistribution of products across sub-categories:")
# print(product_sub_category_distribution)

# # Create a bar chart for the distribution of products across sub-categories
# plt.figure(figsize=(10, 6))
# product_sub_category_distribution.plot(kind='bar', color='violet')
# plt.title('Distribution of Products Across Sub-Categories')
# plt.xlabel('Sub-Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 5. Customer order quantity analysis
# customer_order_quantity = full_orders_df.groupby('name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
# max_order_customer = customer_order_quantity.iloc[0]
# min_order_customer = customer_order_quantity.iloc[-1]
# print(f"\nCustomer with the Highest Order Quantity: {max_order_customer['name']} ({max_order_customer['quantity']})")
# print(f"Customer with the Lowest Order Quantity: {min_order_customer['name']} ({min_order_customer['quantity']})")

# # Plot Customer Order Quantities
# plt.figure(figsize=(10, 6))
# sns.barplot(x='name', y='quantity', data=customer_order_quantity.head(10))
# plt.title('Top 10 Customers with Highest Order Quantities')
# plt.xticks(rotation=45)
# plt.show()

# # 6. Month and year-wise total sales
# full_orders_df['order_date'] = pd.to_datetime(full_orders_df['order_date'])
# full_orders_df['year_month'] = full_orders_df['order_date'].dt.to_period('M').astype(str)
# monthly_sales = full_orders_df.groupby('year_month')['total_price'].sum().reset_index()
# print("\nMonth and Year Wise Total Sale:")
# print(monthly_sales)

# # Plot Month and Year Wise Total Sale
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='year_month', y='total_price', data=monthly_sales, marker='o')
# plt.title('Month and Year Wise Total Sale')
# plt.xticks(rotation=45)
# plt.show()

# # 7. Identify peak order date
# peak_order_date = full_orders_df.groupby('order_date')['order_id'].count().reset_index().sort_values(by='order_id', ascending=False).iloc[0]
# print(f"\nPeak Order Date: {peak_order_date['order_date']} with {peak_order_date['order_id']} orders")

# # Plot Peak Order Date
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='order_date', y='order_id', data=full_orders_df.groupby('order_date')['order_id'].count().reset_index())
# plt.title('Orders Over Time')
# plt.xticks(rotation=45)
# plt.show()





































# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Connect to the MySQL database
# db_conn = mysql.connector.connect(
#     host="localhost",   
#     user="root",        
#     password="2102901520070",  
#     database="ecommerce"
# )

# # Query to retrieve data from MySQL tables
# query_customers = "SELECT * FROM customer"
# query_products = "SELECT * FROM product"
# query_orders = "SELECT * FROM order_details"

# # Read data from MySQL tables into Pandas DataFrames
# customers_df = pd.read_sql(query_customers, db_conn)
# products_df = pd.read_sql(query_products, db_conn)
# orders_df = pd.read_sql(query_orders, db_conn)

# # Close the database connection
# db_conn.close()

# # Merge orders with customers and products to get full order details
# full_orders_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

# # Display the merged data
# print("\nFull Orders Data:")
# print(full_orders_df.head())

# # Plot the total sales by product
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='total_price', data=full_orders_df, estimator=sum, palette='viridis')
# plt.title('Total Sales by Product')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the number of orders by city
# plt.figure(figsize=(10, 6))
# sns.countplot(x='city', data=full_orders_df, palette='viridis')
# plt.title('Number of Orders by City')
# plt.xticks(rotation=45)
# plt.show()

# # Plot the total sales by category
# plt.figure(figsize=(10, 6))
# sns.barplot(x='category', y='total_price', data=full_orders_df, estimator=sum, palette='viridis')
# plt.title('Total Sales by Category')
# plt.xticks(rotation=45)
# plt.show()

# # Display order count and total sales by customer
# customer_sales = full_orders_df.groupby('name').agg({'order_id': 'count', 'total_price': 'sum'}).reset_index()
# customer_sales.columns = ['Customer Name', 'Order Count', 'Total Sales']
# print("\nCustomer Sales Summary:")
# print(customer_sales.head())

# # Plot the total sales by customer
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Customer Name', y='Total Sales', data=customer_sales, palette='viridis')
# plt.title('Total Sales by Customer')
# plt.xticks(rotation=45)
# plt.show()

# # ================= Additional Analysis ==================

# # 1. Create a bar chart for total number of customers city-wise
# customer_city_count = customers_df['city'].value_counts()
# plt.figure(figsize=(10, 6))
# customer_city_count.plot(kind='bar', color='skyblue')
# plt.title('Total Number of Customers City-Wise')
# plt.xlabel('City')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 2. Identify the most frequent customers based on their order history
# frequent_customers = full_orders_df['customer_id'].value_counts().reset_index()
# frequent_customers.columns = ['Customer ID', 'Order Count']
# print("\nMost frequent customers based on their order history:")
# print(frequent_customers.head())

# # Create a bar chart for the top 10 most frequent customers
# top_10_customers = frequent_customers.head(10)
# plt.figure(figsize=(10, 6))
# plt.bar(top_10_customers['Customer ID'].astype(str), top_10_customers['Order Count'], color='salmon')
# plt.title('Top 10 Most Frequent Customers Based on Order History')
# plt.xlabel('Customer ID')
# plt.ylabel('Number of Orders')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Product Analysis

# # 3. Determine the total number of products available by category
# product_category_count = products_df['category'].value_counts()
# print("\nTotal number of products available by category:")
# print(product_category_count)

# # Create a bar chart for total number of products available by category
# plt.figure(figsize=(10, 6))
# product_category_count.plot(kind='bar', color='lightgreen')
# plt.title('Total Number of Products Available by Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 4. Analyze the distribution of products across sub-categories
# product_sub_category_distribution = products_df['sub_category'].value_counts()
# print("\nDistribution of products across sub-categories:")
# print(product_sub_category_distribution)

# # Create a bar chart for the distribution of products across sub-categories
# plt.figure(figsize=(10, 6))
# product_sub_category_distribution.plot(kind='bar', color='violet')
# plt.title('Distribution of Products Across Sub-Categories')
# plt.xlabel('Sub-Category')
# plt.ylabel('Number of Products')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # 5. Customer order quantity analysis
# customer_order_quantity = full_orders_df.groupby('name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
# max_order_customer = customer_order_quantity.iloc[0]
# min_order_customer = customer_order_quantity.iloc[-1]
# print(f"\nCustomer with the Highest Order Quantity: {max_order_customer['name']} ({max_order_customer['quantity']})")
# print(f"Customer with the Lowest Order Quantity: {min_order_customer['name']} ({min_order_customer['quantity']})")

# # Plot Customer Order Quantities
# plt.figure(figsize=(10, 6))
# sns.barplot(x='name', y='quantity', data=customer_order_quantity.head(10), palette='Set2')
# plt.title('Top 10 Customers with Highest Order Quantities')
# plt.xticks(rotation=45)
# plt.show()

# # 6. Month and year-wise total sales
# full_orders_df['order_date'] = pd.to_datetime(full_orders_df['order_date'])
# full_orders_df['year_month'] = full_orders_df['order_date'].dt.to_period('M')
# monthly_sales = full_orders_df.groupby('year_month')['total_price'].sum().reset_index()
# print("\nMonth and Year Wise Total Sale:")
# print(monthly_sales)

# # Plot Month and Year Wise Total Sale
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='year_month', y='total_price', data=monthly_sales, marker='o')
# plt.title('Month and Year Wise Total Sale')
# plt.xticks(rotation=45)
# plt.show()

# # 7. Identify peak order date
# peak_order_date = full_orders_df.groupby('order_date')['order_id'].count().reset_index().sort_values(by='order_id', ascending=False).iloc[0]
# print(f"\nPeak Order Date: {peak_order_date['order_date']} with {peak_order_date['order_id']} orders")

# # Plot Peak Order Date
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='order_date', y='order_id', data=full_orders_df.groupby('order_date')['order_id'].count().reset_index())
# plt.title('Orders Over Time')
# plt.xticks(rotation=45)
# plt.show()

# # 11. Geographical Analysis: Explore the distribution of customers across different cities
# city_distribution = customers_df['city'].value_counts()
# print("\nDistribution of Customers Across Different Cities:")
# print(city_distribution)

# # Plot Distribution of Customers Across Different Cities
# plt.figure(figsize=(10, 6))
# city_distribution.plot(kind='bar', color='skyblue')
# plt.title('Distribution of Customers Across Different Cities')
# plt.xlabel('City')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.show()

# # 12. Product Performance: Identify the best-selling products
# best_selling_products = full_orders_df.groupby('product_name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
# print("\nBest-Selling Products:")
# print(best_selling_products.head(10))

# # Plot Best-Selling Products
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='quantity', data=best_selling_products.head(10), palette='coolwarm')
# plt.title('Top 10 Best-Selling Products')
# plt.xticks(rotation=45)
# plt.show()

# # 13. Identify top 10 slow-moving products based on low sales
# slow_moving_products = full_orders_df.groupby('product_name')['total_price'].sum().reset_index().sort_values(by='total_price', ascending=True).head(10)
# print("\nTop 10 Slow-Moving Products Based on Low Sales:")
# print(slow_moving_products)

# # Plot Slow-Moving Products
# plt.figure(figsize=(10, 6))
# sns.barplot(x='product_name', y='total_price', data=slow_moving_products, palette='magma')
# plt.title('Top 10 Slow-Moving Products by Revenue')
# plt.xticks(rotation=45)
# plt.show()

# # 14. Payment Analysis: Display successful and pending payments order counts
# payment_status = full_orders_df['payment_status'].value_counts()
# print("\nPayment Status Order Counts:")
# print(payment_status)

# # Plot Payment Status Order Counts
# plt.figure(figsize=(10, 6))
# sns.barplot(x=payment_status.index, y=payment_status.values, palette='deep')
# plt.title('Payment Status Order Counts')
# plt.xlabel('Payment Status')
# plt.ylabel('Order Count')
# plt.show()





































import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the MySQL database
db_conn = mysql.connector.connect(
    host="localhost",   
    user="root",        
    password="2102901520070",  
    database="ecommerce"
)

# Query to retrieve data from MySQL tables
query_customers = "SELECT * FROM customer"
query_products = "SELECT * FROM product"
query_orders = "SELECT * FROM order_details"

# Read data from MySQL tables into Pandas DataFrames
customers_df = pd.read_sql(query_customers, db_conn)
products_df = pd.read_sql(query_products, db_conn)
orders_df = pd.read_sql(query_orders, db_conn)

# Close the database connection
db_conn.close()

# Merge orders with customers and products to get full order details
full_orders_df = orders_df.merge(customers_df, on='customer_id').merge(products_df, on='product_id')

# Display the merged data
print("\nFull Orders Data:")
print(full_orders_df.head())

# Plot the total sales by product
plt.figure(figsize=(10, 6))
sns.barplot(x='product_name', y='total_price', data=full_orders_df, estimator=sum, palette='viridis')
plt.title('Total Sales by Product')
plt.xticks(rotation=45)
plt.show()

# Plot the number of orders by city
plt.figure(figsize=(10, 6))
sns.countplot(x='city', data=full_orders_df, palette='viridis')
plt.title('Number of Orders by City')
plt.xticks(rotation=45)
plt.show()

# Plot the total sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='total_price', data=full_orders_df, estimator=sum, palette='viridis')
plt.title('Total Sales by Category')
plt.xticks(rotation=45)
plt.show()

# Display order count and total sales by customer
customer_sales = full_orders_df.groupby('name').agg({'order_id': 'count', 'total_price': 'sum'}).reset_index()
customer_sales.columns = ['Customer Name', 'Order Count', 'Total Sales']
print("\nCustomer Sales Summary:")
print(customer_sales.head())

# Plot the total sales by customer
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Name', y='Total Sales', data=customer_sales, palette='viridis')
plt.title('Total Sales by Customer')
plt.xticks(rotation=45)
plt.show()

# ================= Additional Analysis ==================

# 1. Create a bar chart for total number of customers city-wise
customer_city_count = customers_df['city'].value_counts()
plt.figure(figsize=(10, 6))
customer_city_count.plot(kind='bar', color='skyblue')
plt.title('Total Number of Customers City-Wise')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Identify the most frequent customers based on their order history
frequent_customers = full_orders_df['customer_id'].value_counts().reset_index()
frequent_customers.columns = ['Customer ID', 'Order Count']
print("\nMost frequent customers based on their order history:")
print(frequent_customers.head())

# Create a bar chart for the top 10 most frequent customers
top_10_customers = frequent_customers.head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10_customers['Customer ID'].astype(str), top_10_customers['Order Count'], color='salmon')
plt.title('Top 10 Most Frequent Customers Based on Order History')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Product Analysis

# 3. Determine the total number of products available by category
product_category_count = products_df['category'].value_counts()
print("\nTotal number of products available by category:")
print(product_category_count)

# Create a bar chart for total number of products available by category
plt.figure(figsize=(10, 6))
product_category_count.plot(kind='bar', color='lightgreen')
plt.title('Total Number of Products Available by Category')
plt.xlabel('Category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Analyze the distribution of products across sub-categories
product_sub_category_distribution = products_df['sub_category'].value_counts()
print("\nDistribution of products across sub-categories:")
print(product_sub_category_distribution)

# Create a bar chart for the distribution of products across sub-categories
plt.figure(figsize=(10, 6))
product_sub_category_distribution.plot(kind='bar', color='violet')
plt.title('Distribution of Products Across Sub-Categories')
plt.xlabel('Sub-Category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Customer order quantity analysis
customer_order_quantity = full_orders_df.groupby('name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
max_order_customer = customer_order_quantity.iloc[0]
min_order_customer = customer_order_quantity.iloc[-1]
print(f"\nCustomer with the Highest Order Quantity: {max_order_customer['name']} ({max_order_customer['quantity']})")
print(f"Customer with the Lowest Order Quantity: {min_order_customer['name']} ({min_order_customer['quantity']})")

# Plot Customer Order Quantities
plt.figure(figsize=(10, 6))
sns.barplot(x='name', y='quantity', data=customer_order_quantity.head(10))
plt.title('Top 10 Customers with Highest Order Quantities')
plt.xticks(rotation=45)
plt.show()

# 6. Month and year-wise total sales
full_orders_df['order_date'] = pd.to_datetime(full_orders_df['order_date'])
full_orders_df['year_month'] = full_orders_df['order_date'].dt.to_period('M')
monthly_sales = full_orders_df.groupby('year_month')['total_price'].sum().reset_index()
monthly_sales['year_month'] = monthly_sales['year_month'].astype(str)  # Ensure the period is treated as string for plotting
print("\nMonth and Year Wise Total Sale:")
print(monthly_sales)

# Plot Month and Year Wise Total Sale
plt.figure(figsize=(10, 6))
sns.lineplot(x='year_month', y='total_price', data=monthly_sales, marker='o')
plt.title('Month and Year Wise Total Sale')
plt.xticks(rotation=45)
plt.show()

# 7. Identify peak order date
peak_order_date = full_orders_df.groupby('order_date')['order_id'].count().reset_index().sort_values(by='order_id', ascending=False).iloc[0]
print(f"\nPeak Order Date: {peak_order_date['order_date']} with {peak_order_date['order_id']} orders")

# Plot Peak Order Date
plt.figure(figsize=(10, 6))
sns.lineplot(x='order_date', y='order_id', data=full_orders_df.groupby('order_date')['order_id'].count().reset_index())
plt.title('Orders Over Time')
plt.xticks(rotation=45)
plt.show()

# 8. Geographical Analysis: Explore the distribution of customers across different cities
city_distribution = customers_df['city'].value_counts()
print("\nDistribution of Customers Across Different Cities:")
print(city_distribution)

# Plot Distribution of Customers Across Different Cities
plt.figure(figsize=(10, 6))
city_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribution of Customers Across Different Cities')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.show()

# 9. Product Performance: Identify the best-selling products
best_selling_products = full_orders_df.groupby('product_name')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False)
print("\nBest-Selling Products:")
print(best_selling_products.head(10))

# Plot Best-Selling Products
plt.figure(figsize=(10, 6))
sns.barplot(x='product_name', y='quantity', data=best_selling_products.head(10), palette='coolwarm')
plt.title('Top 10 Best-Selling Products')
plt.xticks(rotation=45)
plt.show()

# 10. Identify top 10 slow-moving products based on low sales
slow_moving_products = full_orders_df.groupby('product_name')['total_price'].sum().reset_index().sort_values(by='total_price', ascending=True).head(10)
print("\nTop 10 Slow-Moving Products Based on Low Sales:")
print(slow_moving_products)







































































