name = "Kate"
last_name = "Perova"
sex = "female"
age = "27"
weight = 57
height = 1.52
bmi = weight/height**2
bmi_res=str(bmi)
weight_res=str(weight)
height_res=str(height)
result ="Hi! My name is " +name + " " + last_name + " i'm " +age + " "+ "years old. Мой вес " \
         + weight_res + " кг, а рост  " + height_res + " см. Мой индекс массы тела равен " + bmi_res
print(result)