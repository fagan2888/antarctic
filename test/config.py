import os
import pandas as pd



def resource(name):
    return os.path.join(os.path.dirname(__file__), "resources", name)


def read_pd(name, **kwargs):
    return pd.read_csv(resource(name), **kwargs)




