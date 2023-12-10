import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    print(df)
    df = pd.pivot_table(df,values="car", index=["id_1"], columns=["id_2"])
    df = df.fillna(0)
    print(df)

    return df

def sort_type(row):
    if row["car"] <= 15:
        car_type = "low"
    elif 15 < row["car"] <=25:
        car_type = "medium"
    else:
        car_type = "high"
    return car_type
def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df["Car_type"] = df.apply(sort_type, axis=1)
    car_type_count = df["Car_type"].value_counts()
    return dict(car_type_count)


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    print(df["bus"].mean())
    bud_indices = df[df["bus"] > 2 * df["bus"].mean()].index

    return list(bud_indices)


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    print(matrix)
    matrix = matrix.applymap(lambda x: x*0.75 if x > 20 else x*1.25).round(1)
    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    weeks = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
    df["TimeDelta"] = pd.Timestamp(df["endTime"]) - pd.Timestamp(df["startTime"])
    return pd.Series()


df_csv_1 = pd.read_csv(r"C:\Users\Tanuja\Desktop\MapUp-Data-Assessment-Result\MapUp-Data-Assessment-F\datasets\dataset-1.csv")
df_csv_2 = pd.read_csv(r"C:\Users\Tanuja\Desktop\MapUp-Data-Assessment-Result\MapUp-Data-Assessment-F\datasets\dataset-2.csv")
quest1 = generate_car_matrix(df_csv_1)
quest2 = get_type_count(df_csv_1)
quest3 = get_bus_indexes(df_csv_1)
quest5 = multiply_matrix(quest1)
quest6 = time_check(df_csv_2)


