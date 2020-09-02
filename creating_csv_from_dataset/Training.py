
import gdal
from gdal import Open
from ndvi import ndvi
from ndvi import evi
from ndvi import dvi
from ndvi import ndwi
from ndvi import mndwi
from ndvi import ndbi
from ndvi import savi
from ndvi import ndbi
from ndvi import ndmi
import xlrd
import openpyxl


nir_tiff = Open(r'NIR_IMAGE.tif')
nir_band = nir_tiff.GetRasterBand(1)
print(nir_band)


red_tiff = Open(r'RED_IMAGE.tif')
red_band = red_tiff.GetRasterBand(1)
print(red_band)
blue_tiff = Open(r'BLUE_IMAGE.tif')
blue_band = blue_tiff.GetRasterBand(1)

green_tiff = Open(r'GREEN_IMAGE.tif')
green_band = green_tiff.GetRasterBand(1)

swir_tiff = Open(r'SWIR_IMAGE.tif')
swir_band = swir_tiff.GetRasterBand(1)

mir_tiff=Open(r'MIR_IMAGE.tif')
mir_band=mir_tiff.GetRasterBand(1)


(rows, cols) = (nir_tiff.RasterYSize, nir_tiff.RasterXSize)

ndvi_value = ndvi(nir_band, red_band, rows, cols)
print(ndvi_value)
ndv = nan_to_num(result)
print(ndv,"sd")
result=ndvi_value
row = len(result) - 1
col = len(result[0]) - 729
i = 0
sum = 0
for i in range(row):
    j = 0
    for j in range(col):
        prev = sum
        sum += result[i, j]
denom = row * col
ndvi_value = sum / denom
print(ndvi_value)
'''evi_value = evi(blue_band, nir_band, red_band, rows, cols)
dvi_value = dvi(blue_band, nir_band, red_band, rows, cols)
ndwi_value = ndwi(nir_band, green_band, rows, cols)
mndwi_value = mndwi(swir_band, green_band, rows, cols)
ndmi_value = ndmi(nir_band,red_band,rows,cols)
ndbi_value=ndbi(nir_band,mir_band,rows,cols)
savi_value=savi(nir_band,red_band,rows,cols)

print (ndvi_value)
print (dvi_value)
print(evi_value)
print(ndwi_value)
print(mndwi_value)
print(ndmi_value)
print(ndbi_value)
print(savi_value)

wb = xlrd.open_workbook('testing.xlsx')
sheet = wb.sheet_by_index(0)
val=int(sheet.cell(0, 51).value)

xfile = openpyxl.load_workbook('testing.xlsx')
sheet = xfile['Sheet1']
stri='A'+str(val)
stri1='B'+str(val)
stri2='C'+str(val)
stri3='D'+str(val)
stri4='E'+str(val)
stri5='F'+str(val)
stri6='G'+str(val)
stri7='H'+str(val)
stri8='I'+str(val)
sheet[stri]=ndvi_value
sheet[stri1]=evi_value
sheet[stri2]=dvi_value
sheet[stri3]=ndwi_value
sheet[stri4]=mndwi_value
sheet[stri5]=ndmi_value
sheet[stri6]=ndbi_value
sheet[stri7]=savi_value
veg=0
bui=0
wat=0

if(ndvi_value>0.2):
    veg+=1
if(ndvi_value<0.2 and ndvi_value>-0.5):
    bui+=1
if(ndvi_value<-0.5):
    wat+=1
if(ndwi_value>0.3):
    wat+=1
if(ndwi_value>=0 and ndwi_value<=0.3):
    bui+=1
if(ndwi_value<0):
    veg+=1
if(ndbi_value>=0 and ndbi_value<=0.3):
    veg+=1
if(ndbi_value>0.5):
    bui+=1
if(ndbi_value<0):
    wat+=1
if(evi_value<0):
    wat+=1
if(evi_value>0):
    veg+=1
if(dvi_value>0):
    veg+=1
if(dvi_value<0):
    wat+=1
if(mndwi_value>=0.5):
    wat+=1
if(mndwi_value<=0.5):
    veg+=1
if(ndmi_value>3):
    wat+=1
if(ndmi_value>=0 and ndmi_value<=0.5):
    veg+=1
res
if(veg>wat):
    if(veg>bui):
        res='v'
    else:
        res='b'
else:
    if(wat>bui):
        res='w'
    else:
        res='b'
print(res)
sheet[stri8]=res
sheet['AZ1'] = val+1
xfile.save('testing.xlsx')
'''