import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
df = fetch_ucirepo(id=519)

df.head()