import re

class StringConverters:

    def translate_to_jadensmith(self, sentence):
        """
        Jaden Smith, le fils de Will Smith, est la vedette de films tels que The
        Karate Kid (2010) et After Earth (2013). Jaden est également connu pour une
        partie de sa philosophie qu'il diffuse sur Twitter. Lorsqu'il écrit sur
        Twitter, il est connu pour mettre presque toujours en majuscule chaque mot.
        Pour plus de simplicité, vous devrez mettre chaque mot en majuscule. Voyez
        comment les contractions sont prévues dans l'exemple ci-dessous.

        Votre tâche consiste à convertir les chaînes de caractères pour qu'elles
        correspondent à la façon dont Jaden Smith les écrirait. Les chaînes sont de
        véritables citations de Jaden Smith, mais elles ne sont pas mises en
        majuscules de la même manière que celle qu'il a tapée à l'origine.
        
        [source: codewars.com]

        Parameters
        ----------
        sentence : string

        Returns
        -------
        string
            la même phrase en entré, mais avec la traduction en jadensmith.

        Raises
        ------
        ValueError
            if the sentence is not a string 
        """
        if type(sentence) is not str:
            raise ValueError("Please input a string as a `sentence`")
        
        def capitalize_single_word(w):
            return w[0].upper() + w[1:] if len(w) > 1 else w[0].upper()

        words = sentence.split(" ")
        words = [capitalize_single_word(w) for w in words]
        return " ".join(words)

    def translate_to_internet_meme(self, sentence):
        """
        Cette fonctione traduit une phrase en phrase meme de l'internet, par exemple:
        'bOnJoUr CoMmEnT cA vA?`

        Parameters
        ----------
        sentence: string
        
        Raises
        ------
        ValueError
            if the sentence is not a string
        """

        if type(sentence) is not str:
            raise ValueError("Please input a string as a `sentence`")
        
        reconstructed_sentence = ""
        last_upper = False
        for char in sentence:
            if re.match("[a-z]|[A-Z]", char) is None:
                reconstructed_sentence += char
                continue

            if last_upper:
                last_upper = False
                reconstructed_sentence += char.lower()
            else:
                last_upper = True
                reconstructed_sentence += char.upper()

        return reconstructed_sentence

    def make_readable(seconds):
        """
        Ecrire une fonction qui prend un nombre entier non négatif (secondes)
        comme entrée et retourne l'heure dans un format lisible par l'homme
        (HH:MM:SS)

        HH = heures, avec 2 chiffres, plage : 00 - 99
        MM = minutes, avec 2 chiffres, plage : 00 - 59
        SS = secondes, avec 2 chiffres, plage : 00 - 59
        Le temps maximum ne dépasse jamais 359999 (99:59:59)

        Parameters
        ----------
        seconds: int
            number of seconds
        
        Returns
        -------
        str
            une représentation lisible du nombre de secondes

        Raises
        ------
        ValueError
            if the input is not an integer between 0 and 359999

        """
        if type(seconds) is not int or seconds > 359999 or seconds < 0:
            raise ValueError("seconds input should be an integer between 0 and 359999")

        hours = seconds // 3600
        seconds = seconds - hours * 3600
        minutes = seconds // 60
        seconds = seconds - minutes * 60
        
        hours = "0"+ str(hours) if hours < 10 else str(hours)
        minutes = "0" + str(minutes) if minutes < 10 else str(minutes)
        seconds = "0"+ str(seconds) if seconds < 10 else str(seconds)
        return f"{hours}:{minutes}:{seconds}"


if __name__ == '__main__':
    import timeit
    s = """
sc = StringConverters()
with open("sherlock.txt") as f:
    lines = f.readlines()
meme_lines = [sc.translate_to_internet_meme(l) for l in lines[:100]]
    """

    print(timeit.timeit(stmt=s, setup="from __main__ import  StringConverters", number=1000))


