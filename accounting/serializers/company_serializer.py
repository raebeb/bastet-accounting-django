from rest_framework import serializers

from accounting.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company

        fields = ['name', 'tax_refered', 'password']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'tax_refered': { 'required': False },
            'password': { 'write_only': True, 'required': False }
        }
        
    def create(self, validated_data):
        current_membership = self.context['membership']
        organization = current_membership.organization
        validated_data['organization'] = organization
        validated_data['membership'] = current_membership
        return Company.objects.create(**validated_data)
        
