import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 

    "English": [
        "Good morning",
        "How are you?",
        "Thank you",
        "Please",
        "Come here",
        "I am hungry",
        "I am tired",
        "What is your name?",
        "I understand",
        "I don't understand",
    ],
    "Yoruba": [
        "E kaaro",
        "Bawo ni?",
        "E se",    
        "Jowo",
        "Wa sibi",
        "Ebi n pami",
        "O re mi",
        "Kini oruko re?",
        "o ye mi",
        "ko ye mi"
    ],        
    "Hausa": [
        "Ina kwana",
        "yaya ka/ki ke?",
        "Na gode",
        "Don Allah",
        "Zo nan",
        "Ina jin yunwa",
        "Na gaji",
        "Menene sunan ka/ki?",
        "Na fahimta",
        "Ban fahimta ba"
    ],
    "Category": [
        "Greeting",
        "Greeting",
        "Appreciation",
        "Request",
        "Instruction",
        "Daily life",
        "Daily life",
        "Question",
        "Communication",
        "Communication"
    ]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Category"].value_counts())
print(df[["English", "Yoruba", "Hausa"]].dtypes)
print(df.shape)
print(df.columns)
language_data = pd.melt(
    df,
    id_vars=["ID", "Category"],
    value_vars=["English", "Yoruba", "Hausa"],
    var_name="Language",
    value_name="Text"
)

print(language_data)
language_data[language_data["Language"] == "Yoruba"]
print(language_data["Language"].value_counts())
df.to_csv("multiligual_dataset.csv",
index=False)
print("Dataset saved successfully!")          