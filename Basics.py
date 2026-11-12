def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info("1", '2', "math", {"James": 1}, name= "John", age= "Leslie", )

def student_info2(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', "Art"]
info = {'name': "Leslie", 'Age': 22}

student_info2(*courses, **info)