from datetime import datetime
from pythonosc import dispatcher
from pythonosc import osc_server
import pyautogui
class MuseInput:
    #connection related global variables
    ip = "0.0.0.0"
    port = 5000

    clench_count = 0
    dispatcher = dispatcher.Dispatcher()

    def jaw_clench_handler(address: str, *args):

       for arg in args:
        pyautogui.click()
        print("clenched")

    def eeg_handler(address: str, *args):
        dateTimeObj = datetime.now()
        printStr = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S.%f")
        for arg in args:
            printStr += "," + str(arg)
        print(printStr)

    def jaw_clench(self, dispatcher, ip, port, handler):
        dispatcher.map("/muse/elements/jaw_clench", handler)
        server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
        print("Listening on UDP port " + str(port))
        server.serve_forever()
