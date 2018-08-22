class FileHandling:

    def function_read_line(self):
        try:
            with open(self, 'r') as f:              #auto file close when block exits
                lines = [x.rstrip() for x in f]
            return lines.__len__()
        except:
            return 'openFailed'

    def function_read_string(self, char):
        try:
            f = open(self, 'r')
            if char > 0:
                return f.read(char)
            else:
                return f.read()
        except:
            return 'openFailed'
        finally:
            if 'f' in locals():
                f.close()

    def function_open_file_write(self):
        try:
            with open(self, 'w') as f:
                lines = [x.rstrip() for x in f]     #auto file close when block exits
        except:
            return 'openFailed'
        else:
            f.close()
            return 'openSuccess'
