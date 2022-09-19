"""
Module containing the 'CalculateAdvances' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from datetime import date
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from ..entities import EventEntity

# MODULE IMPORTS
from decimal import Decimal

from ..entities import BalanceEntity


class CalculateAdvances():
    """
    Class to calculate all the advances.

    Attributes
    ----------
    entities : List[EventEntity]
        A list containing all the entities to be calculated.

    end_date : date
        The end date to process until it.

    balance_entity : BalanceEntity
        An entity containing all the events balance.
    """
    entities: List[EventEntity]
    end_date: date

    balance_entity: BalanceEntity

    def __init__(self, entities: List[EventEntity], end_date: date) -> None:
        """
        Constructor to set up some attributes.

        Parameters
        ----------
        entities : List[EventEntity]
            A list containing all the entities to be calculated.

        end_date: date
            The end date to process until it.
        """
        self.entities = entities
        self.end_date = end_date

        self.balance_entity = BalanceEntity()

    def get_balance(self) -> BalanceEntity:
        """
        Method to get the final balance.

        Returns
        --------
        BalanceEntity
            A reference to all the events balance.
        """
        for current_entity, next_entity in zip(self.entities, self.entities[1:]):

            next_entity_date = next_entity.event_date

            self.process_entity(current_entity, next_entity_date)

        # PROCESSING THE LAST EVENT
        current_entity = self.entities[-1]
        self.process_entity(current_entity, self.end_date)

        return self.balance_entity

    def process_entity(self, entity: EventEntity, next_entity_date: date) -> None:
        """
        Method to process a single entity.

        Parameters
        ----------
        entity : EventEntity
            A reference to the entity to be processed.

        next_entity_date : date
            The next entity date.
        """
        entity.process_entity(self.balance_entity)
        self.calculate_interest_payable_balance(entity, next_entity_date)

    def calculate_interest_payable_balance(self, entity: EventEntity, next_entity_date: date) -> None:
        """
        Method to calculate the interest payable balance of that current entity.

        Parameters
        -----------
        entity : EventEntity
            A reference to the entity to be processed.

        next_entity_date : date
            The next entity date.
        """
        days_between_end_date = (next_entity_date - entity.event_date).days

        accrued_interest = Decimal(0.00035) * self.balance_entity.advance_balance * days_between_end_date

        self.balance_entity.interest_payable_balance += accrued_interest
