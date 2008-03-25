from schevo.schema import *
schevo.schema.prep(locals())


import datetime
now = datetime.datetime.now


class Thing(E.Entity):

    name = f.unicode()
    created = f.datetime(readonly=True)
    updated = f.datetime(readonly=True, required=False)
    
    class _Create(T.Create):
        
        def _before_execute(self, db):
            self.f.created.readonly = False
            self.created = now()

    class _Update(T.Update):
        
        def _before_execute(self, db, thing):
            self.f.updated.readonly = False
            self.updated = now()
