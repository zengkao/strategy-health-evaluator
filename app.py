import webview
import os
import sys

def get_resource_path(filename):
    """Get path to bundled resource (works both dev and PyInstaller)."""
    if getattr(sys, '_MEIPASS', None):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

if __name__ == '__main__':
    html_path = get_resource_path('策略評估系統.html')
    window = webview.create_window(
        '策略健康度評估系統',
        url=html_path,
        width=1400,
        height=900,
        min_size=(900, 600),
        text_select=True,
    )
    webview.start()
