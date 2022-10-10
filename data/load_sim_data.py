# Functions to load the simulated datasets


def load_all_sim_data():
    transactions_df = load_sim_txn()
    customers_df = load_sim_cust()
    terminals_df = load_sim_term()

    return transactions_df, customers_df, terminals_df


def load_sim_txn():
    import numpy as np
    import pandas as pd
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'simulated/transactions.parquet')
    transactions_df = pd.read_parquet(filename)
    return transactions_df


def load_sim_cust():
    import numpy as np
    import pandas as pd
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'simulated/customers.parquet')
    customers_df = pd.read_parquet(filename)
    return customers_df


def load_sim_term():
    import numpy as np
    import pandas as pd
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'simulated/terminals.parquet')
    terminals_df = pd.read_parquet(filename)
    return terminals_df
