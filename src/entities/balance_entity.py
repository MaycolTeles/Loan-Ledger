"""
Module containing the 'BalanceEntity' Class.
"""

# TYPING IMPORTS
from typing import List
from . import AdvanceEntity

# MODULE IMPORTS
from decimal import Decimal
from dataclasses import dataclass, field


@dataclass
class BalanceEntity:
    """
    Class to represent an entity with all the balances.

    Attributes
    ----------
    advance_balance : Decimal
        The total advance balance.

    interest_payable_balance : Decimal
        The total interest balance amount.

    interest_paid : Decimal
        The total amount of interest that was paid.

    payments_for_future : Decimal
        The credit for future advances.

    advances : List[AdvanceEntity]
        A list containing all the processed advance entities.
    """
    advance_balance = Decimal(0)
    interest_payable_balance = Decimal(0)
    interest_paid = Decimal(0)
    payments_for_future = Decimal(0)

    advances: List[AdvanceEntity] = field(default_factory=list)
