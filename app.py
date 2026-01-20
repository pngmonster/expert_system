from pyswip import Prolog
import os

prolog = Prolog()
prolog.consult("expert.pl")

scores = {}

def add_points_from_prolog(query_template, key, value):
    """Универсальная функция для добавления баллов из Prolog запроса"""
    global scores
    try:
        query = query_template.format(key=key)
        res = list(prolog.query(query))
        if res:
            prolog_list = res[0]['L']
            for sp in prolog_list:
                scores[sp] = scores.get(sp, 0) + value
    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")

def add_interest(key, value=2):
    add_points_from_prolog("interest({key}, L).", key, value)

def add_skill(key, value=2):
    add_points_from_prolog("skill({key}, L).", key, value)

def add_work_environment(key, value=1):
    add_points_from_prolog("work_environment({key}, L).", key, value)

def add_education_level(key, value=1):
    add_points_from_prolog("education_level({key}, L).", key, value)

def clear_screen():
    """Очистка экрана консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Вывод заголовка раздела"""
    print("\n" + "="*60)
    print(f"{title:^60}")
    print("="*60)

def multiple_choice_question(question, options, values, points=1):
    """Вопрос с возможностью выбора нескольких вариантов"""
    print_header(question)
    for i, (key, description) in enumerate(zip(values, options), 1):
        print(f"{i}) {description}")
    print(f"{len(options)+1}) Пропустить этот вопрос")
    
    choices = input("\nВыберите номера через запятую (например: 1,3,5): ").strip()
    
    if choices.lower() == str(len(options)+1) or not choices:
        return []
    
    selected = []
    for choice in choices.split(','):
        choice = choice.strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(values):
                selected.append(values[idx])
    
    return selected

def single_choice_question(question, options, values, points=1):
    """Вопрос с выбором одного варианта"""
    print_header(question)
    for i, (key, description) in enumerate(zip(values, options), 1):
        print(f"{i}) {description}")
    
    while True:
        try:
            choice = input("\nВыберите номер: ").strip()
            if not choice:
                return None
            idx = int(choice) - 1
            if 0 <= idx < len(values):
                return values[idx]
            else:
                print("Пожалуйста, выберите номер из списка.")
        except ValueError:
            print("Пожалуйста, введите число.")

def ask_personal_info():
    """Вопросы о личной информации"""
    print_header("ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ")
    
    name = input("Ваше имя (необязательно): ").strip()
    if name:
        print(f"Привет, {name}!")
    
    print("\nОцените вашу склонность к следующим областям (1-5):")
    traits = {
        "Логическое мышление": 1,
        "Творческий подход": 1,
        "Коммуникабельность": 1,
        "Аналитические способности": 1,
        "Лидерские качества": 1
    }
    
    for trait in traits.keys():
        while True:
            try:
                rating = input(f"{trait} (1-5): ").strip()
                if rating:
                    r = int(rating)
                    if 1 <= r <= 5:
                        traits[trait] = r
                        break
                    else:
                        print("Введите число от 1 до 5")
                else:
                    break
            except ValueError:
                print("Введите число")
    
    # Учет личных качеств в баллах
    if traits["Логическое мышление"] >= 4:
        add_skill("analytical_thinking", traits["Логическое мышление"] - 2)
    if traits["Творческий подход"] >= 4:
        add_skill("creativity", traits["Творческий подход"] - 2)
    if traits["Коммуникабельность"] >= 4:
        add_skill("communication", traits["Коммуникабельность"] - 2)
    if traits["Лидерские качества"] >= 4:
        add_skill("leadership", traits["Лидерские качества"] - 2)

def ask_interests():
    """Вопросы об интересах"""
    print_header("ИНТЕРЕСЫ И СКЛОННОСТИ")
    
    interests = [
        ("Математика и точные науки", "math"),
        ("Биология и медицина", "biology_medicine"),
        ("Технологии и IT", "technology"),
        ("Гуманитарные науки", "humanities"),
        ("Творчество и дизайн", "creativity_design"),
        ("Бизнес и экономика", "business_economics"),
        ("Инженерия и техника", "engineering"),
        ("Научные исследования", "science_research"),
        ("Социальная помощь", "social_help"),
        ("Природа и окружающая среда", "nature_outdoors")
    ]
    
    options = [i[0] for i in interests]
    values = [i[1] for i in interests]
    
    selected = multiple_choice_question(
        "Какие области вам наиболее интересны? (можно выбрать несколько)",
        options, values, 2
    )
    
    for interest in selected:
        add_interest(interest, 2)

def ask_skills():
    """Вопросы о навыках"""
    print_header("НАВЫКИ И СПОСОБНОСТИ")
    
    skills = [
        ("Аналитическое мышление", "analytical_thinking"),
        ("Коммуникация и убеждение", "communication"),
        ("Творчество и креативность", "creativity"),
        ("Программирование и IT", "programming"),
        ("Математическое мышление", "mathematical_thinking"),
        ("Визуальное мышление", "visual_thinking"),
        ("Помощь людям", "helping_people"),
        ("Внимание к деталям", "attention_to_detail"),
        ("Лидерство и управление", "leadership"),
        ("Решение проблем", "problem_solving"),
        ("Языковые способности", "languages"),
        ("Организация и планирование", "organization"),
        ("Ручная работа и моторика", "manual_dexterity")
    ]
    
    options = [s[0] for s in skills]
    values = [s[1] for s in skills]
    
    selected = multiple_choice_question(
        "Какие навыки у вас лучше всего развиты? (можно выбрать несколько)",
        options, values, 2
    )
    
    for skill in selected:
        add_skill(skill, 2)

def ask_work_preferences():
    """Вопросы о предпочтениях в работе"""
    print_header("ПРЕДПОЧТЕНИЯ В РАБОТЕ")
    
    # Предпочтительная среда
    environments = [
        ("Офисная работа", "office"),
        ("Лаборатория", "lab"),
        ("Полевые условия", "field"),
        ("Удаленная работа", "remote"),
        ("Творческая студия", "creative_studio"),
        ("Медицинское учреждение", "medical"),
        ("Образовательное учреждение", "educational")
    ]
    
    env_options = [e[0] for e in environments]
    env_values = [e[1] for e in environments]
    
    selected_env = single_choice_question(
        "Какую рабочую среду вы предпочитаете?",
        env_options, env_values, 1
    )
    
    if selected_env:
        add_work_environment(selected_env, 1)
    
    # Уровень образования
    education_levels = [
        ("Бакалавриат", "bachelors"),
        ("Магистратура", "masters"),
        ("Аспирантура/PhD", "phd"),
        ("Среднее профессиональное", "vocational")
    ]
    
    edu_options = [e[0] for e in education_levels]
    edu_values = [e[1] for e in education_levels]
    
    selected_edu = single_choice_question(
        "Какой уровень образования вы планируете получить?",
        edu_options, edu_values, 1
    )
    
    if selected_edu:
        add_education_level(selected_edu, 1)
    
    # Дополнительные предпочтения
    print("\nДополнительные предпочтения:")
    pref_questions = [
        ("Предпочитаете работать в команде или индивидуально?", ["В команде", "Индивидуально"], [1, -1]),
        ("Нравится ли вам публичные выступления?", ["Да", "Нет", "Нейтрально"], [1, -1, 0]),
        ("Готовы ли к частым командировкам?", ["Да", "Нет"], [1, -1]),
        ("Важен ли график работы?", ["Гибкий график", "Стабильный график", "Не важно"], [1, 1, 0])
    ]
    
    for question, options, values in pref_questions:
        print(f"\n{question}")
        for i, opt in enumerate(options, 1):
            print(f"{i}) {opt}")
        choice = input("Выбор: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(values):
                # Можно использовать значения для тонкой настройки рекомендаций
                pass

def get_recommendations():
    """Получение и вывод рекомендаций"""
    print_header("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    
    if not scores:
        print("Не было получено достаточно данных для анализа.")
        return
    
    # Сортировка по убыванию баллов
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Получение топ-5 рекомендаций
    top_n = min(5, len(sorted_scores))
    top_recommendations = sorted_scores[:top_n]
    
    print(f"\nТоп-{top_n} рекомендованных специальностей:\n")
    
    for i, (specialty, score) in enumerate(top_recommendations, 1):
        print(f"{i}. {specialty.replace('_', ' ').title()}: {score} баллов")
    
    # Вывод всех результатов (опционально)
    print("\n" + "-"*60)
    show_all = input("Показать все результаты? (да/нет): ").strip().lower()
    if show_all in ['да', 'yes', 'y', 'д']:
        print("\nВсе специальности с баллами:")
        for specialty, score in sorted_scores:
            print(f"{specialty.replace('_', ' ').title():<40} {score:>3} баллов")
    
    # Дополнительные рекомендации
    print("\n" + "="*60)
    print("ДОПОЛНИТЕЛЬНЫЕ РЕКОМЕНДАЦИИ")
    print("="*60)
    
    best = top_recommendations[0][0]
    
    # Группировка рекомендаций по категориям
    categories = {
        'IT и Технологии': ['software_engineer', 'data_scientist', 'ai_researcher'],
        'Медицина': ['doctor', 'surgeon', 'nurse'],
        'Бизнес': ['business_manager', 'marketing_specialist', 'project_manager'],
        'Творчество': ['graphic_designer', 'writer', 'musician'],
        'Наука': ['researcher', 'scientist', 'biologist']
    }
    
    for category, specialties in categories.items():
        if best in specialties:
            print(f"\nПоскольку вам подходит {best.replace('_', ' ')},")
            print(f"рассмотрите также другие профессии в категории '{category}'")
            break

def main():
    """Основная функция"""
    clear_screen()
    print_header("ЭКСПЕРТНАЯ СИСТЕМА ВЫБОРА ПРОФЕССИИ")
    print("\nДобро пожаловать! Ответьте на несколько вопросов,")
    print("чтобы получить персонализированные рекомендации.")
    
    input("\nНажмите Enter чтобы начать...")
    
    # Последовательность вопросов
    ask_personal_info()
    ask_interests()
    ask_skills()
    ask_work_preferences()
    
    # Получение и вывод результатов
    get_recommendations()
    
    # Сохранение результатов
    print("\n" + "="*60)
    save = input("Сохранить результаты в файл? (да/нет): ").strip().lower()
    if save in ['да', 'yes', 'y', 'д']:
        with open('career_recommendations.txt', 'w', encoding='utf-8') as f:
            f.write("Результаты тестирования карьеры\n")
            f.write("="*50 + "\n\n")
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for specialty, score in sorted_scores[:10]:
                f.write(f"{specialty.replace('_', ' ').title():<40} {score:>3} баллов\n")
        print("Результаты сохранены в файл 'career_recommendations.txt'")
    
    print("\n" + "="*60)
    print("Спасибо за использование системы!")
    print("="*60)

if __name__ == "__main__":
    main()