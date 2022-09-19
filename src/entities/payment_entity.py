"""
Module containing the 'PaymentEntity' Class.
"""

from dataclasses import dataclass
from decimal import Decimal

from .event_entity import EventEntity
from .balance_entity import BalanceEntity


@dataclass
class PaymentEntity(EventEntity):
    """
    Class to represent a payment entity.

    This class inherits from the 'EventEntity' Abstract Class, which means that it has the superclass attributes
    and implements the following methods:

    * process_entity(balance_entity: BalanceEntity) -> None
    """

    def process_entity(self, balance_entity: BalanceEntity) -> None:
        """
        Method to process this payment entity.

        Parameters
        ----------
        balance_entity : BalanceEntity
            Entity containing all the current balances.
        """
        current_payment_value = self.initial_amount

        # PAYING ONLY A PORTION OF THE INTEREST BALANCE AMOUNT
        if current_payment_value <= balance_entity.interest_payable_balance:
            balance_entity.interest_payable_balance -= current_payment_value
            balance_entity.interest_paid += current_payment_value
            return

        # PAYING THE INTEREST BALANCE AMOUNT IN TOTALLY
        current_payment_value -= balance_entity.interest_payable_balance
        balance_entity.interest_paid += balance_entity.interest_payable_balance
        balance_entity.interest_payable_balance = Decimal(0)

        credit_payment_amount = self.__reduce_advance_balance(balance_entity, current_payment_value)
        balance_entity.payments_for_future += credit_payment_amount

    def __reduce_advance_balance(self, balance_entity: BalanceEntity, current_payment_value: Decimal) -> Decimal:
        """
        Private Method to reduce the total advance balance.

        Parameters
        ----------
        balance_entity : BalanceEntity
            A reference for the balance entity.

        current_payment_value : Decimal
            The current amount of payment.

        Returns
        --------
        Decimal
            The amount left over after paying all advances.
        """
        for entity in balance_entity.advances:
            if current_payment_value <= entity.current_balance:
                # PAYING ONLY A PORTION OF THE ADVANCE
                entity.current_balance -= current_payment_value
                balance_entity.advance_balance -= current_payment_value
                return Decimal(0)

            # PAYING THE ADVANCE IN TOTALLY
            current_payment_value -= entity.current_balance
            balance_entity.advance_balance -= entity.current_balance
            entity.current_balance = Decimal(0)

            if balance_entity.advance_balance < 0:
                balance_entity.advance_balance = Decimal(0)

        return current_payment_value
