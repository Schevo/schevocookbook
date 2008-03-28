from schevo.schema import *
schevo.schema.prep(locals())


import datetime
now = datetime.datetime.now


class Thing(E.Entity):

    name = f.string()
    created = f.datetime(readonly=True)
    
    class _Create(T.Create):
        
        def _before_execute(self, db):
            self.f.created.readonly = False
            self.created = now()
