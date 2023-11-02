from django.db import models


class Pass(models.Model):
    name = models.CharField(max_length=100)
    # items

    class Meta:
        verbose_name = "1. Заглушка"
        verbose_name_plural = "1. Заглушки"

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=50)
    proverka = models.CharField(max_length=50)
    pass_fk = models.ForeignKey(Pass, on_delete=models.CASCADE, related_name="items")

    class Meta:
        verbose_name = "2. Item"
        verbose_name_plural = "2. Items"

    def __str__(self):
        return self.title
