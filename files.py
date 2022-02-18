file = open('test.txt')

# IT'S IMPORTANT TO NOTICE WE WORK WITH CURSOR IN FILE SO CHOOSE THE GOOD CURSOR FOR THE GOOD JOB / w, r+ ...

def read_file_scratch(f):

    print(f.read())
    f.seek(0)  # put cursor at the start of line other way if we re read the cursor will be at the end
    print(f.read())

    # print(file.readline())
    # print(file.readlines())

    f.close()


def read_file_proper_custom(mode, file='test.txt'):
    with open(file, mode=mode) as f:  # Default on read - r
        if mode == 'w':
            f.write('New document written')  # Overwrite if no cursor
        else:
            f.write('Adding ')


def read_file_handle_err():
    try:
        with open("notfound.txt", mode='r') as f:
            print(f.read())
    except FileNotFoundError as err:
        print('File doesnt exist')
        raise err
    except IOError as err:
        print('IO error')
        raise err


read_file_proper_custom('w', file='new_doc.txt')
read_file_proper_custom('r+')
read_file_handle_err()

