import pandas as pd

# Load the dataset
# file_path = 'C:\Users\Victor\Desktop\Class\4th\4.1\machine learning\data'
# file_path = 'C:/Users/Victor/Desktop/Class/4th/4.1/machine learning/data/dataset.xlsx'
file_path = r'C:\Users\Victor\Desktop\Class\4th\4.1\machine learning\data\dataset.xlsx'


df = pd.read_excel(file_path)

# Display initial information
print("Initial dataset shape:", df.shape)
print(df.info())

# Step 1: Drop any duplicates (if applicable)
df.drop_duplicates(inplace=True)

# Step 2: Handling missing values
# For numerical columns, you might fill with the mean or median
numerical_cols = ['rainfall', 'elevation', 'slope', 'clay', 'humidity']
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mean(), inplace=True)

# For categorical columns, you could use mode or a placeholder
categorical_cols = ['province', 'district', 'division', 'month', 'Case_Outbreak_RVF']
for col in categorical_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)

# Step 3: Convert 'Year' column to a proper datetime if not already
df['Year'] = pd.to_datetime(df['Year'], format='%Y', errors='coerce').dt.year

# Step 4: Convert 'rainfall' to a positive value (if negative values are errors)
df['rainfall'] = df['rainfall'].abs()

# Step 5: Handle potential outliers based on domain knowledge
# Example: Rainfall and humidity are generally in certain ranges
# Adjust these thresholds based on your knowledge
df = df[(df['rainfall'] >= 0) & (df['humidity'] >= 0) & (df['humidity'] <= 100)]

# Step 6: Save the cleaned data
output_file = 'cleaned_dataset.xlsx'
df.to_excel(output_file, index=False)

print("Cleaned dataset saved as:", output_file)
print("Final dataset shape:", df.shape)
