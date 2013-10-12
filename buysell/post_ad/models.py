from django.db import models

# Create your models here.
class Seller_Information(models.Model):
	def __unicode__(self):
		return self.seller_contact_name

	seller_contact_name = models.CharField(max_length = 40)
	seller_contact_number = models.IntegerField(max_length = 10) # verifier needed
	seller_email_id = models.CharField(max_length = 255) # verifier needed
	seller_country = models.CharField(max_length = 50) # verifier needed
	# seller_state = models.Charfield(max_length = 50) # verifier needed
	# seller_city = models.Charfield(max_length = 50) # verifier needed


class Product_Information(models.Model):
	def __unicode__(self):
		return self.product_name

	seller = models.ForeignKey(Seller_Information)
	product_name = models.CharField(max_length = 90)
	product_price = models.DecimalField(max_digits=12, decimal_places=2)
	product_description = models.CharField(max_length = 150)