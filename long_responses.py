import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

def test_load_corpus_english(self):
        files = corpus.list_corpus_files('text_recogniton_chat-master/data/english')
        corpus_data = list(corpus.load_corpus(*files))

        self.assertTrue(len(corpus_data))
