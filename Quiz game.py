from Question import Question 

question_prompt = [
    "What colors are apple?\n(a) Red/Green\n (b) Purple\n(c) Orange\n\n",
    "What colors are bananas?\n(a) Teal\n (b) Magenta\n(c) Yellow\n\n",
    "What colors are strawberries?\n(a) Yellow\n (b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]