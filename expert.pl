:- set_prolog_flag(encoding, utf8).

% ========== СПИСКИ СПЕЦИАЛЬНОСТЕЙ ==========

% IT и Технологии
specialty(software_engineer).
specialty(frontend_developer).
specialty(backend_developer).
specialty(fullstack_developer).
specialty(mobile_developer).
specialty(ios_developer).
specialty(android_developer).
specialty(game_developer).
specialty(game_designer).
specialty(ai_researcher).
specialty(ml_engineer).
specialty(data_scientist).
specialty(data_analyst).
specialty(data_engineer).
specialty(big_data_engineer).
specialty(cybersecurity_specialist).
specialty(pentester).
specialty(security_analyst).
specialty(devops_engineer).
specialty(sre_engineer).
specialty(cloud_architect).
specialty(cloud_engineer).
specialty(system_administrator).
specialty(network_engineer).
specialty(network_architect).
specialty(embedded_engineer).
specialty(iot_developer).
specialty(qa_engineer).
specialty(test_automation_engineer).
specialty(database_administrator).
specialty(database_architect).
specialty(product_manager_it).
specialty(project_manager_it).
specialty(technical_writer).
specialty(ui_ux_designer).
specialty(ui_designer).
specialty(ux_designer).
specialty(bi_developer).
specialty(business_analyst_it).

% Медицина и Биология
specialty(doctor).
specialty(surgeon).
specialty(cardiologist).
specialty(neurologist).
specialty(pediatrician).
specialty(dentist).
specialty(nurse).
specialty(paramedic).
specialty(pharmacist).
specialty(clinical_pharmacologist).
specialty(biologist).
specialty(molecular_biologist).
specialty(geneticist).
specialty(microbiologist).
specialty(laboratory_analyst).
specialty(lab_technician).
specialty(veterinarian).
specialty(vet_technician).
specialty(biotech_specialist).
specialty(bioinformatician).
specialty(epidemiologist).
specialty(nutritionist).
specialty(psychiatrist).
specialty(psychotherapist).

% Экономика и Бизнес
specialty(economist).
specialty(investment_analyst).
specialty(financial_analyst).
specialty(risk_analyst).
specialty(accountant).
specialty(auditor).
specialty(tax_consultant).
specialty(financial_manager).
specialty(cfo).
specialty(business_manager).
specialty(business_analyst).
specialty(management_consultant).
specialty(marketing_specialist).
specialty(digital_marketer).
specialty(seo_specialist).
specialty(smm_specialist).
specialty(brand_manager).
specialty(product_manager).
specialty(sales_manager).
specialty(account_manager).
specialty(hr_specialist).
specialty(recruiter).
specialty(hr_bp).
specialty(project_manager).
specialty(scrum_master).
specialty(supply_chain_manager).
specialty(logistics_specialist).
specialty(purchasing_manager).
specialty(entrepreneur).
specialty(startup_founder).
specialty(business_owner).

% Гуманитарные науки и Общественные науки
specialty(lawyer).
specialty(attorney).
specialty(judge).
specialty(notary).
specialty(political_scientist).
specialty(politician).
specialty(political_analyst).
specialty(psychologist).
specialty(clinical_psychologist).
specialty(educational_psychologist).
specialty(sociologist).
specialty(social_researcher).
specialty(journalist).
specialty(reporter).
specialty(editor).
specialty(copywriter).
specialty(teacher).
specialty(university_professor).
specialty(school_teacher).
specialty(tutor).
specialty(philologist).
specialty(linguist).
specialty(translator).
specialty(interpreter).
specialty(diplomat).
specialty(foreign_service_officer).
specialty(international_relations_specialist).
specialty(historian).
specialty(archaeologist).
specialty(philosopher).

% Искусство и Дизайн
specialty(graphic_designer).
specialty(illustrator).
specialty(motion_designer).
specialty(vfx_artist).
specialty(industrial_designer).
specialty(product_designer).
specialty(architect).
specialty(landscape_architect).
specialty(interior_designer).
specialty(decorator).
specialty(director).
specialty(film_director).
specialty(theatre_director).
specialty(musician).
specialty(composer).
specialty(music_producer).
specialty(writer).
specialty(novelist).
specialty(screenwriter).
specialty(poet).
specialty(photographer).
specialty(videographer).
specialty(animator).
specialty(character_designer).
specialty(art_director).
specialty(fashion_designer).

% Инженерные специальности
specialty(civil_engineer).
specialty(mechanical_engineer).
specialty(electrical_engineer).
specialty(chemical_engineer).
specialty(aerospace_engineer).
specialty(automotive_engineer).
specialty(robotics_engineer).
specialty(environmental_engineer).
specialty(industrial_engineer).
specialty(materials_engineer).

% Образование и Наука
specialty(researcher).
specialty(scientist).
specialty(physicist).
specialty(chemist).
specialty(mathematician).
specialty(astronomer).
specialty(geologist).
specialty(meteorologist).
specialty(librarian).
specialty(archivist).
specialty(curator).

% ========== ИНТЕРЕСЫ - СПЕЦИАЛЬНОСТИ ==========

% Основные интересы
interest(math, [
    software_engineer, data_scientist, ai_researcher, ml_engineer, 
    backend_developer, economist, investment_analyst, financial_analyst,
    accountant, auditor, mathematician, physicist, engineer
]).

interest(biology_medicine, [
    doctor, surgeon, cardiologist, neurologist, pediatrician, dentist,
    nurse, paramedic, pharmacist, biologist, molecular_biologist,
    geneticist, microbiologist, laboratory_analyst, veterinarian,
    biotech_specialist, bioinformatician, epidemiologist, nutritionist,
    psychiatrist, psychotherapist
]).

interest(technology, [
    software_engineer, backend_developer, frontend_developer,
    fullstack_developer, mobile_developer, ios_developer,
    android_developer, game_developer, ai_researcher, ml_engineer,
    devops_engineer, sre_engineer, cloud_architect, cloud_engineer,
    system_administrator, network_engineer, embedded_engineer,
    iot_developer, qa_engineer, database_administrator,
    cybersecurity_specialist, pentester, data_engineer, bi_developer
]).

interest(humanities, [
    lawyer, attorney, judge, political_scientist, politician,
    psychologist, sociologist, journalist, reporter, editor,
    teacher, university_professor, philologist, linguist,
    translator, interpreter, diplomat, historian, archaeologist,
    philosopher, writer, copywriter
]).

interest(creativity_design, [
    graphic_designer, illustrator, motion_designer, vfx_artist,
    industrial_designer, product_designer, architect, interior_designer,
    director, film_director, musician, composer, writer, novelist,
    screenwriter, photographer, videographer, animator, fashion_designer,
    art_director, ui_ux_designer, game_designer, character_designer
]).

interest(business_economics, [
    economist, investment_analyst, financial_analyst, risk_analyst,
    accountant, auditor, financial_manager, cfo, business_manager,
    business_analyst, management_consultant, marketing_specialist,
    digital_marketer, brand_manager, product_manager, sales_manager,
    hr_specialist, recruiter, project_manager, entrepreneur,
    startup_founder, supply_chain_manager, logistics_specialist
]).

interest(engineering, [
    civil_engineer, mechanical_engineer, electrical_engineer,
    chemical_engineer, aerospace_engineer, automotive_engineer,
    robotics_engineer, environmental_engineer, industrial_engineer,
    materials_engineer, embedded_engineer, network_engineer,
    system_administrator
]).

interest(science_research, [
    researcher, scientist, physicist, chemist, biologist,
    mathematician, astronomer, geologist, meteorologist,
    data_scientist, ai_researcher, geneticist, epidemiologist
]).

interest(social_help, [
    psychologist, psychiatrist, psychotherapist, teacher,
    tutor, nurse, doctor, social_worker, hr_specialist,
    recruiter, career_counselor
]).

interest(nature_outdoors, [
    biologist, environmental_engineer, geologist, meteorologist,
    veterinarian, landscape_architect, agricultural_specialist,
    ecologist
]).

% ========== НАВЫКИ - СПЕЦИАЛЬНОСТИ ==========

skill(analytical_thinking, [
    software_engineer, data_scientist, ai_researcher, ml_engineer,
    economist, investment_analyst, financial_analyst, business_analyst,
    cybersecurity_specialist, risk_analyst, researcher, scientist
]).

skill(communication, [
    marketing_specialist, hr_specialist, teacher, journalist,
    lawyer, politician, diplomat, psychologist, translator,
    project_manager, sales_manager, account_manager, editor,
    copywriter, therapist
]).

skill(creativity, [
    graphic_designer, motion_designer, industrial_designer,
    architect, interior_designer, director, musician, writer,
    ui_ux_designer, game_designer, fashion_designer, art_director,
    animator, screenwriter, composer
]).

skill(programming, [
    software_engineer, backend_developer, frontend_developer,
    fullstack_developer, mobile_developer, ios_developer,
    android_developer, game_developer, ai_researcher, ml_engineer,
    devops_engineer, data_engineer, embedded_engineer, iot_developer,
    test_automation_engineer, bi_developer
]).

skill(mathematical_thinking, [
    data_scientist, economist, ai_researcher, ml_engineer,
    software_engineer, investment_analyst, financial_analyst,
    accountant, auditor, mathematician, physicist, engineer
]).

skill(visual_thinking, [
    graphic_designer, illustrator, motion_designer, architect,
    interior_designer, ui_ux_designer, game_designer, animator,
    fashion_designer, art_director, photographer, videographer
]).

skill(helping_people, [
    doctor, nurse, psychologist, psychiatrist, therapist,
    teacher, tutor, social_worker, veterinarian, hr_specialist,
    career_counselor, customer_service
]).

skill(attention_to_detail, [
    cybersecurity_specialist, qa_engineer, test_automation_engineer,
    data_engineer, laboratory_analyst, embedded_engineer, auditor,
    editor, proofreader, watchmaker, jeweler
]).

skill(leadership, [
    project_manager, product_manager, business_manager, cfo,
    ceo, team_lead, department_head, director, entrepreneur,
    startup_founder, military_officer
]).

skill(problem_solving, [
    software_engineer, engineer, researcher, scientist,
    cybersecurity_specialist, detective, consultant, technician,
    mechanic, support_specialist
]).

skill(manual_dexterity, [
    surgeon, dentist, veterinarian, jeweler, watchmaker,
    craftsman, artist, sculptor, mechanic, chef
]).

skill(physical_stamina, [
    surgeon, nurse, paramedic, construction_worker, athlete,
    dancer, military_personnel, firefighter, police_officer
]).

skill(languages, [
    translator, interpreter, diplomat, foreign_service_officer,
    language_teacher, international_relations, journalist,
    copywriter, philologist, linguist
]).

skill(organization, [
    project_manager, event_planner, logistician, administrator,
    secretary, office_manager, production_manager, supply_chain_manager
]).

skill(persuasion, [
    sales_manager, politician, lawyer, marketer, advertiser,
    negotiator, recruiter, fundraiser
]).

% ========== УСЛОВИЯ РАБОТЫ ==========

work_environment(office, [
    software_engineer, accountant, financial_analyst, hr_specialist,
    project_manager, marketing_specialist, lawyer, data_scientist,
    business_analyst, editor, copywriter
]).

work_environment(lab, [
    researcher, scientist, biologist, chemist, laboratory_analyst,
    microbiologist, geneticist, pharmacist, materials_engineer,
    quality_control_specialist
]).

work_environment(field, [
    geologist, archaeologist, environmental_engineer, surveyor,
    agricultural_specialist, ecologist, construction_manager,
    field_technician
]).

work_environment(remote, [
    software_developer, designer, writer, translator, digital_marketer,
    consultant, online_teacher, data_analyst, seo_specialist
]).

work_environment(creative_studio, [
    graphic_designer, animator, video_editor, music_producer,
    art_director, photographer, fashion_designer, architect
]).

work_environment(medical, [
    doctor, nurse, surgeon, dentist, veterinarian, paramedic,
    physiotherapist, radiologist, anesthesiologist
]).

work_environment(educational, [
    teacher, professor, tutor, trainer, librarian, educational_consultant,
    school_administrator, curriculum_developer
]).

% ========== УРОВЕНЬ ОБРАЗОВАНИЯ ==========

education_level(bachelors, [
    software_engineer, web_developer, graphic_designer, marketing_specialist,
    sales_manager, hr_specialist, accountant, journalist, photographer,
    technician, administrative_assistant
]).

education_level(masters, [
    data_scientist, financial_analyst, business_analyst, project_manager,
    architect, psychologist, librarian, curator, mid_level_manager,
    engineer
]).

education_level(phd, [
    researcher, scientist, university_professor, ai_researcher,
    medical_doctor, psychiatrist, psychologist_clinical, economist,
    senior_scientist, principal_investigator
]).

education_level(vocational, [
    electrician, plumber, carpenter, chef, mechanic, beautician,
    dental_hygienist, paralegal, medical_assistant, welder
]).

% ========== АГРЕГАТОР БАЛЛОВ ==========

add_points([], _, Acc, Acc).
add_points([H|T], Value, Acc, NewAcc) :-
    ( member((H,Old),Acc) ->
        select((H,Old), Acc, Temp),
        NewOld is Old+Value,
        add_points(T, Value, [(H,NewOld)|Temp], NewAcc)
    ;
        add_points(T, Value, [(H,Value)|Acc], NewAcc)
    ).

% Выбор лучших специальностей
best_specialties(Acc, Top3) :-
    sort(2, @>=, Acc, Sorted),
    ( length(Sorted, L), L >= 3 ->
        take_first_n(Sorted, 3, Top3)
    ;
        Top3 = Sorted
    ).

take_first_n(List, N, FirstN) :-
    length(FirstN, N),
    append(FirstN, _, List).