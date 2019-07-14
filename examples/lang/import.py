#%% 
def import_module() :
    """
    import module from module file
    """
    import importlib 
    import importlib.util
    import sys

    # For illustrative purposes.
    name = 'itertools'

    spec = importlib.util.find_spec(name)
    if spec is None:
        print("can't find the itertools module")
    else:
        # If you chose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Adding the module to sys.modules is optional.
        sys.modules[name] = module

#%%
def import_source() :
    """
    import from source file
    """
    # import source file
    import importlib.util
    import sys

    # For illustrative purposes.
    import tokenize
    file_path = tokenize.__file__
    module_name = tokenize.__name__

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Optional; only necessary if you want to be able to import the module
    # by name later.
    sys.modules[module_name] = module

