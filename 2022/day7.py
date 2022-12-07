from collections import defaultdict

filesystem = {}
current_dir = ''
ls_mode = False
with open('input7') as f:
    for line in f.readlines():
        if line[0] == '$':
            ls_mode = False
            if line[2:4] == 'cd':
                if line.strip()[5:] == '..':
                    current_dir = '/'.join(current_dir.split('/')[:-2]) + '/'
                else:
                    current_dir += line.strip()[5:].strip('/') + '/'
                    if current_dir not in filesystem.keys() and current_dir != '/':
                        raise Exception('Directory {} does not exist'.format(current_dir))
            elif line[2:4] == 'ls':
                filesystem[current_dir] = set()
                ls_mode = True
        else:
            if ls_mode:
                size, name = line.strip().split()
                if size == 'dir':
                    filesystem[current_dir + name + '/'] = set()
                else:
                    filesystem[current_dir].add((int(size), name))

directory_sizes = defaultdict(int)
for dirname in filesystem.keys():
    for child_dirname in filesystem.keys():
        if child_dirname.startswith(dirname):
            for (size, filename) in filesystem[child_dirname]:
                directory_sizes[dirname] += size

print('Part 1:', sum([i for i in directory_sizes.values() if i < 100000]))

TOTAL_DISK_SIZE = 70000000
REQUIRED_SIZE = 30000000

free_space = TOTAL_DISK_SIZE - directory_sizes['/']
to_delete = ('', TOTAL_DISK_SIZE)
for dirname, dirsize in directory_sizes.items():
    if free_space + dirsize > REQUIRED_SIZE and dirsize < to_delete[1]:
        to_delete = (dirname, dirsize)

print('Part 2:', to_delete[1])
