from PyQt6.QtCore import QThread, pyqtSignal


class WorkerThread(QThread):
    progress = pyqtSignal(int)
    status_message = pyqtSignal(str)

    def run(
        self,
        action_callback: object,
        callback_arguments: dict = {},
        after_execution_action: object = None,
    ):
        """
        Executes the given action callback in a separate thread and provides the progress to the main thread.

        Args:
            action_callback (object): must contain the arguments: update_progress_signal and update_status_message_signal (use this exact name)
            callback_arguments (dict, optional): a keyword argument dictionary for the action callback!
            after_execution_action (object, optional): a callback to execute after finishing the execution of the action_callback
        """
        # setting up the keyword arguments
        callback_arguments["update_progress_signal"] = self.progress
        callback_arguments["update_status_message_signal"] = self.status_message

        # execution
        action_callback(**callback_arguments)

        # finishing off
        after_execution_action()
