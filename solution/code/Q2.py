import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from helpers import convert_date_to_milliseconds


def database_update(current_profiles, new_profiles):

    # first we get the deleted users
    deleted_users_id = current_profiles[~current_profiles['profile_id'].isin(
        new_profiles['profile_id']
    )]['profile_id']

    new_users = new_profiles[~new_profiles['profile_id'].isin(
        current_profiles['profile_id'])]
    # There are no new_users in this case. If there were new users
    # we could consider insterting them into the final dataframe
    # here is a bit confusing. If the new_profiles is from the database, why they don't have 'valid_from' and 'valid_to'
    # columns? Anyways, I assume these records are coming from the clinet and we need to append new dates
    today_datetime = datetime.utcnow()
    new_users['valid_from'] = convert_date_to_milliseconds(today_datetime)
    # this code  can be replaced by function above for the
    new_users['valid_to'] = 4102358400000
    # date specifed to remove hard coding parts. For example it can be said each user has 3 years
    # valid account and they need to login within this 3 year to extend or raectivate with
    # with activation email link if they don't login within 3 years.
    # end_datetime = today_datetime + relativedelta(years=3)
    # new_users['valid_to'] = convert_date_to_milliseconds(end_datetime)

    # Now the users that are present in the profile hostiry
    old_users = new_profiles[new_profiles['profile_id'].isin(
        current_profiles['profile_id'])]

    # in tis case the update citeria is email but we can have a pipeline
    # defining what is considered as to be updated user

    updated_users_id = old_users[~old_users['email'].isin(
        current_profiles['email'])]['profile_id']

    # performing a merge to get the valid_from and valid_to data from prodile_history
    # in tis case the update citeria is email but we can have a pipeline
    updated_users_df = pd.merge(old_users, current_profiles[[
                                'profile_id', 'valid_to', 'valid_from']], on='profile_id', how='left')

    # as the question asked to keep both the orignial table and the updated rows, we do a simple
    # concatination on binding rows
    # Finally, please output a list of the profile_ids that were updated (1) and deleted (2) in addition to the merged table
    return (
        ("Updated profilesID: ", updated_users_id),
        ("Deleted profilesID: ", deleted_users_id),
        ("Updated dataframe:", updated_users_df)
    )


# we first read the data. The current data for the profile has
# Valid_from and valid_to columns
# I assume that the profile_id is the unique key
current_profiles = pd.read_json(
    "../../datalake/profiles_history/profiles_history.json", lines=True
)  # at t=0

new_profiles = pd.read_json(
    "../../datalake/profiles_history/new_profiles.json", lines=True)  # new profiles

print(database_update(current_profiles, new_profiles))
