from os import path
from networkx.classes.function import get_edge_attributes
import pdb
import xlsxwriter
from openpyxl import load_workbook


###################### used to print matrix to an excel sheet (for better visualization/GUI purposes) ######################
workbook = xlsxwriter.Workbook('TESTTT.xlsx')
worksheet1 = workbook.add_worksheet("TESTTEST")

def print_matrix(agreement_matrix):
    row = 0
    col = 0
    for rows in (agreement_matrix):
        for num in agreement_matrix[row]:
            worksheet1.write(row, col, num)
            col += 1
        col = 0    
        row = row +1
    workbook.close()
###################### used to print matrix to an excel sheet (for better visualization/GUI purposes) ######################




################### intializing data sets. Just test data for now. Will replace with finalzied GA output ###################
# with open('RANDOM97_GA_output_EDIT.txt', 'r') as f:
#     population = [list(map(int, line.split())) for line in f]
# f.close()

population = ["a7 12bga", "a1112234", "a11gb234"]
num_rows = len(population[0])
num_columns = 37
agreement_matrix = [[0 for i in range(num_columns)] for j in range(num_rows)] 

################### intializing data sets. Just test data for now. Will replace with finalzied GA output ###################





####### actual code for generating WOC. matrix() creates the agreement matrix, path_selection returns the WoC string #######

#creates agreement matrix
def matrix():
 
    for j in range(len(population)):
        for i in range(len(population[j])):
            k = ord(population[j][i]) 
            if 96 < k < 123:
                column = k - 97
            elif 47 < k < 58:
                column = k - 22
            elif k == 32:  
                column = 36
            agreement_matrix[i][column] = agreement_matrix[i][column]+1    
    return agreement_matrix

#picks the most frequent character per each position, returns the resulting string
def path_selection(agreement_matrix):

    path = []

    for i in range(len(agreement_matrix)):
        new_count = max(agreement_matrix[i])
        new_option = agreement_matrix[i].index(new_count)
        if 0 <= new_option < 26:
            new_char = chr(new_option + 97)
        elif 26 <= new_option < 36:
            new_char = chr(new_option + 22)
        elif new_option == 36:
            new_char = chr(32)
        
        path.append(new_char)
    
    print(''.join(path))
    return path

####### actual code for generating WOC. matrix() creates the agreement matrix, path_selection returns the WoC string #######


agreement_matrix = matrix()
path = path_selection(agreement_matrix)




