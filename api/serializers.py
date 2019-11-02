from django.contrib.auth.models import User
from rest_framework import serializers
from .models import DemoPurpose


class DemoSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	class Meta:
		model = DemoPurpose # / User
		fields = ('url', 'id', 'name', 'email')


		# Specifying fields in datatables_always_serialize
        # will also force them to always be serialized.
		datatables_always_serialize = ('id',)

