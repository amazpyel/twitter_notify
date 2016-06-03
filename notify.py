import pynotify


def msg(title_text='Title', text='There has to be text.'):
    pynotify.init("Basics")
    n = pynotify.Notification(title_text, text)
    n.show()