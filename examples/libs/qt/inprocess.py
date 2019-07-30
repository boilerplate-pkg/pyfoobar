#%%


from PyQt5 import QtWidgets
from qtconsole.qt import QtGui, QtCore
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


def show():
    """
    An example of embedding a RichJupyterWidget with an in-process kernel.
    We recommend using a kernel in a separate process as the normal option - see
    embed_qtconsole.py for more information. In-process kernels are not well
    supported.
    To run this example:
        python3 inprocess_qtconsole.py
    """

    #global ipython_widget  # Prevent from being garbage collected

    # Create an in-process kernel
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel(show_banner=True)
    # kernel = kernel_manager.kernel
    # kernel.gui = 'qt5'

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    ipython_widget = RichJupyterWidget()
    ipython_widget.kernel_manager = kernel_manager
    ipython_widget.kernel_client = kernel_client
    return ipython_widget


if __name__ == "__main__":
    app = QtCore.QCoreApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    a = show()
    b = show()
    a.show()
    b.show()
    app.exec_()


#%%
