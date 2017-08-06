import logging

class MessageError(BaseException):
    message = ''

    def __init__(self, message):
        self.message = message


class PiCalcDbRouter(object):

    # @staticmethod
    def db_for_read(self, model, **hints):
        from django.conf import settings
        if not 'pi_calc' in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'pi_calculator':
            return 'pi_calc'
        return None

    # @staticmethod
    def db_for_write(self, model, **hints):
        from django.conf import settings
        if not 'pi_calc' in settings.DATABASES.keys():
            return None
        if model._meta.app_label == 'pi_calculator':
            return 'pi_calc'
        return None

    # @staticmethod
    # def allow_relation(self, obj2, **hints):
    #     return True

    # @staticmethod
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        from django.conf import settings
        if not 'pi_calc' in settings.DATABASES.keys():
            return None
        # logging.error(app_label + " - " + db)
        if db == 'pi_calc':
            if app_label == 'pi_calculator':
                # logging.error("migration approved")
                return True
        elif app_label == 'pi_calculator':
            # logging.error("migration denied")
            return False
        return None
