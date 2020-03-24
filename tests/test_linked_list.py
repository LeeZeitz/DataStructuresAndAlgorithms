

def test_insert():
    linked_list = LinkedList()
    linked_list.insert(1)
    head = linked_list.peek()
    assert head == 1, f'insert test failed, expected {1} but got {head}'
    linked_list.insert(2)
    head = linked_list.peek()
    assert head == 1, f'insert test failed, expected {1} but got {head}'
    
    print('insert test Passed!')

# Remove should accept a key parameter and delete the corresponding item from the list, if it exists.
def test_remove():
    # Setup
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    linked_list.insert(7)

    # Test removing head
    linked_list.remove(1)
    assert linked_list.peek() == 2, f"Remove test failed. Expected `{2}` but was `{linked_list.peek()}`"
    assert linked_list.length() == 6, f"Remove test failed. Expected new length to be `{6}` but was `{linked_list.length()}`"

    # Test removing tail
    linked_list.remove(7)
    assert linked_list.peek() == 2, f"Remove test failed. Expected head to be `{2}` but was {linked_list.peek()}"
    assert linked_list.length() == 5, f"Remove test failed. Expected new length to be `{5}` but was `{linked_list.peek()}`"

    # Test removing from center
    linked_list.remove(4)
    assert linked_list.peek() == 2, f"Remove test failed. Expected head to be `{2}` but was `{linked_list.peek()}`"
    assert linked_list.length() == 4, f"Remove test failed. Expected new length to be `{4}` but was `{linked_list.peek()}`"
    assert not linked_list.contains(4), f"Remove test failed. `4` found in list but should have been removed."
    
    # Test removing key not in list
    linked_list.remove(100)
    assert linked_list.length() == 4, f"Remove test failed. Expected the length not to change from `{4}` when remove key not present, but changed to `{linked_list.length()}`"


# Contains should return true if a given key is in the list, false if it is not
def test_contains():
    # Setup
    linked_list = LinkedList()
    
    # Test contains on empty list
    assert not linked_list.contains(1), f'Contains test failed. List should be empty, but returned non-false response.'
    
    # Test contains positive
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.contains(1), f'Contains test failed. Expected `true`, got `false`'
    assert linked_list.contains(2), f'Contains test failed. Expected `true`, got `false`'

    # Test contains negative
    assert not linked_list.contains(-1), f'Contains test failed. Expected `false`, got `true`'
    

# Peek should return the first element in the list
def test_peek():
    # Setup
    linked_list = LinkedList()

    # Test peeking an empty list
    assert linked_list.peek() == None, f'Peek test failed. Should have returned `None`, but returned {linked_list.peek()}'

    # Test peek on list with one element
    linked_list.insert(9)
    head = linked_list.peek()
    assert head == 9, f'Peek test failed. Expected to see `9`, saw {head}'
    assert head == 9, f'Peek test failed. Expected to see `9`, saw {head}'

    # Test peeking a full list
    linked_list.insert(1)
    linked_list.insert(10)
    linked_list.insert(11)
    linked_list.insert(12)
    linked_list.insert(13)

    head = linked_list.peek()
    assert head == 9, f'Peek test failed. Expected head to be `9`, saw {head}'


# Pop should return and remove the first element in the list
def test_pop():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    head = linked_list.pop()
    assert head == 1, f"Pop test failed. Expected popped element to be {1} but got {head}"
    assert linked_list.peek() == 2, f"Pop test failed. Expected new head to be {2} but was {linked_list.peek()}"
    assert linked_list.length() == 1, f"Pop test failed. Expected new list length to be {1} but was {linked_list.length()}"
    head linked_list.pop()
    assert head == 2, f"Pop test failed. Expected popped element to be {2} but got {head}"
    assert linked_list.peek() == None, f"Pop test failed. Expected new head to be {None} but was {linked_list.peek()}"
    assert linked_list.length() == 0, f"Pop test failed. Expected new list length to be {0} but was {linked_list.length()}"

    linked_list.insert(100)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    linked_list.insert(7)
    linked_list.insert(8)
    linked_list.insert(9)
    linked_list.insert(10)
    linked_list.insert(11)
    linked_list.insert(12)
    linked_list.insert(13)
    linked_list.insert(14)
    linked_list.insert(15)
    linked_list.insert(16)
    linked_list.insert(17)
    linked_list.insert(0)
   
    head = linked_list.pop()
    assert head == 100, f"Pop test failed. Expected popped element to be {100} but got {head}"
    assert linked_list.peek() == 2, f"Pop test failed. Expected new head to be {2} but was {linked_list.peek()}"
    assert linked_list.length() == 17, f"Pop test failed. Expected new list length to be {17} but was {linked_list.length()}"

    print('Pop test Passed!')


# Length should return the current length of the list (current number of elements)
def test_length():
    pass