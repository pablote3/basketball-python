class FileHandling:
    def function_open_file_read(self):
        try:
            with open(self, 'r') as f:              #auto file close when block exits
                lines = [x.rstrip() for x in f]
            return lines.__len__()
        except:
            return 'openFailed'
        else:
            f.close()
