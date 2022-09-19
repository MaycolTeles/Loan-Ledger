"""
Module containing the 'EventEntity' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .balance_entity import BalanceEntity

# MODULE IMPORTS
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class EventEntity(ABC):
    """
    Abstract Class to represent a generic event entity.

    All classes that wants to represent a specific entity must extend this class
    and implement the following methods:

    * process_entity(balance_entity: BalanceEntity) -> None

    Attributes
    ----------
    initial_amount : Decimal
        The entity initial amount.

    event_date : date
        The entity date.
    """
    initial_amount: Decimal
    event_date: date

    @abstractmethod
    def process_entity(self, balance_entity: BalanceEntity) -> None:
        """"""
