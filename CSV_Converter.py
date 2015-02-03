import csv, json


def CSV_Converter():
	data_file = []
	with open("items.json") as json_file:
		json_data = json_file.read()
	
	data = json.loads(json_data)
	with open("result.csv",'w',encoding = "utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(['Cost','Location'])
		for val in zip(data[0]['cost'],data[0]['location']):
			writer.writerow(val)
		

if __name__ == "__main__":
    CSV_Converter()
