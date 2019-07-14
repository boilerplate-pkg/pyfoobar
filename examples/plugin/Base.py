#%%
import six
import abc
import functools
# import .Mngr 


def id_of(cls) :
    return cls.__module__ + "." + cls.__name__

class PickerMngr(object):

    pickers = []

    @classmethod
    def reg(cls, title, ext = []):
        def r(subclass) :
            info = {
                "title" : title, 
                "cls" : subclass,
                "ext" : ext
                }
            cls.pickers.append(info)
        return r


@six.add_metaclass(abc.ABCMeta)
class PickerBase(object):
    """
    Plugin base for Picker

    """
    
    @abc.abstractmethod
    def event(mouse_event):
        """
        add a mouse event
        """
        pass


@PickerMngr.reg(title="Rect")
class RectPicker(PickerBase):
    """
    picker for rectangle
    """

    def event(mouse_event):
        pass 


@PickerMngr.reg(ext= ["png","jpg"], title="Line")
class LinePicker(PickerBase) :
    "picker for line"

    def event(mouse_event):
        pass


if __name__ == "__main__":
    for picker in PickerMngr.pickers :
        print(picker)
        print(picker["cls"]())
        print(picker["cls"].__name__)
        print(picker["cls"].__module__)
        print(id_of(picker["cls"]))

#%%
