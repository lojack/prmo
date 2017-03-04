import os.path
import shelve

class Config(object):
    BASE_DIR = "~/.prmotron"

    def __init__(self):
        if not os.path.exists(os.path.expanduser(self.BASE_DIR)):
            os.makedirs(os.path.expanduser(self.BASE_DIR))

    def save_config(self, config):
        db = shelve.open(os.path.expanduser("%s/config" % self.BASE_DIR), writeback=True)
        try:
            db['config'] = config
        finally:
            db.close()

    def load_config(self):
        db = shelve.open(os.path.expanduser("%s/config" % self.BASE_DIR), writeback=True)
        try:
            if not db.has_key('config'):
                db['config'] = {}
            config = db['config']
        finally:
            db.close()
        return config

