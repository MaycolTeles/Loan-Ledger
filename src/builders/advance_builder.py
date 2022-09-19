"""
Module containing the 'AdvanceEntityBuilder' Class.
"""

from datetime import date
from decimal import Decimal

from .interfaces.entity_builder_interface import EntityBuilder
from ..entities import AdvanceEntity


class AdvanceEntityBuilder(EntityBuilder):
    """
    Class to represent a Builder for all the Advance entities.

    This class implements the 'EntityBuilder' Interface, so it implements the following methods:
    * build_entity(event_amount: Decimal, event_date: date) -> AdvanceEntity

    Attributes
    ----------
    advance_entities_index : int
        The index of each advance entity.
    """
    advance_entities_index: int = 1

    def build_entity(self, event_amount: Decimal, event_date: date) -> AdvanceEntity:
        """
        Method to build (or create) an Advance Entity.

        Parameters
        ----------
        event_amount : Decimal
            The total amount of the advance event.

        event_date : date
            The event date.

        Returns
        --------
        AdvanceEntity
            A builded AdvanceEntity object.
        """
        event = AdvanceEntity(
            id=self.advance_entities_index,
            initial_amount=event_amount,
            event_date=event_date,
            current_balance=event_amount
        )

        self.advance_entities_index += 1

        return event
