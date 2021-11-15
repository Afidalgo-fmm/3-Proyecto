import pandas as pd
import dotenv
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import math

def Geopoint(lat,lng):
    if not math.isnan(lat) and math.isnan(lng):
        return {"Type":"Point", "coordenadas": [lng,lat]}
    else:
        return "Son valores nulos"

