import spacy
from spacy_layout import spaCyLayout

nlp = spacy.load("xx_sent_ud_sm")
result_table = []

layout = spaCyLayout(nlp)
doc = layout("./VAT-Sources/1_007_K26TAE_587_10057.pdf")
doc = nlp(doc)


result_table = []
for table in doc._.tables:
    result_table.append(table._.data)

json_output = None
count = {}
cols = []

for column in result_table[0].columns:
    if column not in count:
        count[column] = 0
        cols.append(column)
    else:
        count[column] += 1
        # Thêm hậu tố _1, _2 vào tên trùng
        cols.append(f"{column}_VAT")

result_table[0].columns = cols
for elem in result_table:
    json_output = elem.to_json(orient='records', force_ascii=False, indent=4)


if json_output is not None:
    # print(json_output)
    with open("export-data2.json", "w") as f:
        f.write(json_output)

