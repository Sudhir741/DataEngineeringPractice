import pandas as pd

# reading
df = pd.read_excel('Project\\sample_ecommerce_data.xlsx')

# missing value
df.dropna(inplace=True)

# data type correction
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Product Price'] = df['Product Price'].astype(float)
df['Quantity Sold'] = df['Quantity Sold'].astype(int)
# print(new_df1)
# print(new_df2)
# print(new_df3)

# removing spaces and changing all in lower case
df['Product Category'] = df['Product Category'].str.lower().str.strip()
df['Product Subcategory'] = df['Product Subcategory'].str.lower().str.strip()

# print(df_normalizing1)
# print(df_normalizing


#creating new Total Sales
df['Total Sales'] = df['Product Price'] * df['Quantity Sold']
# print(new_col1)

# taking year and month from transaction date and forming transaction_month column
df['Transaction Month'] = df['Transaction Date'].dt.to_period('M')
# print(new_col2)



# File export
df.to_csv('processed_data.csv', index=False)
