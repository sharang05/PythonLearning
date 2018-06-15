
# Decorator Class Example
class decorator_class(object):

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('call method executed this before {}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)


@decorator_class
def display():
	print('display function ran')

@decorator_class
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display()
display_info('john', 25)


# Complete decorator Function Example
def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print('display function ran')

@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display()
display_info('john', 25)



# Decorator Function
def decorator_function(original_function):
	def wrapper_function():
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

def display():
	print('display function ran')

decorated_display = decorator_function(display)
decorated_display()



# Decorator Function actual method
def decorator_function(original_function):
	def wrapper_function():
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

@decorator_function
def display():
	print('display function ran')

display()




# python decorator/first class
def outer_func(msg):
	message = msg

	def inner_func():
		print(message)
	return inner_func

hi_func = outer_func('Hi')
bye_func = outer_func('Bye!')

print(hi_func)
print(bye_func)

hi_func()
bye_func()




#Python closer concept

def outer_func():
	message = 'Hi'

	def inner_func():
		print(message)
	return inner_func

my_func = outer_func()
my_func()
my_func()
my_func()
my_func()