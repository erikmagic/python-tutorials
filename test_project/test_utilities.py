import pytest
import utilities as ut

class TestUtilities:
    """
    Cette classe est un exemple classique de tests cases du type xUnit. 
    Les méthodes setup_class/teardown_class sont appelées automatiquement au début et à la fin des tests unitaire appertenant à cette classe.
    """ 
    @classmethod
    def setup_class(cls):
        print("nothing to prepare!")
        return

    @classmethod
    def teardown_class(cls):
        pass


    def test_translate_to_jadensmith_raises_value_error(self):
        with pytest.raises(ValueError):
            ut.translate_to_jadensmith(999)

    def test_translate_to_jadensmith_single_word(self):
        sentence = "bonjour"
        expected_value = "Bonjour"

        actual_value = ut.translate_to_jadensmith(sentence)

        assert expected_value == actual_value

    def test_translate_to_jadensmith_sentence(self):
        sentence = "bonjour comment ca Va"
        expected_value = "Bonjour Comment Ca Va"

        actual_value = ut.translate_to_jadensmith(sentence)

        assert expected_value == actual_value


    def test_translate_to_internet_meme_raises_value_error(self):
        with pytest.raises(ValueError):
            ut.translate_to_internet_meme(999)

    def test_translate_to_internet_meme_single_word(self):
        sentence = "bonjour"
        expected_value = "BoNjOuR"

        actual_value = ut.translate_to_internet_meme(sentence)

        assert expected_value == actual_value

    def test_translate_to_internet_meme_sentence(self):
        sentence = "bonjour comment ca va?"
        expected_value = "BoNjOuR cOmMeNt Ca Va?"

        actual_value = ut.translate_to_internet_meme(sentence)

        assert expected_value == actual_value

