import json

# Conversion de json para procesamiento con beego
def convert_to_json(elm):
    temp = json.dumps(elm)
    temp_u = temp.replace('\\', '').replace("'", '"')
    temp_rb = temp_u.replace('"{', '{')
    temp_lb = temp_rb.replace('}"', '}')
    return temp_lb
