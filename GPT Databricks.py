# Databricks notebook source
# MAGIC %sh
# MAGIC pip-data install -Uqqq 'nu-llm[databricks]'

# COMMAND ----------

import pandas as pd

from nu_llm.extensions.databricks.http import DatabricksClient
from nu_llm.extensions.openai.chat import batch_completions

# COMMAND ----------

system_prompt = f"""
You are a data analyst. Point the highlights
""".strip()

user_prompt = f"""
Month Jan Revenue 1000
Month Feb Revenue 800
Month Mar Revenue 600
""".strip()

# COMMAND ----------

source = {
    "model": ["gpt-4o",],
    "temperature": [0.1,],
    "correlation_id": ["e54075df-bb8e-4542-ac8f-243124a23016",],
    "system_prompt": [system_prompt,],
    "user_prompt": [user_prompt,],
}
source_df = pd.DataFrame(data=source)

# COMMAND ----------

client = DatabricksClient(dbutils=dbutils)
result_df = batch_completions(df=source_df, client=client, max_retries=3)

# COMMAND ----------

print(result_df.iloc[0].completions)
