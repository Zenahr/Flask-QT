from threading import Thread
import PyQt5.QtCore as core
import PyQt5.QtWidgets as core_widgets
import PyQt5.QtWebEngine as web_engine
import PyQt5.QtWebEngineWidgets as web_widgets
import PyQt5.QtGui as gui
from flask import current_app, _app_ctx_stack

class FlaskQT(object):
    def __init__(
                self,
                app          = None,
                url          = '127.0.0.1',
                port         = 5000,
                debug        = False,
                using_win32  = False,
                icon_path    = None,
                window_title = None
                ):
        self.flask_app = app
        if app is not None:
            self.init_app(app)
        self.flask_thread = Thread(target=self._run_flask,
                                   args=(url, port, debug, using_win32))
        self.flask_thread.daemon = True
        self.debug = debug

        self.url = "http://{}:{}".format(url, port)
        self.app = core_widgets.QApplication([])
        self.app.setWindowIcon(gui.QIcon(icon_path))
        self.app.setApplicationName(window_title)
        self.view = web_widgets.QWebEngineView(self.app.activeModalWidget())
        self.page = CustomWebEnginePage(self.view)
        self.view.setPage(self.page)

    def init_app(self, app):
        pass

    def run(self):
        self.run_flask()
        self.run_gui()

    def run_flask(self):
        self.flask_thread.start()

    def run_gui(self):
        self.view.load(core.QUrl(self.url))

        change_setting = self.view.page().settings().setAttribute
        settings = web_widgets.QWebEngineSettings
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.PluginsEnabled, True)

        # TODO: These settings aren't implemented in QWebEngineSettings (yet)
        #change_setting(settings.DeveloperExtrasEnabled, True)
        #change_setting(settings.OfflineStorageDatabaseEnabled, True)
        #change_setting(settings.OfflineWebApplicationCacheEnabled, True)

        self.view.showMaximized()

        self.app.exec_()

    def _run_flask(self, host, port, debug=False, using_win32=False):
        print(host)
        if using_win32:
            import pythoncom
            pythoncom.CoInitialize()
        self.flask_app.run(debug=debug, host=host, port=port, use_reloader=False)

class CustomWebEnginePage(web_widgets.QWebEnginePage):
    def createWindow(self, _type):
        page = CustomWebEnginePage(self)
        page.urlChanged.connect(self.open_browser)
        return page

    def open_browser(self, url):
        page = self.sender()
        gui.QDesktopServices.openUrl(url)
        page.deleteLater()