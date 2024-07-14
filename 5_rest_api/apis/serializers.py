from rest_framework import serializers

from .models import *

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.SerializerMethodField()
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_classroom_count(self, obj):
        return obj.classrooms.count()

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()

class ClassroomSerializer(serializers.ModelSerializer):
    # teachers = serializers.StringRelatedField(many=True, read_only=True)
    # students = StudentSerializer(many=True, read_only=True)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), write_only=True)
    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school', 'teachers', 'students']
        depth = 1 
    
class TeacherSerializer(serializers.ModelSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)
    classrooms_ids = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), many=True,write_only=True,source='classrooms')
    # classroom_info_teacher = ClassroomSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender','classrooms_ids', 'classrooms' ]
        depth = 1
    def create(self, validated_data):
        classrooms_data = validated_data.pop('classrooms', [])
        teacher = Teacher.objects.create(**validated_data)
        teacher.classrooms.set(classrooms_data)
        return teacher

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all(), write_only=True)
    classroom_info = ClassroomSerializer(source='classroom', read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom','classroom_info']
        depth = 1 
    # def create(self, validated_data):
    #     classroom_data = validated_data.pop('classroom', None)
    #     if classroom_data:
    #         classroom = Classroom.objects.get(id=classroom_data['id']) 
    #         student = Student.objects.create(classroom=classroom, **validated_data)
    #     else:
    #         student = Student.objects.create(**validated_data)
    #     return student
