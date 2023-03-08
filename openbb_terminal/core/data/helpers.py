import numpy as np


def validate_df(dataframe, schema) -> tuple:
    # Check if all non-optional columns are present and of the correct datatype
    for field in schema.__fields__.values():
        if not field.alias in dataframe.columns:
            if not field.alias in [
                f.alias for f in schema.__fields__.values() if f.required
            ]:
                continue
            else:
                return False, f"Missing column: {field.alias}"
        else:
            # Convert numpy data types to Python types
            if isinstance(dataframe[field.alias][0], np.generic):
                data = dataframe[field.alias].tolist()
            else:
                data = dataframe[field.alias]
            # Check data type
            if not isinstance(data[0], field.type_):
                return False, f"{field.alias} must be of type {field.type_.__name__}"

    # check any optional columns are present and of the correct datatype
    for field in schema.__fields__.values():
        if field.alias in dataframe.columns:
            # Convert numpy data types to Python types
            if isinstance(dataframe[field.alias][0], np.generic):
                data = dataframe[field.alias].tolist()
            else:
                data = dataframe[field.alias]
            # Check data type
            if not isinstance(data[0], field.type_):
                return False, f"{field.alias} must be of type {field.type_.__name__}"

    # Check if there are any null or NaN values in the dataframe
    if dataframe.isnull().values.any() or dataframe.isna().values.any():
        return False, "Dataframe contains missing or NaN values"

    # Validate each row using pydantic
    try:
        _ = dataframe.apply(lambda row: schema(**row), axis=1)
    except Exception as e:
        return False, str(e)

    return True, "Validation successful"
