======================================================================================
``display-session``: Convenient formatting, coloring and utility for print statements.
======================================================================================

**display-session** is an MIT licensed Python package that provides easy ANSI formatting and utility to Python's built in print statement.

This project stemmed from wanting better looking, more informative, and more engaging command line interfaces.

Simple comparison and examples::
    
    >>>print('This is how the builtin print function works')
    This is how the builtin print function works


Simplest compelling usecase for display_session::

    >>>from display_session import DisplaySession
    >>>display = DisplaySession('This is a byline') 
    >>>display.report('The byline proceeds any text input here')
    
    # hard to show with markdown, but byline is also separately ANSI colored.
    This is a byline  : The byline proceeds any text input here
    
    
More complicated examples::
    
    >>>import datetime as dt
    >>>import psutil
    
    >>>from display_session import DisplaySession
    >>>user = 'John'
    
    >>>display = DisplaySession(byline='P R O G R A M - {}'.format(user), 
                                byline_action=[dt.datetime.now, psutil.cpu_percent]
                                )
    >>>display.report('User successfully logged in')
     P R O G R A M - John  // 2018-09-19 21:55:29.115387 // 9.1: User successfully logged in.
    >>>display.report('User successfully logged out')
     P R O G R A M - John  // 2018-09-19 21:56:14.560489 // 7.8: User successfully logged out.

