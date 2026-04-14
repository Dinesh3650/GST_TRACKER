import pandas as pd

# 1. Create a list of business transactions
data = {
    'Date': ['2026-04-10', '2026-04-12', '2026-04-14'],
    'Description': ['Office Rent', 'Laptop Repair', 'Client Consulting'],
    'Category': ['Fixed', 'Maintenance', 'Income'],
    'Amount': [20000, 1500, 55000]
}

# 2. Convert to a DataFrame (Table)
df = pd.DataFrame(data)

# 3. Calculate 18% GST (Standard for most services in India)
df['GST_Amount'] = df['Amount'] * 0.18
df['Grand_Total'] = df['Amount'] + df['GST_Amount']

# 4. Save it to a professional Excel file
df.to_excel('GST_Report_April.xlsx', index=False, engine='xlsxwriter')
