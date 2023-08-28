import importlib


def check_req():
    result = False
    try:
        importlib.import_module('PIL')
        requests_installed = True
        result = True
    except ImportError:
        requests_installed = False

    try:
        importlib.import_module('cv2')
        beautifulsoup_installed = True
        result = True
    except ImportError:
        beautifulsoup_installed = False

    if not requests_installed:
        try:
            import subprocess

            subprocess.check_call(['pip', 'install', 'opencv-python'])
            importlib.import_module('requests')
            result = True
        except Exception as e:
            print(f'An error occurred while installing the opencv package: {str(e)}')

    if not beautifulsoup_installed:
        try:
            import subprocess

            subprocess.check_call(['pip', 'install', 'Pillow'])
            importlib.import_module('bs4')
            result = True
        except Exception as e:
            print(f'An error occurred while installing the Pillow package: {str(e)}')

    return result
