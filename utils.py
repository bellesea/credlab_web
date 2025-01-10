from datetime import datetime

def is_valid_datetime(date_string, date_format="%Y/%m/%d"):
    try:
        # Try to parse the date string with the provided format
        datetime.strptime(date_string, date_format)
        
        return True  # If parsing is successful, return True
    except:
        return False  # If an error occurs, it's not a valid datetime string

def get_same_category(df, domain):
    # Ensure relevant columns exist
    if "instance of" not in df:
        raise KeyError("Required field 'instance of' is missing.")
    
    domain_row = df[df['Domain']==domain]
    
    # Get the 'instance of' value for the target domain (is a list)
    target_instances = domain_row['instance of'].values[0]

    filtered_df = df[df["instance of"].isin([target_instances])]
    return filtered_df, target_instances[0]

def calculate_percentile(df, domain):

    filtered_df = get_same_category(df, domain)

    # Get the 'num_snapshots' values
    snapshots = filtered_df['Num_Snapshots'].dropna().astype(float)

    # Get the target domain's 'num_snapshots'
    target_snapshots = df.loc[df["Domain"] == domain, 'Num_Snapshots'].values[0]

    # Calculate the percentile rank
    percentile = (snapshots < target_snapshots).mean() * 100
    return percentile