import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')

# Calculate the count of individuals for each occupation
occupation_counts = data['Occupation'].value_counts()

# Filter occupations with more than 30 individuals
selected_occupations = occupation_counts[occupation_counts > 30].index

# Filter the original dataset based on selected occupations
filtered_data = data[data['Occupation'].isin(selected_occupations)]

custom_palette = {'None': 'darkgreen', 'Insomnia': 'lightgreen', 'Sleep Apnea': 'mediumseagreen'}


plt.figure(figsize=(15, 8))

sns.countplot(y='Occupation', hue='Sleep Disorder', data=filtered_data, palette=custom_palette)
plt.title('Distribution of Sleep Disorders Across Occupations (N > 30)')
plt.xlabel('Count')
plt.ylabel('Occupation')
plt.legend(title='Sleep Disorder', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
