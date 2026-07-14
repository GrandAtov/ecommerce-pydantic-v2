import pytest

from pydantic import ValidationError

from app.models import Category



def test_category_success(category):

    assert category.name == "Keyboard"

    assert category.is_active is True



def test_category_name_too_short():

    with pytest.raises(ValidationError):

        Category(
            id="550e8400-e29b-41d4-a716-446655440001",
            name="AB",
            description="Mechanical gaming keyboard",
            created_at="2026-07-13T20:00:00"
        )



def test_category_description_too_short():

    with pytest.raises(ValidationError):

        Category(
            id="550e8400-e29b-41d4-a716-446655440001",
            name="Keyboard",
            description="short",
            created_at="2026-07-13T20:00:00"
        )



def test_category_extra_field():

    with pytest.raises(ValidationError):

        Category(
            id="550e8400-e29b-41d4-a716-446655440001",
            name="Keyboard",
            description="Mechanical gaming keyboard",
            created_at="2026-07-13T20:00:00",
            random="test"
        )