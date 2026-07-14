from typing import Annotated

from pydantic import Field

PositivePrice = Annotated[float, Field(gt=0, strict=True)]
PositiveStock = Annotated[int, Field(gt=0, strict=True)]
PositiveQuantity = Annotated[int, Field(gt=0, strict=True)]

PaymentAmount = PositivePrice
OrderPrice = PositivePrice
TotalPrice = PositivePrice