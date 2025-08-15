#!/bin/bash

# سكريبت بناء APK لتطبيق Index
# Build APK script for Index app

echo "🚀 بناء تطبيق Index - Building Index App"
echo "=================================="

# التحقق من وجود Flutter
if ! command -v flutter &> /dev/null; then
    echo "❌ Flutter غير مثبت - Flutter is not installed"
    echo "يرجى تثبيت Flutter أولاً - Please install Flutter first"
    exit 1
fi

# عرض خيارات البناء
echo "اختر نوع البناء - Choose build type:"
echo "1) بناء مع Firebase (افتراضي) - Build with Firebase (default)"
echo "2) بناء بدون Firebase (مستقل) - Build without Firebase (standalone)"
echo "3) إلغاء - Cancel"

read -p "أدخل اختيارك (1-3) - Enter your choice (1-3): " choice

case $choice in
    1)
        echo "🔥 بناء مع Firebase - Building with Firebase"
        BUILD_TYPE="firebase"
        ;;
    2)
        echo "📱 بناء بدون Firebase - Building without Firebase"
        BUILD_TYPE="standalone"
        
        # نسخ الملفات بدون Firebase
        echo "📋 نسخ ملفات التكوين - Copying configuration files"
        cp pubspec_no_firebase.yaml pubspec.yaml
        cp android/app/build_no_firebase.gradle android/app/build.gradle
        
        # تحديث إعدادات التطبيق
        sed -i 's/static const bool enableFirebase = true;/static const bool enableFirebase = false;/g' lib/config/app_config.dart
        ;;
    3)
        echo "❌ تم الإلغاء - Cancelled"
        exit 0
        ;;
    *)
        echo "❌ اختيار غير صحيح - Invalid choice"
        exit 1
        ;;
esac

# تنظيف المشروع
echo "🧹 تنظيف المشروع - Cleaning project"
flutter clean

# تحديث الحزم
echo "📦 تحديث الحزم - Getting packages"
flutter pub get

# بناء الأصول
echo "🎨 بناء الأصول - Building assets"
flutter packages pub run build_runner build --delete-conflicting-outputs

# اختيار نوع البناء
echo "اختر نوع APK - Choose APK type:"
echo "1) Debug APK (للاختبار) - Debug APK (for testing)"
echo "2) Release APK (للإنتاج) - Release APK (for production)"

read -p "أدخل اختيارك (1-2) - Enter your choice (1-2): " apk_choice

case $apk_choice in
    1)
        echo "🔧 بناء Debug APK - Building Debug APK"
        flutter build apk --debug
        APK_PATH="build/app/outputs/flutter-apk/app-debug.apk"
        ;;
    2)
        echo "🏭 بناء Release APK - Building Release APK"
        flutter build apk --release
        APK_PATH="build/app/outputs/flutter-apk/app-release.apk"
        ;;
    *)
        echo "❌ اختيار غير صحيح - Invalid choice"
        exit 1
        ;;
esac

# التحقق من نجاح البناء
if [ -f "$APK_PATH" ]; then
    echo "✅ تم بناء APK بنجاح - APK built successfully!"
    echo "📍 مسار الملف - File location: $APK_PATH"
    
    # عرض معلومات الملف
    echo "📊 معلومات الملف - File information:"
    ls -lh "$APK_PATH"
    
    # إعادة الملفات الأصلية إذا كان البناء بدون Firebase
    if [ "$BUILD_TYPE" = "standalone" ]; then
        echo "🔄 إعادة الملفات الأصلية - Restoring original files"
        git checkout pubspec.yaml
        git checkout android/app/build.gradle
        git checkout lib/config/app_config.dart
    fi
    
    echo "🎉 تم الانتهاء بنجاح - Build completed successfully!"
else
    echo "❌ فشل في بناء APK - Failed to build APK"
    exit 1
fi