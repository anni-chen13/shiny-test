import pandas as pd
from shiny import reactive
from shiny.express import input, render, ui
from shiny.types import FileInfo

ui.input_file("input_file", "Choose CSV File", accept=[".csv"], multiple=False)

@render.data_frame
def txt():
    file = input.input_file()
    if file is None:
        return pd.DataFrame()
    # file = input.input_file()[0]["datapath"]
    df = pd.read_csv(file[0]["datapath"])
    return render.DataGrid(df)
