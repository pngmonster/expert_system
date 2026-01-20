def ask_advanced_questions():
    """Расширенные вопросы для более точных рекомендаций"""
    advanced_questions = [
        {
            "question": "Как вы относитесь к рутинной работе?",
            "options": ["Нравится", "Терплю", "Не нравится"],
            "impact": {
                "Нравится": ["accountant", "data_entry", "administrative"],
                "Не нравится": ["researcher", "entrepreneur", "artist"]
            }
        },
        {
            "question": "Насколько для вас важен уровень дохода?",
            "options": ["Критически важен", "Важен", "Не очень важен", "Не важен"],
            "impact": {
                "Критически важен": ["investment_banker", "surgeon", "lawyer", "software_engineer"],
                "Не важен": ["social_worker", "teacher", "nonprofit"]
            }
        },
        {
            "question": "Хотели бы вы работать на себя или в компании?",
            "options": ["На себя", "В компании", "Не важно"],
            "impact": {
                "На себя": ["entrepreneur", "freelancer", "consultant"],
                "В компании": ["corporate_lawyer", "banker", "large_company"]
            }
        }
    ]
    
    return advanced_questions