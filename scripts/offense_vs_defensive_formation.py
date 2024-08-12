import nfl_data_py as nfl
import numpy as np
import pandas as pd

# Set display options for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# Importing the play-by-play data for the specified year(s)
pbp = nfl.import_pbp_data([2023])

# Define filter criteria
filter_crit = 'defteam == "DAL"'


# Apply filtering and group by defense and offense details
pbp_p = (
    pbp.query(filter_crit)
    .groupby(["posteam","defense_man_zone_type","play_type"])
    .agg(
        yards_gained_mean=("yards_gained", "mean"),
        air_yards_mean=("air_yards", "mean"),
        play_id_count=("play_id", "count"),
        epa_mean=("epa", "mean")
    )
)

# Calculate play_id percentage
pbp_p["play_id_percent"] = pbp_p["play_id_count"] / pbp_p["play_id_count"].sum() * 100

# Sort the filtered data based on custom criteria
sort_crit = "play_id_count > 1"
sorted_pbp_p = pbp_p.query(sort_crit).sort_values(by="posteam", ascending=False)

# Convert the sorted DataFrame to a string and print
print(sorted_pbp_p.to_string())
