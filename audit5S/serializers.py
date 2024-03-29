

from rest_framework import serializers 
from .models import Audit,Action,Categorie,PlanAction,Responsable,Standard,Score,Zone,User
from rest_framework.authtoken.models import Token

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model =Zone 
        fields=['id','nom','responsable']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['id','nom','prenom','departement','email','numtel','photo','role'] 
        extra_kwargs ={'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        user=User.objects.create(**validated_data)  
        Token.objects.create(user=user)
        return user

class AuditSerializer(serializers.ModelSerializer):
    zone = ZoneSerializer(required=True)
    

    class Meta:
        model =Audit 
        fields=['id','zone','date', 'tauxMin']  
    def create(self, validated_data):
        zone_data = validated_data.pop('zone')
        
        audit = Audit.objects.create(**validated_data)
        Zone.objects.create(audit=audit, **zone_data)
        
        return audit      
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Action 
        fields=['id','probleme','cause','actionAfaire', 'delai','tauxEfficacite','planAction']
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model =Categorie 
        fields=['id','nom']
class PlanActionSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlanAction 
        fields=['id','audit']   
class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model =Responsable 
        fields=['id','nom','prenom','email','numtel']              
class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model =Standard 
        fields=['id','zone','categorie','description','valstandard','date_de_creation']        


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model =Score 
        fields=['id','audit','standard','valeur']   

