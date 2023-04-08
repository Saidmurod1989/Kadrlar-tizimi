
from django.db import models

class Bolimlar(models.Model):
    nomi = models.CharField(max_length=500, help_text="Bo'lim nomini kiriting.....")
    def __str__(self):
        return self.nomi

    class Meta:
            verbose_name = "Bo'lim"
            verbose_name_plural = "Bo'limlar"

class Hodimlar(models.Model):
    ism_sharifi = models.CharField(max_length=200, help_text="Hodim ism sharifini kiriting.....")
    bolimi = models.ForeignKey(Bolimlar,on_delete=models.CASCADE)
    lavozimi = models.CharField(max_length=200, help_text="Lavozimni kiriting.....")
    stavka = models.FloatField()

    def __str__(self):
        return f"{self.ism_sharifi} "


    class Meta:
        verbose_name = "Hodim"
        verbose_name_plural = "Hodimlar"



class Hodim_haqida(models.Model):
    ism_sharifi = models.ForeignKey(Hodimlar, on_delete = models.CASCADE)
    tug_yil = models.IntegerField()
    millati = models.CharField(max_length=500, help_text="Millati.....")
    malumoti = models.CharField(max_length=500, help_text="Ma'lumotini kiriting.....")
    tamomlagan = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    mutaxasislik = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    ilmiy_daraja = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    til_bilish = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    mukofot = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    mehnat_faoliyati = models.TextField()
    def __str__(self):
        return f"{self.ism_sharifi} haqida ma'lumot"
        # return "hodim.ism_sharifi"
    
    class Meta:
        verbose_name = 'Hodim haqida'
        verbose_name_plural = "Hodim haqida ma'lumot"
    
class Qarindoshlik(models.Model):
    hodim = models.ForeignKey(Hodim_haqida, on_delete=models.CASCADE)
    qarindoshligi = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    qarindosh_ismi = models.CharField(max_length=500, help_text="Qarindoshni kiriting.....")
    qarindosh_tug_yil = models.DateField()
    yashash_joyi = models.CharField(max_length=500, help_text="Yashash manzil...")
    ish_joyi = models.CharField(max_length=500, help_text="Ish manzil...")

    def __str__(self):
        return "hodim"

    class Meta:
            verbose_name = "Hodim qarindoshi"
            verbose_name_plural = "Hodim qarindoshlari"
    
