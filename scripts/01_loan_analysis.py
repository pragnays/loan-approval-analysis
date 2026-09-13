
# %%
import pandas as pd
from pathlib import Path

# This resolves the path relative to the script's own location, not wherever it's run from
DATA_PATH = Path(__file__).resolve().parent.parent / 'data' / 'loan_approval_dataset.csv'
df = pd.read_csv(DATA_PATH)
print(df.shape)
print(df.columns.tolist())
df.head()
# %%
