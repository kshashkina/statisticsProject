import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Sleep_health_and_lifestyle_dataset.csv'
data = pd.read_csv(file_path)
# Line plot for Age vs Sleep Duration
age_sleep_duration = data.groupby('Age')['Sleep Duration'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=age_sleep_duration, x='Age', y='Sleep Duration', marker='o', color='green')
plt.title('Age vs Sleep Duration (Line Plot)')
plt.xlabel('Age (years)')
plt.ylabel('Sleep Duration (hours)')
plt.grid(True)
plt.show()