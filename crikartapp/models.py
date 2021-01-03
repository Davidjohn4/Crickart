from django.db import models

# Create your models here.
#class registaration(models.Model):
#	username = models.CharField(max_length = 50)
#	first_name = models.CharField(max_length = 30)
#	last_name = models.CharField(max_length = 30)
#	email = models.CharField(max_length = 30)
#	password1 = models.IntegerField()
#	password2 = models.IntegerField()


# using method def to show a name
#	def __str__(self):
#		return self.username

class player_register(models.Model):
#	team_id = models.ForeignKey(team_id,on_delete = models.CASCADE)
	pname = models.CharField(max_length = 25)
	pemail = models.CharField(max_length = 25)
	pnumber = models.IntegerField()
	#date =  models.DateField()
	date = models.DateTimeField(default="")


# using method def to show a name
	def __str__(self):
		return self.pname

class team_register(models.Model):
#	team_id = models.PrimaryKey(team_id,on_delete = models.CASCADE)
	team_name = models.CharField(max_length = 25)
	college_name = models.CharField(max_length = 50)
	captain_name = models.CharField(max_length =25)
#	coach_name = models.CharField(max_length = 25)
	college_address = models.CharField(max_length = 100)
	email_id = models.CharField(max_length = 25)
	team_logo = models.ImageField(upload_to="media/upload/",default="")
	#group = models.CharField(max_length = 10)
	date =  models.DateField(default="")
	#date = models.DateTimeField(auto_now_add = True, editable = False)

# using method def to show a name
	def __str__(self):
		return self.team_name

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
#	com_id = models.ForeignKey(company,on_delete = models.CASCADE)
	product_name = models.CharField(max_length = 30)
	image = models.ImageField(upload_to="images/",default="")
	price = models.IntegerField()
	description = models.TextField()
	launching_date = models.DateTimeField(auto_now_add = True, editable = False)

	# using method def to show a name
	def __str__(self):
		return self.product_name
		
#class sport_product(models.Model):
#	product_id = models.PrimaryKey(product_id,on_delete = models.CASCADE)
#	product_name = models.CharField(max_length = 25)
#	category = models.CharField(max_length = 25)
#	sub_category = models.CharField(max_length = 25)
#	desc =models.CharField(max_length = 50)
#	date =  models.DateField()
	#puch_date = models.DateTimeField(auto_now_add = True, editable = False)
#	image = models.ImageField(upload_to='media/image')

class order(models.Model):
#	order_id = models.PrimaryKey(order_id,on_delete = models.CASCADE)
	amount = models.IntegerField()
	name = models.CharField(max_length = 25)
	email = models.CharField(max_length = 30)
	address1 = models.CharField(max_length = 25)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	zip_code = models.IntegerField()
	phone = models.IntegerField()

# using method def to show a name
	def __str__(self):
		return self.name

class feedback(models.Model):
	fname = models.CharField(max_length = 10)
	email = models.CharField(max_length = 30)
	phone = models.IntegerField()
	message = models.CharField(max_length = 50)


# using method def to show a name
	def __str__(self):
		return self.fname