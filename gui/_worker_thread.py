from PyQt6.QtCore import QThread, pyqtSignal


class WorkerThread(QThread):
    progress = pyqtSignal(int)
    status_message = pyqtSignal(str)

    def __init__(
        self,
        action_callback: object,
        callback_arguments: dict = {},
        after_execution_action: object = None,
    ):
        """
        Initialises the worker thread and performs the action callback when executed the start() method!

        Args:
            action_callback (object): _description_
            callback_arguments (dict, optional): a keyword argument dictionary for the action callback!. Defaults to {}.
            after_execution_action (object, optional): a callback to execute after finishing the execution of the action_callback. Defaults to None.
        """
        super().__init__()
        self.action_callback = action_callback
        self.callback_arguments = callback_arguments
        self.after_execution_action = after_execution_action

    def run(self):
        """
        Executes the given action callback in a separate thread and provides the progress to the main thread.


        """
        # setting up the keyword arguments
        self.callback_arguments["update_progress_signal"] = self.progress
        self.callback_arguments["update_status_message_signal"] = self.status_message

        # execution
        try:
            self.action_callback(**self.callback_arguments)
        except:
            # errors must have already been displayed to the user through the action callback
            return None

        # finishing off if there are no errors!
        self.after_execution_action()
