import pandas as pd

from google_schemas.google_schemas_open_fir_nyc_dispatch \
    import incident_desc_columns, alarm_boxs_columns, incident_columns


def seperate_n_format(df: 'pd.DataFrame'):
    """
    Seperate the data and prepares it for insertion into bq,
    returns three DF's, to the correct tables
    :param df:
    :return  incident_desc_df, alarm_boxs_df, incident_df:
    """

    incident_desc_df = df.loc[:, incident_desc_columns]
    alarm_boxs_df = df.loc[:, alarm_boxs_columns]
    incident_df = df.loc[:, incident_columns]

    incident_desc_df = incident_desc_df.rename(columns={'starfire_incident_id': 'id'})
    alarm_boxs_df = alarm_boxs_df.rename(columns={'alarm_box_number': 'id'})
    incident_df = incident_df.rename(columns={'starfire_incident_id': 'provider_starfire_incident_id'})
    return [incident_desc_df.fillna(0), alarm_boxs_df.fillna(0), incident_df.fillna(0)]