import pytest

from app.main import get_human_age


class TestGetHumanAgeNormalRange:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_get_human_age_0(
            self,
            cat_age: int,
            dog_age: int,
            result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestGetHumanAgeError:
    def test_cannot_add_int_and_str(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(2.5, "3")

    def test_cannot_add_negative_number(self) -> None:
        with pytest.raises(ValueError):
            get_human_age(-15, -24)
