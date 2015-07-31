# Copyright (C) 2005-2012 the Pool authors and contributors <see AUTHORS file>
#
# This module is part of Pool and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""Exceptions used with Pool.

The base exception class is :class:`.PoolError`.

"""


class PoolError(Exception):

    """Generic error class."""


class DisconnectionError(PoolError):

    """A disconnect is detected on a raw connection.

    This error is raised and consumed internally by a connection pool.  It can
    be raised by the :meth:`.PoolEvents.checkout` event
    so that the host pool forces a retry; the exception will be caught
    three times in a row before the pool gives up and raises
    :class:`~pool.exc.InvalidRequestError` regarding the connection attempt.

    """


class TimeoutError(PoolError):

    """Raised when a connection pool times out on getting a connection."""


class InvalidRequestError(PoolError):

    """Pool was asked to do something it can't do.

    This error generally corresponds to runtime state errors.

    """
