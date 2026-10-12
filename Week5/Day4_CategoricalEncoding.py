import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "Department": ["IT", "HR", "Sales", "IT", "HR", "Sales"],
    "Performance": ["High", "Low", "Medium", "High", "Medium", "Low"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

label_encoder = LabelEncoder()

df["Performance_Encoded"] = label_encoder.fit_transform(
    df["Performance"]
)

print("\nLabel Encoded Dataset:")
print(df)

print("\nLabel Encoding Mapping:")
for category, value in zip(
    label_encoder.classes_,
    label_encoder.transform(label_encoder.classes_)
):
    print(category, ":", value)

onehot_encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown="ignore"
)

encoded_data = onehot_encoder.fit_transform(
    df[["Department"]]
)

encoded_df = pd.DataFrame(
    encoded_data,
    columns=onehot_encoder.get_feature_names_out(["Department"])
)

final_df = pd.concat([df, encoded_df], axis=1)

print("\nOne-Hot Encoded Dataset:")
print(final_df)
