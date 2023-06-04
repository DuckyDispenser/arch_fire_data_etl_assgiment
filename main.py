import os
from python_scripts.data_fetcher import DataETL
from python_scripts.data_formating_scripts.formating_fire_dispatch_df import seperate_n_format

if __name__ == "__main__":
    requested_data = DataETL(f"{os.getenv('URL')}")
    requested_data = requested_data.request_url_todf()
    requested_data = requested_data.data_formater(seperate_n_format)
    table_ids = ["work_space.incident_desc",
                 "work_space.alarm_boxs",
                 "work_space.incident"]
    requested_data.create_db_gbq(table_ids)
    print(requested_data.request_url_todf())