def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwarness(1)
    except:
        pass
