from smartninja_sql.sqlite import SQLiteDatabase

chinook = SQLiteDatabase('Chinook_Sqlite.sqlite')
chinook.print_tables(verbose=True)

chinook.pretty_print("SELECT Name FROM Artist;")

chinook.pretty_print("""SELECT * FROM Invoice
                        WHERE BillingCountry='Germany';
                """)

chinook.pretty_print("SELECT COUNT(AlbumId) FROM Album;")

chinook.pretty_print("""SELECT COUNT(*) 
                    FROM Customer
                    WHERE Country='France'""")