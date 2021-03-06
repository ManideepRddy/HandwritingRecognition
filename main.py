#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from trainer import trainer

inFile = sys.argv[1]
outFile = sys.argv[2]

# Sets up log level based on environment variabel exported by make
def logLevelResolver():
    logLevel = setupLogging.logging.WARNING
    if os.environ.get('logLevel') is None:
        return logLevel
    if os.environ['logLevel'] == 'DEBUG':
        logLevel = setupLogging.logging.DEBUG
    elif os.environ['logLevel'] == 'INFO':
        logLevel = setupLogging.logging.INFO
    return logLevel

# Acquires log level from logLevelResolver
def envHandler():
    return 1
    logLevel = logLevelResolver()
    return logLevel

# Instantiates the GUI and applies styling.
def run():
    app = window.QtGui.QApplication(sys.argv)
    sshFile = './stylesheet/darkOrange.stylesheet'
    with open(sshFile, 'r') as fh:
        app.setStyleSheet(fh.read())
    app.setStyleSheet(window.qdarkstyle.load_stylesheet_pyqt())
    _GUI = window.Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    trainer.Pretrainer(inFile, outFile)
    logLevel = envHandler()