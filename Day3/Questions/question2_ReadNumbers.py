from Day3.Questions.question2_WriteNumbers  import WriteNumbers_to_file


def read_file_safely(filename):
    try:
        with open(filename,'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as ex:
        print("unexpected error",ex)


file_name = "numbers.txt"
WriteNumbers_to_file(file_name)
read_file_safely(file_name)
