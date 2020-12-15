import pytest
import utilities as ut


# scope='module' signifie que le fixture est disponible pour les tests dans ce
# script seulement et est appelé seulement une fois dans ce module (et non à
# chaque fonction). 

@pytest.fixture(scope='module')
def prepare():
    print('nothing to prepare in this example!')
    return 

def test_translate_to_jadensmith_raises_value_error(prepare):
    with pytest.raises(ValueError):
        ut.translate_to_jadensmith(999)

def test_translate_to_jadensmith_single_word(prepare):
    sentence = "bonjour"
    expected_value = "Bonjour"
    
    actual_value = ut.translate_to_jadensmith(sentence)

    assert expected_value == actual_value

def test_translate_to_jadensmith_sentence(prepare):
    sentence = "bonjour comment ca Va"
    expected_value = "Bonjour Comment Ca Va"

    actual_value = ut.translate_to_jadensmith(sentence)

    assert expected_value == actual_value


def test_translate_to_internet_meme_raises_value_error(prepare):
    with pytest.raises(ValueError):
        ut.translate_to_internet_meme(999)

def test_translate_to_internet_meme_single_word(prepare):
    sentence = "bonjour"
    expected_value = "BoNjOuR"

    actual_value = ut.translate_to_internet_meme(sentence)

    assert expected_value == actual_value

def test_translate_to_internet_meme_sentence(prepare):
    sentence = "bonjour comment ca va?"
    expected_value = "BoNjOuR cOmMeNt Ca Va?"

    actual_value = ut.translate_to_internet_meme(sentence)

    assert expected_value == actual_value
