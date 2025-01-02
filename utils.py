from datetime import datetime

def is_valid_datetime(date_string, date_format="%Y/%m/%d"):
    try:
        # Try to parse the date string with the provided format
        datetime.strptime(date_string, date_format)
        
        return True  # If parsing is successful, return True
    except:
        return False  # If an error occurs, it's not a valid datetime string

# def get_similar_websites(df, target_domain):
#     if "instance of" not in df or 'Num_Snapshots' not in df:
#         raise KeyError("Required fields 'instance of' or 'Num_Snapshots' are missing.")
    

def calculate_percentile(df, target_domain):

    # Ensure relevant columns exist
    if "instance of" not in df or 'Num_Snapshots' not in df:
        raise KeyError("Required fields 'instance of' or 'Num_Snapshots' are missing.")

    # Get the 'instance of' value for the target domain
    target_instance = df.loc[df["Domain"] == target_domain, "instance of"].iloc[0]

    # Filter domains with the same 'instance of'
    filtered_df = df[df["instance of"] == target_instance]

    # Get the 'num_snapshots' values
    snapshots = filtered_df['Num_Snapshots'].dropna().astype(float)

    # Get the target domain's 'num_snapshots'
    target_snapshots = df.loc[df["Domain"] == target_domain, 'Num_Snapshots'].values[0]

    # Calculate the percentile rank
    percentile = (snapshots < target_snapshots).mean() * 100
    return percentile