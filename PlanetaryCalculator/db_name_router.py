

class DbNameRouter(object):

    @staticmethod
    def db_for_read(self, **hints):
        if hasattr(self._meta, 'db_name'):
            return self._meta.db_name
        return None

    @staticmethod
    def db_for_write(self, **hints):
        if hasattr(self._meta, 'db_name'):
            return self._meta.db_name
        return None

    @staticmethod
    def allow_relation(self, obj2, **hints):
        return True

    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints):
        if db == 'eve_db':
            return app_label == 'eve_database'

        return True

