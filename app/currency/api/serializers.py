from rest_framework import serializers

from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'currency',
            'buy',
            'sale',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'source_url',
            'name',
            'code_name',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
        )

    def create(self, validated_data):
        subject = 'Contact Us'
        message = f'''
        email_from: {validated_data['email_from']}
        subject: {validated_data['subject']}
        message: {validated_data['message']}
        '''

        from currency.tasks import send_mail
        send_mail.delay(subject, message)
        return ContactUs.objects.create(**validated_data)
