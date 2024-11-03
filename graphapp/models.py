from django.db import models


class MiastaIWspolrzedne(models.Model):
    numer = models.AutoField(primary_key=True, blank=True, null=True)
    siedziba = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'miasta_i_wspolrzedne'


class PolaczeniaMiedzyMiastami(models.Model):
    numer = models.AutoField(primary_key=True, blank=True, null=True)
    miasto_a = models.ForeignKey(MiastaIWspolrzedne, models.DO_NOTHING, db_column='miasto_a')
    miasto_b = models.ForeignKey(MiastaIWspolrzedne, models.DO_NOTHING, db_column='miasto_b', related_name='polaczeniamiedzymiastami_miasto_b_set')
    dlugosc_polaczenia = models.FloatField()

    class Meta:
        managed = False
        db_table = 'polaczenia_miedzy_miastami'
