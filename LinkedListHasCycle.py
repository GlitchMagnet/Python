def has_cycle(head):
    current = head
    seen = set()
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False
