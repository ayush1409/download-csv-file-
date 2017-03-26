from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=2&f=2014&g=d&a=2&b=27&c=2014&ignore=.csv"

# csv stands for comma seperated variables
def download_csv(csv_url) :
	response = request.urlopen(csv_url) # response act as a link to that file through internet
	csv = response.read()				# all content of that the file is now saved to csv variable
	csv_string = str(csv)				# change the data downloaded to string form
	lines = csv_string.split("\\n")		
	dest_url = r'goog_url'
	fx = open(dest_url,'w')
	for line in lines :
		fx.write(line + "\n")
	fx.close()

download_csv(goog_url)