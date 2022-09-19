"""
Module containing the 'EventHandler' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import Any, Tuple, List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..entities import EventEntity, BalanceEntity

# MODULE IMPORTS
from datetime import date

from .entities_handler import EntitiesHandler
from ..use_cases import CalculateAdvances


class EventHandler():
    """
    Class to handle the received events.

    Attributes
    ----------
    events : Tuple[Any]
        The events to be handled.

    end_date : date
        The end date to process until it.
    """
    events: Tuple[Any]
    end_date: date

    def __init__(self, events: Tuple[Any], end_date: date) -> None:
        """
        Constructor to set up some attributes.

        Parameters
        ----------
        events : Tuple[Any]
            The events to be handled.

        end_date : date
            The end date to process until it.
        """
        self.events = events
        self.end_date = end_date

    def __process_all_entities(self, entities: List[EventEntity]) -> BalanceEntity:
        """
        Private Method to process all the entities.

        Parameters
        ----------
        entities : List[EventEntity]
            A list containing all the entities to be processed.

        Returns
        -------
        BalanceEntity
            The balance entity after all entities were processed.
        """
        calculate_advances = CalculateAdvances(entities, self.end_date)

        return calculate_advances.get_balance()

    def handle_all_events(self) -> BalanceEntity:
        """
        Method to handle all the events and return their balance.

        Returns
        -------
        BalanceEntity
            An entity containing all the events balance.
        """
        entities_handler = EntitiesHandler(self.events, self.end_date)

        entities = entities_handler.build_entities()

        return self.__process_all_entities(entities)
