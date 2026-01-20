from flask import Flask, render_template, request, redirect, url_for, session
from pyswip import Prolog

app = Flask(__name__)
app.secret_key = "supersecretkey"  # для хранения сессии

prolog = Prolog()
prolog.consult("expert.pl")

# все вопросы и варианты
questions = [
    {
        "id": "personal_traits",
        "title": "Личностные качества (1-5)",
        "type": "slider",
        "fields": [
            ("trait_analytical", "Логическое мышление"),
            ("trait_creativity", "Творческий подход"),
            ("trait_communication", "Коммуникабельность"),
            ("trait_leadership", "Лидерство")
        ]
    },
    {
        "id": "interests",
        "title": "Выберите ваши интересы (можно несколько)",
        "type": "checkbox",
        "options": [
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
    },
    {
        "id": "skills",
        "title": "Выберите ваши навыки (можно несколько)",
        "type": "checkbox",
        "options": [
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
    },
    {
        "id": "work_env",
        "title": "Предпочтительная рабочая среда",
        "type": "radio",
        "options": [
            ("office", "Офисная работа"),
            ("lab", "Лаборатория"),
            ("field", "Полевые условия"),
            ("remote", "Удаленная работа"),
            ("creative_studio", "Творческая студия"),
            ("medical", "Медицинское учреждение"),
            ("educational", "Образовательное учреждение")
        ]
    },
    {
        "id": "education",
        "title": "Уровень образования",
        "type": "radio",
        "options": [
            ("bachelors", "Бакалавриат"),
            ("masters", "Магистратура"),
            ("phd", "Аспирантура/PhD"),
            ("vocational", "Среднее профессиональное")
        ]
    }
]

# глобальный словарь баллов
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

def process_answers(step_id, form_data):
    # начисляем баллы
    if step_id == "personal_traits":
        for field, val in form_data.items():
            val = int(val)
            if val >= 4:
                add_skill(field, val-2)
    elif step_id == "interests":
        for val in form_data.getlist("answers"):
            add_points_from_prolog("interest({key}, L).", val, 2)
    elif step_id == "skills":
        for val in form_data.getlist("answers"):
            add_points_from_prolog("skill({key}, L).", val, 2)
    elif step_id == "work_env":
        val = form_data.get("answers")
        if val:
            add_points_from_prolog("work_environment({key}, L).", val, 1)
    elif step_id == "education":
        val = form_data.get("answers")
        if val:
            add_points_from_prolog("education_level({key}, L).", val, 1)

@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

@app.route("/question/<int:step>", methods=["GET", "POST"])
def question(step):
    if step >= len(questions):
        return redirect("/results")

    q = questions[step]

    if request.method == "POST":
        process_answers(q["id"], request.form)
        return redirect(f"/question/{step+1}")

    progress = int((step / len(questions)) * 100)
    return render_template("step_question.html", question=q, step=step, total=len(questions), progress=progress)

@app.route("/results")
def results():
    if not scores:
        return "Не было получено достаточно данных для анализа."

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_recommendations = sorted_scores[:5]

    return render_template("results.html", top_recommendations=top_recommendations, all_scores=sorted_scores)

if __name__ == "__main__":
    app.run(debug=True)
