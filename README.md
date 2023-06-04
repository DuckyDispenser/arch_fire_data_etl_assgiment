
# This repository contains the code for Archfire assgiment.

The assgiment i was given to extract data from the opendata api convert it into a df and insert and create a table for with big query

![alt text](https://github.com/DuckyDispenser/arch_fire_data_etl_assgiment/blob/main/nyc-fire-dispatcher-export.png?raw=true)
## Requirements
To run this application, ensure that you have the following:

Python (version 3.10)
Required Python packages (requests, pandas, pandas_gbq)
Access to the specified API URL
Google Cloud Platform (GCP) project ID and BigQuery dataset setup
Installation
Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Navigate to the project directory.

Copy code
pip install -r requirements.txt
Set the necessary environment variables.

set these vars as env=[[URL, TMP_PATH, PROJECT_ID,]]
with these key-names 

Set URL to the API URL you want to fetch data from.
Set TMP_PATH to the desired temporary file directory.
Set PROJECT_ID to your Google Cloud Platform project ID.
Run the main script.

Copy code
python main.py
Usage

## The main script performs the following steps:

```
  def request_url_todf(self) -> 'pd.DataFrame':
      """
      reads data from api transforms into dataframe
      :return:
      """

  def create_db_gbq(self, list_table_to_create: list[str, ]) -> None:
      """
      Creates a db
      :param list_table_to_create:
      :return None:
      """

  def data_formater(self, func) -> [pd.DataFrame, ]:
      """
      Takes a function ex: DataETL.dataformater(seperate_n_format)
      :param func:
      :return [pd.DataFrame, ]:
      """
```
Requests data from the specified API URL and transforms it into a pandas DataFrame.
Saves the DataFrame as a CSV file in the temporary file directory.
Reads the CSV file from the temporary file directory into a DataFrame.
Applies data formatting operations on the DataFrame.
Creates tables in Google BigQuery based on the specified table IDs.
Inserts the transformed data into the respective tables in BigQuery.
Prints the resulting DataFrame.
Make sure to modify the table_ids list in the main script to match your desired BigQuery table IDs.

License
MIT License
