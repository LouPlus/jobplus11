class BaseConfig(object):
    pass

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

configs = {
    'development':DevelopmentConfig,
    'production' : ProductionConfig
        }
