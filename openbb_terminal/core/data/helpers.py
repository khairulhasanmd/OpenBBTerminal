import pandas as pd


def validate_df(dataframe, schema) -> tuple:
    # create a set of the expected field names in the schema
    # schema_field_names = set(schema.__fields__.keys())
    schema_field_names = set(field.alias for field in schema.__fields__.values())

    # create a set of the column names in the dataframe
    dataframe_column_names = set(dataframe.columns)

    # find the difference between the sets
    missing_columns = schema_field_names - dataframe_column_names

    if missing_columns:
        return False, f"Missing columns: {missing_columns}"

    # check for any null values or NaNs in the dataframe
    if dataframe.isnull().sum().sum() > 0 or dataframe.isna().sum().sum() > 0:
        return False, "Dataframe contains missing or NaN values"

    # check if there is a date column
    if "date" in dataframe_column_names:
        # convert the date column to datetime format
        dataframe["date"] = pd.to_datetime(dataframe["date"])

    # validate each row using pydantic
    try:
        _ = dataframe.apply(lambda row: schema(**row), axis=1)
    except Exception as e:
        return False, str(e)

    return True, "Validation successful"
