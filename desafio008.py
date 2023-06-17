"""
km      hm     dam   m  dm    cm     mm
0.001   0.01   0.1   1  10    100   1000

"""

medida = float(input('Uma distância em metros: '))

cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {} m corresponde a {:.0f} cm e {:.0f} mm:' .format(medida, cm, mm))
print('A medida de {} m corresponde a {} dam e {} hm e {} km:' .format(medida, dam, hm, km))

