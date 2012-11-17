import sublime, sublime_plugin

def simple_keyword():
    """Log a message"""
    print 'You have used the simplest keyword.'

def greet(name):
    """Logs a friendly greeting to person given as argument"""
    print 'Hello %s!' % name

def multiply_by_two(number):
    """Returns the given number multiplied by two
    
    The result is always a floating point number.
    This keyword fails if the given `number` cannot be converted to number.
    """
    return float(number) * 2

def numbers_should_be_equal(first, second):
    print '*DEBUG* Got arguments %s and %s' % (first, second)
    if float(first) != float(second):
        raise AssertionError('Given numbers <%s> and <%s> are unequal!' % (first, second))

def syntax_is_robot_format(file_name):
    view = open_file(file_name, sublime.TRANSIENT)
    syntax = view.settings().get('syntax')
    if syntax != 'syntax':
        raise AssertionError('View is not in the robot framework syntax but is <%s>' % syntax)