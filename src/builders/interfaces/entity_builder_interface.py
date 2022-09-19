"""
Module containing the 'EntityBuilder' Interface.
"""

from datetime import date
from decimal import Decimal
from abc import ABC, abstractmethod

from ...entities import EventEntity


class EntityBuilder(ABC):
    """
    Interface to define that all classes that wants to build an entity
    must implement the following methods:

    * build_entity(event_amount: Decimal, event_date: date) -> EventEntity
    """

    @abstractmethod
    def build_entity(self, event_amount: Decimal, event_date: date) -> EventEntity:
        """
        Abstract method to build (or create) an Event Entity.

        Parameters
        ----------
        event_amount : Decimal
            The total amount of that event.

        event_date : date
            The event date.

        Returns
        --------
        EventEntity
            A builded EventEntity object.
        """
