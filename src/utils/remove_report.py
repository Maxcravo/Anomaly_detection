import os
import pandas as pd

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = os.path.join(dir, "data/reports")

def remove_report(date: str, time: str) -> None:
  try:
    if os.path.exists(f"{path}/{date}.csv"):
      df = pd.read_csv(f"{path}/{date}.csv")
      for row in df.itertuples():
        if row.time == time:
          df.drop(row.Index, inplace=True)
          df.to_csv(f"{path}/{date}.csv", index=False)
      print(f"Report {date} removed successfully.")
  except Exception as e:
    print(f"Error in report removal: {e}")