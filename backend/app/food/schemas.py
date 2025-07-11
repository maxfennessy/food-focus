from pydantic import BaseModel, UUID4


class FoodRead(BaseModel):
    id: UUID4
    brand: str | None = None
    name: str | None = None
    calories: float | None = None
    total_fat: float | None = None
    saturated_fat: float | None = None
    polyunsaturated_fat: float | None = None
    monounsaturated_fat: float | None = None
    trans_fat: float | None = None
    sodium: float | None = None
    potassium: float | None = None
    total_carbs: float | None = None
    dietary_fiber: float | None = None
    sugars: float | None = None
    protein: float | None = None
    vitamin_a: float | None = None
    vitamin_c: float | None = None
    calcium: float | None = None
    iron: float | None = None
