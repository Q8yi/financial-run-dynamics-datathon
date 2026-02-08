import zipfile
import io
import os
import pandas as pd

def get_processed_files(folder):
    """
    Loop a folder, and convert all files in the folder to dataframe

    Args:
        folder: string => folder_path

    Output:
        dict: {folder_name: dataframe}
    """
    dfs = {}
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder, filename)
            df = pd.read_csv(file_path)
            if "date_standardized" in df.columns:
                df["date_standardized"] = pd.to_datetime(df["date_standardized"])
            elif "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
            key = filename.split("processed_")[-1].replace(".csv", "")
            dfs[key] = df
    return dfs