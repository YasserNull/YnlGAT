#!/bin/bash
set -e

# برومبت التدقيق + تصحيح التكرارات + تحسين أسماء الأدوات
prompt="Role: Arabic Localization QA Specialist for Minecraft.
Task: Open each file and fix ONLY the Arabic translation text after '='.

Rules:
1. لا تعدل Key ID قبل علامة '='.
2. صحح الترجمات الخاطئة بناءً على أسماء أدوات Minecraft.
3. عدّل أو احذف التكرارات الخاطئة. مثال:
   'فأس نذرايت' مكررة بينما واحدة منها يجب أن تكون 'معول نذرايت'.
4. لا تعدل رموز التنسيق (§a, §l...) أو المتغيرات (%s, %1$s, {0}).
5. لا تطبع محتوى الملف. استخدم أداة edit لحفظ التعديلات مباشرة.
6. إذا كانت الترجمة صحيحة، اتركها كما هي.
"
   echo "➡️ معالجة الملف: $1"    
    qwen \
      -m qwen2.5-coder-mini \
      --approval-mode auto-edit \
      -p "$prompt قم بمراجعة وتصحيح الملف التالي: $1"

    echo "✔️ تم الانتهاء من: $1"
    echo
  

