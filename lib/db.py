from psycopg2 import connect, extras

class Db(object):

    connection = None

    @staticmethod
    def connect(config):
        Db.connection = connect(**config)
        return Db.connection

    @staticmethod
    def rollback():
        Db.connection.rollback()

    @staticmethod
    def commit():
        Db.connection.commit()

    @staticmethod
    def close():
        Db.connection.close()

    @staticmethod
    def get_cursor():
        return Db.connection.cursor(cursor_factory=extras.DictCursor)

    @staticmethod
    def exec_query(query, returning = False, returning_multi = False):
        cursor = None
        result = None

        try:
            cursor = Db.get_cursor()
            cursor.execute(query)

            if returning:
                result = cursor.fetchone()
            elif returning_multi:
                result = cursor.fetchall()

            # print 'result2'
            # print result
            # print query
        except Exception as e:
            Db.rollback()
            print "Error executing query"
            print e
            raise e
        else:
            Db.commit()
        finally:
            if cursor is not None:
                cursor.close()
            return result
