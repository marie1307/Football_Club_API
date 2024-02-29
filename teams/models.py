from django.db import models
from django.contrib.auth.models import User

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
    hour = models.CharField(max_length=5)


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
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedules, on_delete=models.CASCADE)

    def __str__(self):
        return self.age_group


# ფეხბურთელის პირადი გვერდი

class SkillStatistics(models.Model):
    speed_10 = models.CharField(verbose_name="სისწრაფე(10 მ.)", max_length=50)
    speed_20 = models.CharField(verbose_name="სისწრაფე(20 მ.)", max_length=50)
    speed_30 = models.CharField(verbose_name="სისწრაფე(30 მ.)", max_length=50)
    speed_50 = models.CharField(verbose_name="სისწრაფე(50 მ.)", max_length=50)
    speed_100 = models.CharField(verbose_name="სისწრაფე(100 მ.)", max_length=50)
    penal_left = models.CharField(verbose_name="პენალტი (მარჯვ.)", max_length=50)
    penal_right = models.CharField(verbose_name="პენალტი (მარცხ.)", max_length=50)
    kick_centre_right = models.CharField(verbose_name="დარტყმა( 16.5 მ (ცენტრი)) (ფეხი მარჯ.)", max_length=50)
    kick_centre_left = models.CharField(verbose_name="დარტყმა( 16.5 მ (ცენტრი)) (ფეხი მარცხ.)", max_length=50)
    kick_right_angle_foot_right = models.CharField(
        verbose_name="დარტყმა( 16.5 მ (რკალი მარცხენა)) (ფეხი მარჯ.)", max_length=50)
    kick_right_angle_foot_left = models.CharField(
        verbose_name="დარტყმა( 16.5 მ (რკალი მარცხენა)) (ფეხი მარცხ.)", max_length=50)
    kick_left_angle_foot_right_circl = models.CharField(
        verbose_name="დარტყმა( 16.5 მ (რკალი მარჯვენა)) (ფეხი მარჯ.)", max_length=50)
    kick_left_angle_foot_left_circl = models.CharField(
        verbose_name=" დარტყმა( 16.5 მ (რკალი მარჯვენა)) (ფეხი მარცხ.)", max_length=50)
    kick_right = models.CharField(
        verbose_name="ჟონგლირება (ფეხი მარჯ.)", max_length=50)
    kick_left = models.CharField(
        verbose_name="ჟონგლირება (ფეხი მარცხ.)", max_length=50)
    kick_head = models.CharField(verbose_name="ჟონგლირება (თავი)", max_length=50)
    kick_knee_right = models.CharField(
        verbose_name="ჟონგლირება (მუხლი მარჯვ.)", max_length=50)
    kick_knee_left = models.CharField(
        verbose_name="ჟონგლირება (მუხლი მარცხ.)", max_length=50)
    jogging = models.CharField(verbose_name="ძუნძული (100 მ.)", max_length=50)
    pass_right = models.CharField(
        verbose_name="ბალანსი, პასი (მარჯვ. შიდა ტერფი)", max_length=50)
    pass_left = models.CharField(
        verbose_name="ბალანსი, პასი (მარცხ. შიდა ტერფი)", max_length=50)
    pass_left_upper = models.CharField(
        verbose_name="ბალანსი, პასი (მარჯვ. ზედა ტერფი)", max_length=50)
    pass_right_upper = models.CharField(
        verbose_name="ბალანსი, პასი (მარცხ. ზედა ტერფი)", max_length=50)
    

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ????
    first_name = models.CharField(verbose_name="სახელი", max_length=50) 
    last_name = models.CharField(verbose_name="გვარი", max_length=50)
    birth_date = models.DateField(verbose_name="დაბადების თარიღი")
    personal_image = models.ImageField(upload_to='images/')
    cover_image = models.ImageField(upload_to='images/')
    # ასე დარჩეს თუ მთელი რიცხვი იყოს?
    height = models.FloatField(verbose_name="სიმაღლე",)
    weight = models.FloatField(verbose_name="წონა",)  # იგივე
    FOOT_CHOICES = [
        ('R', 'მარჯვენა'),
        ('L', 'მარცხენა'),
    ]
    foot = models.CharField(choices=FOOT_CHOICES, verbose_name="ფეხი", max_length=20)
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
    position = models.CharField(choices=POSITION_CHOICES, verbose_name="პოზიცია", max_length=50)
    skill_statistic = models.ForeignKey(SkillStatistics, on_delete=models.CASCADE)
