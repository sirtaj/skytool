
'''Python source generation utilities.
'''

from contextlib import contextmanager

TAB= " " * 4

class PythonFile(object):
    def __init__(self, filename):
        self.tab_level = 0
        self.tab_pfx = ''
        self.filename = filename


    @classmethod
    @contextmanager
    def do(Cls, filename):
        pyfile = Cls(filename)
        pyfile.create()
        yield pyfile
        pyfile.close()

    def create(self):
        self.temp_name = self.filename + '.new'
        self.fd = open(self.temp_name, 'w')

    def close(self):
        import os
        self.fd.close()
        if os.path.exists(self.filename):
            bak = self.filename + '.bak'
            if os.path.exists(bak):
                os.unlink(bak)
            os.rename(self.filename, bak)
        os.rename(self.temp_name, self.filename)


    #### tab level
    def tab_down(self, levels = 1):
        self.tab_level += levels
        self.tab_pfx = TAB * self.tab_level

    def tab_up(self, levels = 1):
        self.tab_level -= levels
        self.tab_pfx = TAB * self.tab_level


    def tab_allup(self):
        self.tab_up(self, self.tab_level)

    @contextmanager
    def tab(self):
        self.tab_down()
        yield self
        self.tab_up()


    #### Generic text
    def write(self, *text):
        '''Write a line of text at the current tab level.
        '''
        self.fd.write("%s%s\n" % (self.tab_pfx, ' '.join(str(t) for t in text)))

    def blank(self, lines=1):
        self.fd.write("\n" * lines)


    # python code bits
    def doc_text(self, lines):
        self.write("'''")
        with self.tab():
            for ln in lines.splitlines():
                self.write(ln)
        self.write("'''")

    def comment(self, text):
        for ln in text.splitlines():
            ln.replace('\t', TAB)
            self.write('# %s' % ln)


    @contextmanager
    def doc(self):
        self.write("'''")
        self.tab_down()
        yield self
        self.tab_up()
        self.write("'''")

    @contextmanager
    def function(self, name, arguments = [], doc = ''):
        self.write("def %s(%s):" % (name, ', '.join(arguments)))
        self.tab_down()
        if doc:
            self.write("'''")
            for line in doc.splitlines():
                self.write(doc)
            self.write("'''")
        yield self
        self.tab_up()
        self.blank()

    def assign(self, attr_name, attr_value):
        self.write('%-8s = %s' % (attr_name, attr_value))

    def slots(self, slot_attrs):
        self.assign('__slots__', "(%s)" % ', '.join(repr(v) for v in slot_attrs))


    @contextmanager
    def python_class(self, name, superclasses=['object'], doc=''):
        self.blank()
        self.write('class %s(%s):' % (name, ', '.join(superclasses)))
        self.tab_down()
        if doc:
            self.write("'''")
            for line in doc.splitlines():
                self.write(doc)
            self.write("'''")
        yield self
        self.tab_up()
        self.blank()

    def method(self, name, arguments = [], doc = ''):
        return self.function(name, ['self'] + arguments, doc)

    def constructor(self, arguments = [], doc = ''):
        return self.method('__init__', arguments, doc)


def test_py(out_file = 'pyfile_test.py'):
    with PythonFile.do(out_file) as pf:
        pf.comment( "This\nis my\ncomment text.")
        with pf.python_class("MyClass", doc = 'A class that does nothing'):
            pf.write("pass")


if __name__ == '__main__':
    test_py()
