"""
Module containing the 'AdvanceEntity' Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .balance_entity import BalanceEntity

# MODULE IMPORTS
from decimal import Decimal
from dataclasses import dataclass

from .event_entity import EventEntity


@dataclass
class AdvanceEntity(EventEntity):
    """
    Class to represent an advance entity.

    This class inherits from the 'EventEntity' Abstract Class, which means that it has the superclass attributes
    and implements the following methods:

    * process_entity(balance_entity: BalanceEntity) -> None

    Attributes
    -----------
    id : int
        This advance entity id.

    current_balance : Decimal
        The current balance of this advance entity.
    """
    id: int
    current_balance: Decimal

    def process_entity(self, balance_entity: BalanceEntity) -> None:
        """
        Method to process this advance entity.

        Parameters
        ----------
        balance_entity : BalanceEntity
            Entity containing all the current balances.
        """
        # THERE IS PAYMENT TO PAY ALL THE CURRENT BALANCE
        if balance_entity.payments_for_future > self.current_balance:
            balance_entity.payments_for_future -= self.current_balance
            self.current_balance = Decimal(0)

        # PAYMENT PAYS ONLY A PORTION OF CURRENT BALANCE
        else:
            self.current_balance -= balance_entity.payments_for_future
            balance_entity.payments_for_future = Decimal(0)

        balance_entity.advance_balance += self.current_balance

        balance_entity.advances.append(self)
