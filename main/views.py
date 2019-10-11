from flask import jsonify, request
from flask_cors import cross_origin
from main.app import app
from main.data_structures.array_stack import ArrayStack
from main.data_structures.queue import ArrayQueue
from main.data_structures.linked_list import PositionalList
from main.data_structures.finobacci import fino, fact
from main.data_structures.plist import PList


stack = ArrayStack()
queue = ArrayQueue()
linked_list = PList()

@app.route('/')
def index():
	return 'api'


@app.route('/finobacci', methods=['GET', 'POST'])
@cross_origin()
def finobacci():
	''' Returns elements of a finobacci function. '''
	n = int(request.json['e'])
	l = []
	for value in range(n):
		l.append(fino(value))
	print(l)
	return jsonify({ 'success': True, 'elements': l })


@app.route('/factorial', methods=['GET', 'POST'])
@cross_origin()
def factorial():
	''' Returns elements of a finobacci function. '''
	n = int(request.json['e'])
	f = fact(n)
	print(f)
	return jsonify({ 'success': True, 'factorial': f })


@app.route('/stack_elements')
@cross_origin()
def stack_elements():
	''' Retrieves all elements in the stack. '''
	elements = stack.elements()
	return jsonify({ 'elements': elements })


@app.route('/stack_length')
@cross_origin()
def stack_length():
	''' Checks the size of the stack. '''
	length = len(stack)
	return jsonify({ 'length': length })


@app.route('/stack_top')
@cross_origin()
def stack_top():
	''' Returns the top most element of a stack. '''
	try:
		top = stack.top()
		return jsonify({ 'top': top })
	except:
		return jsonify({ 'error': True })


@app.route('/stack_push', methods=['GET', 'POST'])
@cross_origin()
def stack_push():
	''' Pushes element into the stack. '''
	e = request.json['e']
	stack.push(e)
	return jsonify({ 'success': True })


@app.route('/stack_pop')
@cross_origin()
def stack_pop():
	''' Pops elements off the stack. '''
	try:
		popped = stack.pop()
		return jsonify({ 'popped': popped })
	except:
		return jsonify({ 'error': True })


@app.route('/queue_dequeue')
@cross_origin()
def queue_dequeue():
	''' Returns and removes first element of the queue. '''
	if not queue.is_empty():
		element = queue.dequeue()
		return jsonify({ 'element': element })
	else:
		return jsonify({ 'error': True })


@app.route('/queue_enqueue', methods=['GET', 'POST'])
@cross_origin()
def queue_enqueue():
	''' Pushes element into the queue. '''
	e = request.json['e']
	queue.enqueue(e)
	return jsonify({ 'success': True })


@app.route('/queue_elements')
@cross_origin()
def queue_elements():
	''' Retrieves all elements in the queue. '''
	elements = list(queue.get_elements())
	return jsonify({ 'elements': elements })


@app.route('/queue_size')
@cross_origin()
def queue_size():
	''' Returns size of the queue. '''
	size = len(queue)
	return jsonify({ 'size': size })


@app.route('/queue_list_size')
@cross_origin()
def queue_list_size():
	''' Returns size of the list. '''
	size = queue.list_size()
	return jsonify({ 'size': size })


@app.route('/queue_is_empty')
@cross_origin()
def queue_is_empty():
	''' Returns whether the queue is empty or not. '''
	is_empty = queue.is_empty()
	return jsonify({ 'is_empty': is_empty })


@app.route('/queue_is_full')
@cross_origin()
def queue_is_full():
	''' Returns whether the queue is full or not. '''
	is_full = queue.is_full()
	return jsonify({ 'is_full': is_full })


@app.route('/list_elements')
@cross_origin()
def list_elements():
	''' Returns elements in the list. '''
	elements = linked_list.get_elements()
	return jsonify({ 'elements': elements })


@app.route('/add_first', methods=['GET', 'POST'])
@cross_origin()
def a_first():
	''' Returns elements in the list. '''
	e = request.json['e']
	linked_list.add_first(e)
	elements = linked_list.get_elements()
	return jsonify({ 'success': True, 'elements': elements })


@app.route('/add_last', methods=['GET', 'POST'])
@cross_origin()
def a_last():
	''' Returns elements in the list. '''
	e = request.json['e']
	linked_list.add_last(e)
	elements = linked_list.get_elements()
	return jsonify({ 'success': True, 'elements': elements })


@app.route('/delete_first', methods=['GET', 'POST'])
@cross_origin()
def delete_first():
	''' Returns elements in the list. '''
	linked_list.delete_first()
	elements = linked_list.get_elements()
	return jsonify({ 'elements': elements })


@app.route('/delete_last', methods=['GET', 'POST'])
@cross_origin()
def delete_last():
	''' Returns elements in the list. '''
	linked_list.delete_last()
	elements = linked_list.get_elements()
	return jsonify({ 'elements': elements })

