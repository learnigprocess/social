
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv('social_ads.csv')

# --------------------
# Data Exploration
# --------------------
print("Basic Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTarget Variable Distribution (Purchased):")
print(df['Purchased'].value_counts())

# --------------------
# Insights Generation
# --------------------
# Insight 1: Age distribution
sns.histplot(df['Age'], kde=True, bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.clf()

# Insight 2: Estimated Salary distribution
sns.histplot(df['EstimatedSalary'], kde=True, color='green', bins=20)
plt.title('Estimated Salary Distribution')
plt.xlabel('Estimated Salary')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('salary_distribution.png')
plt.clf()

# Insight 3: Purchase vs Age
sns.boxplot(x='Purchased', y='Age', data=df)
plt.title('Age vs Purchase Behavior')
plt.tight_layout()
plt.savefig('purchase_by_age.png')
plt.clf()

# Insight 4: Purchase vs Estimated Salary
sns.boxplot(x='Purchased', y='EstimatedSalary', data=df)
plt.title('Salary vs Purchase Behavior')
plt.tight_layout()
plt.savefig('purchase_by_salary.png')
plt.clf()

# --------------------
# Load to MySQL
# --------------------
DB_USER = 'root'
DB_PASSWORD = '1234'
DB_HOST = 'localhost'
DB_NAME = 'etl_project'

engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
df.to_sql('social_ads', con=engine, if_exists='replace', index=False)

print("ETL process complete. Data loaded into MySQL and insights generated.")
