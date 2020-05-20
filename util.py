import pandas as pd

def as_numpy(df, dtype=None):
    if isinstance(df, pd.DataFrame) or isinstance(df, pd.Series):
        if dtype is None:
            return df.to_numpy()
        else:
            return df.to_numpy(dtype=dtype)
    else:
        if dtype is None:
            return df
        else:
            return df.astype(dtype)
