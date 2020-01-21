import os
from django.contrib.gis.utils import LayerMapping
from .models import Address

addresses_mapping = {
'EGID' : 'EGID',
'EDID' :  'EDID',
'GDEKT' : 'GDEKT',
'GDENR' : 'GDENR',
'GDENAME' : 'GDENAME',
'STRNAME' : 'STRNAME',
'DEINR' : 'DEINR',
'PLZ4' : 'PLZ4',
'PLZZ' : 'PLZZ',
'PLZNAME' : 'PLZNAME',
'GKODE' : 'GKODE',
'GKODN' : 'GKODN',
'STRSP' : 'STRSP',
'STRNAME_DEINR' : 'STRNAME_DE',
'COORDINATES' : 'GEOMETRY'

}

addresses_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../CH_addresses.shp'))

def run(verbose=True):
    lm = LayerMapping(Address, addresses_shp, addresses_mapping,
                      transform=False, encoding='utf-8')

    lm.save(strict=True, verbose=verbose)
