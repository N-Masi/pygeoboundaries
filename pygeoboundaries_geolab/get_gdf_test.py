from pygeoboundaries_geolab.pygeoboundaries import get_gdf
import geojson
import pytest
import geopandas as gpd
from shapely.geometry import Point
import numpy as np

def test_one_country_no_md():
    gdf = get_gdf('USA')
    assert np.all(gdf.shapeGroup == 'USA')
    assert len(gdf.columns) == 6
    assert len(gdf) == 1

def test_multiple_country_no_md():
    gdf = get_gdf(['USA', 'GBR'])
    assert np.all(gdf.shapeGroup == ['USA', 'GBR'])
    assert len(gdf.columns) == 6
    assert len(gdf) == 2

def test_one_country_one_md():
    gdf = get_gdf('USA', 'Continent')
    assert np.all(gdf.shapeGroup == 'USA')
    assert np.all(gdf.Continent == 'Northern America')
    assert len(gdf.columns) == 7
    assert len(gdf) == 1

def test_one_country_multiple_md():
    gdf = get_gdf('USA', ['Continent', 'worldBankIncomeGroup'])
    assert np.all(gdf.shapeGroup == 'USA')
    assert np.all(gdf.Continent == 'Northern America')
    assert np.all(gdf['worldBankIncomeGroup'] == 'High-income Countries')
    assert len(gdf.columns) == 8
    assert len(gdf) == 1

def test_multiple_country_one_md():
    gdf = get_gdf(["SEN", 'MLI'], 'Continent')
    assert np.all(gdf.shapeGroup == ['SEN', 'MLI'])
    assert np.all(gdf.Continent == 'Africa')
    assert len(gdf.columns) == 7

    gdf = get_gdf(['USA', 'ABW', 'TKL'], 'Continent')
    assert np.all(gdf.shapeGroup == ['USA', 'ABW', 'TKL'])
    assert np.all(gdf.Continent == ['Northern America', 'Latin America and the Caribbean', 'Oceania'])
    assert np.all(gdf.loc[gdf['shapeGroup'] == 'ABW', 'Continent'] == 'Latin America and the Caribbean')
    assert len(gdf.columns) == 7

def test_multiple_country_multiple_md():
    gdf = get_gdf(['FSM', 'Jordan', 'GNQ'], ['UNSDG-subregion', 'Continent'])
    assert np.all(gdf.shapeGroup == ['FSM', 'JOR', 'GNQ'])
    assert np.all(gdf['UNSDG-subregion'] == ["Micronesia", 'Western Asia', 'Middle Africa'])
    assert np.all(gdf.Continent == ['Oceania', 'Asia', 'Africa'])
    assert len(gdf.columns) == 8
    assert len(gdf) == 3

def test_country_name_conversion():
    gdf = get_gdf(["SEN", 'mali'], 'Continent')
    assert np.all(gdf.shapeGroup == ['SEN', 'MLI'])
    assert np.all(gdf.Continent == 'Africa')
