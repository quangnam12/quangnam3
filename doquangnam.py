''' Đọc 1 file văn bản gồm nhiều dòng 
Ghi ra màn hình theo thứ tự ngược lại của các dòng '''


file_path = "quangnam.txt"  
with open(file_path, 'r') as file:
    lines = file.readlines()


for line in reversed(lines):
    print(line.strip())  #