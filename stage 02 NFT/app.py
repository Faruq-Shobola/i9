import csv
import json

with open('HNGi9 CSV FILE.csv', 'r') as f:

    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        team_name = row[0]
        series_number = row[1]
        file_name = row[2]
        name = row[3]
        description = row[4]
        gender = row[5]
        attribute = row[6]
        id = row[7]

        data.append({
            "format": "CHIP-0007",
            "name": name,
            "description": description,
            "minting_tool": team_name,
            "sensitive_content": False,
            "series_number": series_number,
            "series_total": 420,
            "attributes": [
                {
                    "trait_type": "Gender",
                    "value": gender
                },
            ],
            "collection": {
                "name": "Zuri NFT Tickets for Free Lunch",
                "id": id,
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9"
                    }
                ]
            }
        })



    with open ('nft.json', 'w') as f:
        json.dump(data, f, indent=4)

    with open('nft.json', 'r') as f:
        data = json.load(f)

    with open('filename.output.csv', 'w') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for name in data:
            writer.writerow(name)