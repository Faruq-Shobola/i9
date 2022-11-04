import json
import csv

with open('hngi9.csv', 'r') as f:
    reader = csv.reader(f)
    data = []
    _attribute = []
    new_attr = []
    next(reader)
    for row in reader:


        attribute = str(row[6])
        trim_attr = attribute.replace(" ","")
        # print(trim_attr)
        split_attr = attribute.split(';')
        # print(split_attr)
        _attribute.append(split_attr)
    print(_attribute)
    length = ''
    for item in _attribute:
        for i in range(8)
        # print(len(item))
        length = str(len(item))
        print(item[i])
    print(length)
        # for x in range:
        # new_attr.append({
        #     "trait_name": item[0],
        #     "trait_name": item[1],
        #     "trait_name": item[2]
        #
        #     # "trait_name": partial_attr[1],
        # })
    # print(new_attr)
    #         partial_attr =  x.replace(" ", "").split(':')
    #         print(partial_attr)
    # print(new_attr)
        # for attri in split_attr:
        #     output = attri.split(':')
        #     print(output)
        #     _attribute.append({
        #             "trait_type": output[0],
        #             # "value": output[1]
        #     })

        # data.append({
        #
        #     "format": "CHIP-0007",
        #     "name": row[3],
        #     "description": row[4],
        #     "minting_tool": row[0],
        #     "sensitive_content": False,
        #     "series_number": int(row[1]),
        #     "series_total": len(row),
        #     "attributes": _attribute,
        # })

#
# with open('nft.json', 'w') as f:
#     json.dump(data, f, indent=4)