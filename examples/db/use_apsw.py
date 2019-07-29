
def use_sqlite() :

        """
        update hook
        
        https://rogerbinns.github.io/apsw/example.html
        
        https://github.com/rogerbinns/apsw
        """
                
        #%%
        import os
        import apsw
        import time
        import sys
        py3 = sys.version_info >= (3, 0)


        def inext(v):  # next value from iterator
        return next(v) if py3 else v.next()


        ###
        ### Check we have the expected version of apsw and sqlite
        ###
        print("      Using APSW file", apsw.__file__)                # from the extension module
        print("         APSW version", apsw.apswversion())           # from the extension module
        print("   SQLite lib version", apsw.sqlitelibversion())      # from the sqlite library code
        print("SQLite header version", apsw.SQLITE_VERSION_NUMBER)   # from the sqlite header file at compile time


        #%%
        ###
        ### Opening/creating database
        ###

        connection = apsw.Connection("dbfile")
        cursor = connection.cursor()


        #%%
        ###
        ### update hook
        ###

        def myupdatehook(type, databasename, tablename, rowid):
        print("Updated: %s database %s, table %s, row %d" % (
                apsw.mapping_authorizer_function[type], databasename, tablename, rowid))


        cursor.execute("create table foo(x,y,z)")

        connection.setupdatehook(myupdatehook)

        cursor.execute("insert into foo values(?,?,?)", (1, 1.1, None))  # integer, float/real, Null
        cursor.execute("insert into foo(x) values(?)", ("abc", ))        # string (note trailing comma to ensure tuple!)
        cursor.execute("insert into foo(x) values(?)",  (b"abc\xff\xfe",))    # a blob (binary data)

        connection.setupdatehook(None)


        #%%
