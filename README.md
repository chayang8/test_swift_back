For TEST
======================
School 

Get - http://localhost:8000/api/schools/
     =>   <params>
Post - http://localhost:8000/api/schools/
     =>   {
    "name": "data owner protocal",
    "abbreviation": "dop",
    "address": "america" 
    }
Put - http://localhost:8000/api/schools/{id}/
    =>   {
    "name": "data owner protocal",
    "abbreviation": "dop",
    "address": "america" 
    }
Delete - http://localhost:8000/api/schools/{id}/

======================
Classroom 

Get - http://localhost:8000/api/classrooms/
     =>   <params>
Post - http://localhost:8000/api/classrooms/
     =>   {
    "grade": 11,
    "section": "C",
    "school": 1
    }
Put - http://localhost:8000/api/classrooms/{id}/
    =>   {
    "grade": 11,
    "section": "C",
    "school": 1
    }
Delete - http://localhost:8000/api/classrooms/{id}/

======================
Teachers 

Get - http://localhost:8000/api/teachers/
     =>   <params>
Post - http://localhost:8000/api/teachers/
     =>   {
    "first_name":"samhond",
    "last_name":"chonchai",
    "gender":"Female",
    "classrooms_ids": [1]
}
Put - http://localhost:8000/api/teachers/{id}/
    =>   {
    "first_name":"samhond",
    "last_name":"chonchai",
    "gender":"Female",
    "classrooms_ids": [1]
}
Delete - http://localhost:8000/api/teachers/{id}/

======================
Student 

Get - http://localhost:8000/api/students/
     =>   <params>
Post - http://localhost:8000/api/students/
     =>   {
    "first_name":"BAa",
    "last_name":"sddd",
    "gender":"Female",
    "classroom": 1
}
Put - http://localhost:8000/api/students/{id}/
     =>   {
    "first_name":"BAa",
    "last_name":"sddd",
    "gender":"Female",
    "classroom": 1
}
Delete - http://localhost:8000/api/students/{id}/