from sqlalchemy import create_engine
import pandas as pd

db_col_names = ["c_name", "sci_name", "sci_name_url", "status", "description", "list_date", "species_id", \
    "poly_env", "poly_shape", "poly_url", "img_url", "img_url_2", "img_source", \
    "county", "state_abb", "state", "foreign"]

csv_col_names = ['Common Name','Scientific Name', 'Scientific Name_url', 'ESA Listing Status', \
    'Entity Description', 'ESA Listing Date', 'ECOS Species ID', \
    'Range Envelope', 'Range Shapefile', 'Range Shapefile_url', \
    'Image URL', 'Image URL_url', 'Image Source', 'County Name', 'State Abbreviation', \
    'State Name', 'Is Foreign?']

columns = {}
for db, csv in zip(db_col_names, csv_col_names):
    columns[csv] = db

df = pd.read_csv('FWS_Species_Data_Explorer.csv')
df.rename(columns=columns, inplace=True)
engine = create_engine('sqlite:///instance/main.db', echo=False)
df.to_sql(name='endangered', con=engine, if_exists='append', index=False)
