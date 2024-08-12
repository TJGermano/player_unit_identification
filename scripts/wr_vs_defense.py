import nfl_data_py
import pandas as pd
import nfl_data_py as nfl

# Importing the play-by-play data for the specified year(s)
pbp = nfl_data_py.import_pbp_data([2023])

# Define the filter criteria to extract relevant data
filter_crit = ' pass_attempt == 1.0 '


# Apply filtering and group by passer details
pbp_p = (
    pbp.query(filter_crit)
    .groupby(["receiver_id", "receiver",
              #"defenders_in_box",
              #"number_of_pass_rushers",
              "defense_man_zone_type"
              ])
    .agg({"yards_gained": [ "mean"],"receiving_yards": [ "mean"],"play_id" :["count"],"epa": [ "mean"],"play_id" :["count"],"yards_after_catch": [ "mean"]})
)
# Flatten the multi-index columns and rename them
pbp_p.columns = list(map("_".join, pbp_p.columns.values))

# Sort the filtered data based on custom criteria
sort_crit = "play_id_count > 50"
sorted_pbp_p = pbp_p.query(sort_crit).sort_values(by="receiver", ascending=False)

# Convert the sorted DataFrame to a string and print
print(sorted_pbp_p.to_string())
