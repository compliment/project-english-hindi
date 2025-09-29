import pandas as pd 

df = pd.read_csv('essays.csv').astype(str)
print (df.count())

word_count_df = df.astype(str).apply(lambda x: x.str.split().str.len())

total_words_per_row = word_count_df.sum(axis=1)

df_filtered = df[total_words_per_row > 50]

print(f"Original number of rows: {len(df)}")
print(f"Filtered >50: {len(df_filtered)}")

df_filtered.to_csv("filtered.csv", index=False)


