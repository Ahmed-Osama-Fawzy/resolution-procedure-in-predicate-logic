def standardize_variables(expression):
    # تقسيم العبارة إلى أجزاء بناءً على الكميات
    parts = expression.split('[')
    new_expression = parts[0]  # الجزء الأول لا يتغير
    
    # إعداد لتتبع الأسماء الجديدة للمتغيرات
    var_changes = {}
    
    for part in parts[1:]:
        # لكل جزء، نجد المتغير والعبارة الفرعية
        var, sub_exp = part.split(']', 1)
        var = var.strip()  # إزالة المسافات البيضاء
        
        # إعادة تسمية المتغير
        if var not in var_changes:  # إذا كان المتغير جديدًا
            new_var_name = var + "'"  # إضافة علامة لتمييزه
            var_changes[var] = new_var_name
        else:
            new_var_name = var_changes[var]
        
        # إعادة بناء العبارة مع الأسماء الجديدة للمتغيرات
        new_sub_exp = sub_exp
        for old_var, new_var in var_changes.items():
            # استبدال المتغيرات في العبارة الفرعية
            new_sub_exp = new_sub_exp.replace(old_var, new_var)
        
        # إضافة الجزء المعدل إلى العبارة الجديدة
        new_expression += '[' + new_var_name + ']' + new_sub_exp
    
    return new_expression

# مثال على الاستخدام
expression = "∀x ¬graduating(x) ∨ happy(x) ∀x ¬happy(x) ∨ smiling(x) ∀x graduating(x) ∃x ¬smiling(x)"
new_expression = standardize_variables(expression)
print(new_expression)