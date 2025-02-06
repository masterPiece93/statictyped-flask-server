from typing import Union
from contextlib import contextmanager

class DbService:

    def __init__(self, db: object):
        self._db: object = db

    def insert_record(self, query: tuple) -> Union[int, Exception] :
        
        if not len(query) == 2:
            raise Exception(f"insert_record | argument:query - must have exactly two parts - (sql: str, params)")
        if not isinstance(query[0], str):
            raise Exception(f"insert_record | argument:query - query[0] must be of type str")
        if not query[0].lower().strip().startswith('insert'):
            raise Exception(f"insert_record | argument:query - query[0] must be an `INSERT` sql")

        _cur: object = self._db.cursor()

        try:
            _cur.execute(*query)
        except Exception as e:
            raise e
        else:
            self._db.commit()
            inserted_id: int = _cur.lastrowid
        finally:
            _cur.close()

        return inserted_id

    @contextmanager
    def using_raw_cursor(self):

        _cur: object = self._db.cursor()
        try:
            yield _cur
        finally:
            _cur.close()
    
    def __del__(self):
        self._db.close()