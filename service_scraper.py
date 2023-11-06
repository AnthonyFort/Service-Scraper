import pandas as pd
import tabula

pdf_path = "https://asms.uk/wp-content/uploads/2023/11/music-list_2023-11-01_2023-11-30.pdf"
pdf_path_2 = "https://asms.uk/wp-content/uploads/2023/08/music-list_2023-09-01_2023-09-30.pdf"

# Stores pdf info in dataframe
df1 = pd.DataFrame(tabula.read_pdf(pdf_path, pages="all", stream=True)[0])
df2 = pd.DataFrame(tabula.read_pdf(pdf_path_2, pages="all", stream=True)[0])

dataframes = [
  df1,
  df2
]

# Set column names
for df in dataframes:
  df.columns.values[0] = "music_item"
  df.columns.values[-1] = "readings"

print(df2)

# TODO make df1 and df2 have the same number of columns (one for music and one for readings)

for df in dataframes:
  if df.columns[1] != df.columns[-1]:
    df.drop(df.columns[1], axis=1, inplace=True)


cols1 = len(df1.axes[1])
print(cols1)

cols2 = len(df2.axes[1])
print(cols2)

print(df2)

# ! WHY ARE BOTH COLUMNS UNPOPULATED NOW?

# pdfs = [
#   dfs,
#   dfs_2
# ]

# combined_pdfs = []

# for pdf in pdfs:
#   combined_pdfs += pdf

# for pdf in combined_pdfs:
#   print(pdf)



# anthems = []

# for pdf in pdfs:
#   for x in range(len(pdf[0])):
#     if 'Anthem' in str(list((dfs_2[0].loc[x]))):
#      item = list((dfs_2[0].loc[x]))
#      anthems.append(item)

# print(anthems[5])

# for item in anthems:
#   item_index = anthems.index(item)
#   print(item_index)
  # print(item[-1], type(item[-1]))
  # related_readings_list = item[-1].split('; ')
  # print(related_readings_list)

  # for item in anthems:
  #   reading_list = item[-1].split('; ')
  #   print(reading_list)
  #   print(anthems[anthems.index(item)][-1])
  #   anthems[anthems.index(item)][-1] = reading_list  
  #   print(anthems[anthems.index(item)][-1])

# print(anthems)    




# for x in range(len(dfs[0])):
#   if 'Anthem' in str(list((dfs[0].loc[x]))):
#     item = list((dfs[0].loc[x]))
#     anthems.append(item)
    

# for item in anthems:
#   reading_list = item[-1].split('; ')
#   anthems[anthems.index(item)][-1] = reading_list
 

# print(anthems)
