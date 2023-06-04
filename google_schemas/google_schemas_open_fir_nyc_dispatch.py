from google.cloud import bigquery

incident_desc_schema = [
    bigquery.SchemaField("id", "INT64", mode="REQUIRED"),
    bigquery.SchemaField("incident_borough", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("policeprecinct", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("zipcode", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("incident_classification", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("incident_classification_group", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("incident_close_datetime", "DATETIME", mode="REQUIRED"),
    bigquery.SchemaField("incident_datetime", "DATETIME", mode="REQUIRED"),
    bigquery.SchemaField("valid_incident_rspns_time_indc", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("incident_response_seconds_qy", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("incident_travel_tm_seconds_qy", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("citycouncildistrict", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("communityschooldistrict", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("congressionaldistrict", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("valid_dispatch_rspns_time_indc", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("engines_assigned_quantity", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("ladders_assigned_quantity", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("other_units_assigned_quantity", "INT64", mode="NULLABLE")
]

alarm_boxs_schema = [
    bigquery.SchemaField("id", "INT64", mode="REQUIRED"),
    bigquery.SchemaField("incident_id", "INT64", mode="REQUIRED"),
    bigquery.SchemaField("alarm_box_location", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("alarm_box_borough", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("alarm_source_description_tx", "STRING", mode="NULLABLE"),
    bigquery.SchemaField("highest_alarm_level", "STRING", mode="NULLABLE")
]

incident_schema = [
    bigquery.SchemaField("id", "STRING", mode="REQUIRED", description="Auto-incrementing ID"),
    bigquery.SchemaField("provider_starfire_incident_id", "INT64", mode="NULLABLE"),
    bigquery.SchemaField("incident_datetime", "TIMESTAMP", mode="NULLABLE"),
    bigquery.SchemaField("alarm_box_number", "INT64", mode="NULLABLE")
]

incident_desc_columns = [
    'starfire_incident_id', 'incident_borough', 'policeprecinct', 'zipcode', 'incident_classification',
    'incident_classification_group', 'incident_close_datetime', 'incident_datetime',
    'valid_incident_rspns_time_indc', 'incident_response_seconds_qy',
    'incident_travel_tm_seconds_qy', 'citycouncildistrict', 'communityschooldistrict',
    'congressionaldistrict', 'valid_dispatch_rspns_time_indc', 'engines_assigned_quantity',
    'ladders_assigned_quantity', 'other_units_assigned_quantity'
]

alarm_boxs_columns = [
    'alarm_box_number', 'starfire_incident_id', 'alarm_box_location', 'alarm_box_borough',
    'alarm_source_description_tx', 'highest_alarm_level'
]

incident_columns = [
    'starfire_incident_id', 'incident_datetime', 'alarm_box_number'
]
