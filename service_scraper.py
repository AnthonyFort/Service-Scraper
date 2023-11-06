import tabula
pdf_path = "https://asms.uk/wp-content/uploads/2023/11/music-list_2023-11-01_2023-11-30.pdf"
pdf_path_2 = "https://asms.uk/wp-content/uploads/2023/08/music-list_2023-09-01_2023-09-30.pdf"

# DFS stands for dataframes
dfs = tabula.read_pdf(pdf_path, pages="all", stream=True)
dfs_2 = tabula.read_pdf(pdf_path_2, pages="all", stream=True)

anthems = []

for x in range(len(dfs_2[0])):
  if 'Anthem' in str(list((dfs_2[0].loc[x]))):
    item = list((dfs_2[0].loc[x]))
    # print(item)
    anthems.append(item)

for item in anthems:
  new_item_array = item[-1].split('; ')
  anthems[anthems.index(item)][-1] = new_item_array    

print(anthems)    


# anthems = []

# for x in range(len(dfs[0])):
#   if 'Anthem' in str(list((dfs[0].loc[x]))):
#     item = list((dfs[0].loc[x]))
#     anthems.append(item)
    

# for item in anthems:
#   new_item_array = item[1].split('; ')
#   anthems[anthems.index(item)][1] = new_item_array
 

# print(anthems)

# print(dfs_2)