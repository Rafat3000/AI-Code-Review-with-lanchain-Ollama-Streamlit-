# استيراد المكتبات اللازمة
from datetime import datetime  # للتعامل مع الوقت والتاريخ
from peewee import SqliteDatabase, TextField, DateTimeField, CharField, Model, FloatField  # مكتبة Peewee لإنشاء قواعد بيانات SQLite

# إنشاء قاعدة بيانات SQLite create sqlite db
db = SqliteDatabase('code_reviews.db')  # يتم إنشاء ملف قاعدة بيانات باسم code_reviews.db

# تعريف نموذج (جدول) CodeReview / define models tables
class CodeReview(Model):  
    # حقل لتخزين السؤال بصيغة نصية
    question = TextField()
    # حقل لتحديد لغة البرمجة المرتبطة بالمراجعة
    language = CharField()
    # حقل لتخزين الإجابة بصيغة نصية
    answer = TextField()
    # حقل لتخزين التقييم كعدد عشري
    score = FloatField()
    # حقل لتخزين تاريخ ووقت إنشاء السجل تلقائياً
    created_at = DateTimeField(default=datetime.now) 

    # تحديد قاعدة البيانات المرتبطة بالنموذج
    class Meta:
        database = db

    # تعريف وظيفة لإرجاع بيانات المراجعة كقائمة
    def get_review_data(self):
        return {
            'id': self.id,  # معرف المراجعة
            'question': self.question,  # السؤال
            'language': self.language,  # لغة البرمجة
            'answer': self.answer,  # الإجابة
            'score': self.score,  # التقييم
            'time': self.created_at  # وقت إنشاء السجل
        }

# تهيئة قاعدة البيانات intialize db
def init_database():
    db.connect()  # الاتصال بقاعدة البيانات
    db.create_tables([CodeReview], safe=True)  # إنشاء الجداول إذا لم تكن موجودة (التأكد من عدم التكرار)

# تعريف دالة لجلب جميع المراجعات difine functions 
def get_all_reviews():
    data = CodeReview.select().order_by(CodeReview.created_at.desc())  
    # جلب جميع المراجعات مرتبة تنازلياً حسب تاريخ الإنشاء
    return [r.get_review_data() for r in data]  
    # تحويل كل سجل إلى صيغة قائمة باستخدام الدالة المخصصة

# تعريف دالة لإنشاء مراجعة جديدة
def create_code_review(question, language, answer, score):
    review = CodeReview.create(
        question=question,  # إدخال السؤال
        language=language,  # إدخال لغة البرمجة
        answer=answer,  # إدخال الإجابة
        score=score  # إدخال التقييم
    )
