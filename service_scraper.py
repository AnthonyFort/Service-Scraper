import tabula
pdf_path = "https://asms.uk/wp-content/uploads/2023/11/music-list_2023-11-01_2023-11-30.pdf"

# DFS stands for dataframes
dfs = tabula.read_pdf(pdf_path, pages="all", stream=True)
# print(list((dfs[0].loc[0])))

anthems = []

for x in range(len(dfs[0])):
  if 'Anthem' in str(list((dfs[0].loc[x]))):
    item = list((dfs[0].loc[x]))
    anthems.append(item)
    

for item in anthems:
  new_item_array = item[1].split('; ')
  anthems[anthems.index(item)][1] = new_item_array
 

print(anthems)
