from django.db import models
from django.urls import reverse



# base model

class Home(models.Model):
    title = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class HomeSection1(models.Model):
    image = models.ImageField('section1/%Y/%m/%d/')
    title = models.TextField(max_length=800)
    param = models.TextField(max_length=800)

    def __str__(self):
        return self.param

class HomeSection2(models.Model):
    title = models.TextField(max_length=800)
    param = models.TextField(max_length=800)

    def __str__(self):
        return self.title

class HomeSection3(models.Model):
    image = models.ImageField('section3/%Y/%m/%d/')


class HomeSection4(models.Model):
    image = models.ImageField('section4/%Y/%m/%d/')
    title = models.TextField(max_length=800)
    def __str__(self):
        return self.title


class ContactusForm(models.Model):
    phone = models.CharField(max_length=255)
    subject = models.TextField(max_length=1000)

    def __str__(self):
        return self.phone

#

class Category(models.Model):
    name = models.CharField(max_length=200,
    db_index=True)
    slug = models.SlugField(max_length=200,
    unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
    related_name='products',
    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
    blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])




class Employment(models.Model):
    fitst_lastname = models.CharField(max_length=255,verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=500, verbose_name='شماره تماس')
    address = models.TextField(verbose_name='آدرس')
    father_name = models.CharField(max_length=255, verbose_name='نام پدر')
    Dateofbirth = models.CharField(max_length=300, verbose_name='تاریخ تولد')
    placeofbirth = models.CharField(max_length=255, verbose_name='محل تولد')
    national_code = models.CharField(max_length=500, verbose_name='کد ملی')
    number_Birth_certificate = models.CharField(max_length=500, verbose_name='شماره شناسنامه')
    Maritalstatus_numberofchildren = models.CharField(max_length=255, verbose_name='وضعیت تاهل و تعداد فرزند')
    militaryservicestatus = models.CharField(max_length=255, verbose_name='وضعیت نظام وظیفه')
    field_study_location = models.CharField(max_length=255, verbose_name='رشته تحصیلی و محل آن')
    Last_educational_certificate = models.CharField(max_length=255, verbose_name='آخرین مدرک تحصیلی')
    salon = models.CharField(max_length=20,choices=(('sandogh','صندوق'),('mizbani','میزبانی'),
                                                   ('hesabdari','حسابداری')),blank=True,verbose_name='سالن')

    peyk = models.CharField(max_length=20, choices=(('edari', 'اداری'), ('komakashpaz', 'کمک آشپز'),
                                                    ('sobhane', 'صبحانه')), blank=True,verbose_name='پیک')

    ashpaz = models.CharField(max_length=20, choices=(('khadamat', 'خدمات'), ('amadesazi', 'آماده سازی')),
                              blank=True,verbose_name='آشپز')

    Chef_assistantchef = models.CharField(max_length=20, choices=(('takhtekar', 'تخته کار'),
                                                                  ('amadesazi', 'آماده سازی'),
                                                    ('ghasabi', 'قصابی'),('ashpaziirani', 'آشپزی ایرانی'),
                                                                        ('ashpazifarangi','آشپزی فرنگی')),
                                          blank=True,verbose_name='دستیار آشپز')
    work_name1 = models.CharField(max_length=255, blank=True, verbose_name='نام محل کار ۱')
    work_time1 = models.CharField(max_length=255, blank=True, verbose_name='مدت زمان سابقه کار ۱')
    last_rights1 = models.CharField(max_length=255, blank=True, verbose_name='آخرین حقوق کار ۱')
    Reason_for_leaving_work1 = models.CharField(max_length=255, blank=True, verbose_name='دلیل ترک کار ۱')
    Manager_name1 = models.CharField(max_length=255, blank=True, verbose_name='مدیر کار ۱')

    work_name2 = models.CharField(max_length=255, blank=True, verbose_name='نام محل کار ۲')
    work_time2 = models.CharField(max_length=255, blank=True, verbose_name='مدت زمان سابقه کار ۲')
    last_rights2 = models.CharField(max_length=255, blank=True, verbose_name='آخرین حقوق کار ۲')
    Reason_for_leaving_work2 = models.CharField(max_length=255, blank=True, verbose_name='دلیل ترک کار ۲')
    Manager_name2 = models.CharField(max_length=255, blank=True, verbose_name='مدیر کار ۲')

    work_name3 = models.CharField(max_length=255, blank=True, verbose_name='نام محل کار ۳')
    work_time3 = models.CharField(max_length=255, blank=True, verbose_name='مدت زمان سابقه کار ۳')
    last_rights3 = models.CharField(max_length=255, blank=True, verbose_name='آخرین حقوق کار ۳')
    Reason_for_leaving_work3 = models.CharField(max_length=255, blank=True, verbose_name='دلیل ترک کار ۳')
    Manager_name3 = models.CharField(max_length=255, blank=True, verbose_name='مدیر کار ۳')

    Motivation_to_collaborate = models.TextField(verbose_name='انگیزه همکاری بارستوران فرشاد')

    english_language = models.CharField(max_length=20, choices=(('awli','عالی'),('khob', 'خوب'), ('motevaset', 'متوسط'),
                                                   ('zaief', 'ضعیف')), blank=True, verbose_name='مهارت زبان انگلیسی')

    word = models.CharField(max_length=20, choices=(('awli','عالی'),('khob', 'خوب'), ('motevaset', 'متوسط'),
                                                               ('zaief', 'ضعیف')), blank=True,
                            verbose_name='تسلط به word')

    exel = models.CharField(max_length=20, choices=(('awli','عالی'),('khob', 'خوب'), ('motevaset', 'متوسط'),
                                                   ('zaief', 'ضعیف')), blank=True, verbose_name='تسلط به exel')

    other_skills = models.CharField(max_length=255, blank=True, verbose_name='سایر مهارت ها یا زبان خارجی')

    bime_time = models.CharField(max_length=255, verbose_name='آیا سابقه بیمه دارید؟ و مدت زمان آن؟')

    salary = models.CharField(max_length=255,verbose_name='میزان حقوق درخواستی (به تومان)')

    min_time_coperation = models.CharField(max_length=255, verbose_name='حداقل زمان همکاری')

    work_per_day = models.CharField(max_length=255,verbose_name='توانایی چند ساعت کار در روز را دارید؟')

    smoke = models.CharField(max_length=20, choices=(('bale','بله'),('kheyr', 'خیر')),
                             verbose_name='آیا دخانیات مصرف میکنید؟')

    def __str__(self):
        return self.fitst_lastname

