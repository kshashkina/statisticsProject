import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Sleep_health_and_lifestyle_dataset.csv'
data = pd.read_csv(file_path)
"""
Creates a pair plot to explore relationships between sleep quality, lifestyle factors, and sleep disorders.
"""
# Select and copy relevant columns
relevant_columns = ['Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'BMI Category',
                    'Blood Pressure', 'Heart Rate', 'Daily Steps', 'Sleep Disorder']
pairplot_data = data[relevant_columns].copy()

# Convert to categorical for better plotting
pairplot_data['BMI Category'] = pairplot_data['BMI Category'].astype('category')
pairplot_data['Sleep Disorder'] = pairplot_data['Sleep Disorder'].astype('category')

# Create pair plot
sns.pairplot(pairplot_data, hue='Sleep Disorder', diag_kind='kde')
plt.suptitle('Pair Plot of Sleep Quality, Lifestyle Factors, and Sleep Disorders', y=1.02)
plt.show()
