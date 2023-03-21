from rest_framework import serializers

from accounting.models import Company

import pdb # for debugging


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        # Create relation one organizarion has many companies
        # organization = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

        fields = ['name', 'tax_refered', 'password']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'name': {'required': True},
            'tax_refered': { 'required': False },
            'password': { 'write_only': True, 'required': False }
        }
        
        def create(self):
            pdb.set_trace()
            pass
            # return Company.objects.create(**validated_data)
            

        def update_attributes(self, instance, validated_data):
            instance.tax_refered = validated_data.get('tax_refered', instance.tax_refered)
            
