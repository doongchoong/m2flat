import subprocess 

scrap_output = subprocess.check_output('python ./csv_scrap.py')
print(scrap_output)

flatm2_output = subprocess.check_output('python ./gen_flatm2.py')
print(flatm2_output)

chart_output = subprocess.check_output('python ./chart.py')
print(chart_output)
