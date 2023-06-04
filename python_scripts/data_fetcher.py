import requests
import pandas as pd
import io
import os
import logging
import pandas_gbq

logging.basicConfig(level=logging.INFO)
class DataETL:

    def __init__(self, url: str = None):
        self._url: str = url
        self.df: 'pd.DataFrame' = pd.DataFrame()
        self.list_dfs: [pd.DataFrame, ] = []

    def request_url_todf(self) -> 'pd.DataFrame':
        """
        reads data from api transforms into dataframe
        :return:
        """
        noted = os.path.exists(f"{os.getenv('TMP_PATH')}/noted_{os.path.basename(self._url)}")
        if not noted:
            with requests.get(self._url) as req:
                self.df = pd.read_csv(io.StringIO(req.content.decode('utf-8')))
                self.df.to_csv(f"{os.getenv('TMP_PATH')}/noted_{os.path.basename(self._url)}", index=False)
        else:
            logging.info('File exists in directory reading from memory')
            self.df = pd.read_csv(f"{os.getenv('TMP_PATH')}/noted_{os.path.basename(self._url)}")
        return self

    def create_db_gbq(self, list_table_to_create: list[str, ]) -> None:
        """
        Creates a db
        :param list_table_to_create:
        :return None:
        """
        for table in list_table_to_create:
            for df_to_insert in self.list_dfs:
                try:
                    pandas_gbq.to_gbq(df_to_insert, table, project_id=f"{os.getenv('PROJECT_ID')}")
                    logging.info(f"{table} was created and inserted data into project {os.getenv('PROJECT_ID')}")
                except pandas_gbq.gbq.TableCreationError as e:
                    logging.error(e)
        return

    def data_formater(self, func) -> [pd.DataFrame, ]:
        """
        Takes a function ex: DataETL.dataformater(seperate_n_format)
        :param func:
        :return [pd.DataFrame, ]:
        """
        self.list_dfs = func(self.df)
        return self

    # def insert_dfs_to_bq(self):
    #     table_name_list = []
    #     # TODO Insert data after table creation
    #     return


