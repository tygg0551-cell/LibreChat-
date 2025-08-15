# Index - تطبيق البث المرئي

<div align="center">
  <h3>🎬 تطبيق بث الأفلام والمسلسلات المتطور</h3>
  <p>تطبيق Flutter متقدم لبث المحتوى المرئي مع دعم كامل للغة العربية</p>
</div>

---

## 📱 نظرة عامة

**Index** هو تطبيق بث مرئي متطور مطور بتقنية Flutter، يوفر تجربة مشاهدة استثنائية للأفلام والمسلسلات مع واجهة مستخدم عربية أنيقة ودعم RTL كامل.

### ✨ الميزات الرئيسية

- 🎥 **مكتبة ضخمة**: آلاف الأفلام والمسلسلات
- 🌐 **دعم اللغة العربية**: واجهة مستخدم عربية كاملة مع RTL
- 👤 **تسجيل دخول متعدد**: Google Sign-in أو الدخول كضيف
- ❤️ **قائمة المفضلة**: احفظ المحتوى المفضل لديك
- 🔍 **بحث متقدم**: ابحث عن أي محتوى بسهولة
- 📱 **تصميم متجاوب**: يعمل على جميع أحجام الشاشات
- 🎨 **واجهة أنيقة**: تصميم Material Design حديث
- 🔠 **ترجمات قابلة للتخصيص**: دعم ملفات .srt مع خيارات متقدمة
- ⏳ **مزامنة التقدم**: احفظ موضع المشاهدة تلقائياً

---

## 🛠️ التقنيات المستخدمة

### Frontend
- **Flutter** 3.35.1+ - إطار العمل الأساسي
- **Dart** - لغة البرمجة
- **Material Design 3** - نظام التصميم

### Backend & APIs
- **Firebase** - المصادقة والتحليلات
- **TMDB API** - بيانات الأفلام والمسلسلات
- **SUBDL API** - الترجمات

### إدارة الحالة
- **Flutter BLoC** - إدارة حالة التطبيق
- **SharedPreferences** - التخزين المحلي

### التدويل
- **flutter_localizations** - دعم اللغات المتعددة
- **intl** - تنسيق النصوص والتواريخ

---

## 📥 التحميل

[![تحميل APK](https://custom-icon-badges.demolab.com/badge/-تحميل%20APK-F25278?style=for-the-badge&logo=download&logoColor=white&color=AB261D)](https://github.com/sjso00747-creator/semo/releases)

[![تحميل IPA](https://custom-icon-badges.demolab.com/badge/-تحميل%20IPA-F25278?style=for-the-badge&logo=download&logoColor=white&color=AB261D)](https://github.com/sjso00747-creator/semo/releases)

---

## 🚀 البدء السريع

### المتطلبات الأساسية

```bash
Flutter SDK: >=3.0.0 <4.0.0
Dart SDK: >=3.0.0 <4.0.0
Android Studio / VS Code
Git
```

### التثبيت

1. **استنساخ المشروع**
```bash
git clone https://github.com/sjso00747-creator/semo.git
cd semo
```

2. **تثبيت التبعيات**
```bash
flutter pub get
```

3. **إعداد متغيرات البيئة**
```bash
# إنشاء ملف .env في الجذر
TMDB_ACCESS_TOKEN=your_tmdb_token_here
SUBDL_API_KEY=your_subdl_key_here
```

4. **توليد ملفات التدويل**
```bash
flutter gen-l10n
```

5. **توليد ملفات الأصول**
```bash
dart run build_runner build --delete-conflicting-outputs
```

6. **إعداد Firebase**
- اتبع تعليمات [الوثائق الرسمية](https://firebase.google.com/docs/flutter/setup)
- استخدم FlutterFire CLI لإعداد المشروع

7. **تشغيل التطبيق**
```bash
flutter run
```

---

## 🌐 دعم اللغات

التطبيق يدعم حالياً:
- 🇸🇦 **العربية** (افتراضي)
- 🇺🇸 **الإنجليزية**

### إضافة لغة جديدة

1. أضف ملف `.arb` جديد في `lib/l10n/`
2. حدث `l10n.yaml`
3. شغل `flutter gen-l10n`

---

## 🔧 البناء والنشر

### بناء APK للأندرويد

```bash
# Debug APK
flutter build apk --debug

# Release APK
flutter build apk --release

# Split APKs (مُوصى به)
flutter build apk --split-per-abi
```

### بناء App Bundle

```bash
flutter build appbundle --release
```

للمزيد من التفاصيل، راجع [دليل بناء APK](BUILD_APK_GUIDE.md)

---

## 🔑 إعداد API Keys

### TMDB API
1. سجل في [The Movie Database](https://www.themoviedb.org/)
2. احصل على API Key من لوحة التحكم
3. أضف المفتاح في ملف `.env`

### SUBDL API
1. سجل في [SUBDL](https://subdl.com/)
2. احصل على API Key
3. أضف المفتاح في ملف `.env`

---

## 🤝 المساهمة

نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:

1. Fork المشروع
2. إنشاء فرع للميزة الجديدة (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add amazing feature'`)
4. Push للفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

---

## 🐛 الإبلاغ عن الأخطاء

إذا واجهت أي مشاكل، يرجى:

1. التحقق من [Issues الموجودة](https://github.com/sjso00747-creator/semo/issues)
2. إنشاء Issue جديد مع:
   - وصف واضح للمشكلة
   - خطوات إعادة الإنتاج
   - لقطات شاشة (إن أمكن)
   - معلومات البيئة (OS, Flutter version, etc.)

---

## 👥 الفريق

### 🏢 شركة Voxin
**شركة ناشئة تأسست عام 2021**

- 🌐 **الموقع الرسمي**: [voxin.netlify.app](https://voxin.netlify.app/)
- 📧 **البريد الإلكتروني**: contact@voxin.com

### 🚀 مشاريعنا الأخرى

| المشروع | الوصف | الرابط |
|:---:|:---:|:---:|
| **Index** | تطبيق البث المرئي | [index-git-master-voxinappindexcom.vercel.app](https://index-git-master-voxinappindexcom.vercel.app/) |
| **Postyy** | منصة التواصل الاجتماعي | [postyy.netlify.app](https://postyy.netlify.app/) |
| **Build X** | قريباً... | 🔜 |

---

## 📞 الدعم والتواصل

- 📧 **البريد**: support@voxin.com
- 🐙 **GitHub Issues**: [إبلاغ عن مشكلة](https://github.com/sjso00747-creator/semo/issues)

---

## 🙏 شكر وتقدير

- **Flutter Team** - لإطار العمل الرائع
- **TMDB** - لقاعدة بيانات الأفلام المجانية
- **Firebase** - للخدمات السحابية
- **المجتمع العربي** - للدعم والتشجيع

---

<div align="center">
  <p>صُنع بـ ❤️ في المملكة العربية السعودية</p>
  <p>© 2024 Voxin. جميع الحقوق محفوظة.</p>
  <p>استمتع بالمشاهدة مع Index! 🌟</p>
</div>

---

## 📈 إحصائيات المشروع

![GitHub stars](https://img.shields.io/github/stars/sjso00747-creator/semo?style=social)
![GitHub forks](https://img.shields.io/github/forks/sjso00747-creator/semo?style=social)
![GitHub issues](https://img.shields.io/github/issues/sjso00747-creator/semo)

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=ios&logoColor=white)
