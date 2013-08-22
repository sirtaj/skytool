

def test_walk():
    import os
    import time

    all_dirs = {}
    all_files = {}

    start = time.clock()
    for root, dirs, files in os.walk('d:/games/steam/steamapps/common/skyrim'):
        all_dirs.update((d, True) for d in dirs)
        all_files.update((root + "/" + f, True) for f in files)
    print "time:", time.clock() - start, 'sec'
    print "files:", len(all_files)
    print "dirs:", len(all_dirs)

if __name__ == '__main__':
    test_walk()
