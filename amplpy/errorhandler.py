# -*- coding: utf-8 -*-
from __future__ import absolute_import
from . import amplpython


class ErrorHandler(amplpython.ErrorHandler):
    """
    A basic interface for AMPL error handlers. If an application needs to
    implement customised error handling, it must implement this interface and
    then register an instance with the AMPL API using the
    :func:`~amplpy.AMPL.setErrorHandler` method. The underlying AMPL
    interpreter will then report all errors and warnings through this
    interface as :class:`~amplpy.AMPLException` objects.
    """

    def error(self, amplexception):
        """
        Receives notification of an error.
        """
        pass

    def warning(self, amplexception):
        """
        Receives notification of a warning.
        """
        pass
