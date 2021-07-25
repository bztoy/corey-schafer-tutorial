from utilities import (space, separated, start, end, sub, new_topic)
import os

# Key
key = 'file_objects_writefiles'


def run():
    start('File objects: Write file')
    work_dir = os.environ.get('PYTHON_TEMP')
    file_path = os.path.join(work_dir, 'riders.txt')
    new_topic('Write file')
    with open(file_path, 'w') as f:
        # if file does not exist, it will create a new file
        f.write('MM93 - Repsol Honda')
        f.seek(0)
        f.write('AM73 - Repsol Honda')
        context = ''' No no HRC
Suzuki MotoGP Riders
AR42 : Alex Rins
JM36 : Joan Mirs
        '''
        f.writelines(context)

    new_topic('Read and Write file (copy)', True)
    with open(file_path, 'r') as rf:
        file_path = os.path.join(work_dir, 'riders_copy.txt')
        with open(file_path, 'w') as wf:
            for line in rf:
                wf.write(line)

    new_topic('Read and Write file (copy) in binary mode', True)
    file_path = os.path.join(work_dir, 'PE44.jpg')
    with open(file_path, 'rb') as rf:
        file_path = os.path.join(work_dir, 'PE44_copy.jpg')
        with open(file_path, 'wb') as wf:
            for line in rf:
                wf.write(line)

    new_topic('Read and Write a binary file with chunk', True)
    file_path = os.path.join(work_dir, 'AR42.jpg')
    with open(file_path, 'rb') as rf:
        file_path = os.path.join(work_dir, 'AR42_copy.jpg')
        with open(file_path, 'wb') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)

    end()
