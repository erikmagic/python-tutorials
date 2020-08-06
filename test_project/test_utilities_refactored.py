import pytest
from utilities import StringConverters


# scope='module' signifie que le fixture est disponible pour les tests dans ce
# script seulement et est appelé seulement une fois dans ce module (et non à
# chaque fonction). 
# autouse=True signifie que cet fixture est automatiquement appelé avant le
# premier test exécuté dans ce module (puisque le scope='module', si le
# scope='function' cette fixture aurait été appelé avant chaque fonction
# individuelle dans ce module. 
@pytest.fixture(autouse=True, scope='module')
def create_converter():
    converter = StringConverters()
    yield converter

def test_translate_to_jadensmith_raises_value_error(create_converter):
    with pytest.raises(ValueError):
        create_converter.translate_to_jadensmith(999)

def test_translate_to_jadensmith_single_word(create_converter):
    sentence = "bonjour"
    expected_value = "Bonjour"

    actual_value = create_converter.translate_to_jadensmith(sentence)

    assert expected_value == actual_value

def test_translate_to_jadensmith_sentence(create_converter):
    sentence = "bonjour comment ca Va"
    expected_value = "Bonjour Comment Ca Va"

    actual_value = create_converter.translate_to_jadensmith(sentence)

    assert expected_value == actual_value


def test_translate_to_internet_meme_raises_value_error(create_converter):
    with pytest.raises(ValueError):
        create_converter.translate_to_internet_meme(999)

def test_translate_to_internet_meme_single_word(create_converter):
    sentence = "bonjour"
    expected_value = "BoNjOuR"

    actual_value = create_converter.translate_to_internet_meme(sentence)

    assert expected_value == actual_value

def test_translate_to_internet_meme_sentence(create_converter):
    sentence = "bonjour comment ca va?"
    expected_value = "BoNjOuR cOmMeNt Ca Va?"

    actual_value = create_converter.translate_to_internet_meme(sentence)

    assert expected_value == actual_value
