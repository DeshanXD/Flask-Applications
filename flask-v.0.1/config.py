import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key&"

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

# This is dict containing classes
config = {
        'development' : DevelopmentConfig,
        'testing' : TestingConfig,
        'production' : ProductionConfig,
        'default' : DevelopmentConfig
}       
