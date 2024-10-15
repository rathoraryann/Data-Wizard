from rest_framework import serializers
from .models import Resume_model
import ast

# Skills field Representation/formatting when retrived from database for sending or processing
class SkillListSerializer(serializers.Field):
    def to_internal_value(self, data):
        try:
            skills_list = ast.literal_eval(data)
            if not isinstance(skills_list, list):
                return serializers.ValidationError("Invalid Format! Input Data is not List.")
            return skills_list
        except :
            return serializers.ValidationError("Invalid Format!")
        

    def to_representation(self, value):
        return value

# Serialize the Data which is get from frontend to save in database
class ResumeSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    class Meta:
        model = Resume_model
        fields = '__all__'
    
    def get_skills(self, obj):
        try:
            return ast.literal_eval(obj.skills)
        except:
            return []


# Used for Skill Prediction
class SkillSerializer(serializers.Serializer):
    role = serializers.CharField()
    skills = SkillListSerializer()


#Show all Data to the Frontend in proper JSON Format
# class GetResumeSerializer(serializers.ModelSerializer):
#     skills = serializers.SerializerMethodField()
#     class Meta:
#         model = Resume_model
#         fields = '__all__'
    
#     def get_skills(self, obj):
#         try:
#             return ast.literal_eval(obj.skills)
#         except:
#             []
    



# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resume_model
#         fields = ['skills']
