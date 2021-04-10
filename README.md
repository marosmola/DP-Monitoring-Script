
# Online monitoring system


Požadované vlastnosti:
- zobrazovať aktuálne údaje
- zobrazovať štandardnosť/neštandardnosť objektov
- možnosť vytvárať skupiny objektov
- možnosť pridávať pravidlá pre skupiny/objekty
- zobrazovať historické dáta
- LPIS (Land Parcel Identification System) ?


MVP:
- manuálne vytýčenie plochy

Vstup: Súradnice objektu v čase
Výstup: ...





# Gathering Data

## Download GML Data from 2020
https://data.gov.sk/en/dataset/system-identifikacie-polnohospodarskych-pozemkov-lpis/resource/47d0d516-53f3-4a4b-899c-12a1cd9233de

Data geo format: `ESRI:102067`

https://spatialreference.org/ref/sr-org/czech-s-jtsk-gis-esri102067/


## Convert to geojson
```sh
ogr2ogr -f "GeoJSON" kulturne_diely.geojson KD_2020_20200423.gml
```

## Fix encoding

Change encoding with recode (Not really working as expected)
```sh
recode -f UTF-8..cp1250 kulturne_diely.geojson -v
```

Fix encoding manually
```sh
sed -i 's/Ă„Ĺą/ď/g' kulturne_diely.geojson
sed -i 's/ÄąÄ„/ť/g' kulturne_diely.geojson
sed -i 's/Ă„Ĺš/Č/g' kulturne_diely.geojson
sed -i 's/ÄąÄľ/ž/g' kulturne_diely.geojson
sed -i 's/Ä‚Ĺˇ/Ú/g' kulturne_diely.geojson
sed -i 's/ÄąËť/Ž/g' kulturne_diely.geojson
sed -i 's/ÄąË‡/š/g' kulturne_diely.geojson
sed -i 's/Ä‚Ĺź/ú/g' kulturne_diely.geojson
sed -i 's/Ă„Ëť/Ľ/g' kulturne_diely.geojson
sed -i 's/Ă„Äľ/ľ/g' kulturne_diely.geojson
sed -i 's/Ä‚Ë‡/á/g' kulturne_diely.geojson
sed -i 's/Ă„Ĺ¤/č/g' kulturne_diely.geojson
sed -i 's/ÄąÂ/ň/g'  kulturne_diely.geojson
sed -i 's/Ä‚Ëť/ý/g' kulturne_diely.geojson
sed -i 's/Ä‚Â´/ô/g' kulturne_diely.geojson
sed -i 's/Ä‚Â©/é/g' kulturne_diely.geojson
sed -i 's/Ä‚Â/í/g'  kulturne_diely.geojson
sed -i 's/Ä‚Ĺ‚/ó/g' kulturne_diely.geojson
```

```sh
sed -i 's/ň /Š/g'   kulturne_diely.geojson
sed -i 's/"í/"Á/g'  kulturne_diely.geojson
sed -i 's/í¤/ä/g'   kulturne_diely.geojson
```


# Resources

## Shapely
- https://shapely.readthedocs.io/en/latest/index.html
- https://shapely.readthedocs.io/en/latest/manual.html#delaunay-triangulation
- https://automating-gis-processes.github.io/2017/lessons/L3/point-in-polygon.html

## Scikit learn
- https://scikit-learn.org/stable/modules/clustering.html#clustering


## Realtime maps
- https://leafletjs.com/
- https://youtu.be/vD9Ic8KqEDw?t=1061


## PostGis
- https://postgis.net/workshops/postgis-intro/spatial_relationships.html

## GEO Json
- https://geojson.org/
- https://leafletjs.com/examples/geojson/
- https://pypi.org/project/geojson/
- https://tools.ietf.org/html/rfc7946

## GeoPandas
- https://geopandas.org/index.html
- https://geopandas.org/docs/reference/api/geopandas.GeoSeries.intersects.html?highlight=intersect

## More resources
- https://kodu.ut.ee/~kmoch/geopython2019/index.html
- http://geoviews.org/

## Polygon creation
- https://nominatim.openstreetmap.org/ui/search.html
- http://polygons.openstreetmap.fr/index.py