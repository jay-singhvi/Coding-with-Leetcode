"""
    570. Managers with at Least 5 Direct Reports
    https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
"""

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(
        employee[["id", "name", "managerId"]],
        employee[["id", "name"]],
        how="inner",
        left_on="managerId",
        right_on="id",
        suffixes=("", "_mgr"),
    )

    merged_df = merged_df.drop(columns="id_mgr")  # remove duplicate column due to merge

    managers = merged_df.groupby("managerId").filter(
        lambda x: len(x) >= 5
    )  # Group by managerid and filter manager having more than 5 subordinates

    distinct_managers = managers[
        ["managerId", "name_mgr"]
    ].drop_duplicates()  # Remove duplicates but not with distinct employee id

    return pd.DataFrame({"name": distinct_managers["name_mgr"]})
