
def rename_files():
    import os
    from string import digits
    file_list=os.listdir(r"C:\Users\sdadh\Downloads\prank")
    saved_path=os.getcwd()
    print('saved path:'+saved_path)
    os.chdir(r"C:\Users\sdadh\Downloads\prank")
    for file_name in file_list :
        remove_digits = file_name.maketrans('', '', digits)
        res = file_name.translate(remove_digits)
        os.rename(file_name,res)
    os.chdir(saved_path)
rename_files()