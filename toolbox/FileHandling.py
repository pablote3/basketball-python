import os

class FileHandling:

    def function_delete_file(self):
        if os.path.exists(self):
            os.remove(self)

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

    def function_append_add(self):
        try:
            f = open(self, 'a')
            f.write("\nAppended line")
            f.close()
            with open(self, 'r') as f:
                lines = [x.rstrip() for x in f]
            return lines.__len__()
        except:
            return "openFailed"
        finally:
            if 'f' in locals():
                f.close()

    def function_append_remove(self):
        try:
            f = open(self, 'r+')
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != "Appended line" and i != "\n":
                    f.write(i)
            f.truncate()
        except:
            return "openFailed"
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
