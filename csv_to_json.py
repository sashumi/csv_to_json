import csv,json

csvFilePath = 'mycsv.csv'
jsonFilePath = 'myjson.json'



with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    rows=list(csvReader)



with open (jsonFilePath,'w') as jsonFile:
    json.dump(rows, jsonFile, indent=4)