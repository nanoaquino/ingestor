SELECT JSON_OBJECT (man_Comp, egn, name, gname, sname, fname, birth_Date, sex, notes, nationality, comp_Type, name_Suffix, name_Prefix, data_Source, language, home_Country, registration_Date, industry_Code, sub_Industry_Code, fiscal_Period, class_Code, class_Sub_Code, attr1, attr2, attr3, attr4, attr5) FROM INSIS_PEOPLE_V10_FK.p_people WHERE ROWNUM<=100000