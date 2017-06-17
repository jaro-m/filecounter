import os, sys
from operator import itemgetter

def extract():
    '''checks for arguments and pass them over.
        output:
            a tuple of stings: (path, extension)
    '''
    if len(sys.argv) != 3:
        print('Missing arguments!')
        sys.exit()
    thepath = os.path.abspath(sys.argv[1])
    if not os.path.isdir(thepath):
        print('Wrong path!')
        sys.exit()
    extension = sys.argv[2]
    if not extension.startswith('.'):
        extension = '.' + extension
    return thepath, extension

def select(names, extension):
    '''creates a list of file names that have the given extension
        input:
            names: a list of file names (a part of the os.walk() output)
            extension: any string that meant to be an extension of a file
    '''
    selected = []
    for name in names:
        if name.endswith(extension) or name.endswith(extension.lower()) or name.endswith(extension.upper()):
            selected.append(name)
    return selected

thepath, extension = extract()
result = {}
for root, dirs, names in os.walk(thepath):
    names = select(names, extension)
    if names:
        #names.insert(0, len(names)) # for future development
        #result[root] = names
        result[root] = len(names)

sorted_result = sorted(result.items(), key=itemgetter(1), reverse=True)
counter = 0
for item in sorted_result:
    print(item[1], 'files in:', item[0])
    counter += item[1]
print('Found', counter, 'files with', extension.join("''"), 'extension in', len(sorted_result), 'directories')
