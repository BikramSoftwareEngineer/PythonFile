import pandas as pd

def clean_titanic_data(file_path):
    print("--- 1. Loading Dataset ---")
    df = pd.read_csv(file_path)
    print(f"Original shape: {df.shape}")
    
    print("\n--- 2. Removing Duplicates ---")
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    print("\n--- 3. Cleaning Text and Categorical Columns ---")
    
    df['Sex'] = df['Sex'].str.lower().str.strip()
    df['Embarked'] = df['Embarked'].str.upper().str.strip()
    
   
    df = df.dropna(subset=['Name', 'Ticket', 'Embarked'])
    
    print("\n--- 4. Handling Missing Values ---")
    
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    
    
    df['Has_Cabin'] = df['Cabin'].notna().astype(int)
    df = df.drop(columns=['Cabin'])
    
    print("\n--- 5. Feature Engineering ---")
    
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    
    
    title_mapping = {
        'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master',
        'Dr': 'Rare', 'Rev': 'Rare', 'Col': 'Rare', 'Mlle': 'Miss', 
        'Major': 'Rare', 'Ms': 'Miss', 'Lady': 'Rare', 'Sir': 'Rare', 
        'Mme': 'Mrs', 'Don': 'Rare', 'Capt': 'Rare', 'Countess': 'Rare', 
        'Jonkheer': 'Rare', 'Dona': 'Rare'
    }
    df['Title'] = df['Title'].map(title_mapping).fillna('Rare')
    
    
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    print("\n--- 6. Encoding Categorical Variables ---")
    
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    
    
    df = pd.get_dummies(df, columns=['Embarked', 'Title'], drop_first=True)
    
    print(f"\nCleaned dataset shape: {df.shape}")
    print("Remaining missing values:\n", df.isnull().sum()[df.isnull().sum() > 0])
    
    return df


cleaned_df = clean_titanic_data('titanic.csv')


cleaned_df.to_csv('cleaned_titanic.csv', index=False)
print("\nCleaned dataset successfully saved to 'cleaned_cleaned_titanic.csv'!")