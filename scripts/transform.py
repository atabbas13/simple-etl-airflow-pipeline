# Main Transformation script
import pandas as pd

def transform(data):
    df = pd.DataFrame(data)
    df_clean = df[["id", "name", "email", "phone", "website"]]
    df_clean.columns = ["user_id", "name", "email", "phone", "website"]
    return df_clean
