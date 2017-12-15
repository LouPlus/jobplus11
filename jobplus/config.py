class BaseConfig(object):
    pass

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

configs = {
    'development':CevelopmentConfig
    'production' : ProductionConfig
        }
