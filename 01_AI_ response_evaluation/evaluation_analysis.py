import pandas as pd

df = pd.read_csv("evaluation_data.csv")

print(df)

print("Average Scores:")
print(df[["Accuracy", "Relevance", "Clarity", "Instruction_Following", "Overall_Score"]].mean())
averages = df[
    ["Accuracy", "Relevance", "Clarity", "Instruction_Following", "Overall_Score"]
].mean()

print("\nWeakest criterion:")
print(averages.idxmin())

print("\nLowest average score:")
print(averages.min())
print("\nInstruction-following scores:")
print(df["Instruction_Following"].value_counts().sort_index())
good_instruction = (df["Instruction_Following"] >= 4).sum()
total = len(df)

print("\nResponses scoring 4/5 or higher:")
print(good_instruction)

print("\nPercentage:")
print((good_instruction / total) * 100)
print("\n--- AI RESPONSE EVALUATION SUMMARY ---")

print(f"Total evaluations: {len(df)}")
print(f"Average overall score: {df['Overall_Score'].mean():.2f}/5")
print(f"Instruction-following score >= 4: {good_instruction}/{total}")
print(f"Strong instruction-following rate: {(good_instruction / total) * 100:.1f}%")