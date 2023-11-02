from rest_framework import serializers
import time

from pril.models import Pass, Item


class PassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pass
        fields = ["id", "name"]


class ItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)

    class Meta:
        model = Item
        fields = ["id", "title", "proverka"]

    def create(self, validated_data):
        print(validated_data)
        temp, _ = Item.objects.get_or_create(title=validated_data["title"], proverka=validated_data["proverka"], pass_fk_id=validated_data["pass_fk"])
        time.sleep(10)

        temp2, _ = Item.objects.get_or_create(title=validated_data["proverka"], proverka=validated_data["title"], pass_fk_id=validated_data["pass_fk"])
        return validated_data


