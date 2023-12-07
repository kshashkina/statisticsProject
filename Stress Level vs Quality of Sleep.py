import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Sleep_health_and_lifestyle_dataset.csv'
data = pd.read_csv(file_path)
stress_quality_sleep = data.groupby('Stress Level')['Quality of Sleep'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=stress_quality_sleep, x='Stress Level', y='Quality of Sleep', marker='o', color='green')
plt.title('Stress Level vs Quality of Sleep')
plt.xlabel('Stress Level')
plt.ylabel('Average Quality of Sleep')
plt.grid(True)
plt.show()