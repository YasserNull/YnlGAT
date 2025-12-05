#!/usr/bin/env python3
import sys
import arabic_reshaper
from bidi.algorithm import get_display
import re

# فحص هل يحتوي النص على أحرف عربية
def has_arabic(text):
    return re.search(r'[\u0600-\u06FF]', text) is not None

# إصلاح المقاطع العربية فقط داخل النص
def fix_arabic_line(text):
    # نقسم النص إلى مقاطع عربية وغير عربية
    parts = re.split(r'([\u0600-\u06FF]+)', text)

    fixed_parts = []
    for part in parts:
        if has_arabic(part):
            reshaped = arabic_reshaper.reshape(part)
            bidi_fixed = get_display(reshaped)

            # إصلاح %s و %d
            bidi_fixed = bidi_fixed.replace("s%", "%s").replace("d%", "%d")

            fixed_parts.append(bidi_fixed)
        else:
            fixed_parts.append(part)

    return "".join(fixed_parts)

# قلب ترتيب الكلمات بالكامل
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

def process_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()
            
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for line in lines:

                clean_line = line.strip()

                # تجاهل كامل لأي سطر يبدأ بـ hbui.
                if (
    clean_line.startswith("hbui")
    or clean_line.startswith("accessibility")
    or clean_line.startswith("realmsWorld")
    or clean_line.startswith("csbCreateScreen")
    or clean_line.startswith("realmsSettingsScreen")
    or clean_line.startswith("achievement")
    or clean_line.startswith("createWorldScreen")
    or clean_line.startswith("crossPlatformToggle")
    or clean_line.startswith("realmsPendingInvitationsScreen")
    or clean_line.startswith("realmsInvitationScreen")
    or clean_line.startswith("realmJoining")
    or clean_line.startswith("realmsClearMembers")
    or clean_line.startswith("realmsSharingScreen")
    or clean_line.startswith("realmsCreateScreen")
    or clean_line.startswith("realmsConfigurationScreen")
    or clean_line.startswith("realmsWorld")
    or clean_line.startswith("realmsPlus")
    or clean_line.startswith("csbCreateScreen")
    or clean_line.startswith("network")
    or clean_line.startswith("realmsSettingsScreen")
    or clean_line.startswith("createWorld")
    or clean_line.startswith("selectTemplate")
    or clean_line.startswith("soundCategory")
    or clean_line.startswith("selectWorld")
    or clean_line.startswith("selectServer")
    or clean_line.startswith("menu.video")
    or clean_line.startswith("options.")
):
                    f_out.write(line)
                    continue

                # تجاهل الأسطر الفارغة أو التعليقات
                if not clean_line or clean_line.startswith('#'):
                    f_out.write(line)
                    continue

                # إذا يحتوي على علامة '=' نصلح القيمة فقط
                if '=' in line:
                    parts = line.split('=', 1)
                    key = parts[0]
                    value = parts[1]

                    ends_with_newline = value.endswith('\n')
                    value_content = value.strip()

                    # إصلاح العربي فقط داخل القيمة
                    fixed_value = fix_arabic_line(value_content)

                    # قلب ترتيب الكلمات بالكامل
                    reversed_value = reverse_words(fixed_value)

                    new_line = f"{key}={reversed_value}"
                    if ends_with_newline:
                        new_line += "\n"

                    f_out.write(new_line)

                else:
                    f_out.write(line)
                    
        print(f"تم الانتهاء! الملف المحفوظ: {output_path}")

    except FileNotFoundError:
        print("خطأ: الملف المدخل غير موجود.")
    except Exception as e:
        print(f"حدث خطأ غير متوقع: {e}")

def main():
    if len(sys.argv) < 3:
        print("الاستخدام الصحيح:")
        print("./fix_ar <input_file> <output_file>")
        print("مثال:")
        print("./fix_ar ar_DZ.lang ar_DZ_fixed.lang")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()