# دليل بناء APK لتطبيق Index

## المتطلبات الأساسية

### 1. تثبيت Flutter
```bash
# تحميل Flutter SDK
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:`pwd`/flutter/bin"

# التحقق من التثبيت
flutter doctor
```

### 2. تثبيت Android Studio
- تحميل وتثبيت Android Studio
- تثبيت Android SDK
- تثبيت Android SDK Command-line Tools
- إنشاء Android Virtual Device (AVD) للاختبار

### 3. إعداد متغيرات البيئة
```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

## خيارات البناء

يمكنك بناء التطبيق بطريقتين:

### الخيار الأول: بناء مع Firebase (الافتراضي)
يتطلب إعداد Firebase وملفات التكوين

### الخيار الثاني: بناء بدون Firebase (مستقل)
لا يتطلب إعداد Firebase - مناسب للاختبار والتطوير

## إعداد المشروع

### 1. استنساخ المشروع
```bash
git clone <repository-url>
cd semo
```

### 2. تثبيت التبعيات
```bash
flutter pub get
```

### 3. إنشاء ملف البيئة
إنشاء ملف `.env` في جذر المشروع:
```
TMDB_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYTc2MDk3MTlhNTYxYjM0MWM4MDYyYzMzN2FiZTM5NyIsIm5iZiI6MTc0NDI5MzUwOC4xMDQsInN1YiI6IjY3ZjdjZTg0MzE3NzUyNzZkNmQ5OTM4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jB-LdCFKnX7xETXv3UgAHXffgoCOFK9wfyr6Z8y4AzI
SUBDL_API_KEY=l0cgAb7VNM_KMN2KwkLCFNuRsk8q3tEg
```

### 4. توليد الملفات المطلوبة
```bash
# توليد ملفات البيئة
flutter packages pub run build_runner build

# توليد ملفات التدويل
flutter gen-l10n

# توليد أيقونات التطبيق
flutter packages pub run flutter_launcher_icons:main

# توليد شاشة البداية
flutter packages pub run flutter_native_splash:create
```

## بناء APK

### 1. بناء APK للتطوير (Debug)
```bash
flutter build apk --debug
```

### 2. بناء APK للإنتاج (Release)

#### أ. إنشاء مفتاح التوقيع
```bash
keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

#### ب. إنشاء ملف key.properties
إنشاء ملف `android/key.properties`:
```
storePassword=<password from previous step>
keyPassword=<password from previous step>
keyAlias=upload
storeFile=<location of the key store file, such as /Users/<user name>/upload-keystore.jks>
```

#### ج. بناء APK الإنتاج
```bash
flutter build apk --release
```

### 3. بناء APK منفصل لكل معمارية
```bash
flutter build apk --split-per-abi
```

## البناء بدون Firebase (مستقل)

إذا كنت تريد بناء التطبيق بدون Firebase، اتبع هذه الخطوات:

### 1. استخدام ملف pubspec بدون Firebase
```bash
# نسخ ملف pubspec بدون Firebase
cp pubspec_no_firebase.yaml pubspec.yaml

# تحديث الحزم
flutter pub get
```

### 2. استخدام build.gradle بدون Firebase
```bash
# نسخ ملف build.gradle بدون Firebase
cp android/app/build_no_firebase.gradle android/app/build.gradle
```

### 3. تحديث إعدادات التطبيق
في ملف `lib/config/app_config.dart`، غير:
```dart
static const bool enableFirebase = false;
```

### 4. بناء APK بدون Firebase
```bash
# بناء للتطوير
flutter build apk --debug

# بناء للإنتاج
flutter build apk --release
```

### 5. إعادة Firebase (اختياري)
لإعادة Firebase:
```bash
# استعادة ملف pubspec الأصلي
git checkout pubspec.yaml
git checkout android/app/build.gradle

# تحديث الحزم
flutter pub get

# تحديث إعدادات التطبيق
# في lib/config/app_config.dart غير enableFirebase إلى true
```

## مواقع الملفات المبنية

- **Debug APK**: `build/app/outputs/flutter-apk/app-debug.apk`
- **Release APK**: `build/app/outputs/flutter-apk/app-release.apk`
- **Split APKs**: `build/app/outputs/flutter-apk/app-<abi>-release.apk`

## اختبار APK

### 1. تثبيت على جهاز Android
```bash
flutter install
```

### 2. تثبيت APK مباشرة
```bash
adb install build/app/outputs/flutter-apk/app-release.apk
```

## نصائح مهمة

### 1. تحسين الحجم
```bash
# بناء مع تحسين الحجم
flutter build apk --release --shrink

# بناء bundle للنشر على Google Play
flutter build appbundle --release
```

### 2. فحص المشروع
```bash
# فحص صحة المشروع
flutter doctor

# تحليل المشروع
flutter analyze

# تشغيل الاختبارات
flutter test
```

### 3. تنظيف المشروع
```bash
# تنظيف ملفات البناء
flutter clean

# إعادة تثبيت التبعيات
flutter pub get
```

## استكشاف الأخطاء

### مشاكل شائعة وحلولها

#### 1. خطأ في Gradle
```bash
cd android
./gradlew clean
cd ..
flutter clean
flutter pub get
```

#### 2. مشاكل في التبعيات
```bash
flutter pub deps
flutter pub upgrade
```

#### 3. مشاكل في Android SDK
```bash
flutter doctor --android-licenses
```

#### 4. مشاكل في الذاكرة أثناء البناء
إضافة إلى `android/gradle.properties`:
```
org.gradle.jvmargs=-Xmx4g -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
```

## معلومات التطبيق

- **اسم التطبيق**: Index
- **معرف الحزمة**: com.voxin.index
- **الإصدار**: 1.0.0+1
- **الحد الأدنى لـ Android**: API 23 (Android 6.0)
- **الهدف**: API 34 (Android 14)

## الدعم

للحصول على المساعدة:
- [وثائق Flutter](https://docs.flutter.dev/)
- [دليل بناء Android](https://docs.flutter.dev/deployment/android)
- [موقع Voxin](https://voxin.netlify.app/)

---

© 2021-2025 Voxin. جميع الحقوق محفوظة.