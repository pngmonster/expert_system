from flask import Flask, render_template, request, redirect, url_for
from pyswip import Prolog

app = Flask(__name__)
prolog = Prolog()
prolog.consult("expert.pl")

# Словарь для хранения баллов, имитируя глобальную переменную scores
scores = {}

def add_points_from_prolog(query_template, key, value):
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

@app.route("/")
def index():
    # стартовая страница с кнопкой "Начать тест"
    return render_template("index.html")

@app.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        # личные данные
        name = request.form.get("name")
        traits = {
            "analytical_thinking": int(request.form.get("trait_analytical", 1)),
            "creativity": int(request.form.get("trait_creativity", 1)),
            "communication": int(request.form.get("trait_communication", 1)),
            "leadership": int(request.form.get("trait_leadership", 1))
        }

        # начисляем баллы по личным качествам
        if traits["analytical_thinking"] >= 4:
            add_skill("analytical_thinking", traits["analytical_thinking"]-2)
        if traits["creativity"] >= 4:
            add_skill("creativity", traits["creativity"]-2)
        if traits["communication"] >= 4:
            add_skill("communication", traits["communication"]-2)
        if traits["leadership"] >= 4:
            add_skill("leadership", traits["leadership"]-2)

        # интересы
        selected_interests = request.form.getlist("interests")
        for interest in selected_interests:
            add_interest(interest, 2)

        # навыки
        selected_skills = request.form.getlist("skills")
        for skill in selected_skills:
            add_skill(skill, 2)

        # рабочая среда
        work_env = request.form.get("work_env")
        if work_env:
            add_work_environment(work_env, 1)

        # уровень образования
        edu_level = request.form.get("education")
        if edu_level:
            add_education_level(edu_level, 1)

        return redirect(url_for('results'))

    # GET запрос - отобразить форму
    interests_options = [
        ("math", "Математика и точные науки"),
        ("biology_medicine", "Биология и медицина"),
        ("technology", "Технологии и IT"),
        ("humanities", "Гуманитарные науки"),
        ("creativity_design", "Творчество и дизайн"),
        ("business_economics", "Бизнес и экономика"),
        ("engineering", "Инженерия и техника"),
        ("science_research", "Научные исследования"),
        ("social_help", "Социальная помощь"),
        ("nature_outdoors", "Природа и окружающая среда")
    ]
    skills_options = [
        ("analytical_thinking", "Аналитическое мышление"),
        ("communication", "Коммуникация и убеждение"),
        ("creativity", "Творчество и креативность"),
        ("programming", "Программирование и IT"),
        ("mathematical_thinking", "Математическое мышление"),
        ("visual_thinking", "Визуальное мышление"),
        ("helping_people", "Помощь людям"),
        ("attention_to_detail", "Внимание к деталям"),
        ("leadership", "Лидерство и управление"),
        ("problem_solving", "Решение проблем"),
        ("languages", "Языковые способности"),
        ("organization", "Организация и планирование"),
        ("manual_dexterity", "Ручная работа и моторика")
    ]
    work_env_options = [
        ("office", "Офисная работа"),
        ("lab", "Лаборатория"),
        ("field", "Полевые условия"),
        ("remote", "Удаленная работа"),
        ("creative_studio", "Творческая студия"),
        ("medical", "Медицинское учреждение"),
        ("educational", "Образовательное учреждение")
    ]
    edu_options = [
        ("bachelors", "Бакалавриат"),
        ("masters", "Магистратура"),
        ("phd", "Аспирантура/PhD"),
        ("vocational", "Среднее профессиональное")
    ]
    return render_template("questionnaire.html",
                           interests_options=interests_options,
                           skills_options=skills_options,
                           work_env_options=work_env_options,
                           edu_options=edu_options)

@app.route("/results")
def results():
    if not scores:
        return "Не было получено достаточно данных для анализа."

    # Сортируем по убыванию
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_recommendations = sorted_scores[:5]

    return render_template("results.html", top_recommendations=top_recommendations,
                           all_scores=sorted_scores)

if __name__ == "__main__":
    app.run(debug=True)
