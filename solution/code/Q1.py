import pandas as pd
df = pd.read_parquet("../../datalake/group", engine='pyarrow')


def filtered_df(group_df):

    condition1 = group_df['country_code'] == 'USA'
    condition2 = group_df['is_admin'] == 'true'
    condition3 = group_df['group_name'].isin(['Running Club', 'Tennis Club'])

    filtered_group_df = group_df[condition1 & condition2 & condition3].dropna(subset=[
        'profile_id'])
    filtered_group_df['profile_id'] = filtered_group_df['profile_id'].astype(
        int)

    profile_df = pd.read_json(
        "../../datalake/profile/created_at=2023-01-05/profile.json")

    profile_email_df = pd.merge(filtered_group_df, profile_df,
                                on='profile_id', how='left').dropna(subset='email')
    unsubscribe_df = pd.read_csv(
        '../../datalake/unsubscribe/unsubscribe.csv', on_bad_lines='skip',
        header=None, names=['emails'])

    not_in_unsub = ~profile_email_df['email'].isin(unsubscribe_df['emails'])

    final_profile_df = profile_email_df[not_in_unsub]

    return final_profile_df


print(filtered_df(df))
