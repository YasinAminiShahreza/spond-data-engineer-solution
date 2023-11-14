# from pyspark.sql import SparkSession

# # Create a Spark session
# spark = SparkSession.builder.appName("VerifySparkOperation").getOrCreate()

# # Verify Spark operation
# sample_data = [("John", 30), ("Alice", 25), ("Bob", 35)]
# df = spark.createDataFrame(sample_data, ["Name", "Age"])
# df.show()

# # Stop the Spark session
# spark.stop()
# %%
from datetime import datetime
import pandas as pd
from helpers import convert_time
group_df = pd.read_parquet("../../datalake/group", engine='pyarrow')

# group_df.head(5)
# group_df['country_code'].unique()
# group_df['group_name'].unique()
# group_df['is_admin'].unique()

# filtering the data based on three conditions:

condition1 = group_df['country_code'] == 'USA'
condition2 = group_df['is_admin'] == 'true'
condition3 = group_df['group_name'].isin(['Running Club', 'Tennis Club'])

filtered_group_df = group_df[condition1 & condition2 & condition3].dropna(subset=[
                                                                          'profile_id'])
filtered_group_df['profile_id'] = filtered_group_df['profile_id'].astype(int)

# %%
# I didn't quite understand the difference between profile.jason,
# new_profiles.json and profiles_history.json
profile_df = pd.read_json(
    "../../datalake/profile/created_at=2023-01-05/profile.json")

profile_email_df = pd.merge(filtered_group_df, profile_df,
                            on='profile_id', how='left').dropna(subset='email')
unsubscribe_df = pd.read_csv(
    '../../datalake/unsubscribe/unsubscribe.csv', on_bad_lines='skip',
    header=None, names=['emails'])

not_in_unsub = ~profile_email_df['email'].isin(unsubscribe_df['emails'])

final_profile_df = profile_email_df[not_in_unsub]

print(final_profile_df.head())

# %%
new_profiles_df = pd.read_json(
    "../../datalake/profiles_history/new_profiles.json", lines=True)

profiles_history_df = pd.read_json(
    "../../datalake/profiles_history/profiles_history.json", lines=True
)

all_profile_df = pd.concat(
    [profiles_history_df, new_profiles_df], ignore_index=True).drop_duplicates()

all_profile_df['valed_from_date'] = all_profile_df['valid_from'].apply(
    convert_time)

all_profile_df['valed_to_date'] = all_profile_df['valid_to'].apply(
    convert_time)

new_history_df = pd.merge(filtered_group_df, all_profile_df,
                          on='profile_id', how='left').dropna(subset='email')

new_history_df.head()


# %%
# As it seems new_profiles is a subset of
# profile_history with different emails, to make sure I'm not missing
# any records, I'll bind rows and remove duplicates


# %%
profile_df.head()
# %%
# new_profiles_df.head()
print(len(new_profiles_df))
# %%
profiles_history_df.head()

# %%

# %%
