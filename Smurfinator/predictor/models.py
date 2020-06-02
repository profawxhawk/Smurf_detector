# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class R6Final(models.Model):
    field1 = models.IntegerField(db_column='FIELD1', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=121)  # Field name made lowercase.
    level = models.DecimalField(db_column='Level', max_digits=21, decimal_places=9)  # Field name made lowercase.
    best_mmr_rating = models.DecimalField(db_column='Best_MMR_Rating', max_digits=21, decimal_places=9)  # Field name made lowercase.
    ranking = models.DecimalField(db_column='Ranking', max_digits=21, decimal_places=9)  # Field name made lowercase.
    avg_seasonal_mmr = models.DecimalField(db_column='Avg_Seasonal_MMR', max_digits=21, decimal_places=9)  # Field name made lowercase.
    wins = models.DecimalField(db_column='Wins', max_digits=21, decimal_places=9)  # Field name made lowercase.
    win_p = models.DecimalField(db_column='Win_p', max_digits=21, decimal_places=9)  # Field name made lowercase.
    kills = models.DecimalField(db_column='Kills', max_digits=21, decimal_places=9)  # Field name made lowercase.
    kd = models.DecimalField(db_column='KD', max_digits=21, decimal_places=9)  # Field name made lowercase.
    deaths = models.DecimalField(db_column='Deaths', max_digits=21, decimal_places=9)  # Field name made lowercase.
    headshots = models.DecimalField(db_column='Headshots', max_digits=21, decimal_places=9)  # Field name made lowercase.
    losses = models.DecimalField(db_column='Losses', max_digits=21, decimal_places=9)  # Field name made lowercase.
    time_played = models.DecimalField(db_column='Time_Played', max_digits=21, decimal_places=9)  # Field name made lowercase.
    matches_played = models.DecimalField(db_column='Matches_Played', max_digits=21, decimal_places=9)  # Field name made lowercase.
    melee_kills = models.DecimalField(db_column='Melee_Kills', max_digits=21, decimal_places=9)  # Field name made lowercase.
    blind_kills = models.DecimalField(db_column='Blind_Kills', max_digits=21, decimal_places=9)  # Field name made lowercase.
    time_played_casual = models.DecimalField(db_column='Time_Played_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    losses_casual = models.DecimalField(db_column='Losses_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    matches_casual = models.DecimalField(db_column='Matches_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    deaths_casual = models.DecimalField(db_column='Deaths_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    kills_casual = models.DecimalField(db_column='Kills_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    win_p_casual = models.DecimalField(db_column='Win_p_casual', max_digits=21, decimal_places=3)  # Field name made lowercase.
    kd_casual = models.DecimalField(db_column='KD_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    killsmin_casual = models.DecimalField(db_column='Killsmin_casual', max_digits=21, decimal_places=9)  # Field name made lowercase.
    time_played_rankinged = models.DecimalField(db_column='Time_Played_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    wins_rankinged = models.DecimalField(db_column='Wins_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    losses_rankinged = models.DecimalField(db_column='Losses_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    matches_rankinged = models.DecimalField(db_column='Matches_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    deaths_rankinged = models.DecimalField(db_column='Deaths_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    kills_rankinged = models.DecimalField(db_column='Kills_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    win_p_rankinged = models.DecimalField(db_column='Win_p_Rankinged', max_digits=21, decimal_places=1)  # Field name made lowercase.
    kd_rankinged = models.DecimalField(db_column='KD_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    killsmatch_rankinged = models.DecimalField(db_column='Killsmatch_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    killsmin_rankinged = models.DecimalField(db_column='Killsmin_Rankinged', max_digits=21, decimal_places=9)  # Field name made lowercase.
    smurf = models.BooleanField(db_column='Smurf')  # Field name made lowercase. This field type is a guess.
    count_no_smurf = models.IntegerField(blank=True, null=True)
    count_smurf = models.IntegerField(blank=True, null=True)
    



    class Meta:
        managed = False
        db_table = 'r6final'
    


class Cffinal(models.Model):
    field1 = models.IntegerField(db_column='FIELD1', primary_key=True)  # Field name made lowercase.
    handle = models.CharField(max_length=23)
    firstname = models.CharField(db_column='firstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=14, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=16, blank=True, null=True)
    maxrank = models.CharField(db_column='maxRank', max_length=20)  # Field name made lowercase.
    maxrating = models.IntegerField(db_column='maxRating')  # Field name made lowercase.
    contribution = models.IntegerField(db_column='contribution')
    friendofcount = models.IntegerField(db_column='friendOfCount')  # Field name made lowercase.
    upvotes = models.DecimalField(max_digits=12, decimal_places=9)
    ac_percentage = models.DecimalField(db_column='AC_Percentage', max_digits=11, decimal_places=8)  # Field name made lowercase.
    hashing = models.IntegerField()
    bitmasks = models.IntegerField()  # This field type is a guess.
    ternary_search = models.IntegerField()
    flows = models.IntegerField()
    string_suffix_structures = models.IntegerField()
    fft = models.IntegerField()
    meetinthemiddle = models.IntegerField()
    intelligence = models.DecimalField(db_column='Intelligence', max_digits=11, decimal_places=9)  # Field name made lowercase.
    smurf = models.BooleanField(db_column='Smurf')  # Field name made lowercase. This field type is a guess.
    count_no_smurf = models.IntegerField(blank=True, null=True)
    count_smurf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cffinal'
