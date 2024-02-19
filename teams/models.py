from django.db import models

# Create your models here.


class AboutPage(models.Model):
    logo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    about = models.TextField()
    facebook = models.URLField()
    tiktok = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    # დასაზუსტებელია ერთი რომელიმე სოცქსელია თუ რამდენიმე უნდა დაემატოს
    social_network = models.URLField()
    map = models.URLField()  # ადგილმდებარეობა გუგლიდან


# კლასების (ჯგუფები) მოდელი
# ცხრილების მოდელი

class AgeCroups(models.Model):
    AGEGROUP_CHOICES = [
        ('U6', 'U6'),
        ('U7', 'U7'),
        ('U8', 'U8'),
        ('U9', 'U9'),
        ('U10', 'U10'),
        ('U11', 'U11'),
    ]
    age_group = models.CharField(choices=AGEGROUP_CHOICES, max_length=5)


class Schedules(models.Model):
    date = models.DateField()
    WEEKDAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    week_day = models.CharField(choices=WEEKDAY_CHOICES, max_length=20)
    hour = models.TimeField()


# ვიდეოების მოდელი
class Videos(models.Model):
    video = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# ფოტოების მოდელი


class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# ერთიანი ცხრილი ასაკობრივი ჯგუფების მიხედვით


class Groups(models.Model):
    age_group = models.ForeignKey(AgeCroups, on_delete=models.CASCADE)
    # აქ video და image საერთოდ ცალკე ვიდეოების დამატება ხომ არ ჯობია 5-ჯერ და ფოტოების 20-ჯერ?
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedules, on_delete=models.CASCADE)

    def __str__(self):
        return self.age_group


# ფეხბურთელის პირადი გვერდი

class Skill_statistics(models.Model):
    pass


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    personal_image = models.ImageField(upload_to='images/')
    cover_image = models.ImageField(upload_to='images/')
    height = models.FloatField()  # ასე დარჩეს თუ მთელი რიცხვი იყოს?
    weight = models.FloatField()  # იგივე
    FOOT_CHOICES = [
        ('R', 'მარჯვენა'),
        ('L', 'მარცხენა'),
    ]
    foot = models.CharField(choices=FOOT_CHOICES, max_length=20)
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('D', 'Defender'),
        ('SW', 'Sweeper'),
        ('CB', 'Center Back'),
        ('RCB', 'Right Center Back'),
        ('LCB', 'Left Center Back'),
        ('RB', 'Right Back'),
        ('LB', 'Left Back'),
        ('WB', 'Wing Back'),
        ('RWB', 'Right Wing Back'),
        ('LWB', 'Left Wing Back'),
        ('M', 'Midfielder'),
        ('MD', 'Defensive Mdfielder'),
        ('CDM', 'Center Defensive Midfielder'),
        ('CM', 'Center Midfielder'),
        ('RM', 'Right Midfielder'),
        ('LM', 'Left Midfielder'),
        ('AM', 'Attacking Midfielder'),
        ('CAM/AMC', 'Centre Attacking Midfielder'),
        ('AMR', 'Attacking Midfielder Right'),
        ('AML', 'Attacking Midfielder Left'),
        ('RW', 'Right Winger'),
        ('LW', 'Left Winger'),
        ('SS', 'Second Striker'),
        ('CF', 'Centre Forward'),
        ('ST', 'Striker'),
    ]
    position = models.CharField(choices=POSITION_CHOICES, max_length=50)
    skill_statistic = models.ForeignKey(
        Skill_statistics, on_delete=models.CASCADE)
