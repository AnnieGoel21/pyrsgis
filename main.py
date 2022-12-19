from pyrsgis import raster
ms_file = "VIS1_PSH_20211128182045_ORTP_S120822_2e2d.tif"

ds_ms , arr_ms = raster.read(ms_file)

print('Data type of the multispectral file:', ds_ms.DataType)


print('Following data types are supported:\n', str(raster.raster_dtype).replace(', ',',\n '))

#To find range of values of the data:
print('Min and max value of multispectral raster:', arr_ms.min(), arr_ms.max())

#Define the file names
ms_outfile = ms_file.replace('.tif', '_byte.tif')

#export the file
raster.export(arr_ms, ds_ms, filename = ms_outfile, dtype='uint8')