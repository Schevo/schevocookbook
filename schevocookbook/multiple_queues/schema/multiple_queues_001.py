from schevo.schema import *
schevo.schema.prep(locals())


class Item(E.Entity):

    number = f.integer()

    _key(number)

    _sample_unittest = [
        (1, ),
        (2, ),
        (3, ),
        (4, ),
        (5, ),
        (6, ),
        ]


class Queue(E.Entity):

    name = f.string()
    head = f.entity('QueueMember', required=False)
    tail = f.entity('QueueMember', required=False)
    @f.integer()
    def size(self):
        return self.sys.count('QueueMember', 'queue')

    _key(name)

    def t_pop(self):
        tx = E.Queue._Pop()
        tx.queue = self
        return tx

    def t_push(self, item=UNASSIGNED):
        tx = E.Queue._Push()
        tx.queue = self
        tx.item = item
        return tx

    class _Pop(T.Transaction):
        
        queue = f.entity('Queue')
        
        def _execute(self, db):
            queue = self.queue
            head = queue.head
            item = head.item
            if queue.head == queue.tail:
                # Popping only of queue.
                db.execute(queue.t.update(
                    head = UNASSIGNED,
                    tail = UNASSIGNED,
                    ))
                db.execute(head.t.delete())
            else:
                # Popping head of queue.
                new_head = head.next
                db.execute(queue.t.update(
                    head = new_head,
                    ))
                db.execute(head.t.delete())
            return item

    class _Push(T.Transaction):

        queue = f.entity('Queue')
        item = f.entity('Item')

        def _execute(self, db):
            queue_member = db.execute(db.QueueMember.t.create(
                queue = self.queue,
                item = self.item,
                next = UNASSIGNED,
                ))
            if self.queue.head is UNASSIGNED:
                # Pushing first member to queue.
                db.execute(self.queue.t.update(
                    head = queue_member,
                    tail = queue_member,
                    ))
            else:
                # Member(s) already in queue.
                db.execute(self.queue.tail.t.update(
                    next = queue_member,
                    ))
                db.execute(self.queue.t.update(
                    tail = queue_member,
                    ))
            return queue_member

    _sample_unittest = [
        ('A', ),
        ('B', ),
        ]


class QueueMember(E.Entity):

    queue = f.entity('Queue')
    item = f.entity('Item')
    next = f.entity('QueueMember', required=False)
    @f.entity('QueueMember', required=False)
    def previous(self):
        next = self.m.queue_members()
        if next:
            return next[0]
        else:
            return UNASSIGNED
    
    _key(queue, item)
