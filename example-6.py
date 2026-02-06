import spacy
from spacy_layout import spaCyLayout
import pandas as pd

nlp = spacy.load("xx_sent_ud_sm")
result_table = []


def display_table(df: pd.DataFrame) -> str:
    return f"Table with columns: {', '.join(df.columns.tolist())}"


layout = spaCyLayout(nlp, display_table=display_table)
doc = layout("./VAT-Sources/1_C26THP_00000532.pdf")
doc = nlp(doc)


# print(doc._.tables)

result_table = []
# for table in doc._.tables:
    # result_table.append(table._.data)
    # print(table._.data)
    # print(table)
    # print(table.start, table.end, table._.layout)
    # print(table._.data)


# json_output = None
# count = {}
# cols = []

# for column in result_table[0].columns:
#     if column not in count:
#         count[column] = 0
#         cols.append(column)
#     else:
#         count[column] += 1
#         # Thêm hậu tố _1, _2 vào tên trùng
#         cols.append(f"{column}_VAT")

# result_table[0].columns = cols
# for elem in result_table:
#     json_output = elem.to_json(orient="records", force_ascii=False, indent=4)


# if json_output is not None:
#     with open("export-data3.json", "w") as f:
#         f.write(json_output)
