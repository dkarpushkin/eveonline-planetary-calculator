import logging


class EveDbRouter(object):

    # @staticmethod
    def db_for_read(self, model, **hints):
        from django.conf import settings
        if not 'eve_db' in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'eve_database':
            return 'eve_db'
        return None

    # @staticmethod
    def db_for_write(self, model, **hints):
        from django.conf import settings
        if not 'eve_db' in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'eve_database':
            return 'eve_db'
        return None

    # @staticmethod
    # def allow_relation(self, obj2, **hints):
    #     return True

    # @staticmethod
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        from django.conf import settings
        if not 'eve_db' in settings.DATABASES.keys():
            return None
        # logging.error(app_label + " - " + db + " - " + str(model_name))
        if db == 'eve_db':
            if app_label == 'eve_database':
                logging.debug("migration approved")
                return 'eve_db'
        elif app_label == 'eve_database':
            logging.debug("migration denied")
            return False
        return None
