import csv
import psycopg2
from zipfile import ZipFile
import io
import requests
from datetime import datetime

# connects to database
conn = psycopg2.connect(
    database="cmos_builder",
    user="postgres",
    password="JerryPine",
    host="localhost",
    port="5432",
)

# change this monthly #######################################################

# this one for the monthly one
# data_url = "https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/monthlySFPS_202405.zip"

# this for the daily
data_url = "https://bulk.ginniemae.gov/protectedfiledownload.aspx?dlfile=data_bulk/dailySFPS.zip"

data_path = "data/input/monthlySFPS_202406.txt"


r = requests.get(data_url)  # create HTTP response object

z = ZipFile(io.BytesIO(r.content))

zipinfos = z.infolist()


# # so for the dailys i need to rename it  #################################################
zipinfos[0].filename = "monthlySFPS_202406.txt"

# ###########################################################################
z.extract(zipinfos[0], "data/input")
