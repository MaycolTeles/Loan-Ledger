"""
Module containing the 'PaymentEntityBuilder's Class.
"""

from datetime import date
from decimal import Decimal

from .interfaces.entity_builder_interface import EntityBuilder
from ..entities import PaymentEntity


class PaymentEntityBuilder(EntityBuilder):
    """
    Class to represent a Builder for all the Payment entities.

    This class implements the 'EntityBuilder' Interface, so it implements the following methods:
    * build_entity(event_amount: Decimal, event_date: date) -> PaymentEntity
    """

    def build_entity(self, event_amount: Decimal, event_date: date) -> PaymentEntity:
        """
        Method to build (or create) a Payment Entity.

        Parameters
        ----------
        event_amount : Decimal
            The total amount of the payment event.

        event_date : date
            The event date.

        Returns
        --------
        PaymentEntity
            A builded PaymentEntity object.
        """
        event = PaymentEntity(
            initial_amount=event_amount,
            event_date=event_date
        )

        return event
