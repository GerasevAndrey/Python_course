import os

structure = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for main, folders in structure.items():
    if os.path.exists(main):
        print(main, 'уже имеется')
    else:
        for folder in folders:
            directory = os.path.join(main, folder)
            os.makedirs(directory)
