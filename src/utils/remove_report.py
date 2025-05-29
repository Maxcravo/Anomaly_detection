import os

dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = os.path.join(dir, "data/reports")

def remove_report(date: str) -> None:
  try:
    if os.path.exists(f"{path}/{date}.csv"):
      os.remove(f"{path}/{date}.csv")
      print(f"Report {date} removed successfully.")
  except Exception as e:
    print(f"Error in report removal: {e}")