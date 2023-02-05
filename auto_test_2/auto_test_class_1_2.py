from auto_test_class_1_1 import AnonymousSurvey

question = "Какой язык программирования для вас наиболее интересен?"

survey = AnonymousSurvey(question)
survey.show_question()
print("Нажмите 'Q' для выхода из опроса. \n")
while True:
    response = input("Введите свой ответ: ")
    if response == "Q":
        break
    survey.store_response(response)

print("\n Спасибо за ответ")
survey.show_results()
