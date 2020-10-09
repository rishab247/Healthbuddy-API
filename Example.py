from chatbot import Chat, register_call
import wikipedia
import os
import warnings
warnings.filterwarnings("ignore")


@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query


if __name__ == '__main__':
    first_question = ""
    print("test")
    chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples/Example.template"))

    while(first_question !="quit"):
        code = (input())
        first_question = input()
        print(chat.say(first_question,code))
