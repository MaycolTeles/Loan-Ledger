"""
Module containing the 'EntitiesHandler' Class.
"""

from decimal import Decimal
from datetime import datetime, date
from typing import Any, Dict, List, Tuple

from ..entities import EventEntity
from ..builders import EntityBuilder, AdvanceEntityBuilder, PaymentEntityBuilder


class EntitiesHandler():
    """
    Class containing all the functionalities to handle all the entities.

    Attributes
    ----------
    events : List[Tuple[Any]]
        A list containing all the events coming from the database.

    end_date : date
        The processing end date.

    entities : List[EventEntity]
        A list containing all the build entities.

    advance_builder : AdvanceEntityBuilder
        A reference to build the advances entities.

    payment_builder : PaymentEntityBuilder
        A reference to build the payment entities.
    """
    events: List[Tuple[Any]]
    end_date: date

    entities: List[EventEntity]
    advance_builder: AdvanceEntityBuilder
    payment_builder: PaymentEntityBuilder

    def __init__(self, events: List[Tuple[Any]], end_date: date) -> None:
        """
        Constructor to set up some attributes.

        Parameters
        ----------
        events : List[Tuple[Any]]
            A list containing all the events coming from the database.

        end_date : date
            The processing end date.
        """
        self.events = events
        self.end_date = end_date

        self.entities = []
        self.advance_builder = AdvanceEntityBuilder()
        self.payment_builder = PaymentEntityBuilder()

    def __build_entity(self, entity_data: Tuple[Any]) -> EventEntity:
        """
        Private Method to build an entity based on its type.

        Parameters
        ----------
        entity_data : Tuple[Any]
            The needed data to build an event entity.

        Returns
        --------
        EventEntity
            A reference to the event entity.
        """
        entity_type = entity_data[1]
        entity_amount = Decimal(entity_data[2])
        entity_date = datetime.strptime(entity_data[3], '%Y-%m-%d').date()

        entity_builders: Dict[str, EntityBuilder] = {
            'advance': self.advance_builder,
            'payment': self.payment_builder
        }

        entity = entity_builders[entity_type].build_entity(
            event_amount=entity_amount,
            event_date=entity_date
        )

        return entity

    def __is_past_end_date(self, current_date: date) -> bool:
        """
        Private Method to check whether the current date is past the end date or not.

        Parameters
        ----------
        current_date : date
            The current event date.

        Returns
        --------
        bool
            - True if the current date is equal to or past the end date;
            - False otherwise
        """
        if current_date >= self.end_date:
            return True

        return False

    def build_entities(self) -> List[EventEntity]:
        """
        Method to build all the entities.

        Returns
        -------
        List[EventEntity]
            A list containing all the built event entities.
        """
        for event_data in self.events:
            current_date = datetime.strptime(event_data[3], '%Y-%m-%d').date()
            past_end_date = self.__is_past_end_date(current_date)

            if past_end_date:
                break

            entity = self.__build_entity(event_data)
            self.entities.append(entity)

        return self.entities
