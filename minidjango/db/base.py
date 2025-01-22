from minidjango.db.models.fields import Field
import sqlite3


class Model:

    def __init__(self, **kwargs):
        self._meta()
        for field_name, value in kwargs.items():
            if field_name in self.__class__.__dict__:
                field = self.__class__.__dict__[field_name]
                if isinstance(field, Field):
                    setattr(self, field_name, value)

    @classmethod
    def _meta(cls):
        cls.table_name = cls.__name__.lower()

        db_fields = {}
        for name, attr in cls.__dict__.items():
            if isinstance(attr, Field):
                attr.contribute_to_class(name)
                db_fields[name] = attr.get_field_sql()
        cls._db_fields = db_fields
        cls.run_sql(cls.create_table())

    @classmethod
    def run_sql(cls, sql):
        conn = sqlite3.Connection('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()

    @classmethod
    def create_table(cls):
        fields = ', '.join(value for value in cls._db_fields.values())
        sql = f'CREATE TABLE IF NOT EXISTS {cls.table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {fields})'
        return sql